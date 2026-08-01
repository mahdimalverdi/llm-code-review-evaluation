#!/usr/bin/env python3
"""Apply a conservative, auditable title/abstract triage to search candidates.

This script never marks a previously unseen study as included or excluded on
substantive grounds. It only identifies exact duplicates of the local corpus,
obvious non-software peer-review records, and records that contain no code-review
or review-feedback signal. Every remaining record requires human full-text
screening.
"""

from __future__ import annotations

import argparse
import csv
import re
import unicodedata
from pathlib import Path


def normalise(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "", value)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidates", required=True, type=Path)
    parser.add_argument("--corpus", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    with args.corpus.open(encoding="utf-8", newline="") as handle:
        existing = {normalise(row["title"]): row["paper_id"] for row in csv.DictReader(handle)}

    with args.candidates.open(encoding="utf-8", newline="") as handle:
        candidates = list(csv.DictReader(handle))

    fields = (
        "candidate_id", "source", "query_ids", "title", "authors", "year",
        "venue_or_repository", "doi_or_identifier", "url", "existing_paper_id",
        "title_abstract_decision", "exclusion_reason", "decision_basis",
        "screening_reviewer", "abstract_or_snippet",
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in candidates:
            text = f"{row['title']} {row['abstract']}".lower()
            existing_id = existing.get(normalise(row["title"]), "")
            decision = "uncertain_full_text"
            reason = ""
            basis = "Potentially relevant; retain for full-text screening."
            if existing_id:
                decision = "duplicate_or_version_of_existing"
                reason = "duplicate/companion"
                basis = "Exact normalized-title match with an existing corpus record; verify version relationship."
            elif re.search(r"scientific (?:peer )?review|manuscript review|reviewer feedback.*manuscript", text) and not re.search(r"software (?:code )?review|code review|pull request|merge request", text):
                decision = "exclude_title_abstract"
                reason = "no review-feedback connection"
                basis = "The record concerns scientific manuscript peer review rather than software code review."
            elif not re.search(r"code review|code-review|review comment|pull request|merge request", text):
                decision = "exclude_title_abstract"
                reason = "no review-feedback connection"
                basis = "Neither title nor abstract indicates a code-review or review-feedback connection."
            writer.writerow({
                "candidate_id": row["candidate_id"],
                "source": row["source"],
                "query_ids": row["query_ids"],
                "title": row["title"],
                "authors": row["authors"],
                "year": row["published"][:4],
                "venue_or_repository": "arXiv",
                "doi_or_identifier": row["arxiv_id"],
                "url": row["url"],
                "existing_paper_id": existing_id,
                "title_abstract_decision": decision,
                "exclusion_reason": reason,
                "decision_basis": basis,
                "screening_reviewer": "Codex (conservative rule-based triage)",
                "abstract_or_snippet": row["abstract"],
            })


if __name__ == "__main__":
    main()
