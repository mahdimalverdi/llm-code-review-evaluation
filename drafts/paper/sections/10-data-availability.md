# Data and Replication Package Availability

The repository supports audit of corpus membership, study-level extraction, descriptive counts, and the supplementary search amendment. The bibliography lists all 121 included studies. `data/search/final-corpus-freeze-register.csv` records amendment-derived corpus membership; `data/slr-extraction.csv` contains the generated study-level dataset; and `papers/canonical/notes/` stores evidence locations, appraisal records, confidence, and unresolved items. The corpus was last frozen on 4 August 2026.

Artifacts specific to the amendment include `method/search-protocol-amendment.md`, `method/search-run-log.csv`, the raw responses under `data/search/raw/`, title/abstract decisions in `data/search/arxiv-title-abstract-screening.csv`, reviewed full-text decisions in `data/search/arxiv-full-text-screening-reviewed.csv`, and identity reconciliation in `data/search/core-reconciliation-queue.csv`. The supporting-reserve mapping is stored in `data/search/supporting-reserve-sensitivity.csv`.

The manifest at `docs/replication-package.md` lists the reproduction boundary and commands. Running `python3 scripts/build_slr_dataset.py` rebuilds the study-level extraction dataset and generated summaries from the canonical notes. Running `python3 scripts/build_latex.py` rebuilds the manuscript source. These operations reproduce derived artifacts and permit candidate-level audit of the amendment; they do not reproduce the selection of the 71-study historical baseline or provide independent agreement evidence.

A versioned public archive and explicit artifact license have not yet been issued, so no DOI is claimed for the present repository snapshot. Public release requires a frozen archive and reuse license.
