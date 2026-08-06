# Replication Package Manifest

This manifest identifies the repository artifacts used to audit the 121-study synthesis corpus and reproduce the manuscript's descriptive tables. It does not reconstruct the unavailable search history of the 71-study historical baseline. The checkout is release candidate `v1.0` (last updated 2026-08-06); a persistent DOI and public archive URL must be added after depositing this release in Zenodo, OSF, or an equivalent repository.

## Corpus and Bibliography

- `data/search/final-corpus-freeze-register.csv`: frozen corpus membership and amendment status.
- `data/slr-extraction.csv`: one generated study-level extraction row for each included record.
- `references/references.bib`: bibliographic source of truth.
- `papers/canonical/notes/`: full-text extraction notes with evidence locations and appraisal fields.

## Supplementary Search Amendment

- `method/search-protocol-amendment.md`: scope and procedure of the dated amendment.
- `method/search-run-log.csv`: recorded search runs and query provenance.
- `method/source-search-execution-audit.md`: source-by-source endpoints, observed access failures, and completion rule.
- `scripts/search_semantic_scholar.py`: Semantic Scholar query expansion, pagination, cutoff filtering, and deduplication.
- `scripts/build_unified_candidate_pool.py`: cross-source identity reconciliation without inferring eligibility.
- `scripts/enrich_candidate_dois.py`: resumable Crossref/OpenAlex DOI suggestions with title/year scoring and provenance.
- `scripts/resolve_source_url_dois.py`: cached DOI resolution for source-URL-only candidates, including direct arXiv/URL extraction and unresolved-status logging.
- `scripts/apply_high_confidence_dois.py`: auditable promotion of high-confidence DOI suggestions into the unified candidate pool.
- `scripts/sync_external_references.py`: dry-run-first, DOI/title-deduplicated promotion of reviewed external candidates into the canonical BibTeX file.
- `scripts/triage_unified_candidate_pool.py`: conservative title/abstract triage with explicit metadata-only handling.
- `scripts/build_full_text_screening_queue.py`: deterministic queue of candidates still requiring human full-text screening.
- `scripts/split_screening_queue.py`: deterministic 50-record batches for manual screening.
- `scripts/screen_remaining_batches.py`: conservative preliminary screening for batches without a manually reviewed decision file.
- `data/search/unified-candidate-pool.csv`: one row per reconciled candidate identity with source provenance and screening placeholders.
- The unified candidate pool contains 1,358 identities, but it is a screening/provenance artifact; only the 121 frozen records form the synthesis denominator and PDF bibliography.
- `data/search/unified-candidate-duplicate-audit.csv`: all identity clusters supported by more than one source record.
- `data/search/doi-enrichment.csv`: DOI suggestions, when the provider lookup completes; suggestions require review before promotion.
- `data/search/doi-enrichment.log`: execution progress, provider failures, cache hits, and final counts.
- `data/search/doi-lookup-cache.json`: resumable provider-response cache; interrupted runs resume from cached title/year keys.
- `data/search/source-url-doi-resolution.csv`: DOI resolution results for source-URL-only candidates.
- `data/search/source-url-doi-cache.json`: cache for source-URL DOI resolution.
- `data/search/source-url-doi-resolution.log`: progress and provider-error log for source-URL DOI resolution.
- `data/search/high-confidence-doi-application.csv`: per-candidate DOI promotion decisions.
- `data/search/external-reference-sync-report.csv`: per-candidate decisions from the bibliography promotion step.
- `data/search/unified-title-abstract-screening.csv`: dated screening sheet for the 1,358 reconciled identities.
- `data/search/full-text-screening-queue.csv`: 1,067 pending records separated into abstract-available and metadata-only queues.
- `data/search/screening-batches/`: 22 review batches generated from the pending queue.
- `data/search/unified-candidate-pool-summary.json`: source counts, cluster counts, and corpus-match summary.
- `data/search/unified-candidate-pool-report.md`: human-readable candidate-pool accounting.
- `data/search/semantic-scholar/semantic-scholar-run.json`: exact query manifest, page accounting, timestamps, and counts.
- `data/search/semantic-scholar/semantic-scholar-raw.jsonl.gz`: compressed retained responses before cross-query deduplication.
- `data/search/semantic-scholar/semantic-scholar-unique.csv`: paper-ID-deduplicated result set with query membership.
- `data/search/ieee-xplore-search-2026-08-06.csv`: complete 69-record IEEE Xplore browser result set.
- `scripts/import_acm_search_html.py`: deterministic parser and completeness checks for a manually saved ACM result page.
- `data/search/acm/acm-search-2026-08-06.html.gz`: compressed manual-browser capture of the complete ACM result page.
- `data/search/acm/acm-search-2026-08-06.csv`: parsed 449-record ACM result set.
- `data/search/acm/acm-search-2026-08-06.json`: ACM query, count, checksum, uniqueness, and provenance manifest.
- `data/search/springerlink-attempt-2026-08-06.json`: retained evidence from the initial incomplete SpringerLink export attempt.
- `data/search/springerlink/springerlink-search-2026-08-06.csv`: complete native 155-record SpringerLink export.
- `data/search/springerlink/springerlink-search-2026-08-06.json`: SpringerLink count, checksum, uniqueness, content-type, and provenance manifest.
- `scripts/import_sciencedirect_search_html.py`: deterministic parser and completeness checks for manually saved ScienceDirect result pages.
- `data/search/sciencedirect/sciencedirect-search-2026-08-06-page-*.html.gz`: four compressed manual-browser captures covering ranks 1-318.
- `data/search/sciencedirect/sciencedirect-search-2026-08-06.csv`: parsed 318-record ScienceDirect result set.
- `data/search/sciencedirect/sciencedirect-search-2026-08-06.json`: ScienceDirect query, page ranges, checksums, count, uniqueness, and provenance manifest.
- `scripts/import_google_scholar_search_html.py`: privacy-safe parser and completeness checks for private signed-in Google Scholar captures.
- `data/search/google-scholar/google-scholar-search-2026-08-06.csv`: parsed 81-record Google Scholar result set with no account identifiers.
- `data/search/google-scholar/google-scholar-search-2026-08-06.json`: Google Scholar query, page counts, private-input checksums, count limitation, privacy policy, and provenance manifest.
- `data/search/acm-attempt-2026-08-06-retry.json`: retained evidence from the second ACM/Cloudflare verification block.
- `data/search/raw/`: retained raw arXiv responses.
- `data/search/arxiv-title-abstract-screening.csv`: title and abstract decisions.
- `data/search/arxiv-full-text-screening-reviewed.csv`: reviewed full-text decisions and reasons.
- `data/search/core-reconciliation-queue.csv`: duplicate, version, and corpus-identity reconciliation.
- `data/search/external-candidate-screening.csv`: post-closure external cross-check decisions.

