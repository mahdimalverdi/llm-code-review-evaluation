#!/usr/bin/env python3
"""Audit low-confidence arXiv-to-publication matches through Crossref."""

from __future__ import annotations

import csv
import difflib
import json
import os
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data/search/openalex_bib_upgrade_report.tsv"
OUTPUT = ROOT / "data/search/crossref_bib_audit.tsv"


def normalize(value: str) -> str:
    value = re.sub(r"[^a-z0-9]+", " ", value.lower())
    return re.sub(r"\s+", " ", value).strip()


def title_score(left: str, right: str) -> float:
    return difflib.SequenceMatcher(None, normalize(left), normalize(right)).ratio()


def search_crossref(title: str) -> list[dict]:
    params = urllib.parse.urlencode({"query.bibliographic": title, "rows": 5})
    url = f"https://api.crossref.org/works?{params}"
    mailto = os.environ.get("CROSSREF_MAILTO", "").strip()
    headers = {"User-Agent": "crossref-bib-audit/1.0"}
    if mailto:
        headers["User-Agent"] += f" (mailto:{mailto})"
    print(f"[crossref] request {url}", flush=True)
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.loads(response.read().decode("utf-8")).get("message", {}).get("items", [])


def bib_titles() -> dict[str, str]:
    text = (ROOT / "references/references.bib").read_text(encoding="utf-8")
    titles = {}
    for block in re.split(r"(?=^@)", text, flags=re.MULTILINE):
        key = re.search(r"^@\w+\{([^,]+),", block, re.MULTILINE)
        title = re.search(r"\btitle\s*=\s*\{([^}]+)\}", block, re.IGNORECASE)
        if key and title:
            titles[key.group(1)] = title.group(1)
    return titles


def main() -> None:
    with INPUT.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    pending = {}
    titles = bib_titles()
    for row in rows:
        if row["action"] == "candidate_below_threshold":
            pending[row["key"]] = row

    output = []
    fields = ["key", "source_title", "arxiv_url", "openalex_doi", "crossref_title", "crossref_doi", "crossref_year", "crossref_score", "status"]
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    def save_checkpoint() -> None:
        with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
            writer.writeheader()
            writer.writerows(output)

    for index, row in enumerate(pending.values(), start=1):
        print(f"[crossref] [{index}/{len(pending)}] {row['key']}", flush=True)
        try:
            source_title = titles.get(row["key"], row["key"])
            candidates = search_crossref(source_title)
            best = candidates[0] if candidates else {}
            candidate_title = " ".join(best.get("title", [""]))
            score = title_score(source_title, candidate_title)
            output.append({
                "key": row["key"],
                "source_title": source_title,
                "arxiv_url": row.get("old_url", ""),
                "openalex_doi": row.get("new_doi", ""),
                "crossref_title": candidate_title,
                "crossref_doi": best.get("DOI", ""),
                "crossref_year": str((best.get("published", {}).get("date-parts", [[""]])[0] or [""])[0]),
                "crossref_score": f"{score:.3f}",
                "status": "manual_review_required" if best else "no_crossref_candidate",
            })
        except Exception as error:
            output.append({"key": row["key"], "status": f"crossref_error: {error}"})
        save_checkpoint()
        time.sleep(1.0)

    print(f"[crossref] wrote {len(output)} audit rows to {OUTPUT}", flush=True)


if __name__ == "__main__":
    main()
