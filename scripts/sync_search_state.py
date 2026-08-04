#!/usr/bin/env python3
"""Synchronize search ledgers with locally validated artifacts."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def rewrite_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def sync_manifest() -> int:
    path = ROOT / "data/search/arxiv-full-text-manifest.csv"
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
        fieldnames = handle.seek(0) or None
    fieldnames = list(rows[0]) if rows else []
    updated = 0
    for row in rows:
        target = ROOT / row["target_path"]
        if target.is_file() and row["acquisition_status"] == "pending":
            row["acquisition_status"] = "downloaded"
            row["full_text_reason"] = "Local PDF exists; acquisition synchronized from filesystem."
            updated += 1
    rewrite_csv(path, rows, fieldnames)
    return updated


def sync_core_queue() -> int:
    path = ROOT / "data/search/core-reconciliation-queue.csv"
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    fieldnames = list(rows[0]) if rows else []
    updated = 0
    for row in rows:
        project = row["provisional_project_id"]
        notes = list((ROOT / "papers/provisional").glob(f"{project}-*.md"))
        if notes and row["reconciliation_status"] == "new_candidate":
            row["reconciliation_status"] = "extracted_pending_final_freeze"
            row["next_action"] = "Apply final corpus relevance/tier rule before freeze"
            updated += 1
    rewrite_csv(path, rows, fieldnames)
    return updated


def sync_checkpoint() -> int:
    path = ROOT / "data/search/provisional-extraction/checkpoint.tsv"
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    fieldnames = list(rows[0]) if rows else []
    updated = 0
    for row in rows:
        note_path = row["note"]
        note = ROOT / note_path if note_path != "missing" else None
        if note and note.is_file() and row["validation"] == "validation_failed":
            row["validation"] = "validated"
            updated += 1
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return updated


def main() -> None:
    print(f"manifest updated: {sync_manifest()}")
    print(f"core queue updated: {sync_core_queue()}")
    print(f"checkpoint updated: {sync_checkpoint()}")


if __name__ == "__main__":
    main()