## Coding and Derived Results

- `method/slr-data-dictionary.md`: field definitions and controlled labels.
- `method/quality-appraisal-rubric.md`: auditable Q1–Q12 definitions, scoring rules, and interpretation limits.
- `method/slr-screening-log.md`: verified corpus accounting and unavailable historical fields.
- `data/slr-summary.md`: generated demographics and RQ-level counts.
- `data/search/supporting-reserve-sensitivity.csv`: supporting-reserve sensitivity mapping.
- `scripts/build_slr_dataset.py`: deterministic dataset and summary generator.
- `scripts/build_latex.py`: manuscript-to-LaTeX generator.

## Reproduction

From the repository root, run:

```bash
python3 -m pip install -r requirements-search.txt
python3 scripts/import_acm_search_html.py saved-acm-results.html data/search/acm
python3 scripts/build_unified_candidate_pool.py
python3 scripts/enrich_candidate_dois.py --providers openalex
python3 scripts/sync_external_references.py
# After reviewing the report:
python3 scripts/sync_external_references.py --apply
python3 scripts/triage_unified_candidate_pool.py \
  --pool data/search/unified-candidate-pool.csv \
  --output data/search/unified-title-abstract-screening.csv
python3 scripts/build_full_text_screening_queue.py
python3 scripts/split_screening_queue.py
python3 scripts/build_slr_dataset.py
python3 scripts/build_latex.py
```

The ACM importer verifies the expected 449 rows and 449 unique record URLs before replacing its CSV and manifest. The candidate-pool command reconciles DOI, arXiv ID, canonical URL, and normalized-title identities but does not make eligibility decisions. The dataset command rebuilds the study-level dataset and summary tables from the canonical notes. The LaTeX command rebuilds `build/paper.tex` from the manuscript sections. These checks reproduce the structured corpus outputs; they do not supply independent reviewer agreement.

The canonical notes contain criterion-level Q1–Q12 scores and evidence notes for each study; `data/slr-extraction.csv` currently exposes only their totals. The current extraction dataset also contains broad RQ4 reporting-availability fields rather than a completed study-by-study evidence-status field distinguishing quantitative measurement, qualitative evaluation, limitation/design mention, and review inference. Both publication-facing exports require an additional deterministic projection or manual audit before they are presented as standalone supplementary tables.

## Known Limits

The original database-specific queries, dates, retrieval counts, deduplication counts, and exclusion log for the historical baseline were not preserved. The supplementary amendment is auditable through the files listed above. No public DOI or artifact license is claimed for the current repository snapshot.
