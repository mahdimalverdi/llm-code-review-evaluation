#!/usr/bin/env python3
"""Unify dated database exports into an auditable candidate pool.

The script performs identity reconciliation only. It does not decide whether a
new record is eligible for the review. DOI, arXiv identifier, canonical URL,
and normalized title are used as progressively weaker identity signals; every
record retains its source and the signal that joined it to a cluster.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urlparse


SOURCE_FILES = {
    "semantic_scholar": Path("data/search/semantic-scholar/semantic-scholar-unique.csv"),
    "acm": Path("data/search/acm/acm-search-2026-08-06.csv"),
    "ieee_xplore": Path("data/search/ieee-xplore-search-2026-08-06.csv"),
    "sciencedirect": Path("data/search/sciencedirect/sciencedirect-search-2026-08-06.csv"),
    "springerlink": Path("data/search/springerlink/springerlink-search-2026-08-06.csv"),
    "google_scholar": Path("data/search/google-scholar/google-scholar-search-2026-08-06.csv"),
}
EXTRACTION_FILE = Path("data/slr-extraction.csv")
ARXIV_FILES = (
    Path("data/search/arxiv-candidates.csv"),
    Path("data/search/arxiv-title-abstract-screening.csv"),
    Path("data/search/arxiv-full-text-screening-reviewed.csv"),
)
DEFAULT_OUTPUT = Path("data/search/unified-candidate-pool.csv")
DEFAULT_SUMMARY = Path("data/search/unified-candidate-pool-summary.json")
DEFAULT_REPORT = Path("data/search/unified-candidate-pool-report.md")
DEFAULT_DUPLICATES = Path("data/search/unified-candidate-duplicate-audit.csv")


def read_csv(path: Path) -> list[dict[str, str]]:
    """Read a UTF-8 CSV file while tolerating a BOM."""
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def normalize_text(value: str) -> str:
    """Normalize text for conservative exact-title matching."""
    value = value.lower().replace("&", " and ")
    return re.sub(r"[^a-z0-9]+", "", value)


def normalize_doi(value: str) -> str:
    """Return a normalized DOI or an empty string."""
    value = value.strip().lower()
    value = re.sub(r"^(https?://)?(dx\.)?doi\.org/", "", value)
    value = value.strip(" .;,)")
    return value if value.startswith("10.") else ""


def extract_doi(row: dict[str, str]) -> str:
    """Extract a DOI from common source-specific fields."""
    for key, value in row.items():
        if "doi" in key.lower() and value:
            doi = normalize_doi(value)
            if doi:
                return doi
    for value in row.values():
        match = re.search(r"10\.\d{4,9}/[-._;()/:a-z0-9]+", value.lower())
        if match:
            return normalize_doi(match.group(0))
    return ""


def extract_arxiv_id(row: dict[str, str]) -> str:
    """Extract an arXiv identifier without its version suffix."""
    for key, value in row.items():
        if "arxiv" in key.lower() and value:
            match = re.search(r"(?:arxiv[.:/])?([0-9]{4}\.[0-9]{4,5})", value, re.I)
            if match:
                return match.group(1).lower()
    for value in row.values():
        match = re.search(r"arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]{4,5})", value, re.I)
        if match:
            return match.group(1).lower()
    return ""


def canonical_url(value: str) -> str:
    """Canonicalize a URL for identity matching while preserving the source URL."""
    value = value.strip()
    if not value:
        return ""
    parsed = urlparse(value)
    if not parsed.scheme or not parsed.netloc:
        return ""
    host = parsed.netloc.lower().removeprefix("www.")
    path = parsed.path.rstrip("/")
    return f"{host}{path}".lower()


def extract_url(row: dict[str, str]) -> str:
    """Extract the first non-search URL from a source row."""
    preferred = ("url", "result_url", "official_url")
    values = [row[key] for key in preferred if row.get(key)]
    values.extend(row.values())
    for value in values:
        if "http" in value:
            match = re.search(r"https?://[^\s,;]+", value)
            if match:
                return match.group(0).rstrip("\"'>)")
    return ""


def title_from_row(row: dict[str, str]) -> str:
    """Extract a title from the known source schemas."""
    for key in ("title", "Item Title"):
        if row.get(key, "").strip():
            return row[key].strip()
    return ""


def first_value(row: dict[str, str], keys: tuple[str, ...]) -> str:
    """Return the first non-empty value from a set of source-specific fields."""
    for key in keys:
        if row.get(key, "").strip():
            return row[key].strip()
    return ""


def year_from_row(row: dict[str, str]) -> str:
    """Extract a publication year from a source row."""
    for key in ("year", "Publication Year", "publication_year"):
        if row.get(key, "").strip():
            return row[key].strip()
    value = " ".join(row.values())
    match = re.search(r"\b(20\d{2})\b", value)
    return match.group(1) if match else ""


@dataclass
class Candidate:
    """A reconciled identity cluster and its source records."""

    cluster_id: int
    records: list[dict[str, str]] = field(default_factory=list)
    join_signals: set[str] = field(default_factory=set)

    @property
    def representative(self) -> dict[str, str]:
        return self.records[0]


class DisjointSet:
    """Small union-find structure for transitive identity reconciliation."""

    def __init__(self, size: int) -> None:
        self.parent = list(range(size))

    def find(self, item: int) -> int:
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def union(self, left: int, right: int) -> None:
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root != right_root:
            self.parent[right_root] = left_root


def source_record(source: str, row: dict[str, str], index: int) -> dict[str, str]:
    """Convert a source-specific row to the common identity schema."""
    title = title_from_row(row)
    url = extract_url(row)
    return {
        "source": source,
        "source_record_id": f"{source.upper()}-{index:04d}",
        "title": title,
        "title_key": normalize_text(title),
        "year": year_from_row(row),
        "doi": extract_doi(row),
        "arxiv_id": extract_arxiv_id(row),
        "canonical_url": canonical_url(url),
        "source_url": url,
        "authors": first_value(row, ("authors", "Authors", "authors_publication")),
        "venue": first_value(row, ("venue", "publication", "publication_title", "Publication Title")),
        "abstract_or_snippet": first_value(row, ("abstract", "abstract_snippet", "snippet")),
    }


def identity_keys(record: dict[str, str]) -> list[tuple[str, str]]:
    """Return identity keys from strongest to weakest."""
    keys = []
    for key_field in ("doi", "arxiv_id", "canonical_url", "title_key"):
        if record[key_field]:
            keys.append((key_field, record[key_field]))
    return keys


def cluster_value(candidate: Candidate, field_name: str) -> str:
    """Return the first non-empty value for a field across a cluster."""
    for record in candidate.records:
        if record.get(field_name, ""):
            return record[field_name]
    return ""


def load_existing() -> dict[str, dict[str, str]]:
    """Load identity keys for the frozen corpus and existing search queue."""
    existing: dict[str, dict[str, str]] = {}
    for row in read_csv(EXTRACTION_FILE):
        existing[f"title_key:{normalize_text(row.get('title', ''))}"] = row
        doi = extract_doi(row)
        if doi:
            existing[f"doi:{doi}"] = row
        arxiv_id = extract_arxiv_id(row)
        if arxiv_id:
            existing[f"arxiv_id:{arxiv_id}"] = row
        url = canonical_url(extract_url(row))
        if url:
            existing[f"canonical_url:{url}"] = row
    for path in ARXIV_FILES:
        if not path.exists():
            continue
        for row in read_csv(path):
            title = title_from_row(row)
            if title:
                existing.setdefault(f"title_key:{normalize_text(title)}", row)
            arxiv_id = extract_arxiv_id(row)
            if arxiv_id:
                existing.setdefault(f"arxiv_id:{arxiv_id}", row)
    return existing


def reconcile(records: list[dict[str, str]]) -> list[Candidate]:
    """Build transitive clusters and record the identity signals used."""
    disjoint = DisjointSet(len(records))
    key_owner: dict[tuple[str, str], int] = {}
    pair_signals: dict[tuple[int, int], set[str]] = {}
    for index, record in enumerate(records):
        for key_field, value in identity_keys(record):
            owner = key_owner.get((key_field, value))
            if owner is None:
                key_owner[(key_field, value)] = index
            else:
                disjoint.union(index, owner)
                pair_signals.setdefault((index, owner), set()).add(key_field)

    grouped: dict[int, Candidate] = {}
    for index, record in enumerate(records):
        root = disjoint.find(index)
        candidate = grouped.setdefault(root, Candidate(len(grouped) + 1))
        candidate.records.append(record)
    for (left, right), signals in pair_signals.items():
        root = disjoint.find(left)
        grouped[root].join_signals.update(signals)
    return sorted(grouped.values(), key=lambda item: item.cluster_id)


def match_existing(candidate: Candidate, existing: dict[str, dict[str, str]]) -> tuple[str, str]:
    """Return existing paper ID and matching signal for a candidate."""
    for record in candidate.records:
        for key_field, value in identity_keys(record):
            match = existing.get(f"{key_field}:{value}")
            if match:
                return match.get("paper_id", ""), key_field
    return "", ""


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    """Write the unified candidate pool."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0]) if rows else []
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    """Build the unified candidate pool and its audit artifacts."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--summary", type=Path, default=DEFAULT_SUMMARY)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--duplicates", type=Path, default=DEFAULT_DUPLICATES)
    args = parser.parse_args()

    records: list[dict[str, str]] = []
    source_counts: dict[str, int] = {}
    for source, path in SOURCE_FILES.items():
        rows = read_csv(path)
        converted = [source_record(source, row, index) for index, row in enumerate(rows, 1)]
        records.extend(converted)
        source_counts[source] = len(converted)

    candidates = reconcile(records)
    existing = load_existing()
    output_rows: list[dict[str, str]] = []
    status_counts: dict[str, int] = {}
    for candidate in candidates:
        representative = candidate.representative
        paper_id, match_signal = match_existing(candidate, existing)
        status = "existing_corpus" if paper_id else "new_candidate"
        status_counts[status] = status_counts.get(status, 0) + 1
        output_rows.append({
            "candidate_id": f"POOL-{candidate.cluster_id:04d}",
            "title": representative["title"],
            "year": representative["year"],
            "doi": cluster_value(candidate, "doi"),
            "arxiv_id": cluster_value(candidate, "arxiv_id"),
            "source_url": cluster_value(candidate, "source_url"),
            "authors": cluster_value(candidate, "authors"),
            "venue": cluster_value(candidate, "venue"),
            "abstract_or_snippet": cluster_value(candidate, "abstract_or_snippet"),
            "evidence_availability": "abstract_or_snippet" if cluster_value(candidate, "abstract_or_snippet") else "metadata_only",
            "source_databases": ";".join(sorted({item["source"] for item in candidate.records})),
            "source_record_count": str(len(candidate.records)),
            "source_record_ids": ";".join(item["source_record_id"] for item in candidate.records),
            "identity_signals": ";".join(sorted(candidate.join_signals)),
            "existing_paper_id": paper_id,
            "existing_match_signal": match_signal,
            "screening_status": status,
            "title_abstract_decision": "",
            "full_text_decision": "",
            "exclusion_reason": "",
            "decision_rationale": "",
        })

    write_rows(args.output, output_rows)
    duplicate_rows = [
        {
            "candidate_id": row["candidate_id"],
            "title": row["title"],
            "source_databases": row["source_databases"],
            "source_record_count": row["source_record_count"],
            "source_record_ids": row["source_record_ids"],
            "identity_signals": row["identity_signals"],
            "existing_paper_id": row["existing_paper_id"],
        }
        for row in output_rows
        if int(row["source_record_count"]) > 1
    ]
    write_rows(args.duplicates, duplicate_rows)
    summary = {
        "source_counts": source_counts,
        "raw_record_count": len(records),
        "unique_identity_clusters": len(candidates),
        "duplicate_records_removed": len(records) - len(candidates),
        "status_counts": status_counts,
        "identity_priority": ["doi", "arxiv_id", "canonical_url", "title_key"],
        "screening_note": "No eligibility decision was inferred by this script.",
    }
    args.summary.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    report = [
        "# Unified candidate-pool report",
        "",
        "This artifact reconciles source identities only; it does not perform eligibility screening.",
        "",
        "| Source | Records |",
        "|---|---:|",
    ]
    report.extend(f"| {source} | {count} |" for source, count in source_counts.items())
    report.extend([
        "",
        f"- Raw source records: **{len(records)}**",
        f"- Identity clusters: **{len(candidates)}**",
        f"- Duplicate source records removed: **{len(records) - len(candidates)}**",
        f"- Identity clusters with multiple source records: **{len(duplicate_rows)}**",
        f"- Existing corpus clusters: **{status_counts.get('existing_corpus', 0)}**",
        f"- New candidate clusters: **{status_counts.get('new_candidate', 0)}**",
        "",
        "A new candidate remains unscreened until a dated title/abstract decision is recorded.",
        "",
    ])
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text("\n".join(report), encoding="utf-8")
    print(json.dumps(summary))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
