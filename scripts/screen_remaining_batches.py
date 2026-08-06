#!/usr/bin/env python3
"""Create conservative preliminary decisions for unreviewed screening batches."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


DEFAULT_BATCH_DIR = Path("data/search/screening-batches")
REVIEW_SIGNAL = re.compile(
    r"code[- ]review|review comment|pull request|merge request|review agent|"
    r"automated review|ai-assisted review|code reviewer|review feedback",
    re.IGNORECASE,
)
NON_REVIEW_SIGNAL = re.compile(
    r"peer review(?!.*code)|scientific paper|code generation|code repair|"
    r"vulnerability detection|software testing|coding agent|software development",
    re.IGNORECASE,
)


def read_rows(path: Path) -> list[dict[str, str]]:
    """Read CSV rows."""
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def classify(row: dict[str, str]) -> tuple[str, str]:
    """Return a conservative preliminary decision and rationale."""
    text = f"{row['title']} {row['abstract_or_snippet']}"
    if REVIEW_SIGNAL.search(text):
        return (
            "include_full_text_candidate",
            "Title/abstract contains a direct software code-review signal; verify eligibility in full text.",
        )
    if NON_REVIEW_SIGNAL.search(text):
        return (
            "exclude_title_abstract",
            "Available title/abstract indicates adjacent software-engineering work without a direct review signal.",
        )
    return (
        "uncertain",
        "The available metadata are insufficient for a reliable eligibility decision.",
    )


def main() -> int:
    """Process batches without an existing decision file."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-dir", type=Path, default=DEFAULT_BATCH_DIR)
    args = parser.parse_args()
    total = 0
    for batch_path in sorted(args.batch_dir.glob("batch-[0-9][0-9][0-9].csv")):
        output_path = batch_path.with_name(f"{batch_path.stem}-decisions.csv")
        if output_path.exists():
            continue
        rows = read_rows(batch_path)
        fields = ["candidate_id", "title_abstract_decision", "decision_rationale",
                  "screening_reviewer", "screening_date"]
        decisions = []
        for row in rows:
            decision, rationale = classify(row)
            decisions.append({
                "candidate_id": row["candidate_id"],
                "title_abstract_decision": decision,
                "decision_rationale": rationale,
                "screening_reviewer": "Codex-assisted preliminary screen",
                "screening_date": "2026-08-06",
            })
        with output_path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(decisions)
        total += len(decisions)
    print(f"Processed remaining preliminary batches: {total} records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
