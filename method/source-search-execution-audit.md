# Source-search execution audit

This audit records the source-by-source execution attempted on 6 August 2026. Blank counts mean that no result set was returned; they do not mean zero results. The exact run-level records are in `method/search-run-log.csv`.

| Source | Executed route | Observed outcome | Reproducibility consequence |
|---|---|---|---|
| arXiv | Public Atom API, Q1–Q3 | Complete retained run: 417 raw and 293 unique records | Reproducible from retained queries and raw responses |
| Semantic Scholar | Bulk Graph API; 16 phrase-level conjunctions | Complete retained run after rate-limited retries: 963 raw and 427 unique records | Reproducible from the run manifest, raw JSONL, deduplicated CSV, and rerun script |
| ACM Digital Library | Manual browser run of `/action/doSearch`; 1,000 items per page; descending electronic-publication date | Complete native set: 449 results and 449 unique record URLs retained | Reproducible from the exact URL, retained HTML, parsed CSV, manifest, and importer script |
| IEEE Xplore | Public search page; 75 items per page | Complete visible set: 69 results; titles, years, and canonical record links retained | Reproducible from the exact query and retained CSV |
| ScienceDirect | Manual browser run; 100 items per page; date sorting; 2021-2026 year filter | Complete native set: 318 results and 318 unique PII record URLs retained | Reproducible from the exact URL, four retained HTML pages, parsed CSV, manifest, and importer script |
| SpringerLink | Manual browser search and native CSV export | Complete native set: 155 results, 155 unique DOIs, and 155 unique record URLs retained | Reproducible from the documented query, retained CSV, and checksum/provenance manifest |
| Google Scholar | Scholar search page in headless Chrome | Google refused the request as automated traffic | Must be executed manually; scraping is not used |
| Scopus | Elsevier Scopus Search API | No HTTP response before bounded timeout; authenticated API access may also be required | Requires API credentials/institutional access or manual export |

## Completion rule

A source is marked complete only when the run retains the exact query, execution date, date-range handling, native retrieved count, and an export or result set that can be screened. A blocked request is an executed diagnostic attempt, not a completed database search. Manual runs are added as new dated rows rather than replacing these failure records. The ACM run did not apply a native date filter, and the ScienceDirect interface applied only a 2021-2026 year filter. The planned 2021-01-01 through 2026-08-02 eligibility window must therefore be enforced during screening.
