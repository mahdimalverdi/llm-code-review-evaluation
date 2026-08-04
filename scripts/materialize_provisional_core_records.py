#!/usr/bin/env python3
"""Materialize explicitly provisional intake records for new core candidates."""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def slug(value: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")
    return value[:45].rstrip("_")


def main() -> None:
    queue_path = ROOT / "data/search/core-reconciliation-queue.csv"
    rows = list(csv.DictReader(queue_path.open(encoding="utf-8", newline="")))
    notes_dir = ROOT / "papers/provisional"
    notes_dir.mkdir(exist_ok=True)
    bib_path = ROOT / "references/references.bib"
    bib_blocks: list[str] = []
    for row in rows:
        project_id = row["provisional_project_id"]
        first_author = (row["authors"].split(";")[0] or "unknown").split()[-1]
        year = row["submitted"][:4] or "0000"
        key = f"p{project_id[1:]}_{slug(first_author)}{year}_{slug(row['title'])[:30]}"
        note_path = notes_dir / f"{project_id}-{slug(row['title'])[:60]}.md"
        note_path.write_text(
            f"# {project_id} — {row['title']}\n\n"
            f"> **Provisional intake record.** This is not a canonical paper note.\n\n"
            f"| Field | Value |\n|---|---|\n"
            f"| Project ID | `{project_id}` (provisional) |\n"
            f"| Citation key | `{key}` |\n"
            f"| Authors | {row['authors'] or 'Not reported'} |\n"
            f"| Year | {year} |\n"
            f"| Source | arXiv |\n"
            f"| arXiv | `{row['arxiv_id']}` |\n"
            f"| Screening tier | `core` |\n"
            f"| Reconciliation status | New candidate after initial local matching |\n"
            f"| Metadata status | {row['metadata_status']} |\n"
            f"| Evidence status | Full-text eligibility recorded; extraction not yet completed |\n\n"
            f"## Required next actions\n\n"
            f"- Verify publisher/preprint relationship and duplicate status.\n"
            f"- Verify bibliographic metadata against the official record.\n"
            f"- Complete the canonical eleven-section extraction record.\n"
            f"- Replace the provisional BibTeX entry before submission.\n\n"
            f"## Evidence boundary\n\n"
            f"This record is not yet usable as paper-level evidence in the synthesis. The provisional project ID and citation key must not be reported as final.\n",
            encoding="utf-8",
        )
        bib_blocks.append(
            f"% TODO_VERIFY: provisional intake record generated from local arXiv metadata.\n"
            f"@misc{{{key},\n"
            f"  title = {{{row['title']}}},\n"
            f"  author = {{{' and '.join(a.strip() for a in row['authors'].split(';'))}}},\n"
            f"  year = {{{year}}},\n"
            f"  eprint = {{{row['arxiv_id'].removesuffix('v1').removesuffix('v2')}}},\n"
            f"  archivePrefix = {{arXiv}},\n"
            f"  url = {{https://arxiv.org/abs/{row['arxiv_id']}}},\n"
            f"  note = {{Provisional P{project_id[1:]}; verify official metadata before citation.}}\n"
            f"}}\n"
        )
    with bib_path.open("a", encoding="utf-8") as handle:
        handle.write("\n% Provisional arXiv intake records; do not cite until verified.\n")
        handle.write("\n".join(bib_blocks))
    print(f"materialized {len(rows)} provisional notes and BibTeX records")


if __name__ == "__main__":
    main()
