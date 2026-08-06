# Replication Package Manifest

This manifest identifies the repository artifacts used to audit the 121-study synthesis corpus and reproduce the manuscript's descriptive tables. It does not reconstruct the unavailable search history of the 71-study historical baseline.

## Corpus and Bibliography

- `data/search/final-corpus-freeze-register.csv`: frozen corpus membership and amendment status.
- `data/slr-extraction.csv`: one generated study-level extraction row for each included record.
- `references/references.bib`: bibliographic source of truth.
- `papers/canonical/notes/`: full-text extraction notes with evidence locations and appraisal fields.

## Supplementary Search Amendment

- `method/search-protocol-amendment.md`: scope and procedure of the dated amendment.
- `method/search-run-log.csv`: recorded search runs and query provenance.
- `method/source-search-execution-audit.md`: source-by-source endpoints, observed access failures, and completion rule.
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
python3 scripts/build_slr_dataset.py
python3 scripts/build_latex.py
```

The first command rebuilds the study-level dataset and summary tables from the canonical notes. The second rebuilds `build/paper.tex` from the manuscript sections. These checks reproduce the structured corpus outputs; they do not supply independent reviewer agreement.

The canonical notes contain criterion-level Q1–Q12 scores and evidence notes for each study; `data/slr-extraction.csv` currently exposes only their totals. The current extraction dataset also contains broad RQ4 reporting-availability fields rather than a completed study-by-study evidence-status field distinguishing quantitative measurement, qualitative evaluation, limitation/design mention, and review inference. Both publication-facing exports require an additional deterministic projection or manual audit before they are presented as standalone supplementary tables.

## Known Limits

The original database-specific queries, dates, retrieval counts, deduplication counts, and exclusion log for the historical baseline were not preserved. The supplementary amendment is auditable through the files listed above. No public DOI or artifact license is claimed for the current repository snapshot.
