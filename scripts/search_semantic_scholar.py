#!/usr/bin/env python3
"""Run and retain the Semantic Scholar search stream for the SLR.

The Academic Graph API does not implement arbitrary nested Boolean expressions.
This script expands the documented concept blocks into phrase-level conjunctions,
retrieves every bulk-search page, and deduplicates records by Semantic Scholar ID.
Set S2_API_KEY to use an authenticated quota.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import os
import random
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


API_URL = "https://api.semanticscholar.org/graph/v1/paper/search/bulk"
FIELDS = "paperId,title,abstract,year,authors,venue,externalIds,url,publicationDate"
MODEL_TERMS = ('"large language model"', "LLM", '"generative AI"', '"AI-assisted"')
REVIEW_TERMS = ('"code review"', '"review comment"', '"pull request feedback"', '"automated code review"')
CUTOFF_DATE = "2026-08-02"


def query_pairs() -> list[dict[str, str]]:
    return [
        {"query_id": f"SS-{index:02d}", "model_term": model, "review_term": review,
         "api_query": f"{model} + {review}"}
        for index, (model, review) in enumerate(
            ((model, review) for model in MODEL_TERMS for review in REVIEW_TERMS), start=1
        )
    ]


def request_json(url: str, api_key: str | None, retries: int) -> dict:
    headers = {"User-Agent": "llm-code-review-evaluation/1.0"}
    if api_key:
        headers["x-api-key"] = api_key
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60) as response:
                return json.load(response)
        except urllib.error.HTTPError as error:
            retryable = error.code in {429, 500, 502, 503, 504}
            if not retryable or attempt == retries:
                body = error.read().decode("utf-8", errors="replace")
                raise RuntimeError(f"HTTP {error.code} for {url}: {body}") from error
            retry_after = error.headers.get("Retry-After")
            delay = float(retry_after) if retry_after else min(60.0, (2 ** attempt) + random.random())
            time.sleep(delay)
        except urllib.error.URLError as error:
            if attempt == retries:
                raise RuntimeError(f"Network failure for {url}: {error}") from error
            time.sleep(min(60.0, (2 ** attempt) + random.random()))
    raise AssertionError("unreachable")


def fetch_query(spec: dict[str, str], api_key: str | None, retries: int) -> tuple[list[dict], list[dict]]:
    records: list[dict] = []
    pages: list[dict] = []
    token: str | None = None
    while True:
        params = {"query": spec["api_query"], "year": "2021-2026", "fields": FIELDS}
        if token:
            params["token"] = token
        url = f"{API_URL}?{urllib.parse.urlencode(params)}"
        payload = request_json(url, api_key, retries)
        data = payload.get("data", [])
        pages.append({"token_used": token, "records": len(data), "next": payload.get("token")})
        records.extend(data)
        token = payload.get("token")
        if not token:
            break
        time.sleep(1.05 if api_key else 2.0)
    return records, pages


def write_csv(path: Path, records: list[dict], memberships: dict[str, list[str]]) -> None:
    def clean(value: object) -> str:
        return re.sub(r"\s+", " ", str(value or "")).strip()

    fields = ["paper_id", "title", "year", "publication_date", "authors", "venue", "doi", "arxiv_id", "url", "matched_queries", "abstract"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for record in records:
            external = record.get("externalIds") or {}
            paper_id = record["paperId"]
            writer.writerow({
                "paper_id": paper_id,
                "title": clean(record.get("title")),
                "year": record.get("year", ""),
                "publication_date": record.get("publicationDate", ""),
                "authors": "; ".join(clean(author.get("name")) for author in record.get("authors", [])),
                "venue": clean(record.get("venue")),
                "doi": external.get("DOI", ""),
                "arxiv_id": external.get("ArXiv", ""),
                "url": record.get("url", ""),
                "matched_queries": ";".join(memberships[paper_id]),
                "abstract": clean(record.get("abstract")),
            })


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path("data/search/semantic-scholar"))
    parser.add_argument("--retries", type=int, default=6)
    parser.add_argument("--request-delay", type=float, default=5.0,
                        help="Polite delay between query families (default: 5 seconds)")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    started = datetime.now(timezone.utc)
    api_key = os.environ.get("S2_API_KEY")
    unique: dict[str, dict] = {}
    memberships: dict[str, list[str]] = {}
    query_log: list[dict] = []
    raw_path = args.output_dir / "semantic-scholar-raw.jsonl.gz"

    with gzip.open(raw_path, "wt", encoding="utf-8") as raw_handle:
        for spec in query_pairs():
            records, pages = fetch_query(spec, api_key, args.retries)
            after_cutoff = [item for item in records if (item.get("publicationDate") or "") > CUTOFF_DATE]
            records = [item for item in records if item not in after_cutoff]
            query_log.append({**spec, "retrieved": len(records), "excluded_after_cutoff": len(after_cutoff), "pages": pages})
            for record in records:
                raw_handle.write(json.dumps({"query_id": spec["query_id"], "record": record}, ensure_ascii=False) + "\n")
                paper_id = record["paperId"]
                unique[paper_id] = record
                memberships.setdefault(paper_id, []).append(spec["query_id"])
            time.sleep(args.request_delay)

    records = sorted(unique.values(), key=lambda item: ((item.get("year") or 0), item.get("title") or ""), reverse=True)
    write_csv(args.output_dir / "semantic-scholar-unique.csv", records, memberships)
    manifest = {
        "database": "Semantic Scholar Academic Graph API",
        "endpoint": API_URL,
        "started_at_utc": started.isoformat(),
        "completed_at_utc": datetime.now(timezone.utc).isoformat(),
        "date_filter": "API year filter 2021-2026; records with publicationDate after 2026-08-02 excluded locally",
        "authenticated": bool(api_key),
        "query_expansion": query_pairs(),
        "raw_retrieved": sum(item["retrieved"] for item in query_log),
        "unique_retrieved": len(records),
        "queries": query_log,
    }
    (args.output_dir / "semantic-scholar-run.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"raw": manifest["raw_retrieved"], "unique": len(records), "output": str(args.output_dir)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
