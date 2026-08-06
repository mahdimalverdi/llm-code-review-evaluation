#!/usr/bin/env python3
"""Apply only high-confidence DOI suggestions to the unified candidate pool."""

from __future__ import annotations

import argparse
import csv
import shutil
from datetime import datetime
from pathlib import Path


DEFAULT_POOL = Path("data/search/unified-candidate-pool.csv")
DEFAULT_ENRICHMENT = Path("data/search/doi-enrichment.csv")
DEFAULT_REPORT = Path("data/search/high-confidence-doi-application.csv")


def read_rows(path: Path) -> list[dict[str, str]]:
    """Read CSV rows."""
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    """Apply DOI suggestions without overwriting existing DOI values."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--pool", type=Path, default=DEFAULT_POOL)
    parser.add_argument("--enrichment", type=Path, default=DEFAULT_ENRICHMENT)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    rows = read_rows(args.pool)
    suggestions = {
        row["candidate_id"]: row
        for row in read_rows(args.enrichment)
        if row.get("status") == "high_confidence_suggestion" and row.get("proposed_doi")
    }
    report = []
    changed = 0
    for row in rows:
        suggestion = suggestions.get(row["candidate_id"])
        old_doi = row.get("doi", "")
        new_doi = old_doi
        decision = "not_selected"
        if suggestion and old_doi:
            decision = "existing_doi_preserved"
        elif suggestion:
            new_doi = suggestion["proposed_doi"]
            decision = "apply" if args.apply else "would_apply"
            if args.apply:
                row["doi"] = new_doi
                changed += 1
        report.append({
            "candidate_id": row["candidate_id"],
            "old_doi": old_doi,
            "proposed_doi": suggestion.get("proposed_doi", "") if suggestion else "",
            "decision": decision,
        })

    args.report.parent.mkdir(parents=True, exist_ok=True)
    with args.report.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(report[0]))
        writer.writeheader()
        writer.writerows(report)
    if args.apply and changed:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        shutil.copy2(args.pool, args.pool.with_suffix(f".csv.bak.{timestamp}"))
        fields = list(rows[0])
        with args.pool.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)
    print(f"High-confidence DOI suggestions: {len(suggestions)}")
    print(f"Pool rows changed: {changed}")
    print(f"Report: {args.report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
