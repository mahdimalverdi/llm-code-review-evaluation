#!/usr/bin/env python3
"""Convert a manually saved ACM Digital Library result page into audit artifacts."""

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
DATE_RANGE = "No native date filter; planned eligibility window 2021-01-01 to 2026-08-02"


def clean(value: str) -> str:
    return " ".join(value.split())


def first_text(node, xpath: str) -> str:
    matches = node.xpath(xpath)
    return clean(matches[0].text_content()) if matches else ""


def parse(source: Path) -> list[dict[str, str | int]]:
    document = html.fromstring(source.read_bytes())
    items = document.xpath(
        '//li[contains(concat(" ", normalize-space(@class), " "), " search__item ") '
        'and contains(concat(" ", normalize-space(@class), " "), " issue-item-container ")]'
    )
    records: list[dict[str, str | int]] = []
    for rank, item in enumerate(items, start=1):
        title_links = item.xpath('.//h4[contains(@class,"issue-item__title")]//a[1]')
        if not title_links:
            raise ValueError(f"result {rank} has no title link")
        link = title_links[0]
        href = link.get("href", "")
        author_nodes = item.xpath('.//ul[@aria-label="authors"]//a[@title]')
        authors = [clean(author.get("title", "").replace("\xa0", " ")) for author in author_nodes]
        doi_url = first_text(
            item,
            './/*[contains(concat(" ",normalize-space(@class)," ")," issue-item__doi ")]',
        )
        doi_match = re.search(r"10\.1145/[^\s]+", doi_url or href)
        records.append(
            {
                "rank": rank,
                "title": clean(link.text_content()),
                "authors": "; ".join(authors),
                "publication_type": first_text(item, './/*[contains(@class,"issue-heading")]'),
                "published_date": first_text(item, './/*[contains(@class,"bookPubDate")]'),
                "publication": first_text(
                    item,
                    './/*[contains(@class,"issue-item__detail")]//*[contains(@class,"epub-section__title")]',
                ),
                "doi": doi_match.group(0).rstrip(".,") if doi_match else "",
                "url": f"https://dl.acm.org{href}" if href.startswith("/") else href,
                "abstract_snippet": first_text(item, './/*[contains(@class,"issue-item__abstract")]'),
            }
        )
    return records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("html", type=Path, help="manually saved ACM result-page HTML")
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args()

    records = parse(args.html)
    urls = [str(record["url"]) for record in records]
    if len(records) != 449 or len(set(urls)) != 449:
        raise SystemExit(
            f"expected 449 rows and 449 unique URLs; found {len(records)} rows and {len(set(urls))} unique URLs"
        )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = args.output_dir / "acm-search-2026-08-06.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)

    manifest = {
        "database": "ACM Digital Library",
        "search_date": SEARCH_DATE,
        "date_range": DATE_RANGE,
        "exact_query": QUERY,
        "search_url": (
            "https://dl.acm.org/action/doSearch?AllField=%22large+language+model%22+AND+%22code+review%22"
            "&startPage=0&pageSize=1000&sortBy=EpubDate_desc"
        ),
        "sort": "EpubDate_desc",
        "native_result_count": 449,
        "parsed_row_count": len(records),
        "unique_url_count": len(set(urls)),
        "unique_doi_count": len({record["doi"] for record in records if record["doi"]}),
        "input_sha256": hashlib.sha256(args.html.read_bytes()).hexdigest(),
        "retained_raw_artifact": "data/search/acm/acm-search-2026-08-06.html.gz",
        "parsed_artifact": "data/search/acm/acm-search-2026-08-06.csv",
        "screening_status": "not started",
        "provenance": "Manual authenticated-browser HTML capture supplied by the repository owner.",
    }
    (args.output_dir / "acm-search-2026-08-06.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
