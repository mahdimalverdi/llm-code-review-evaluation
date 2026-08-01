#!/usr/bin/env python3
"""Preserve externally supplied search exports and prepare a screened candidate queue.

The supplied exports may document only a partial result set. This script preserves
their original fields in UTF-8 and deduplicates candidates by persistent identifier
without converting a supplied relevance label into a final eligibility decision.
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import defaultdict
from pathlib import Path


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def canonical_identifier(row: dict[str, str]) -> str:
    return row["doi_or_official_url"].strip().lower().removeprefix("https://doi.org/")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidates", required=True, type=Path)
    parser.add_argument("--search-log", required=True, type=Path)
    parser.add_argument("--extraction", required=True, type=Path)
    parser.add_argument("--arxiv-worksheet", required=True, type=Path)
    parser.add_argument("--raw-candidates-output", required=True, type=Path)
    parser.add_argument("--raw-log-output", required=True, type=Path)
    parser.add_argument("--queue-output", required=True, type=Path)
    args = parser.parse_args()

    candidates = read_csv(args.candidates)
    logs = read_csv(args.search_log)
    required = {"database", "title", "doi_or_official_url", "label", "label_reason"}
    missing = required - set(candidates[0])
    if missing:
        raise SystemExit(f"Candidate export lacks required columns: {sorted(missing)}")

    write_csv(args.raw_candidates_output, candidates, list(candidates[0]))
    write_csv(args.raw_log_output, logs, list(logs[0]))

    existing = read_csv(args.extraction)
    existing_titles = {normalize(row["title"]): row["paper_id"] for row in existing}
    arxiv = read_csv(args.arxiv_worksheet)
    arxiv_titles = {normalize(row["title"]): row["candidate_id"] for row in arxiv}
    arxiv_ids = {row["arxiv_id"].split("v")[0].lower(): row["candidate_id"] for row in arxiv}
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in candidates:
        grouped[canonical_identifier(row)].append(row)

    queue: list[dict[str, str]] = []
    for index, group in enumerate(grouped.values(), start=1):
        representative = group[0]
        existing_id = existing_titles.get(normalize(representative["title"]), "")
        identifier = canonical_identifier(representative)
        arxiv_match = arxiv_ids.get(identifier.removeprefix("10.48550/arxiv."), "")
        arxiv_match = arxiv_match or arxiv_titles.get(normalize(representative["title"]), "")
        labels = sorted({row["label"].strip() for row in group})
        supplied_label = "; ".join(labels)
        status = (
            "duplicate_existing_corpus"
            if existing_id
            else "duplicate_existing_search_queue"
            if arxiv_match
            else "pending_title_abstract_verification"
        )
        queue.append(
            {
                "candidate_id": f"EXT-{index:04d}",
                "title": representative["title"],
                "authors": representative["authors"],
                "year": representative["year"],
                "venue_or_repository": representative["venue_or_repository"],
                "doi_or_official_url": representative["doi_or_official_url"],
                "source_databases": "; ".join(sorted({row["database"] for row in group})),
                "supplied_label": supplied_label,
                "supplied_label_reason": representative["label_reason"],
                "existing_paper_id": existing_id,
                "existing_search_candidate_id": arxiv_match,
                "screening_status": status,
                "screening_decision": "",
                "inclusion_group": "",
                "evidence_location": "",
                "decision_rationale": "",
                "screening_reviewer": "",
                "screening_date": "",
            }
        )
    write_csv(args.queue_output, queue, list(queue[0]))
    print(f"preserved {len(candidates)} supplied rows; {len(queue)} unique identifiers")


if __name__ == "__main__":
    main()
