#!/usr/bin/env python3
"""Resolve DOI candidates for records that currently have only a source URL.

The script never invents a DOI. It records direct URL/arXiv resolution first,
then uses cached Crossref/OpenAlex title searches with conservative matching.
Unresolved records are explicitly retained for manual investigation.
"""

from __future__ import annotations

import argparse
import csv
import json
import logging
import re
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path


DEFAULT_QUEUE = Path("data/search/candidate-full-text-acquisition-queue.csv")
DEFAULT_OUTPUT = Path("data/search/source-url-doi-resolution.csv")
DEFAULT_CACHE = Path("data/search/source-url-doi-cache.json")
DEFAULT_LOG = Path("data/search/source-url-doi-resolution.log")
USER_AGENT = "llm-code-review-evaluation/1.0 (mailto:research@example.invalid)"
DOI_PATTERN = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.IGNORECASE)
ARXIV_PATTERN = re.compile(r"(?:arxiv\.org/(?:abs|pdf)/|10\.48550/arxiv\.)((?:\d{4}\.\d{4,5}|[a-z-]+/[0-9]+)(?:v\d+)?)", re.IGNORECASE)


def read_rows(path: Path) -> list[dict[str, str]]:
    """Read UTF-8 CSV rows."""
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def normalize_doi(value: str) -> str:
    """Normalize a DOI or return an empty value for non-DOI placeholders."""
    match = DOI_PATTERN.search(value or "")
    if not match:
        return ""
    return match.group(0).rstrip(".,;)}]").lower()


def normalize_title(value: str) -> str:
    """Normalize a title for conservative similarity comparison."""
    return "".join(char.lower() for char in value if char.isalnum())


def fetch_json(url: str) -> dict[str, object]:
    """Fetch one JSON response."""
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def crossref_candidates(title: str) -> list[dict[str, object]]:
    """Query Crossref by title."""
    query = urllib.parse.urlencode({"query.bibliographic": title, "rows": 5})
    payload = fetch_json(f"https://api.crossref.org/works?{query}")
    return payload.get("message", {}).get("items", [])


def openalex_candidates(title: str) -> list[dict[str, object]]:
    """Query OpenAlex by title."""
    query = urllib.parse.urlencode({"search": title, "per-page": 5})
    payload = fetch_json(f"https://api.openalex.org/works?{query}")
    return payload.get("results", [])


def candidate_score(title: str, year: str, item: dict[str, object], provider: str) -> tuple[float, str]:
    """Score a provider candidate using title and publication year."""
    if provider == "crossref":
        candidate_title = str((item.get("title") or [""])[0])
        candidate_year = str(((item.get("published") or {}).get("date-parts") or [[""]])[0][0])
        doi = normalize_doi(str(item.get("DOI", "")))
    else:
        candidate_title = str(item.get("title", ""))
        candidate_year = str(item.get("publication_year", ""))
        doi = normalize_doi(str(item.get("doi", "")))
    score = SequenceMatcher(None, normalize_title(title), normalize_title(candidate_title)).ratio()
    if year and candidate_year and year[:4] == candidate_year[:4]:
        score += 0.08
    return score, doi


def atomic_write(path: Path, value: object) -> None:
    """Write JSON atomically."""
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def direct_resolution(row: dict[str, str]) -> tuple[str, str]:
    """Resolve DOI directly from the source URL or arXiv identifier."""
    direct_doi = normalize_doi(row.get("source_url", ""))
    if direct_doi:
        return direct_doi, "doi_in_source_url"
    match = ARXIV_PATTERN.search(" ".join((row.get("source_url", ""), row.get("arxiv_id", ""))))
    if match:
        return f"10.48550/arxiv.{match.group(1).lower().removesuffix('.pdf')}", "arxiv_identifier"
    return "", ""


def main() -> int:
    """Resolve and report DOI candidates for source-URL records."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--queue", type=Path, default=DEFAULT_QUEUE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--cache", type=Path, default=DEFAULT_CACHE)
    parser.add_argument("--log-file", type=Path, default=DEFAULT_LOG)
    parser.add_argument("--delay", type=float, default=0.5)
    args = parser.parse_args()

    args.log_file.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[logging.FileHandler(args.log_file, encoding="utf-8"), logging.StreamHandler()],
    )
    logger = logging.getLogger(__name__)
    cache = json.loads(args.cache.read_text(encoding="utf-8")) if args.cache.exists() else {}
    rows = [row for row in read_rows(args.queue) if row["acquisition_route"] == "source_url"]
    output: list[dict[str, str]] = []
    for index, row in enumerate(rows, start=1):
        direct_doi, direct_method = direct_resolution(row)
        if direct_doi:
            best_doi, method, status = direct_doi, direct_method, "resolved_directly"
            score = "1.0000"
        else:
            key = f"{row['title']}|{row['year']}"
            cached = cache.get(key)
            if cached is None:
                cached = {"crossref": [], "openalex": [], "errors": []}
                for provider, loader in (("crossref", crossref_candidates), ("openalex", openalex_candidates)):
                    try:
                        cached[provider] = loader(row["title"])
                    except Exception as error:  # provider failures are isolated and retried later
                        cached["errors"].append(f"{provider}: {type(error).__name__}")
                        logger.warning("provider failure candidate=%s provider=%s", row["candidate_id"], provider)
                    time.sleep(args.delay)
                if not cached["errors"]:
                    args.cache.parent.mkdir(parents=True, exist_ok=True)
                    cache[key] = cached
                    atomic_write(args.cache, cache)
            suggestions = []
            for provider in ("crossref", "openalex"):
                for item in cached.get(provider, []):
                    item_score, item_doi = candidate_score(row["title"], row["year"], item, provider)
                    if item_doi:
                        suggestions.append((item_score, item_doi, provider))
            suggestions.sort(reverse=True)
            best = suggestions[0] if suggestions else (0.0, "", "")
            second_score = suggestions[1][0] if len(suggestions) > 1 else 0.0
            confident = best[1] and best[0] >= 1.03 and best[0] - second_score >= 0.03
            best_doi = best[1] if confident else ""
            method = best[2] if confident else ""
            status = "resolved_by_metadata" if confident else "likely_no_doi_or_unresolved"
            score = f"{best[0]:.4f}"
        output.append({
            "candidate_id": row["candidate_id"], "title": row["title"], "year": row["year"],
            "source_url": row["source_url"], "proposed_doi": best_doi, "method": method,
            "score": score, "status": status, "lookup_errors": "; ".join(cached.get("errors", [])) if not direct_doi else "",
            "checked_at": datetime.now(timezone.utc).isoformat(),
        })
        logger.info("resolved %d/%d candidate=%s status=%s", index, len(rows), row["candidate_id"], status)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fields = list(output[0]) if output else []
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(output)
    print(json.dumps({"source_url_records": len(output), "resolved": sum(bool(r["proposed_doi"]) for r in output), "unresolved": sum(not r["proposed_doi"] for r in output)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
