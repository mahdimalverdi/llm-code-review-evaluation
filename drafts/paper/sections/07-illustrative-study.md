# Study Selection and Characteristics

## Corpus Accounting

The evidence pool contains 71 unique project IDs, 71 local PDFs, 71 authoritative extraction notes, and 71 project-prefixed bibliography entries. All notes pass the structural extraction validator. P18 and P21 previously had duplicate note files; these were consolidated so that each project ID now contributes one authoritative record.

| Corpus property | Value |
|---|---:|
| Full-text substantive records | 71 |
| Core evidence | 41 |
| Supporting evidence | 24 |
| Peripheral evidence | 6 |
| Methodological anchors outside the substantive corpus | 4 |
| Duplicate authoritative IDs | 0 |

These counts describe the local evidence pool, not a PRISMA-style database search flow. Identification, deduplication, title/abstract exclusion, and full-text exclusion counts remain unavailable.

## Research Streams

The corpus spans six overlapping streams:

1. generated review-comment models and datasets;
2. PR-level and context-aware benchmarks;
3. data curation, taxonomy, relevance, and usefulness;
4. industrial and human--AI workflow evidence;
5. LLM-as-a-Judge and evaluator-validity studies; and
6. specialized security, static-analysis, context-consistency, and non-functional evidence.

The first four streams provide the strongest direct evidence for review-comment evaluation. Evaluator studies primarily qualify measurement claims. Specialized and adjacent studies contribute optional sublayers and transfer risks.

## Publication Demographics

The corpus is recent: 54 of 71 records (76.1%) are dated 2025 or 2026. This concentration reflects rapid growth in LLM-based review research, but it also means that many records are recent preprints whose metadata or peer-review status may change.

<!-- table: caption="Distribution of the 71 records by publication period." label="tab:publication-years" -->
| Publication period | Studies | Share |
|---|---:|---:|
| 2013--2018 | 4 | 5.6% |
| 2021--2023 | 5 | 7.0% |
| 2024 | 8 | 11.3% |
| 2025 | 31 | 43.7% |
| 2026 | 23 | 32.4% |

The bibliography classifies 29 records as conference papers, 17 as journal articles, and 25 as preprints or other publication forms. Publication type is descriptive and is not used as an inclusion or quality criterion.

## Reporting-quality Profile

All 71 records have Q1--Q12 scores. The mean is 19.62/24, with a range from 12 to 24. Mean quality differs by evidence tier because peripheral studies are less aligned with the review-specific instrument, not necessarily because their underlying research is methodologically weaker.

<!-- table: caption="Quality score by evidence tier." label="tab:quality-tier" -->
| Evidence tier | Studies | Mean quality score |
|---|---:|---:|
| Core | 41 | 20.90/24 |
| Supporting | 24 | 18.67/24 |
| Peripheral | 6 | 14.67/24 |
| Overall | 71 | 19.62/24 |

## Evidence Weighting

Quality score and evidence tier are used together. A supporting or peripheral study is not promoted to direct evidence because it has a high quality score, and a direct study is not excluded solely because some reporting criteria are weak. Where a paper does not report useful-feedback preservation, escalation, or cost, the absence is coded as missing evidence rather than interpreted as zero impact.

## Traceability

The complete paper-level inventory appears in the cross-paper synthesis, progress log, and generated `data/slr-extraction.csv`. Each thematic result in the following section links to bibliography keys, while the dataset preserves paper IDs and source-note paths. This structure permits claims and counts to be checked against the corresponding full-text extraction while keeping the report organized by research question rather than by paper.
