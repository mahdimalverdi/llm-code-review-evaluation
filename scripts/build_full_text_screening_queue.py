#!/usr/bin/env python3
"""Build a full-text screening queue from title/abstract decisions.

The queue contains only records that still require human review. It does not
infer eligibility or promote any candidate into the synthesis corpus.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


DEFAULT_INPUT = Path("data/search/unified-title-abstract-screening.csv")
DEFAULT_OUTPUT = Path("data/search/full-text-screening-queue.csv")
PENDING_DECISIONS = {"pending_manual_screening", "pending_metadata_only"}


def read_rows(path: Path) -> list[dict[str, str]]:
    """Read screening rows from a UTF-8 CSV file."""
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    """Write the pending full-text screening queue."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    rows = read_rows(args.input)
    queue = [
        {
            "candidate_id": row["candidate_id"],
            "title": row["title"],
            "authors": row["authors"],
            "year": row["year"],
            "venue": row["venue"],
            "doi": row["doi"],
            "arxiv_id": row["arxiv_id"],
            "source_url": row["source_url"],
            "source_databases": row["source_databases"],
            "abstract_or_snippet": row["abstract_or_snippet"],
            "evidence_availability": row["evidence_availability"],
            "title_abstract_decision": row["title_abstract_decision"],
            "full_text_status": "pending_acquisition",
            "full_text_decision": "",
            "exclusion_reason": "",
            "decision_rationale": "",
            "screening_reviewer": "",
            "screening_date": "",
        }
        for row in rows
        if row["title_abstract_decision"] in PENDING_DECISIONS
    ]
    fields = list(queue[0]) if queue else [
        "candidate_id", "title", "authors", "year", "venue", "doi", "arxiv_id",
        "source_url", "source_databases", "abstract_or_snippet",
        "evidence_availability", "title_abstract_decision", "full_text_status",
        "full_text_decision", "exclusion_reason", "decision_rationale",
        "screening_reviewer", "screening_date",
    ]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(queue)
    print(f"Full-text screening queue: {len(queue)} records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
