# Dated Search Amendment

## Purpose and boundary

This amendment begins a new, reproducible identification stage for the review. It does not reconstruct the unavailable historical search. Results from this stage remain candidates until title/abstract screening, full-text eligibility assessment, duplicate handling, and evidence-tier assignment are complete.

The publication window is 2021-01-01 through 2026-08-02 for the LLM-focused search. Earlier modern-code-review and methodology studies may later be retained only through a documented backward-citation or foundational-study route.

## Search run S2026-08-02

The first source is arXiv because its public Atom API exposes both an exact query and a retrieval count. Three queries adapted from the proposal were executed on 2026-08-02, sorted by submission date in descending order:

| Query | Scope | Retrieved | Role |
|---|---|---:|---|
| Q1 | LLM-related records with `code review` in title or abstract | 200 | Direct LLM code-review discovery |
| Q2 | LLM-related records with `review comment` in title or abstract | 61 | Generated-comment discovery |
| Q3 | Code-review records mentioning hallucination, grounding, or context | 156 | Evaluation-validity discovery |
| Pooled | Q1 union Q2 union Q3 | 417 raw; 293 unique | Title/abstract screening completed |

The raw Atom responses are retained with the query identifiers. Candidates are deduplicated only by arXiv identifier at this stage; records found through more than one query preserve all matching query identifiers. Conservative title/abstract screening produced 140 candidates for full-text assessment, 116 exclusions, and 37 records that duplicate or are likely versions of the existing corpus.

## Source-access status

| Source | Status on 2026-08-02 | Consequence |
|---|---|---|
| arXiv | Executed and recorded | 293 unique candidates; title/abstract screening retained 140 for full text, of which 132 were included and 8 excluded |
| Semantic Scholar | Complete retained bulk-API rerun on 2026-08-06: 963 raw, 427 unique | Exact query expansion and outputs retained |
| ACM Digital Library | Complete manual-browser run on 2026-08-06: 449 native results and 449 unique record URLs | Exact URL, raw HTML capture, parsed CSV, manifest, and importer retained; apply the planned date window during screening |
| IEEE Xplore | Complete public-browser run on 2026-08-06: 69 native results and 69 unique record links | Exact query and complete parsed CSV retained |
| ScienceDirect | Attempted; search page returned no retrievable result set | Execute the same documented query manually or with institutional access |
| SpringerLink | Complete manual-browser export on 2026-08-06: 155 native results and 155 unique DOI-bearing records | Native CSV and checksum/provenance manifest retained; screening remains pending |
| Google Scholar | Pending | Use only a documented manual search; do not scrape |
| Scopus | Pending | Execute if institutional access is available; otherwise record the limitation |

## Supplied partial external-source export

On 2026-08-02, a separately produced export was supplied for five of the planned external sources. It contains 38 source rows: 10 from ACM Digital Library, 7 from IEEE Xplore, 5 from ScienceDirect, 5 from SpringerLink, and 11 from Semantic Scholar. The accompanying source log explicitly records that native result totals were unavailable and that each source subset is not exhaustive. Google Scholar and Scopus contributed no executable result set.

The export is therefore treated as a supplementary, partial identification route rather than a completed database search. Identifier-level deduplication yields 30 candidate records. Nine exactly match studies already present in the working corpus; the remaining 21 require independent title/abstract verification and full-text eligibility assessment before any inclusion or evidence-tier decision. Supplied `core`, `supporting`, and `exclude` labels are retained as discovery metadata only and are not treated as reviewer decisions.

## Screening rules for this run

Title/abstract screening uses the existing core, supporting, and exclusion criteria. Each candidate receives exactly one initial outcome: `include for full text`, `exclude`, `duplicate/companion`, or `uncertain`. Exclusions must use the controlled reason vocabulary. A candidate is not added to the evidence pool until full-text eligibility is confirmed.

## Reporting restriction

The review remains a targeted structured review during this amendment. The arXiv full-text decisions are now documented, but the review may be called an SLR only after the remaining source searches, screening decisions, full-text decisions, and final included set are documented.
