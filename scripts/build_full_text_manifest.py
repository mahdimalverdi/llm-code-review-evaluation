#!/usr/bin/env python3
"""Build a full-text acquisition manifest for candidates retained after screening."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


def safe_component(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", value)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--screening", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--pdf-dir", required=True, type=Path)
    args = parser.parse_args()

    with args.screening.open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["title_abstract_decision"] == "include_full_text"]

    fields = (
        "candidate_id", "arxiv_id", "title", "source", "pdf_url", "target_path",
        "acquisition_status", "full_text_decision", "full_text_reason",
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            arxiv_id = row["doi_or_identifier"]
            versionless = arxiv_id.split("v", 1)[0]
            target = args.pdf_dir / f"{row['candidate_id']}_{safe_component(versionless)}.pdf"
            writer.writerow({
                "candidate_id": row["candidate_id"],
                "arxiv_id": arxiv_id,
                "title": row["title"],
                "source": row["source"],
                "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}",
                "target_path": str(target),
                "acquisition_status": "pending",
                "full_text_decision": "pending",
                "full_text_reason": "",
            })


if __name__ == "__main__":
    main()
