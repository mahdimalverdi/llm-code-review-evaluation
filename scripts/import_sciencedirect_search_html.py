#!/usr/bin/env python3
"""Convert manually saved ScienceDirect search pages into audit artifacts."""

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
DATE_RANGE = "Native year filter 2021-2026; eligibility cutoff 2026-08-02 applied during screening"
EXPECTED_ROWS = 318


def clean(value: str) -> str:
    return " ".join(value.split())


def first_text(node, xpath: str) -> str:
    matches = node.xpath(xpath)
    return clean(matches[0].text_content()) if matches else ""


def parse_page(source: Path) -> tuple[list[dict[str, str | int]], dict[str, str | int]]:
    document = html.fromstring(source.read_bytes())
    title = clean(document.xpath("string(//title)"))
    count_match = re.search(r"([\d,]+) results", clean(document.text_content()), re.I)
    if not count_match:
        raise ValueError(f"native count not found in {source}")
    items = document.xpath(
        '//*[contains(concat(" ",normalize-space(@class)," ")," result-item-container ")]'
    )
    records: list[dict[str, str | int]] = []
    for item in items:
        links = item.xpath(
            './/a[contains(concat(" ",normalize-space(@class)," ")," result-list-title-link ")][1]'
        )
        if not links:
            raise ValueError(f"result without title link in {source}")
        link = links[0]
        href = link.get("href", "")
        pii_match = re.search(r"/pii/([^/?#]+)", href)
        source_fields = item.xpath('.//*[contains(@class,"srctitle-date-fields")]/span')
        authors = [
            clean(author.text_content())
            for author in item.xpath(
                './/*[contains(concat(" ",normalize-space(@class)," ")," author ")]'
            )
        ]
        records.append(
            {
                "rank": int(link.get("data-rank", "0")),
                "title": clean(link.text_content()),
                "authors": "; ".join(authors),
                "article_type": first_text(
                    item,
                    './/*[contains(concat(" ",normalize-space(@class)," ")," article-type ")]',
                ),
                "access": first_text(
                    item,
                    './/*[contains(concat(" ",normalize-space(@class)," ")," access-label ")]',
                ),
                "publication_title": first_text(
                    item, './/*[contains(@class,"srctitle-date-fields")]//a[1]'
                ),
                "publication_date": clean(source_fields[-1].text_content()) if source_fields else "",
                "pii": pii_match.group(1) if pii_match else "",
                "url": f"https://www.sciencedirect.com{href}" if href.startswith("/") else href,
            }
        )
    return records, {
        "page_title": title,
        "native_result_count": int(count_match.group(1).replace(",", "")),
        "row_count": len(records),
        "first_rank": min(record["rank"] for record in records),
        "last_rank": max(record["rank"] for record in records),
        "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("html", nargs="+", type=Path, help="saved result pages in any order")
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
    pages.sort(key=lambda page: int(page["first_rank"]))

    ranks = [int(record["rank"]) for record in records]
    urls = [str(record["url"]) for record in records]
    piis = [str(record["pii"]) for record in records]
    native_counts = {int(page["native_result_count"]) for page in pages}
    if native_counts != {EXPECTED_ROWS}:
        raise SystemExit(f"expected native count {EXPECTED_ROWS}; found {sorted(native_counts)}")
    if ranks != list(range(1, EXPECTED_ROWS + 1)):
        raise SystemExit("result ranks are incomplete, duplicated, or out of order")
    if len(set(urls)) != EXPECTED_ROWS or len(set(piis)) != EXPECTED_ROWS:
        raise SystemExit("expected 318 unique URLs and PII identifiers")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = args.output_dir / "sciencedirect-search-2026-08-06.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)

    manifest = {
        "database": "ScienceDirect",
        "search_date": SEARCH_DATE,
        "exact_query": QUERY,
        "date_range": DATE_RANGE,
        "sort": "date",
        "search_url": (
            "https://www.sciencedirect.com/search?qs=%22large%20language%20model%22%20AND%20%22code%20review%22"
            "&date=2021-2026&sortBy=date&show=100"
        ),
        "native_result_count": EXPECTED_ROWS,
        "parsed_row_count": len(records),
        "unique_url_count": len(set(urls)),
        "unique_pii_count": len(set(piis)),
        "pages": pages,
        "retained_raw_artifacts": [
            f"data/search/sciencedirect/sciencedirect-search-2026-08-06-page-{index}.html.gz"
            for index in range(1, len(pages) + 1)
        ],
        "parsed_artifact": "data/search/sciencedirect/sciencedirect-search-2026-08-06.csv",
        "screening_status": "not started",
        "provenance": "Manual browser HTML captures supplied by the repository owner.",
    }
    (args.output_dir / "sciencedirect-search-2026-08-06.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
