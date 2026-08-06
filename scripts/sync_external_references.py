#!/usr/bin/env python3
"""Prepare vetted external search records for the canonical bibliography.

The script combines the unified candidate pool with DOI enrichment results,
deduplicates by DOI or normalized title, and adds only high-confidence DOI
suggestions.  It is a dry run by default; use ``--apply`` after reviewing the
generated report.
"""

from __future__ import annotations

import argparse
import csv
import html
import re
import shutil
from datetime import datetime
from pathlib import Path

from update_references_from_sheet import find_bib_entries


DEFAULT_POOL = Path("data/search/unified-candidate-pool.csv")
DEFAULT_ENRICHMENT = Path("data/search/doi-enrichment.csv")
DEFAULT_BIB = Path("references/references.bib")
DEFAULT_REPORT = Path("data/search/external-reference-sync-report.csv")


def read_csv(path: Path) -> list[dict[str, str]]:
    """Read a UTF-8 CSV file."""
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def normalize_doi(value: str) -> str:
    """Return a comparable DOI string."""
    value = value.strip().lower()
    value = re.sub(r"^(https?://)?(dx\.)?doi\.org/", "", value)
    return "" if value in {"", "none", "null", "nan"} else value.strip(" .;,)")


def normalize_title(value: str) -> str:
    """Return a comparable title string."""
    return "".join(char.lower() for char in value if char.isalnum())


def bib_dois_and_titles(content: str) -> tuple[set[str], set[str]]:
    """Extract DOI and title identities from existing BibTeX entries."""
    dois: set[str] = set()
    titles: set[str] = set()
    for _, _, entry in find_bib_entries(content).values():
        doi_match = re.search(r"^\s*doi\s*=\s*\{([^}]+)", entry, re.MULTILINE | re.IGNORECASE)
        title_match = re.search(r"^\s*title\s*=\s*\{([^}]+)", entry, re.MULTILINE | re.IGNORECASE)
        if doi_match:
            dois.add(normalize_doi(doi_match.group(1)))
        if title_match:
            titles.add(normalize_title(title_match.group(1)))
    return dois, titles


def bib_escape(value: str) -> str:
    """Escape common BibTeX special characters."""
    value = html.unescape(value)
    return (value.replace("\\", "\\textbackslash{}")
            .replace("&", "\\&")
            .replace("%", "\\%")
            .replace("_", "\\_"))


def normalize_authors(value: str) -> str:
    """Convert source-specific semicolon author lists to BibTeX syntax."""
    return " and ".join(part.strip() for part in value.split(";") if part.strip())


def make_entry(row: dict[str, str], doi: str) -> tuple[str, str]:
    """Create a stable BibTeX entry and key from a pool record."""
    candidate_id = row["candidate_id"].lower().replace("-", "_")
    key = f"ext_{candidate_id}"
    fields = [
        ("title", row["title"]),
        ("author", normalize_authors(row.get("authors", ""))),
        ("year", row.get("year", "")),
        ("journal", row.get("venue", "")),
        ("doi", doi),
        ("url", row.get("source_url", "")),
        ("note", f"External candidate {row['candidate_id']}; sources: "
                 f"{row.get('source_databases', '')}"),
    ]
    entry_type = "article" if row.get("venue", "").strip() else "misc"
    lines = [f"@{entry_type}{{{key},"]
    for name, value in fields:
        if value.strip():
            lines.append(f"  {name} = {{{bib_escape(value.strip())}}},")
    lines[-1] = lines[-1].rstrip(",")
    lines.append("}")
    return key, "\n".join(lines)


def main() -> int:
    """Generate or apply external bibliography additions."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--pool", type=Path, default=DEFAULT_POOL)
    parser.add_argument("--enrichment", type=Path, default=DEFAULT_ENRICHMENT)
    parser.add_argument("--bib", type=Path, default=DEFAULT_BIB)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    pool = {row["candidate_id"]: row for row in read_csv(args.pool)}
    enrichment = read_csv(args.enrichment)
    bib_content = args.bib.read_text(encoding="utf-8") if args.bib.exists() else ""
    existing_dois, existing_titles = bib_dois_and_titles(bib_content)
    selected: list[dict[str, str]] = []
    report: list[dict[str, str]] = []
    seen_dois: set[str] = set()
    seen_titles: set[str] = set()

    for item in enrichment:
        candidate = pool.get(item["candidate_id"])
        doi = normalize_doi(item.get("proposed_doi", ""))
        reason = "selected"
        if item.get("status") != "high_confidence_suggestion":
            reason = "not_high_confidence"
        elif not candidate or not doi:
            reason = "missing_candidate_or_doi"
        elif doi in existing_dois or doi in seen_dois:
            reason = "duplicate_doi"
        elif normalize_title(candidate["title"]) in existing_titles | seen_titles:
            reason = "duplicate_title"
        else:
            seen_dois.add(doi)
            seen_titles.add(normalize_title(candidate["title"]))
            selected.append({"candidate": candidate["candidate_id"], "doi": doi})
        report.append({"candidate_id": item["candidate_id"], "proposed_doi": doi,
                       "status": item.get("status", ""), "decision": reason})

    args.report.parent.mkdir(parents=True, exist_ok=True)
    with args.report.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(report[0]) if report else
                                ["candidate_id", "proposed_doi", "status", "decision"])
        writer.writeheader()
        writer.writerows(report)

    entries = [make_entry(pool[item["candidate"]], item["doi"])[1] for item in selected]
    print(f"Selected new references: {len(entries)}")
    print(f"Report: {args.report}")
    if not args.apply:
        print("Dry run only. Use --apply after reviewing the report.")
        return 0

    if entries:
        updated = bib_content.rstrip() + "\n\n% External candidates synced after DOI review\n"
        updated += "\n\n".join(entries) + "\n"
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        shutil.copy2(args.bib, args.bib.with_suffix(f".bib.bak.{timestamp}"))
        args.bib.write_text(updated, encoding="utf-8")
    print(f"Updated: {args.bib}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
