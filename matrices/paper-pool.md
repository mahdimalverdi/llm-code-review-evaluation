# Paper Pool

This file records the current scope and evidence role of the 71-paper local corpus. Paper titles and paper-specific uses are listed in `matrices/cross-paper-synthesis.md`; extraction status, quality score, confidence, and unresolved items are listed in `papers/slr-review-progress.md`. A compact snapshot of the earlier planning sheet and its provenance is preserved in `data/historical-baseline-inventory.csv` and `method/historical-baseline-provenance.md`.

## Corpus Status

| Item | Count | Status |
|---|---:|---|
| Unique project IDs | 71 | P01–P71 |
| Local PDFs | 71 | One per project ID |
| Authoritative notes | 71 | One per project ID |
| Structurally valid notes | 71 | Pass the eleven-section validator |
| Bibliography entries | 71 | Project-prefixed keys available |
| Duplicate note IDs | 0 | P18/P21 duplicates consolidated |
| Final formal-SLR included set | Not frozen | Requires reproducible search and screening history |

## Evidence-Tier Assignment

The tiers control argumentative weight; they are not quality rankings.

| Tier | Paper IDs | Count | Permitted use |
|---|---|---:|---|
| Core | P01–P22, P24–P26, P35, P40, P49, P53–P55, P57–P60, P62–P66, P69 | 41 | Direct review-specific findings, benchmarks, mitigation, or closely coupled framework evidence |
| Supporting | P23, P27–P34, P36–P39, P41–P43, P46, P48, P51–P52, P56, P61, P67–P68 | 24 | Constructs, evaluator validity, human workflow, foundational review, context, or bounded security transfer |
| Peripheral | P44–P45, P47, P50, P70–P71 | 6 | Adjacent background only; not sufficient alone for review-specific conclusions |
| Methodological anchor | M01–M04 | 4 | Taxonomy construction, agreement, and evaluator-method guidance; excluded from the 71-paper substantive corpus |

The tiers cover all 71 substantive IDs exactly once. The final formal-SLR included set nevertheless remains provisional until the search process is reconstructed or the report is explicitly retained as a targeted structured review.

## Scope Rules

- Core papers may support direct answers to RQ1–RQ5 when the extracted evidence is relevant.
- Supporting papers may define constructs or qualify interpretation, but must not be presented as direct evidence about generated review-comment performance when they study another artifact.
- Peripheral papers require an explicit transfer statement and cannot establish the central research gap alone.
- Quality score, confidence, and evidence tier must be considered together; no single total score determines inclusion.
- The denominator for every reported count must state whether it covers core papers, all substantive papers, or only papers reporting the relevant field.

## Current Gaps

- Database-specific search strings, dates, retrieval counts, deduplication counts, and excluded-record logs are unavailable.
- The final included set is therefore not frozen as a formal SLR set.
- Some records retain publisher-metadata or independent-calibration uncertainty.
- Publication-facing synthesis still requires complete citation-key traceability.

## Working Rule

Do not add a paper merely because it is adjacent to LLMs or code. Add or retain a study only when it changes an RQ answer, taxonomy category, evaluation dimension, mitigation family, validity concern, or framework claim.
