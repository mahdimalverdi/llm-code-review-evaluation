#!/usr/bin/env python3
"""Build a provisional queue for unmatched core arXiv candidates."""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def arxiv_key(value: str) -> str:
    match = re.search(r"([0-9]{4}\\.[0-9]{4,5})", value)
    return match.group(1) if match else value


def main() -> None:
    reconciliation = read_csv(ROOT / "data/search/arxiv-reconciliation.csv")
    candidates = {
        arxiv_key(row["arxiv_id"]): row
        for row in read_csv(ROOT / "data/search/arxiv-candidates.csv")
    }
    core = [
        row
        for row in reconciliation
        if row["screening_tier"] == "core"
        and row["reconciliation_status"] == "new_candidate"
    ]
    first_id = 72
    output: list[dict[str, str]] = []
    for offset, row in enumerate(core):
        metadata = candidates.get(arxiv_key(row["arxiv_id"]), {})
        output.append(
            {
                "provisional_project_id": f"P{first_id + offset:02d}",
                "candidate_id": row["candidate_id"],
                "arxiv_id": row["arxiv_id"],
                "title": row["title"],
                "authors": metadata.get("authors", ""),
                "submitted": metadata.get("published", ""),
                "full_text_path": metadata.get("full_text_path", ""),
                "screening_tier": row["screening_tier"],
                "reconciliation_status": row["reconciliation_status"],
                "metadata_status": "local_arxiv_metadata" if metadata else "metadata_missing",
                "next_action": "verify duplicate/version, then create canonical note and BibTeX",
            }
        )
    output_path = ROOT / "data/search/core-reconciliation-queue.csv"
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0]))
        writer.writeheader()
        writer.writerows(output)
    print(f"wrote {len(output)} provisional core records to {output_path}")


if __name__ == "__main__":
    main()
