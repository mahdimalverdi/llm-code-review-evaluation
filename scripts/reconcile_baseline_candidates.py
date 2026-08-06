#!/usr/bin/env python3
"""Reconcile exact-title matches between the baseline and candidate pool."""

from __future__ import annotations

import argparse
import csv
import shutil
from datetime import datetime
from pathlib import Path


DEFAULT_BASELINE = Path("data/historical-baseline-inventory.csv")
DEFAULT_POOL = Path("data/search/unified-candidate-pool.csv")
DEFAULT_REPORT = Path("data/search/baseline-candidate-reconciliation.csv")


def read_rows(path: Path) -> list[dict[str, str]]:
    """Read CSV rows."""
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def normalize_title(value: str) -> str:
    """Normalize a title for exact identity comparison."""
    return "".join(char.lower() for char in value if char.isalnum())


def main() -> int:
    """Apply exact-title baseline matches with a backup and audit report."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", type=Path, default=DEFAULT_BASELINE)
    parser.add_argument("--pool", type=Path, default=DEFAULT_POOL)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    baseline = read_rows(args.baseline)
    pool = read_rows(args.pool)
    baseline_by_title = {normalize_title(row["Source Title"]): row for row in baseline}
    report = []
    changed = 0
    for row in pool:
        match = baseline_by_title.get(normalize_title(row["title"]))
        decision = "no_exact_title_match"
        if match:
            decision = "match_existing_value" if row.get("existing_paper_id") else "apply_exact_title_match"
            if args.apply and not row.get("existing_paper_id"):
                row["existing_paper_id"] = match["ID"]
                row["existing_match_signal"] = "historical_baseline_exact_title"
                row["screening_status"] = "existing_corpus"
                changed += 1
        report.append({
            "candidate_id": row["candidate_id"],
            "baseline_id": match["ID"] if match else "",
            "candidate_title": row["title"],
            "baseline_title": match["Source Title"] if match else "",
            "decision": decision,
        })
    args.report.parent.mkdir(parents=True, exist_ok=True)
    with args.report.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(report[0]))
        writer.writeheader()
        writer.writerows(report)
    if args.apply and changed:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        shutil.copy2(args.pool, args.pool.with_suffix(f".csv.bak.{timestamp}"))
        with args.pool.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(pool[0]))
            writer.writeheader()
            writer.writerows(pool)
    print(f"Exact baseline matches: {sum(bool(r['baseline_id']) for r in report)}")
    print(f"Pool rows changed: {changed}")
    print(f"Report: {args.report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
