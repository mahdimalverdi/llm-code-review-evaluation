#!/usr/bin/env python3
"""Create the review worksheet for retained full-text search candidates."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    with args.manifest.open(encoding="utf-8", newline="") as handle:
        manifest = list(csv.DictReader(handle))

    fields = (
        "candidate_id", "title", "arxiv_id", "source", "full_text_path",
        "acquisition_status", "full_text_decision", "inclusion_group",
        "exact_criterion", "evidence_location", "decision_rationale",
        "duplicate_or_companion", "screening_reviewer", "screening_date",
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in manifest:
            pdf = Path(row["target_path"])
            acquisition_status = "downloaded_valid_pdf" if pdf.exists() and pdf.read_bytes()[:5] == b"%PDF-" else "acquisition_failed"
            writer.writerow({
                "candidate_id": row["candidate_id"],
                "title": row["title"],
                "arxiv_id": row["arxiv_id"],
                "source": row["source"],
                "full_text_path": row["target_path"],
                "acquisition_status": acquisition_status,
                "full_text_decision": "pending",
                "inclusion_group": "",
                "exact_criterion": "",
                "evidence_location": "",
                "decision_rationale": "",
                "duplicate_or_companion": "",
                "screening_reviewer": "",
                "screening_date": "",
            })


if __name__ == "__main__":
    main()
