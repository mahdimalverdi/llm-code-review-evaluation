#!/usr/bin/env python3
"""Merge recorded full-text decisions into the acquisition worksheet."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--worksheet", required=True, type=Path)
    parser.add_argument("--manual", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    worksheet = read_rows(args.worksheet)
    manual = {row["candidate_id"]: row for row in read_rows(args.manual)}
    worksheet_ids = {row["candidate_id"] for row in worksheet}
    unknown = set(manual) - worksheet_ids
    if unknown:
        raise SystemExit(f"Manual decisions contain unknown candidate IDs: {sorted(unknown)}")

    fields = [
        "full_text_decision",
        "inclusion_group",
        "exact_criterion",
        "evidence_location",
        "decision_rationale",
        "duplicate_or_companion",
        "screening_reviewer",
        "screening_date",
    ]
    for row in worksheet:
        decision = manual.get(row["candidate_id"])
        if decision:
            for field in fields:
                row[field] = decision[field]

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(worksheet[0]))
        writer.writeheader()
        writer.writerows(worksheet)


if __name__ == "__main__":
    main()
