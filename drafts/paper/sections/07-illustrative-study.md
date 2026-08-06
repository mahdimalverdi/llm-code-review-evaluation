# Study Selection and Characteristics

## Corpus Accounting

The evidence pool contains 121 unique full-text studies. Each study has one structured extraction record and one bibliographic identity. Duplicate representations were reconciled before analysis, and all records passed the same completeness check.

| Corpus property | Value |
|---|---:|
| Included full-text studies | 121 |
| Core evidence | 91 |
| Supporting evidence | 24 |
| Peripheral evidence | 6 |
| Methodological anchors outside the substantive corpus | 4 |
| Unresolved duplicate study identities | 0 |

These counts describe the unified synthesis corpus rather than additive database-search totals. Search-stream records overlap and were reconciled by study identity before the 121-study denominator was frozen.

All counts in this section use the study as the unit of analysis. Percentages use the row-specific study count shown in the corresponding table; none is a comment-level prevalence estimate.

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

The corpus is recent: 95 of 121 records (78.5%) are dated 2025 or 2026. This concentration reflects rapid growth in LLM-based review research, but it also means that many records are recent preprints whose metadata or peer-review status may change.

<!-- table: caption="Distribution of the 121 records by publication period." label="tab:publication-years" -->
| Publication period | Studies | Share |
|---|---:|---:|
| 2013--2018 | 4 | 3.3% |
| 2021--2023 | 7 | 5.8% |
| 2024 | 15 | 12.4% |
| 2025 | 49 | 40.5% |
| 2026 | 46 | 38.0% |

The bibliography classifies 44 records as conference papers, 25 as journal articles, and 52 as preprints or other publication forms. Publication type is descriptive and is not used as an inclusion or quality criterion.

## Reporting-quality Profile

All 121 records have Q1--Q12 scores. The mean is 19.90/24, with a range from 12 to 24. Mean quality differs by evidence tier because peripheral studies are less aligned with the review-specific instrument, not necessarily because their underlying research is methodologically weaker.

<!-- table: caption="Quality score by evidence tier." label="tab:quality-tier" -->
| Evidence tier | Studies | Mean quality score |
|---|---:|---:|
| Core | 91 | 20.57/24 |
| Supporting | 24 | 18.67/24 |
| Peripheral | 6 | 14.67/24 |
| Overall | 121 | 19.90/24 |

## Sensitivity Analysis

We repeated the RQ4 reporting-availability counts for prespecified corpus subsets. To avoid selecting studies partly on the same reporting fields examined by RQ4, the RQ4-independent appraisal subset excludes Q10 (trade-off measurement) and Q12 (direct review support) and retains Q1--Q9 plus Q11. Its threshold is at least 17/20; this threshold is descriptive rather than an inclusion rule. The peer-reviewed subset includes records classified as conference or journal articles. Removing supporting and peripheral studies does not change the four RQ4 numerators because all coded preservation, coverage, escalation, and cost evidence occurs in the core tier. Restricting by publication status or RQ4-independent reporting and methodological appraisal lowers the numerators, but the reporting asymmetry remains.

<!-- table: caption="Sensitivity of RQ4 reporting availability to corpus composition." label="tab:sensitivity-rq4" -->
| Analysis set | Studies | Useful feedback | Coverage | Escalation | Cost |
|---|---:|---:|---:|---:|---:|
| All included studies | 121 | 45 (37.2%) | 46 (38.0%) | 27 (22.3%) | 34 (28.1%) |
| Core evidence only | 91 | 45 (49.5%) | 46 (50.5%) | 27 (29.7%) | 34 (37.4%) |
| Peer-reviewed only | 69 | 19 (27.5%) | 20 (29.0%) | 10 (14.5%) | 15 (21.7%) |
| RQ4-independent appraisal at least 17/20 | 77 | 34 (44.2%) | 34 (44.2%) | 18 (23.4%) | 27 (35.1%) |

## Evidence Weighting

Quality score and evidence tier are used together. A supporting or peripheral study is not promoted to direct evidence because it has a high quality score, and a direct study is not excluded solely because some reporting criteria are weak. Where a paper does not report useful-feedback preservation, escalation, or cost, the absence is coded as missing evidence rather than interpreted as zero impact.

## Traceability

The bibliography provides the complete references for the 121 included studies. The paper reports the corpus accounting, evidence tiers, and synthesis procedure, but the study-level extraction records are not included with the standalone PDF.
