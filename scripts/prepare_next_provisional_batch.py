#!/usr/bin/env python3
"""Prepare and checkpoint the next provisional-paper extraction batch.

This script automates mechanical work only: queue selection, PDF text extraction,
note validation, and extraction-packet generation. Scientific synthesis remains a
human/agent review step and is intentionally not inferred by this script.
"""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "data/search/core-reconciliation-queue.csv"
PDF_DIR = ROOT / "papers/candidates/pdfs"
NOTE_DIR = ROOT / "papers/provisional"
OUT_DIR = ROOT / "data/search/provisional-extraction"
CHECKPOINT = OUT_DIR / "checkpoint.tsv"


def read_queue() -> list[dict[str, str]]:
    with QUEUE.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def paper_number(value: str) -> int:
    match = re.fullmatch(r"P(\d+)", value)
    if not match:
        raise ValueError(f"Invalid project id: {value}")
    return int(match.group(1))


def find_pdf(arxiv_id: str) -> Path | None:
    short_id = arxiv_id.removesuffix("v1").removesuffix("v2").removesuffix("v3")
    matches = sorted(PDF_DIR.glob(f"*_{short_id}.pdf"))
    return matches[0] if matches else None


def find_note(project_id: str) -> Path | None:
    matches = sorted(NOTE_DIR.glob(f"{project_id}-*.md"))
    return matches[0] if matches else None


def extract_text(pdf: Path, output: Path) -> bool:
    result = subprocess.run(
        ["pdftotext", "-layout", str(pdf), str(output)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode:
        output.unlink(missing_ok=True)
        return False
    return True


def validate_note(note: Path | None) -> str:
    if note is None:
        return "missing_note"
    validator = ROOT / "skills/slr-paper-reviewer/scripts/validate-note.sh"
    result = subprocess.run(
        ["bash", str(validator), str(note)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    return "validated" if result.returncode == 0 else "validation_failed"


def write_packet(row: dict[str, str], text_path: Path, note: Path | None) -> Path:
    project_id = row["provisional_project_id"]
    packet = OUT_DIR / f"{project_id}-extraction-packet.md"
    packet.write_text(
        "\n".join(
            [
                f"# {project_id} extraction packet",
                "",
                f"- Title: {row['title']}",
                f"- arXiv: {row['arxiv_id']}",
                f"- Authors: {row['authors']}",
                f"- Full text: `{text_path}`",
                f"- Provisional note: `{note}`" if note else "- Provisional note: missing",
                "",
                "## Required extraction",
                "",
                "1. Study purpose and research questions",
                "2. System/intervention and input context",
                "3. Dataset, sampling, and annotation/evaluator protocol",
                "4. Failure/problematic-comment categories",
                "5. Metrics and quantitative/qualitative results",
                "6. Mitigation effects, trade-offs, and operational cost",
                "7. Validity threats, missing evidence, and quality score",
                "8. Synthesis-ready bounded claims with section/page locations",
                "",
                "Do not promote this record to the canonical P01-P71 dataset until metadata and duplicate resolution are complete.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    return packet


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, required=True, help="First project number, e.g. 88")
    parser.add_argument("--count", type=int, default=10)
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    rows = sorted(read_queue(), key=lambda row: paper_number(row["provisional_project_id"]))
    selected = [
        row
        for row in rows
        if args.start <= paper_number(row["provisional_project_id"]) < args.start + args.count
    ]

    records: list[dict[str, str]] = []
    for row in selected:
        project_id = row["provisional_project_id"]
        pdf = find_pdf(row["arxiv_id"])
        text_path = OUT_DIR / f"{project_id}.txt"
        note = find_note(project_id)
        extracted = bool(pdf and extract_text(pdf, text_path))
        validation = validate_note(note)
        packet = write_packet(row, text_path, note) if extracted else None
        records.append(
            {
                "project_id": project_id,
                "arxiv_id": row["arxiv_id"],
                "pdf": str(pdf.relative_to(ROOT)) if pdf else "missing",
                "text": str(text_path.relative_to(ROOT)) if extracted else "missing",
                "note": str(note.relative_to(ROOT)) if note else "missing",
                "validation": validation,
                "packet": str(packet.relative_to(ROOT)) if packet else "missing",
            }
        )

    with CHECKPOINT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=records[0].keys(), delimiter="\t") if records else None
        if writer:
            writer.writeheader()
            writer.writerows(records)

    print(f"Prepared {len(records)} records")
    print(f"Checkpoint: {CHECKPOINT.relative_to(ROOT)}")
    for record in records:
        print(
            f"[{record['project_id']}] text={record['text']} "
            f"note={record['note']} validation={record['validation']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
