# SLR Screening and Extraction Log

This log records the current local corpus. Counts from the original database search are not available and must not be fabricated.

Future reproducible searches must be recorded row by row in `method/search-run-log.csv`. The empty data rows in that file are intentional: no historical database counts have been reconstructed.

| Stage | Count | Status |
|---|---:|---|
| Frozen canonical records | 121 | P01–P123 excluding duplicate identities P108 and P116 |
| Unique project IDs with canonical notes | 121 | Verified from `papers/canonical/notes/` |
| Relevance and evidence-tier decision recorded | 121 | 91 core, 24 supporting, and 6 peripheral records |
| Records marked completed | 121 | All frozen canonical records pass the structural gate |
| Access-limited external candidates outside denominator | 7 | Recorded in `data/search/provisional-external-resolution.md` |
| Canonical records passing the uniformity validator | 121 | Validator rerun after the freeze |
| Legacy records still requiring canonical reconstruction | 0 | None |
| Duplicate/companion records resolved | 2 | P108/EXT-0028 and P116/EXT-0030 are counted once |
| Supplementary supporting reserve | 70 | Text and extraction packets retained outside the frozen denominator |
| Final included set | 121 | Frozen on 2026-08-04; generated counts are reproducible from `data/slr-extraction.csv` |

## Supplementary reproducible identification stage

The dated arXiv amendment is tracked separately from the baseline P01–P71 corpus. It produced 293 unique candidates after deduplication; 140 reached full-text assessment, with 132 included for consideration and 8 excluded. From the 52 core candidates, 50 unique studies were admitted to the frozen corpus and two were resolved as duplicate external/search identities. Seventy supporting records were retained as an evidence reserve and were not counted as canonical additions.

The supplementary external export contains 30 candidate records: 19 duplicates, 3 full-text verified inclusions, 7 access-limited metadata-only records, and 1 exclusion. Access-limited records are not counted in the final included set.

## Required fields for each record

Each record must have: project ID, citation key, source PDF, screening decision, inclusion group, exact criterion, RQ1–RQ6 evidence, quality score, exclusion/limitation rationale, duplicate status, and unresolved verification items.

## Exclusion-reason vocabulary

Use one or more of: `out of scope`, `no review-feedback connection`, `insufficient method/evaluation`, `duplicate/companion`, `non-English`, `inaccessible`, or `supporting-only methodology`.

## Current limitation

The frozen 121-study corpus is suitable for a targeted structured review, but not for a fully reproducible systematic review claim. The original database-specific search strings, dates, retrieved counts, deduplication counts, and exclusion trail were not preserved. The dated amendment improves traceability but cannot reconstruct the historical search.
