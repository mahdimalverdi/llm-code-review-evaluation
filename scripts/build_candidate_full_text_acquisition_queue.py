#!/usr/bin/env python3
"""Build an acquisition queue for externally screened candidates."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


DEFAULT_POOL = Path("data/search/unified-candidate-pool.csv")
DEFAULT_BATCH_DIR = Path("data/search/screening-batches")
DEFAULT_OUTPUT = Path("data/search/candidate-full-text-acquisition-queue.csv")
DEFAULT_MANIFEST = Path("data/search/arxiv-full-text-manifest.csv")
TARGET_DECISIONS = {"include_full_text_candidate", "uncertain"}


def read_rows(path: Path) -> list[dict[str, str]]:
    """Read CSV rows."""
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def route(row: dict[str, str]) -> str:
    """Choose the cheapest reproducible acquisition route."""
    if row.get("arxiv_id"):
        return "arxiv_pdf"
    if row.get("doi"):
        return "doi_or_publisher"
    return "source_url"


def main() -> int:
    """Write the pending full-text acquisition queue."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--pool", type=Path, default=DEFAULT_POOL)
    parser.add_argument("--batch-dir", type=Path, default=DEFAULT_BATCH_DIR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--arxiv-manifest", type=Path, default=DEFAULT_MANIFEST)
    args = parser.parse_args()

    pool = {row["candidate_id"]: row for row in read_rows(args.pool)}
    arxiv_manifest = {
        row["arxiv_id"].lower().split("v")[0]: row
        for row in read_rows(args.arxiv_manifest)
    } if args.arxiv_manifest.exists() else {}
    decisions: dict[str, dict[str, str]] = {}
    for path in sorted(args.batch_dir.glob("batch-*-decisions.csv")):
        for row in read_rows(path):
            if row["title_abstract_decision"] in TARGET_DECISIONS:
                decisions[row["candidate_id"]] = row

    fields = [
        "candidate_id", "title", "year", "doi", "arxiv_id", "source_url",
        "authors", "venue", "source_databases", "abstract_or_snippet",
        "title_abstract_decision", "decision_rationale", "acquisition_route",
        "acquisition_status", "full_text_path", "full_text_decision",
        "full_text_reason", "screening_reviewer", "screening_date",
    ]
    output = []
    for candidate_id, decision in sorted(decisions.items()):
        row = pool[candidate_id]
        manifest_row = arxiv_manifest.get(row.get("arxiv_id", "").lower().split("v")[0])
        already_downloaded = bool(
            manifest_row
            and manifest_row.get("acquisition_status", "").startswith("download")
            and Path(manifest_row.get("target_path", "")).exists()
        )
        output.append({
            field: row.get(field, "") for field in fields[:11]
        } | {
            "title_abstract_decision": decision["title_abstract_decision"],
            "decision_rationale": decision["decision_rationale"],
            "acquisition_route": route(row),
            "acquisition_status": "already_downloaded" if already_downloaded else "pending",
            "full_text_path": manifest_row.get("target_path", "") if already_downloaded else "",
            "full_text_decision": "pending",
            "full_text_reason": "",
            "screening_reviewer": decision["screening_reviewer"],
            "screening_date": decision["screening_date"],
        })
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(output)
    print(f"Candidate full-text acquisition queue: {len(output)} records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
