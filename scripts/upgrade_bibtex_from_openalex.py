#!/usr/bin/env python3

import csv
import difflib
import json
import os
import re
import shutil
import subprocess
import time
import urllib.parse
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


OPENALEX_WORKS_URL = "https://api.openalex.org/works"
ARXIV_DOI_PREFIX = "10.48550/arxiv."

MIN_SCORE = 0.86
PER_PAGE = 10
REQUEST_SLEEP_SECONDS = 1.0
MAX_REQUEST_RETRIES = 5

REPORT_PATH = "data/search/openalex_bib_upgrade_report.tsv"

BIB_CANDIDATES = (
    "references.bib",
    "references/references.bib",
    "paper/references.bib",
    "paper.bib",
    "refs.bib",
    "bibliography.bib",
)


@dataclass
class BibEntry:
    entry_type: str
    key: str
    fields: dict[str, str]
    start: int
    end: int
    original: str


def git_root() -> Path:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return Path(result.stdout.strip())


def find_bib_path(root: Path) -> Path:
    for candidate in BIB_CANDIDATES:
        path = root / candidate
        if path.exists():
            return path

    ignored_parts = {
        ".git",
        "build",
        ".venv",
        "venv",
        "node_modules",
        "__pycache__",
    }

    bib_files = [
        path
        for path in root.rglob("*.bib")
        if not any(part in ignored_parts for part in path.parts)
    ]

    if not bib_files:
        raise SystemExit("No .bib file found in repository.")

    def score(path: Path) -> tuple[int, int]:
        name = path.name.lower()
        preferred = int(name in {"references.bib", "refs.bib", "bibliography.bib"})
        try:
            content = path.read_text(encoding="utf-8")
            entry_count = len(re.findall(r"@\w+\s*\{", content))
        except UnicodeDecodeError:
            entry_count = 0
        return preferred, entry_count

    return max(bib_files, key=score)


