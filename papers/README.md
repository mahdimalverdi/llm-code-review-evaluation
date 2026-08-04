# Paper Artifact Structure

This directory separates manuscript-facing paper notes from search and extraction artifacts.

## Directories

| Path | Role | Source of truth |
|---|---|---|
| `papers/canonical/notes/P01-*.md` through `P123-*.md` (excluding resolved duplicates P108/P116) | Frozen canonical study notes | `data/slr-extraction.csv` and `references/references.bib` |
| `papers/provisional/notes/P108-*.md`, `P116-*.md`, `P124-*.md`, `P125-*.md` | Duplicate/provisional records retained outside the frozen corpus | `data/search/core-reconciliation-queue.csv`; external candidate ledger |
| `papers/candidates/pdfs/` | PDFs acquired during supplementary search | `data/search/arxiv-full-text-manifest.csv` |
| `papers/canonical/pdfs/` | PDFs associated with the baseline corpus | Paper IDs and the baseline paper pool |

Supporting supplementary extraction text and packets live under:

```text
data/search/provisional-extraction/supporting/
```

They remain outside `papers/provisional/notes/` until a candidate receives a stable final study ID and is admitted to the evidence set.

## Naming rules

- Canonical notes use `PXX-descriptive-slug.md`.
- Provisional notes use `PXX-descriptive-slug.md` and must remain clearly marked provisional.
- Search PDFs use `ARXIV-####_<arxiv-id>.pdf`, with the version suffix represented in the manifest metadata.
- Do not duplicate BibTeX entries in paper notes; bibliography data belongs in `references/references.bib`.

## Promotion rule

A provisional record is promoted only after full-text validation, duplicate/version resolution, relevance and evidence-tier assignment, and the final evidence-set freeze. Resolved duplicate records and access-limited external candidates remain outside the frozen denominator.

## Synchronization

Run the following after adding or validating local search artifacts:

```bash
python3 scripts/sync_search_state.py
```

This updates acquisition state, core reconciliation state, and extraction checkpoints from local artifacts. It does not promote provisional studies or alter screening decisions.
