#!/usr/bin/env python3

import argparse
import csv
import re
import shutil
from datetime import datetime
from pathlib import Path
from urllib.request import Request, urlopen


DEFAULT_SPREADSHEET_ID = "14tTs2nwIwS40JU-na5bbwBNgyPYkZv9IPXVPfbPUR1I"
PAPER_POOL_GID = "0"
DEFAULT_BIB_PATH = "references/references.bib"


def sheet_csv_url(spreadsheet_id: str, gid: str) -> str:
    return (
        f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export"
        f"?format=csv&gid={gid}"
    )


def read_csv_from_url(url: str) -> list[dict[str, str]]:
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(request, timeout=60) as response:
        content = response.read().decode("utf-8-sig")

    return list(csv.DictReader(content.splitlines()))


def read_csv_from_file(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def clean(value: str | None) -> str:
    return (value or "").strip()


def bib_escape(value: str) -> str:
    value = clean(value)
    value = value.replace("\\", "\\textbackslash{}")
    value = value.replace("&", "\\&")
    value = value.replace("%", "\\%")
    value = value.replace("$", "\\$")
    value = value.replace("#", "\\#")
    value = value.replace("_", "\\_")
    return value


def normalize_authors(row: dict[str, str]) -> str:
    full_author_list = clean(row.get("Full Author List"))
    if full_author_list:
        authors = [author.strip() for author in full_author_list.split(",") if author.strip()]
        return " and ".join(authors)

    author_columns = [
        "Authors",
        "Authors.1",
        "Authors.2",
        "Authors.3",
        "Authors.4",
        "Authors.5",
        "Authors.6",
        "Authors.7",
    ]
    authors = [clean(row.get(column)) for column in author_columns if clean(row.get(column))]
    first_author = clean(row.get("First Author"))
    if not authors and first_author:
        authors = [first_author]

    return " and ".join(authors)


def source_url(row: dict[str, str]) -> str:
    return (
        clean(row.get("Official Publication URL"))
        or clean(row.get("Source URL"))
        or clean(row.get("PDF URL"))
    )


def entry_type(row: dict[str, str]) -> str:
    peer_status = clean(row.get("Peer-Reviewed Status")).lower()
    venue = clean(row.get("Venue / Source")).lower()
    study_type = clean(row.get("Study Type")).lower()

    if "book" in peer_status or "book" in venue:
        return "book"

    if "journal" in peer_status or "journal" in venue:
        return "article"

    if (
        "conference" in peer_status
        or "conference" in venue
        or "proceedings" in venue
        or "icse" in venue
        or "fse" in venue
        or "ase" in venue
        or "msr" in venue
        or "scam" in venue
        or "issre" in venue
        or "acl" in venue
    ):
        return "inproceedings"

    if "survey" in study_type and "arxiv" not in venue:
        return "article"

    return "misc"


def venue_field_name(entry_kind: str) -> str:
    if entry_kind == "article":
        return "journal"
    if entry_kind == "inproceedings":
        return "booktitle"
    if entry_kind == "book":
        return "publisher"
    return "howpublished"


def make_bib_entry(row: dict[str, str]) -> str | None:
    key = clean(row.get("BibTeX Key"))
    title = clean(row.get("Title"))
    year = clean(row.get("Year"))

    if not key or not title or not year:
        return None

    kind = entry_type(row)
    authors = normalize_authors(row)
    venue = clean(row.get("Venue / Source")) or clean(row.get("Journal/Conference Name"))
    doi = clean(row.get("DOI"))
    arxiv_id = clean(row.get("arXiv ID"))
    url = source_url(row)
    pdf_url = clean(row.get("PDF URL"))
    note = clean(row.get("Reference Notes")) or clean(row.get("Notes"))

    fields: list[tuple[str, str]] = [
        ("title", title),
        ("author", authors),
        ("year", year),
    ]

    if venue:
        fields.append((venue_field_name(kind), venue))

    if doi:
        fields.append(("doi", doi))

    if arxiv_id:
        fields.append(("eprint", arxiv_id))
        fields.append(("archivePrefix", "arXiv"))

    if url:
        fields.append(("url", url))

    if pdf_url and pdf_url != url:
        fields.append(("pdf", pdf_url))

    if note:
        fields.append(("note", note))

    lines = [f"@{kind}{{{key},"]
    for field_name, field_value in fields:
        if not clean(field_value):
            continue
        lines.append(f"  {field_name} = {{{bib_escape(field_value)}}},")
    lines[-1] = lines[-1].rstrip(",")
    lines.append("}")

    return "\n".join(lines)


def find_bib_entries(content: str) -> dict[str, tuple[int, int, str]]:
    entries: dict[str, tuple[int, int, str]] = {}
    index = 0

    while True:
        match = re.search(r"@\w+\s*\{\s*([^,\s]+)\s*,", content[index:])
        if not match:
            break

        start = index + match.start()
        key = match.group(1)
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

        entries[key] = (start, end, content[start:end])
        index = end

    return entries


def update_bib_content(existing_content: str, generated_entries: dict[str, str]) -> str:
    existing_entries = find_bib_entries(existing_content)
    updated_content = existing_content

    replacements: list[tuple[int, int, str]] = []

    for key, new_entry in generated_entries.items():
        if key in existing_entries:
            start, end, _ = existing_entries[key]
            replacements.append((start, end, new_entry))

    for start, end, replacement in sorted(replacements, reverse=True):
        updated_content = updated_content[:start] + replacement + updated_content[end:]

    missing_entries = [
        entry
        for key, entry in generated_entries.items()
        if key not in existing_entries
    ]

    if missing_entries:
        if updated_content and not updated_content.endswith("\n"):
            updated_content += "\n"
        updated_content += "\n% Entries synced from Paper Pool sheet\n"
        updated_content += "\n\n".join(missing_entries)
        updated_content += "\n"

    return updated_content


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--spreadsheet-id", default=DEFAULT_SPREADSHEET_ID)
    parser.add_argument("--gid", default=PAPER_POOL_GID)
    parser.add_argument("--csv", type=Path, help="Use a local Paper Pool CSV instead of Google Sheets export")
    parser.add_argument("--bib", type=Path, default=Path(DEFAULT_BIB_PATH))
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--only-included", action="store_true", help="Skip rows not marked as included")
    args = parser.parse_args()

    if args.csv:
        rows = read_csv_from_file(args.csv)
    else:
        rows = read_csv_from_url(sheet_csv_url(args.spreadsheet_id, args.gid))

    generated_entries: dict[str, str] = {}

    skipped = []
    for row in rows:
        included_value = clean(row.get("Included (Yes)/Excluded (No)")).lower()
        if args.only_included and included_value not in {"yes", "included", ""}:
            skipped.append((clean(row.get("ID")), "not included"))
            continue

        entry = make_bib_entry(row)
        if not entry:
            skipped.append((clean(row.get("ID")), "missing BibTeX Key / Title / Year"))
            continue

        key = clean(row.get("BibTeX Key"))
        generated_entries[key] = entry

    existing_content = args.bib.read_text(encoding="utf-8") if args.bib.exists() else ""
    updated_content = update_bib_content(existing_content, generated_entries)

    existing_keys = set(find_bib_entries(existing_content).keys())
    generated_keys = set(generated_entries.keys())

    added = sorted(generated_keys - existing_keys)
    updated = sorted(generated_keys & existing_keys)

    print(f"Generated entries: {len(generated_entries)}")
    print(f"Updated existing entries: {len(updated)}")
    print(f"Added new entries: {len(added)}")
    print(f"Skipped rows: {len(skipped)}")

    if added:
        print("\nAdded keys:")
        for key in added:
            print(f"- {key}")

    if skipped:
        print("\nSkipped rows:")
        for paper_id, reason in skipped:
            print(f"- {paper_id or 'UNKNOWN'}: {reason}")

    if args.dry_run:
        print("\nDry run only. No file was changed.")
        return 0

    args.bib.parent.mkdir(parents=True, exist_ok=True)

    if args.bib.exists():
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        backup_path = args.bib.with_suffix(f".bib.bak.{timestamp}")
        shutil.copy2(args.bib, backup_path)
        print(f"\nBackup written to: {backup_path}")

    args.bib.write_text(updated_content, encoding="utf-8")
    print(f"Updated: {args.bib}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())