def normalize_text(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[{}\\]", "", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def clean_doi(value: str) -> str:
    value = (value or "").strip()
    value = value.replace("https://doi.org/", "")
    value = value.replace("http://doi.org/", "")
    value = value.replace("doi:", "")
    return value.rstrip(".")


def is_arxiv_doi(value: str) -> bool:
    return clean_doi(value).lower().startswith(ARXIV_DOI_PREFIX)


def is_arxiv_like(value: str) -> bool:
    value = (value or "").lower()
    return "arxiv.org" in value or "arxiv" in value or "10.48550" in value


def extract_arxiv_id(value: str) -> str:
    patterns = (
        r"arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]{4,5})(?:v\d+)?",
        r"10\.48550/arxiv\.([0-9]{4}\.[0-9]{4,5})(?:v\d+)?",
        r"\b([0-9]{4}\.[0-9]{4,5})(?:v\d+)?\b",
    )

    for pattern in patterns:
        match = re.search(pattern, value or "", flags=re.IGNORECASE)
        if match:
            return match.group(1)

    return ""


def parse_bib_entries(content: str) -> list[BibEntry]:
    entries: list[BibEntry] = []
    index = 0

    while True:
        match = re.search(r"@([A-Za-z]+)\s*\{\s*([^,\s]+)\s*,", content[index:])
        if not match:
            break

        start = index + match.start()
        entry_type = match.group(1)
        key = match.group(2)

        brace_start = content.find("{", start)
        depth = 0
        end = brace_start

        while end < len(content):
            char = content[end]
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    end += 1
                    break
            end += 1

        original = content[start:end]
        body_start = content.find(",", start) + 1
        body = content[body_start : end - 1]

        entries.append(
            BibEntry(
                entry_type=entry_type,
                key=key,
                fields=parse_fields(body),
                start=start,
                end=end,
                original=original,
            )
        )
        index = end

    return entries


def parse_fields(body: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    index = 0

    while index < len(body):
        while index < len(body) and body[index] in " \n\r\t,":
            index += 1

        name_start = index
        while index < len(body) and re.match(r"[A-Za-z0-9_\-]", body[index]):
            index += 1

        name = body[name_start:index].strip().lower()
        if not name:
            index += 1
            continue

        while index < len(body) and body[index].isspace():
            index += 1

        if index >= len(body) or body[index] != "=":
            index += 1
            continue

        index += 1

        while index < len(body) and body[index].isspace():
            index += 1

        if index >= len(body):
            break

        if body[index] == "{":
            index += 1
            value_start = index
            depth = 1

            while index < len(body) and depth > 0:
                if body[index] == "{":
                    depth += 1
                elif body[index] == "}":
                    depth -= 1
                    if depth == 0:
                        fields[name] = body[value_start:index].strip()
                        index += 1
                        break
                index += 1

        elif body[index] == '"':
            index += 1
            value_start = index

            while index < len(body):
                if body[index] == '"' and body[index - 1] != "\\":
                    fields[name] = body[value_start:index].strip()
                    index += 1
                    break
                index += 1

        else:
            value_start = index
            while index < len(body) and body[index] != ",":
                index += 1
            fields[name] = body[value_start:index].strip()

    return fields


def bib_escape(value: str) -> str:
    return (
        value.strip()
        .replace("&", "\\&")
        .replace("%", "\\%")
        .replace("$", "\\$")
        .replace("#", "\\#")
        .replace("_", "\\_")
    )


def serialize_entry(entry: BibEntry) -> str:
    field_order = (
        "title",
        "author",
        "year",
        "journal",
        "booktitle",
        "publisher",
        "volume",
        "number",
        "pages",
        "doi",
        "url",
        "eprint",
        "archiveprefix",
        "note",
    )

    keys = [key for key in field_order if key in entry.fields]
    keys.extend(sorted(set(entry.fields) - set(keys)))

    lines = [f"@{entry.entry_type}{{{entry.key},"]
    for key in keys:
        value = entry.fields.get(key, "").strip()
        if value:
            lines.append(f"  {key} = {{{bib_escape(value)}}},")

    if len(lines) > 1:
        lines[-1] = lines[-1].rstrip(",")

    lines.append("}")
    return "\n".join(lines)


def request_json(url: str) -> dict[str, Any]:
    for attempt in range(1, MAX_REQUEST_RETRIES + 1):
        started = time.monotonic()
        print(f"[openalex] request attempt {attempt}/{MAX_REQUEST_RETRIES}: {url}", flush=True)
        headers = {"User-Agent": "openalex-bibtex-upgrader/1.0"}
        mailto = os.environ.get("OPENALEX_MAILTO", "").strip()
        if mailto:
            headers["User-Agent"] += f" (mailto:{mailto})"
        request = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                payload = json.loads(response.read().decode("utf-8"))
            elapsed = time.monotonic() - started
            print(f"[openalex] response in {elapsed:.1f}s", flush=True)
            return payload
        except urllib.error.HTTPError as error:
            elapsed = time.monotonic() - started
            if error.code != 429 or attempt == MAX_REQUEST_RETRIES:
                print(f"[openalex] error after {elapsed:.1f}s: HTTP {error.code}", flush=True)
                raise
            retry_after = error.headers.get("Retry-After")
            delay = float(retry_after) if retry_after and retry_after.isdigit() else 2**attempt
            print(f"[openalex] HTTP 429 after {elapsed:.1f}s; retrying in {delay:.1f}s", flush=True)
            time.sleep(delay)
        except Exception as error:
            elapsed = time.monotonic() - started
            print(f"[openalex] error after {elapsed:.1f}s: {error}", flush=True)
            raise
    raise RuntimeError("OpenAlex request retries exhausted")


def openalex_search(title: str) -> list[dict[str, Any]]:
    query = urllib.parse.urlencode(
        {
            "search": title,
            "per-page": str(PER_PAGE),
            "select": ",".join(
                (
                    "id",
                    "display_name",
                    "doi",
                    "publication_year",
                    "type",
                    "authorships",
                    "primary_location",
                    "locations",
                    "biblio",
                )
            ),
        }
    )

    payload = request_json(f"{OPENALEX_WORKS_URL}?{query}")
    return payload.get("results", [])


def source_name(work: dict[str, Any]) -> str:
    primary = work.get("primary_location") or {}
    source = primary.get("source") or {}

    if source.get("display_name"):
        return source["display_name"]

    for location in work.get("locations") or []:
        source = (location or {}).get("source") or {}
        if source.get("display_name"):
            return source["display_name"]

    return ""


def source_type(work: dict[str, Any]) -> str:
    primary = work.get("primary_location") or {}
    source = primary.get("source") or {}

    if source.get("type"):
        return source["type"]

    for location in work.get("locations") or []:
        source = (location or {}).get("source") or {}
        if source.get("type"):
            return source["type"]

    return ""


def landing_page_url(work: dict[str, Any]) -> str:
    doi = clean_doi(work.get("doi") or "")
    if doi and not is_arxiv_doi(doi):
        return f"https://doi.org/{doi}"

    primary = work.get("primary_location") or {}
    url = primary.get("landing_page_url") or ""
    if url and not is_arxiv_like(url):
        return url

    for location in work.get("locations") or []:
        url = (location or {}).get("landing_page_url") or ""
        if url and not is_arxiv_like(url):
            return url

    return ""


def is_published_candidate(work: dict[str, Any]) -> bool:
    doi = clean_doi(work.get("doi") or "")
    venue = source_name(work)
    url = landing_page_url(work)

    if doi and not is_arxiv_doi(doi):
        return True

    if venue and "arxiv" not in venue.lower():
        return True

    return bool(url and not is_arxiv_like(url))


def entry_is_arxivish(entry: BibEntry) -> bool:
    joined = " ".join(
        (
            entry.entry_type,
            entry.fields.get("doi", ""),
            entry.fields.get("url", ""),
            entry.fields.get("eprint", ""),
            entry.fields.get("journal", ""),
            entry.fields.get("booktitle", ""),
            entry.fields.get("note", ""),
        )
    )
    return is_arxiv_like(joined) or "preprint" in joined.lower()


def author_last_names_from_bib(author_field: str) -> set[str]:
    names = set()

    for author in re.split(r"\s+and\s+", author_field or ""):
        author = re.sub(r"[{}]", "", author).strip()
        if not author:
            continue

        if "," in author:
            last_name = author.split(",", 1)[0].strip()
        else:
            last_name = author.split()[-1].strip()

        names.add(normalize_text(last_name))

    return names


def author_last_names_from_work(work: dict[str, Any]) -> set[str]:
    names = set()

    for authorship in work.get("authorships") or []:
        author = authorship.get("author") or {}
        display_name = author.get("display_name") or ""

        if display_name:
            names.add(normalize_text(display_name.split()[-1]))

    return names


def candidate_score(entry: BibEntry, work: dict[str, Any]) -> tuple[float, str]:
    old_title = normalize_text(entry.fields.get("title", ""))
    new_title = normalize_text(work.get("display_name") or "")

    title_score = difflib.SequenceMatcher(None, old_title, new_title).ratio()

    old_year = entry.fields.get("year", "").strip()
    new_year = str(work.get("publication_year") or "").strip()
    year_bonus = 0.0

    if old_year and new_year:
        try:
            year_bonus = 0.04 if abs(int(old_year) - int(new_year)) <= 1 else -0.05
        except ValueError:
            year_bonus = 0.0

    old_authors = author_last_names_from_bib(entry.fields.get("author", ""))
    new_authors = author_last_names_from_work(work)
    author_bonus = 0.0

    if old_authors and new_authors:
        overlap = len(old_authors & new_authors) / max(
            1,
            min(len(old_authors), len(new_authors)),
        )
        author_bonus = min(0.10, overlap * 0.10)

    published_bonus = 0.10 if is_published_candidate(work) else -0.20
    score = max(0.0, min(1.0, title_score + year_bonus + author_bonus + published_bonus))

    reason = (
        f"title={title_score:.2f}; "
        f"year={year_bonus:.2f}; "
        f"authors={author_bonus:.2f}; "
        f"published={published_bonus:.2f}"
    )

    return score, reason


def best_candidate(entry: BibEntry) -> tuple[dict[str, Any] | None, float, str]:
    title = entry.fields.get("title", "")
    if not title:
        return None, 0.0, "missing title"

    try:
        candidates = openalex_search(title)
    except Exception as error:
        return None, 0.0, f"openalex error: {error}"

    print(f"[openalex] {entry.key}: {len(candidates)} candidates", flush=True)

    best_work = None
    best_score = 0.0
    best_reason = "no candidate"

    for candidate in candidates:
        if not is_published_candidate(candidate):
            continue

        score, reason = candidate_score(entry, candidate)
        if score > best_score:
            best_work = candidate
            best_score = score
            best_reason = reason

    return best_work, best_score, best_reason


def candidate_entry_type(work: dict[str, Any]) -> str:
    current_source_type = source_type(work).lower()
    work_type = (work.get("type") or "").lower()

    if current_source_type == "journal" or "article" in work_type:
        return "article"

    if "conference" in current_source_type or "proceedings" in current_source_type:
        return "inproceedings"

    return "misc"


def apply_candidate(entry: BibEntry, work: dict[str, Any]) -> None:
    old_arxiv_id = (
        entry.fields.get("eprint", "")
        or extract_arxiv_id(entry.fields.get("doi", ""))
        or extract_arxiv_id(entry.fields.get("url", ""))
    )

    doi = clean_doi(work.get("doi") or "")
    url = landing_page_url(work)
    venue = source_name(work)
    year = str(work.get("publication_year") or "").strip()
    biblio = work.get("biblio") or {}

    entry.entry_type = candidate_entry_type(work)

    if year:
        entry.fields["year"] = year

    if doi:
        entry.fields["doi"] = doi

    if url:
        entry.fields["url"] = url

    if venue:
        if entry.entry_type == "article":
            entry.fields.pop("booktitle", None)
            entry.fields["journal"] = venue
        elif entry.entry_type == "inproceedings":
            entry.fields.pop("journal", None)
            entry.fields["booktitle"] = venue
        else:
            entry.fields["howpublished"] = venue

    volume = str(biblio.get("volume") or "").strip()
    issue = str(biblio.get("issue") or "").strip()
    first_page = str(biblio.get("first_page") or "").strip()
    last_page = str(biblio.get("last_page") or "").strip()

    if volume:
        entry.fields["volume"] = volume

    if issue:
        entry.fields["number"] = issue

    if first_page and last_page:
        entry.fields["pages"] = f"{first_page}--{last_page}"
    elif first_page:
        entry.fields["pages"] = first_page

    if old_arxiv_id:
        entry.fields["eprint"] = old_arxiv_id
        entry.fields["archiveprefix"] = "arXiv"


def rebuild_content(content: str, changed_entries: list[BibEntry]) -> str:
    updated = content

    for entry in sorted(changed_entries, key=lambda item: item.start, reverse=True):
        updated = updated[: entry.start] + serialize_entry(entry) + updated[entry.end :]

    return updated


def write_report(root: Path, rows: list[list[str]]) -> Path:
    report_path = root / REPORT_PATH
    report_path.parent.mkdir(parents=True, exist_ok=True)

    report_path.write_text(
        "\n".join("\t".join(str(cell) for cell in row) for row in rows) + "\n",
        encoding="utf-8",
    )

    return report_path


def main() -> int:
    root = git_root()
    bib_path = find_bib_path(root)

    content = bib_path.read_text(encoding="utf-8")
    entries = parse_bib_entries(content)

    report_path = root / REPORT_PATH
    report_rows = [
        [
            "key",
            "action",
            "score",
            "old_doi",
            "new_doi",
            "old_url",
            "new_url",
            "old_venue",
            "new_venue",
            "reason",
        ]
    ]
    completed_keys: set[str] = set()
    if report_path.exists():
        with report_path.open(encoding="utf-8", newline="") as handle:
            previous_rows = list(csv.DictReader(handle, delimiter="\t"))
        for previous in previous_rows:
            if previous.get("action") in {
                "upgraded",
                "candidate_below_threshold",
                "no_published_candidate",
                "false_positive_reverted",
            }:
                completed_keys.add(previous.get("key", ""))
        report_rows.extend(
            [[row.get(column, "") for column in report_rows[0]] for row in previous_rows]
        )
        print(f"[openalex] loaded checkpoint: {len(completed_keys)} completed entries will be skipped", flush=True)

    changed_entries: list[BibEntry] = []

    arxiv_entries = [entry for entry in entries if entry_is_arxivish(entry)]
    print(f"[openalex] parsed {len(entries)} entries; processing {len(arxiv_entries)} arXiv-like entries", flush=True)
    for index, entry in enumerate(arxiv_entries, start=1):
        if entry.key in completed_keys:
            print(f"[openalex] [{index}/{len(arxiv_entries)}] {entry.key}: checkpoint skip", flush=True)
            continue
        print(f"[openalex] [{index}/{len(arxiv_entries)}] {entry.key}: {entry.fields.get('title', '')}", flush=True)
        old_doi = entry.fields.get("doi", "")
        old_url = entry.fields.get("url", "")
        old_venue = (
            entry.fields.get("journal")
            or entry.fields.get("booktitle")
            or entry.fields.get("howpublished", "")
        )

        candidate, score, reason = best_candidate(entry)
        print(f"[openalex] {entry.key}: score={score:.3f}; {reason}", flush=True)
        time.sleep(REQUEST_SLEEP_SECONDS)

        if candidate is None:
            report_rows.append(
                [
                    entry.key,
                    "no_published_candidate",
                    "",
                    old_doi,
                    "",
                    old_url,
                    "",
                    old_venue,
                    "",
                    reason,
                ]
            )
            write_report(root, report_rows)
            continue

        new_doi = clean_doi(candidate.get("doi") or "")
        new_url = landing_page_url(candidate)
        new_venue = source_name(candidate)

        if score < MIN_SCORE:
            report_rows.append(
                [
                    entry.key,
                    "candidate_below_threshold",
                    f"{score:.3f}",
                    old_doi,
                    new_doi,
                    old_url,
                    new_url,
                    old_venue,
                    new_venue,
                    reason,
                ]
            )
            write_report(root, report_rows)
            continue

        apply_candidate(entry, candidate)
        changed_entries.append(entry)

        report_rows.append(
            [
                entry.key,
                "upgraded",
                f"{score:.3f}",
                old_doi,
                entry.fields.get("doi", ""),
                old_url,
                entry.fields.get("url", ""),
                old_venue,
                entry.fields.get("journal")
                or entry.fields.get("booktitle")
                or entry.fields.get("howpublished", ""),
                reason,
            ]
        )
        completed_keys.add(entry.key)
        write_report(root, report_rows)

    report_path = write_report(root, report_rows)

    if not changed_entries:
        print("No BibTeX entries were upgraded.")
        print(f"BibTeX: {bib_path.relative_to(root)}")
        print(f"Report: {report_path.relative_to(root)}")
        return 0

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_path = bib_path.with_suffix(f".bib.bak.{timestamp}")
    shutil.copy2(bib_path, backup_path)

    updated_content = rebuild_content(content, changed_entries)
    bib_path.write_text(updated_content, encoding="utf-8")

    print(f"Updated entries: {len(changed_entries)}")
    print(f"BibTeX: {bib_path.relative_to(root)}")
    print(f"Backup: {backup_path.relative_to(root)}")
    print(f"Report: {report_path.relative_to(root)}")
    print()
    print("Review changes with:")
    print(f"  git diff -- {bib_path.relative_to(root)}")
    print(f"  column -t -s $'\\t' {report_path.relative_to(root)} | less -S")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
