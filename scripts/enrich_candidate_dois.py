#!/usr/bin/env python3
"""Suggest missing DOIs using cached Crossref and OpenAlex metadata.

The script never overwrites the candidate pool. It records provider responses,
title similarity, year agreement, and a conservative status so that only
high-confidence suggestions can later be reviewed and promoted.
"""

from __future__ import annotations

import argparse
import csv
import json
import logging
import re
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path


DEFAULT_POOL = Path("data/search/unified-candidate-pool.csv")
DEFAULT_OUTPUT = Path("data/search/doi-enrichment.csv")
DEFAULT_CACHE = Path("data/search/doi-lookup-cache.json")
DEFAULT_LOG = Path("data/search/doi-enrichment.log")
USER_AGENT = "llm-code-review-evaluation/1.0 (mailto:research@example.invalid)"


def read_rows(path: Path) -> list[dict[str, str]]:
    """Read UTF-8 CSV rows."""
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def normalize_title(value: str) -> str:
    """Normalize a title for similarity comparison."""
    return "".join(char.lower() for char in value if char.isalnum())


def normalize_doi(value: str) -> str:
    """Normalize a DOI candidate."""
    value = value.lower().strip()
    value = re.sub(r"^(https?://)?(dx\.)?doi\.org/", "", value)
    return value.strip(" .;,)")


