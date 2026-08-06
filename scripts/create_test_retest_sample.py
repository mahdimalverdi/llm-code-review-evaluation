#!/usr/bin/env python3
"""Create a reproducible blinded test--retest coding worksheet."""

import argparse
import csv
import random
from pathlib import Path


FIELDS = [
    "paper_id",
    "citation_key",
    "title",
    "eligibility_retest",
    "evidence_tier_retest",
    "principal_failure_category_retest",
    "mitigation_family_retest",
    "usefulness_actionability_retest",
    "context_quality_retest",
    "retest_notes",
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=20260806)
    parser.add_argument("--sample-size", type=int, default=12)
    parser.add_argument("--input", type=Path, default=Path("data/slr-extraction.csv"))
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/supplement/test-retest-blinded-sample.csv"),
    )
    args = parser.parse_args()

    with args.input.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if args.sample_size > len(rows):
        raise SystemExit("sample size exceeds the number of extraction records")

    rng = random.Random(args.seed)
    sample = sorted(rng.sample(rows, args.sample_size), key=lambda row: row["paper_id"])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        for row in sample:
            writer.writerow({
                "paper_id": row["paper_id"],
                "citation_key": row["citation_key"],
                "title": row["title"],
            })
    print(f"wrote {len(sample)} blinded rows to {args.output}")


if __name__ == "__main__":
    main()
