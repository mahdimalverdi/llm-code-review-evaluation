#!/usr/bin/env python3
"""Render a bounded curl configuration from a full-text manifest."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--offset", required=True, type=int)
    parser.add_argument("--limit", required=True, type=int)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    with args.manifest.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))[args.offset:args.offset + args.limit]
    if not rows:
        raise SystemExit("Selected download batch is empty")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    lines = ["location", "fail", "silent", "show-error", "retry = 2", "retry-delay = 2"]
    for row in rows:
        lines.extend((f'url = "{row["pdf_url"]}"', f'output = "{row["target_path"]}"'))
    args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
