#!/usr/bin/env python3
"""Split the human screening queue into deterministic review batches."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


DEFAULT_INPUT = Path("data/search/full-text-screening-queue.csv")
DEFAULT_OUTPUT_DIR = Path("data/search/screening-batches")


def read_rows(path: Path) -> list[dict[str, str]]:
    """Read queue rows from CSV."""
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    """Write fixed-size screening batches."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--batch-size", type=int, default=50)
    args = parser.parse_args()
    if args.batch_size < 1:
        raise ValueError("--batch-size must be positive")

    rows = read_rows(args.input)
    fields = list(rows[0]) if rows else []
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for start in range(0, len(rows), args.batch_size):
        batch_number = start // args.batch_size + 1
        output = args.output_dir / f"batch-{batch_number:03d}.csv"
        with output.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows[start : start + args.batch_size])
    print(f"Created {(len(rows) + args.batch_size - 1) // args.batch_size} batches")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
