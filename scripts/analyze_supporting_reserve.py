#!/usr/bin/env python3
"""Audit high-level themes in the non-canonical supporting reserve.

This analysis is intentionally directional. It checks whether substantively
extracted reserve packets map to the framework's existing high-level themes;
it does not add reserve records to corpus denominators or estimate effects.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCREENING_FILE = ROOT / "data/search/arxiv-full-text-screening-reviewed.csv"
PACKET_DIR = ROOT / "data/search/provisional-extraction/supporting"
OUTPUT_FILE = ROOT / "data/search/supporting-reserve-sensitivity.csv"

EXPECTED_SUPPORTING_RECORDS = 79
EXPECTED_SUBSTANTIVE_PACKETS = 53
EXPECTED_SCAFFOLDS = 16
EXPECTED_WITHOUT_PACKET = 10

THEMES: dict[str, tuple[str, ...]] = {
    "evaluation_or_evaluator_validity": (
        r"evaluat",
        r"validity",
        r"metric",
        r"benchmark",
        r"reliab",
        r"trust",
        r"calibrat",
    ),
    "context_or_grounding_quality": (
        r"context",
        r"ground",
        r"provenance",
        r"retriev",
        r"specification",
        r"tool evidence",
    ),
    "annotation_or_dataset_validity": (
        r"annotat",
        r"dataset",
        r"corpus",
        r"label",
        r"curat",
        r"reference",
    ),
    "human_review_or_workflow_value": (
        r"human",
        r"reviewer",
        r"workflow",
        r"socio-technical",
        r"knowledge transfer",
        r"accountability",
        r"actionability",
        r"usefulness",
    ),
    "trade_off_or_mitigation_design": (
        r"trade-off",
        r"cost",
        r"latency",
        r"coverage",
        r"escalat",
        r"gate",
        r"filter",
        r"verif",
        r"mitigat",
        r"routing",
    ),
}


def supporting_ids() -> set[str]:
    """Return included records assigned to the supporting screening group."""
    with SCREENING_FILE.open(encoding="utf-8", newline="") as handle:
        rows = csv.DictReader(handle)
        identifiers = {
            row["candidate_id"]
            for row in rows
            if row["full_text_decision"] == "include"
            and row["inclusion_group"] == "supporting"
        }
    if len(identifiers) != EXPECTED_SUPPORTING_RECORDS:
        raise ValueError(
            f"Expected {EXPECTED_SUPPORTING_RECORDS} supporting records; "
            f"found {len(identifiers)}"
        )
    return identifiers


def packet_text(candidate_id: str) -> str | None:
    """Read a candidate's packet when one exists."""
    path = PACKET_DIR / f"{candidate_id}-extraction-packet.md"
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


def synthesis_claim(text: str, candidate_id: str) -> str:
    """Extract the packet's bounded synthesis claim."""
    match = re.search(r"^8\. Synthesis claim:\s*(.+)$", text, re.MULTILINE)
    if match is None:
        raise ValueError(f"Substantive packet lacks synthesis claim: {candidate_id}")
    return match.group(1).strip()


def classify_themes(claim: str) -> list[str]:
    """Map a bounded synthesis claim to predefined framework-level themes."""
    normalized = claim.lower()
    return [
        theme
        for theme, patterns in THEMES.items()
        if any(re.search(pattern, normalized) for pattern in patterns)
    ]


def main() -> None:
    """Write the reserve audit and enforce the reported accounting."""
    output_rows: list[dict[str, str]] = []
    status_counts = {"substantive": 0, "scaffold": 0, "no_packet": 0}

    for candidate_id in sorted(supporting_ids()):
        text = packet_text(candidate_id)
        if text is None:
            status = "no_packet"
            claim = ""
            themes: list[str] = []
        elif "extraction scaffold" in text.lower():
            status = "scaffold"
            claim = ""
            themes = []
        else:
            status = "substantive"
            claim = synthesis_claim(text, candidate_id)
            themes = classify_themes(claim)
            if not themes:
                raise ValueError(
                    f"Substantive packet has no mapped theme: {candidate_id}"
                )
        status_counts[status] += 1
        output_rows.append(
            {
                "candidate_id": candidate_id,
                "reserve_status": status,
                "synthesis_claim": claim,
                "mapped_high_level_themes": ";".join(themes),
            }
        )

    expected_counts = {
        "substantive": EXPECTED_SUBSTANTIVE_PACKETS,
        "scaffold": EXPECTED_SCAFFOLDS,
        "no_packet": EXPECTED_WITHOUT_PACKET,
    }
    if status_counts != expected_counts:
        raise ValueError(
            f"Unexpected supporting-reserve accounting: {status_counts}; "
            f"expected {expected_counts}"
        )

    with OUTPUT_FILE.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=output_rows[0].keys())
        writer.writeheader()
        writer.writerows(output_rows)

    theme_counts = {
        theme: sum(
            theme in row["mapped_high_level_themes"].split(";")
            for row in output_rows
        )
        for theme in THEMES
    }
    print(f"Wrote {OUTPUT_FILE.relative_to(ROOT)}")
    print(f"Reserve status counts: {status_counts}")
    print(f"Theme counts among substantive packets: {theme_counts}")


if __name__ == "__main__":
    main()
