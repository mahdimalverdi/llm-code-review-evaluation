#!/usr/bin/env python3
"""Merge conservative automated triage with recorded manual screening decisions."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--triage", required=True, type=Path)
    parser.add_argument("--manual", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    triage = read_rows(args.triage)
    manual = {row["candidate_id"]: row for row in read_rows(args.manual)}
    triage_ids = {row["candidate_id"] for row in triage}
    unknown = set(manual) - triage_ids
    if unknown:
        raise SystemExit(f"Manual decisions contain unknown candidate IDs: {sorted(unknown)}")

    for row in triage:
        override = manual.get(row["candidate_id"])
        if override:
            row["title_abstract_decision"] = override["title_abstract_decision"]
            row["exclusion_reason"] = override["exclusion_reason"]
            row["decision_basis"] = override["decision_basis"]
            row["screening_reviewer"] = override["screening_reviewer"]

    remaining = [row["candidate_id"] for row in triage if row["title_abstract_decision"] == "uncertain_full_text"]
    if remaining:
        raise SystemExit(f"Candidates still lack a title/abstract decision: {remaining}")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(triage[0]))
        writer.writeheader()
        writer.writerows(triage)


if __name__ == "__main__":
    main()