def fetch_json(url: str) -> dict:
    """Fetch one metadata response."""
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def write_cache(path: Path, cache: dict[str, object]) -> None:
    """Persist cache atomically so an interrupted run cannot corrupt it."""
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(cache, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def crossref_candidates(title: str) -> list[dict[str, object]]:
    """Query Crossref bibliographic metadata by title."""
    query = urllib.parse.urlencode({"query.bibliographic": title, "rows": 5})
    payload = fetch_json(f"https://api.crossref.org/works?{query}")
    return payload.get("message", {}).get("items", [])


def openalex_candidates(title: str) -> list[dict[str, object]]:
    """Query OpenAlex works by title."""
    query = urllib.parse.urlencode({"search": title, "per-page": 5})
    payload = fetch_json(f"https://api.openalex.org/works?{query}")
    return payload.get("results", [])


def candidate_score(title: str, year: str, item: dict[str, object], provider: str) -> tuple[float, str, str]:
    """Score a provider result using title similarity and year agreement."""
    if provider == "crossref":
        candidate_title = str((item.get("title") or [""])[0])
        candidate_year = str(((item.get("published") or {}).get("date-parts") or [[""]])[0][0])
        doi = normalize_doi(str(item.get("DOI", "")))
    else:
        candidate_title = str(item.get("title", ""))
        candidate_year = str((item.get("publication_year") or ""))
        doi = normalize_doi(str(item.get("doi", "")))
    title_score = SequenceMatcher(None, normalize_title(title), normalize_title(candidate_title)).ratio()
    year_match = bool(year and candidate_year and year[:4] == candidate_year[:4])
    score = title_score + (0.08 if year_match else 0.0)
    return score, doi, candidate_year


def main() -> int:
    """Create a DOI suggestion table with cached provider responses."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--pool", type=Path, default=DEFAULT_POOL)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--cache", type=Path, default=DEFAULT_CACHE)
    parser.add_argument("--delay", type=float, default=0.2)
    parser.add_argument("--log-file", type=Path, default=DEFAULT_LOG)
    parser.add_argument(
        "--providers",
        nargs="+",
        choices=("crossref", "openalex"),
        default=["crossref", "openalex"],
    )
    args = parser.parse_args()

    args.log_file.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[
            logging.FileHandler(args.log_file, encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )
    logger = logging.getLogger(__name__)

    cache = json.loads(args.cache.read_text(encoding="utf-8")) if args.cache.exists() else {}
    invalid_cache_entries = [key for key, value in cache.items() if value.get("errors")]
    for key in invalid_cache_entries:
        del cache[key]
    if invalid_cache_entries:
        logger.info("removed %d failed entries from existing cache", len(invalid_cache_entries))
        args.cache.parent.mkdir(parents=True, exist_ok=True)
        write_cache(args.cache, cache)
    rows = read_rows(args.pool)
    missing_rows = [row for row in rows if not row["doi"]]
    logger.info(
        "starting DOI enrichment: pool=%s total=%d missing_doi=%d providers=%s",
        args.pool,
        len(rows),
        len(missing_rows),
        ",".join(args.providers),
    )
    output: list[dict[str, str]] = []
    for index, row in enumerate(missing_rows, start=1):
        if row["doi"]:
            continue
        cache_key = f"{row['title']}|{row['year']}"
        cached = cache.get(cache_key)
        # Older cache files may contain provider errors.  Treat those entries
        # as misses so transient HTTP failures are retried.
        if cached and cached.get("errors"):
            logger.info("discarding error cache entry candidate=%s", row["candidate_id"])
            cached = None
        if cached is None:
            logger.info("lookup %d/%d candidate=%s", index, len(missing_rows), row["candidate_id"])
            cached = {"crossref": [], "openalex": [], "errors": []}
            loaders = {"crossref": crossref_candidates, "openalex": openalex_candidates}
            for provider in args.providers:
                loader = loaders[provider]
                try:
                    cached[provider] = loader(row["title"])
                except Exception as error:
                    cached["errors"].append(f"{provider}: {type(error).__name__}: {error}")
                    logger.warning(
                        "provider failure candidate=%s provider=%s error=%s",
                        row["candidate_id"],
                        provider,
                        type(error).__name__,
                    )
                time.sleep(args.delay)
            if cached["errors"]:
                # Do not persist transient provider failures (for example
                # HTTPError/429/5xx).  A later run must retry them.
                logger.info(
                    "not caching failed lookup candidate=%s errors=%d",
                    row["candidate_id"],
                    len(cached["errors"]),
                )
            else:
                cache[cache_key] = cached
                args.cache.parent.mkdir(parents=True, exist_ok=True)
                write_cache(args.cache, cache)
        else:
            logger.info("cache hit %d/%d candidate=%s", index, len(missing_rows), row["candidate_id"])
        suggestions: list[tuple[float, str, str, str]] = []
        for provider in args.providers:
            for item in cached.get(provider, []):
                score, doi, provider_year = candidate_score(row["title"], row["year"], item, provider)
                if doi:
                    suggestions.append((score, doi, provider, provider_year))
        suggestions.sort(reverse=True)
        best = suggestions[0] if suggestions else (0.0, "", "", "")
        second = suggestions[1] if len(suggestions) > 1 else (0.0, "", "", "")
        status = "high_confidence_suggestion" if best[1] and best[0] >= 1.03 and best[0] - second[0] >= 0.03 else "manual_review"
        output.append({
            "candidate_id": row["candidate_id"],
            "title": row["title"],
            "year": row["year"],
            "existing_doi": row["doi"],
            "proposed_doi": best[1],
            "provider": best[2],
            "title_year_score": f"{best[0]:.4f}",
            "runner_up_doi": second[1],
            "provider_year": best[3],
            "status": status,
            "lookup_errors": "; ".join(cached.get("errors", [])),
            "checked_at": datetime.now(timezone.utc).isoformat(),
        })
        logger.info(
            "candidate=%s status=%s provider=%s score=%.4f",
            row["candidate_id"],
            status,
            best[2] or "none",
            best[0],
        )
    args.cache.parent.mkdir(parents=True, exist_ok=True)
    write_cache(args.cache, cache)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fields = list(output[0]) if output else []
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(output)
    summary = {
        "missing_doi_records": len(output),
        "high_confidence": sum(row["status"] == "high_confidence_suggestion" for row in output),
        "manual_review": sum(row["status"] == "manual_review" for row in output),
        "log_file": str(args.log_file),
    }
    logger.info("completed DOI enrichment: %s", summary)
    print(json.dumps(summary))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
