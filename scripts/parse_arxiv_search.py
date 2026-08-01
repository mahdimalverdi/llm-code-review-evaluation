#!/usr/bin/env python3
"""Create a deduplicated, screenable CSV from saved arXiv Atom responses.

The network retrieval itself is intentionally separate from this parser.  Keeping
the raw Atom responses lets a later reviewer reproduce the candidate list without
silently rerunning a time-sensitive search.
"""

from __future__ import annotations

import argparse
import csv
import re
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path


ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV = "{http://arxiv.org/schemas/atom}"


def clean(value: str | None) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def parse_response(path: Path) -> tuple[str, list[dict[str, str]]]:
    root = ET.parse(path).getroot()
    query_id = path.stem
    rows: list[dict[str, str]] = []
    for entry in root.findall(f"{ATOM}entry"):
        url = clean(entry.findtext(f"{ATOM}id"))
        arxiv_id = url.rsplit("/", 1)[-1]
        authors = "; ".join(clean(author.findtext(f"{ATOM}name")) for author in entry.findall(f"{ATOM}author"))
        categories = "; ".join(category.attrib.get("term", "") for category in entry.findall(f"{ATOM}category"))
        rows.append({
            "arxiv_id": arxiv_id,
            "title": clean(entry.findtext(f"{ATOM}title")),
            "authors": authors,
            "published": clean(entry.findtext(f"{ATOM}published")),
            "updated": clean(entry.findtext(f"{ATOM}updated")),
            "categories": categories,
            "url": url,
            "abstract": clean(entry.findtext(f"{ATOM}summary")),
            "query_id": query_id,
        })
    return query_id, rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("responses", nargs="+", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--search-date", required=True)
    args = parser.parse_args()

    candidates: dict[str, dict[str, str]] = {}
    provenance: defaultdict[str, list[str]] = defaultdict(list)
    for response in args.responses:
        query_id, rows = parse_response(response)
        for row in rows:
            key = row["arxiv_id"]
            if key not in candidates:
                candidates[key] = row
            provenance[key].append(query_id)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    fields = (
        "candidate_id", "source", "search_date", "query_ids", "arxiv_id",
        "title", "authors", "published", "updated", "categories", "url",
        "abstract", "screening_status", "screening_reason",
    )
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for index, row in enumerate(sorted(candidates.values(), key=lambda item: (item["published"], item["arxiv_id"]), reverse=True), 1):
            writer.writerow({
                "candidate_id": f"ARXIV-{index:04d}",
                "source": "arXiv",
                "search_date": args.search_date,
                "query_ids": ";".join(sorted(provenance[row["arxiv_id"]])),
                **{key: row[key] for key in ("arxiv_id", "title", "authors", "published", "updated", "categories", "url", "abstract")},
                "screening_status": "pending_title_abstract",
                "screening_reason": "",
            })


if __name__ == "__main__":
    main()
