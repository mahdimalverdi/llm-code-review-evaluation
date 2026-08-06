#!/usr/bin/env python3
"""Convert private Google Scholar HTML captures into a privacy-safe result CSV."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path

from lxml import html


QUERY = '"large language model" AND "code review"'
SEARCH_DATE = "2026-08-06"
EXPECTED_ROWS = 81


def clean(value: str) -> str:
    return " ".join(value.replace("\u200f", "").split())


def parse_int(value: str) -> int:
    translation = str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789")
    return int(value.translate(translation).replace(",", "").replace("٬", ""))


def page_number(summary: str) -> int:
    match = re.search(r"صفحه\s+([۰-۹0-9]+)", summary)
    return parse_int(match.group(1)) if match else 1


def native_count(summary: str) -> int:
    numbers = re.findall(r"[۰-۹0-9][۰-۹0-9,٬]*", summary)
    values = [parse_int(number) for number in numbers]
    plausible = [value for value in values if value >= 10]
    if not plausible:
        raise ValueError(f"native count not found in {summary!r}")
    return max(plausible)


def parse_page(source: Path) -> tuple[list[dict[str, str | int]], dict[str, str | int]]:
    document = html.fromstring(source.read_bytes())
    summary = clean(document.xpath('string(//*[@id="gs_ab_md"])'))
    page = page_number(summary)
    items = document.xpath(
        '//div[contains(concat(" ",normalize-space(@class)," ")," gs_r ") '
        'and .//div[contains(concat(" ",normalize-space(@class)," ")," gs_ri ")]]'
    )
    records: list[dict[str, str | int]] = []
    for position, item in enumerate(items, start=1):
        headings = item.xpath(
            './/h3[contains(concat(" ",normalize-space(@class)," ")," gs_rt ")][1]'
        )
        if not headings:
            raise ValueError(f"result without title in {source}")
        heading = headings[0]
        links = heading.xpath(".//a[1]")
        metadata = clean(
            item.xpath(
                'string(.//div[contains(concat(" ",normalize-space(@class)," ")," gs_a ")])'
            )
        )
        year_matches = re.findall(r"\b(?:20\d{2})\b", metadata)
        records.append(
            {
                "rank": (page - 1) * 10 + position,
                "scholar_id": item.get("data-cid", ""),
                "title": clean(heading.text_content()),
                "result_url": links[0].get("href", "") if links else "",
                "authors_publication": metadata,
                "publication_year": year_matches[-1] if year_matches else "",
                "snippet": clean(
                    item.xpath(
                        'string(.//div[contains(concat(" ",normalize-space(@class)," ")," gs_rs ")])'
                    )
                ),
            }
        )
    return records, {
        "page": page,
        "row_count": len(records),
        "native_result_count": native_count(summary),
        "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("html", nargs="+", type=Path, help="private saved pages in any order")
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()

    records: list[dict[str, str | int]] = []
    pages = []
    for source in args.html:
        page_records, page = parse_page(source)
        page["source_file"] = source.name
        records.extend(page_records)
        pages.append(page)
    records.sort(key=lambda record: int(record["rank"]))
    pages.sort(key=lambda page: int(page["page"]))

    ranks = [int(record["rank"]) for record in records]
    scholar_ids = [str(record["scholar_id"]) for record in records]
    counts = {int(page["native_result_count"]) for page in pages}
    if counts != {EXPECTED_ROWS}:
        raise SystemExit(f"expected native count {EXPECTED_ROWS}; found {sorted(counts)}")
    if ranks != list(range(1, EXPECTED_ROWS + 1)):
        raise SystemExit("result ranks are incomplete, duplicated, or out of order")
    if len(set(scholar_ids)) != EXPECTED_ROWS or "" in scholar_ids:
        raise SystemExit("expected 81 non-empty unique Scholar result identifiers")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = args.output_dir / "google-scholar-search-2026-08-06.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)

    manifest = {
        "database": "Google Scholar",
        "search_date": SEARCH_DATE,
        "exact_query": QUERY,
        "date_range": "No native date filter; planned eligibility window 2021-01-01 to 2026-08-02",
        "sort": "date (scisbd=1)",
        "native_result_count": EXPECTED_ROWS,
        "parsed_row_count": len(records),
        "unique_scholar_id_count": len(set(scholar_ids)),
        "pages": pages,
        "parsed_artifact": "data/search/google-scholar/google-scholar-search-2026-08-06.csv",
        "raw_html_retained": False,
        "raw_html_policy": "Not committed because signed-in captures contain account identifiers; per-page SHA-256 values audit the private inputs.",
        "screening_status": "not started",
        "provenance": "Manual signed-in browser HTML captures supplied by the repository owner.",
        "count_limit": "Google Scholar reports an approximate count; 81 records were actually exposed across the complete nine-page result set.",
    }
    (args.output_dir / "google-scholar-search-2026-08-06.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
