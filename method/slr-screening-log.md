# SLR Screening and Extraction Log

This log records the current local corpus. Counts from the original database search are not available and must not be fabricated.

Future reproducible searches must be recorded row by row in `method/search-run-log.csv`. The empty data rows in that file are intentional: no historical database counts have been reconstructed.

| Stage | Count | Status |
|---|---:|---|
| Local PDF records identified | 71 | Verified from `papers/canonical/pdfs/` |
| Unique project IDs with notes | 71 | Verified from `papers/` |
| Markdown note files | 71 | One authoritative record for each project ID |
| Relevance decision recorded | 71 | Recorded in `papers/slr-review-progress.md`; final three-tier evidence classification remains to be frozen |
| Records marked completed | 71 | All unique P01–P71 authoritative records pass the structural gate |
| Records requiring provisional/full-PDF verification | 0 | Remaining uncertainty is recorded per paper rather than as provisional status |
| Canonical records passing the uniformity validator | 71 | P01–P71 |
| Legacy records still requiring canonical reconstruction | 0 | None |
| Duplicate/companion review needed | 0 | P18/P21 duplicate notes consolidated and removed |
| Full-PDF extraction complete | 71 | All local PDFs were available for canonical reconstruction |
| Final included set | Not yet frozen | Freeze core/supporting/peripheral tiers before reporting study counts by RQ |

## Supplementary reproducible identification stage

The dated arXiv amendment is tracked separately from the baseline P01–P71 corpus. It produced 293 unique candidates after deduplication; 140 reached full-text assessment, with 132 included for consideration and 8 excluded. These 132 records are screening outcomes, not automatic additions to the final evidence set. Duplicate/companion resolution, project-ID assignment, extraction, quality assessment, and tier reconciliation remain pending.

The supplementary external export contains 30 candidate records: 18 duplicates, 3 full-text verified inclusions, 8 provisional metadata-only inclusions, and 1 exclusion. Provisional records are not counted in the final included set.

## Required fields for each record

Each record must have: project ID, citation key, source PDF, screening decision, inclusion group, exact criterion, RQ1–RQ6 evidence, quality score, exclusion/limitation rationale, duplicate status, and unresolved verification items.

## Exclusion-reason vocabulary

Use one or more of: `out of scope`, `no review-feedback connection`, `insufficient method/evaluation`, `duplicate/companion`, `non-English`, `inaccessible`, or `supporting-only methodology`.

## Current limitation

The 71-PDF corpus is suitable for a targeted structured review, but not yet for a fully reproducible systematic review claim because database search strings, dates, retrieved counts, deduplication counts, title/abstract screening counts, and full-text exclusion decisions were not preserved. These fields require a new documented search; they must not be reconstructed from the local PDF folder.
