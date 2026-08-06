# Source-search execution audit

This audit records the source-by-source execution attempted on 6 August 2026. Blank counts mean that no result set was returned; they do not mean zero results. The exact run-level records are in `method/search-run-log.csv`.

| Source | Executed route | Observed outcome | Reproducibility consequence |
|---|---|---|---|
| arXiv | Public Atom API, Q1–Q3 | Complete retained run: 417 raw and 293 unique records | Reproducible from retained queries and raw responses |
| Semantic Scholar | Bulk Graph API; 16 phrase-level conjunctions | Complete retained run after rate-limited retries: 963 raw and 427 unique records | Reproducible from the run manifest, raw JSONL, deduplicated CSV, and rerun script |
| ACM Digital Library | `/action/doSearch`; direct HTTP and headless Chrome | `HTTP 403` Cloudflare challenge; browser stopped at Turnstile verification | Requires a manual browser run; automated count is unavailable |
| IEEE Xplore | Public search page and `/rest/search` | No HTTP response before bounded timeout from the current network | Requires manual or institutional execution |
| ScienceDirect | Official `/search` page | No HTTP response before bounded timeout from the current network | Requires manual or institutional execution |
| SpringerLink | Official `/search` page | No HTTP response before bounded timeout from the current network | Requires manual or institutional execution |
| Google Scholar | Scholar search page in headless Chrome | Google refused the request as automated traffic | Must be executed manually; scraping is not used |
| Scopus | Elsevier Scopus Search API | No HTTP response before bounded timeout; authenticated API access may also be required | Requires API credentials/institutional access or manual export |

## Completion rule

A source is marked complete only when the run retains the exact query, execution date, date range, native retrieved count, and an export or result set that can be screened. A blocked request is an executed diagnostic attempt, not a completed database search. Manual runs should be added as new dated rows rather than replacing these failure records.
