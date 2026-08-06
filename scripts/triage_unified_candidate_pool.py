#!/usr/bin/env python3
"""Prepare conservative title/abstract screening for the unified pool.

This script may identify obvious duplicates and obvious non-code-review records,
but it never includes a new study automatically. Records without an abstract or
usable snippet remain pending manual verification.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


REVIEW_SIGNAL = re.compile(
    r"code[- ]review|review comment|pull request|merge request|software review|"
    r"automated review|ai-assisted code",
    re.IGNORECASE,
)
SCIENTIFIC_REVIEW = re.compile(
    r"scientific (?:peer )?review|manuscript review|reviewer feedback.*manuscript",
    re.IGNORECASE,
)


def read_rows(path: Path) -> list[dict[str, str]]:
    """Read UTF-8 CSV rows."""
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    """Create a screening sheet without making new inclusion decisions."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--pool", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    rows = read_rows(args.pool)
    fields = [
        "candidate_id", "title", "authors", "year", "venue", "doi", "arxiv_id",
        "source_url", "source_databases", "source_record_ids", "abstract_or_snippet",
        "evidence_availability", "existing_paper_id", "screening_status",
        "title_abstract_decision", "exclusion_reason", "decision_basis",
        "screening_reviewer", "screening_date",
    ]
    output: list[dict[str, str]] = []
    for row in rows:
        text = f"{row['title']} {row['abstract_or_snippet']}".strip()
        decision = "pending_manual_screening"
        reason = ""
        basis = "Requires human title/abstract verification before full-text screening."
        if row["existing_paper_id"]:
            decision = "duplicate_or_version_of_existing"
            reason = "duplicate/companion"
            basis = "Identity cluster matches a frozen corpus record; verify version relationship."
        elif row["evidence_availability"] == "metadata_only":
            decision = "pending_metadata_only"
            basis = "No abstract or usable snippet was retained; acquire abstract/full text before deciding."
        elif SCIENTIFIC_REVIEW.search(text) and not re.search(
            r"software (?:code )?review|code review|pull request|merge request", text, re.IGNORECASE
        ):
            decision = "exclude_title_abstract"
            reason = "no review-feedback connection"
            basis = "The available text concerns scientific manuscript peer review rather than software code review."
        elif not REVIEW_SIGNAL.search(text):
            decision = "exclude_title_abstract"
            reason = "no review-feedback connection"
            basis = "The available title and abstract/snippet do not indicate a software code-review connection."
        output.append({
            field: row.get(field, "") for field in fields[:-5]
        } | {
            "title_abstract_decision": decision,
            "exclusion_reason": reason,
            "decision_basis": basis,
            "screening_reviewer": "Codex (conservative rule-based triage)",
            "screening_date": "2026-08-06",
        })

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(output)
    counts: dict[str, int] = {}
    for row in output:
        decision = row["title_abstract_decision"]
        counts[decision] = counts.get(decision, 0) + 1
    print(counts)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
