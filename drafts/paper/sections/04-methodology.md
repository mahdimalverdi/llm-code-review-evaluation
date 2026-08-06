# Review Method

## Review Design

We conducted a targeted structured literature review with an auditable supplementary search amendment. The review follows question definition, eligibility assessment, quality appraisal, data extraction, thematic synthesis, and reporting, drawing on software-engineering SLR guidance without claiming a reproducible search for the historical baseline. Taxonomy construction and reliability planning additionally draw on established taxonomy and agreement methods [@m01_nickerson2013_taxonomy; @m02_cohen1960_kappa; @m03_krippendorff2018_content_analysis].

### Goal definition

Following a Goal--Question--Metric structure, the review goal is defined as follows:

- **Purpose:** analyze and characterize;
- **Issue:** evaluation and mitigation trade-offs;
- **Object:** LLM-generated and automated code review comments and their evaluation instruments; and
- **Viewpoint:** researchers and tool builders designing reliable code-review evaluation.

Five review questions refine this goal, while the extraction fields identify the evidence required to answer each question. Framework derivation is treated separately as a traceability objective rather than as a research question, because the framework is an author-derived synthesis artifact.

## Review Questions

<!-- table: first-column-width="0.55in" -->
| RQ | Question |
|---|---|
| RQ1 | Which problematic-comment types and failure categories have been reported? |
| RQ2 | Which evaluation dimensions have been used for correctness, grounding, relevance, usefulness, actionability, context quality, and evaluator validity? |
| RQ3 | Which mitigation families have been proposed or evaluated, and where do they intervene? |
| RQ4 | What evidence exists about error reduction versus useful-feedback preservation, coverage, escalation, and cost? |
| RQ5 | How are context quality, dataset validity, and annotation difficulty treated? |

### Framework-traceability objective

For each taxonomy category, annotation decision, and framework layer, we record whether support is direct code-review evidence, supporting evidence, or a bounded transfer from peripheral evidence. This mapping documents derivation; it is not treated as independent validation of the proposed framework.

## Search Scope and Corpus Assembly

The review protocol identified ACM Digital Library, IEEE Xplore, ScienceDirect, SpringerLink, arXiv, Semantic Scholar, Google Scholar, and Scopus where available, with a primary focus on work from 2021 onward and earlier foundational modern-code-review studies. Query families covered LLM code review, automated review, generated comments, evaluation metrics, hallucination and grounding, context-aware review, LLM-as-a-Judge, and human--AI review.

The synthesis corpus contains 121 unique full-text studies. It combines a 71-study historical baseline with 50 unique core studies admitted through a dated supplementary amendment. The historical set is treated as an assembled corpus, not as the output of a reproducible search flow. We report verified corpus and amendment counts and leave unavailable historical identification-stage counts as `NR`.

### Dated supplementary amendment and corpus closure

The amendment searched arXiv using documented query families and produced 293 unique title/abstract records after pooled deduplication. Full text was assessed for 140 records: 132 were retained for consideration and eight were excluded. Of 53 records classified as core evidence, one matched a baseline study, two were duplicate or companion versions, and 50 unique studies entered the synthesis corpus. The other 79 records provided adjacent supporting evidence; we refer to them below as the reserve. Of these, 53 received substantive provisional extraction, 16 have extraction scaffolds only, and ten have no extraction packet. None contributes to the 121-study denominator.

An external 30-record export was screened separately after corpus closure. Reconciliation found 20 duplicates, two full-text candidates retained outside the closed corpus, seven access-limited metadata-only candidates, and one exclusion. The external export therefore contributes no additional study to the 121-study denominator. Candidate-level decisions and provenance are included in the replication package.

<!-- table: caption="Auditable accounting of the baseline corpus and dated search amendments." label="tab:corpus-flow-audit" -->
| Source | Identified | Full text assessed | Corpus records contributed | Reserve or post-closure | Overlaps or duplicate identities | Access-limited |
|---|---:|---:|---:|---:|---:|---:|
| Historical baseline | NR | 71 | 71 | 0 | NR | NR |
| Dated arXiv amendment | 293 | 140 | 50 | 79 supporting: 53 substantive, 16 scaffolds, 10 without packets | 3 core identities | 0 |
| External cross-check export | 30 | 3 | 0 | 2 full-text candidates | 20 | 7 |

The rows are not additive identification stages: the external export is a post-closure cross-check and overlaps the baseline and arXiv records. The corpus arithmetic is therefore `71 + 50 = 121`.

## Eligibility and Evidence Tiers

Core eligibility covered LLM-based, AI-assisted, or automated code review; generated review comments or PR feedback; code-review benchmarks and rubrics; relevant failure types; and mitigation through prompting, filtering, retrieval, verification, tool support, rewriting, or escalation. Supporting eligibility covered evaluator validity, human review, workflow value, annotation, context quality, and methodological foundations. General code generation or repair without a review connection was excluded unless retained as explicitly bounded peripheral evidence.

The synthesis corpus assigns 91 studies to the core tier, 24 to supporting evidence, and six to peripheral evidence. These tiers indicate argumentative role, not methodological quality. The 24 supporting studies in the corpus completed the same structured extraction as the core studies. The 79 reserve studies did not: 53 have substantive but provisional packets, 16 have scaffolds only, and ten lack packets. Mixing this partial coding with standardized study records would make quantitative counts non-comparable. Their exclusion is therefore based on extraction completeness rather than timing alone.

## Quality Appraisal

The initial protocol specified eight 0--2 criteria. The extraction workflow expanded these into 12 items covering artifact clarity, context, data, metrics, judging, reliability, limitations, relevance to the review questions, preservation, coverage/escalation, cost/workflow, and evaluator validity. The expanded instrument improves extraction consistency but is not presented as the original rubric. Total scores do not determine inclusion; criterion-level evidence, confidence, and evidence tier guide interpretation.

## Data Extraction

Each included study has one structured extraction record derived from its available full text. Records contain bibliographic identity, screening decision, study design, RQ1--RQ5 evidence, traceability, quality appraisal, trade-off and evaluator-validity fields, evidence locations, and unresolved verification items. All 121 records pass the same completeness check. This validation establishes completeness of form, not independent reviewer agreement.

<!-- table: caption="Study-level data items and their use in the review." label="tab:data-items" -->
| Data-item group | Fields | Use |
|---|---|---|
| Bibliographic | ID, citation key, title, year, venue, publication type | Corpus demographics |
| Evidence weighting | evidence tier, decision, relevance, quality score, confidence | Framework traceability and validity |
| Review artifact | context types, evaluated artifact, evaluator types | RQ2 and RQ5 |
| Failure coding | problematic-comment and related failure categories | RQ1 |
| Evaluation coding | quality, workflow, cost, and evaluator-validity dimensions | RQ2 |
| Mitigation coding | family and intervention point | RQ3 |
| Trade-off reporting | preservation, coverage, escalation, and cost availability | RQ4 |
| Method validity | annotation, limitations, and RQ evidence status | RQ5 and framework traceability |

The complete field definitions and controlled labels are provided in the replication package.

## Synthesis

We used tabulation, thematic grouping, and framework mapping. We did not pool incompatible metrics. Initial categories were derived during cross-study synthesis and normalized into controlled vocabularies for failure types, evaluation dimensions, mitigation families, and context types. A deterministic transformation procedure produced one study-level record per included study, retained multi-valued controlled labels, and used `NR` when the extraction did not contain enough evidence. The resulting counts therefore describe coded evidence in the reviewed studies, not the prevalence of failures in deployed systems.

Automated consistency checks ensure that each included study occurs once, evidence tiers do not overlap, admitted supplementary studies receive the intended tier, citations resolve, and appraisal scores are available. Findings were organized by research question. Stable study identifiers support traceability within the replication package, while citations support claims in this report. Every reported count uses the 121-study evidence pool as its denominator unless another denominator is stated.

### Supporting-reserve sensitivity analysis

We separately mapped the bounded synthesis claims in the 53 substantively extracted reserve packets to five framework-level themes defined before the mapping: evaluation or evaluator validity, context or grounding quality, annotation or dataset validity, human-review or workflow value, and trade-off or mitigation design. This directional analysis asks whether the reserve would require a new top-level component for RQ2, RQ5, or framework traceability. It does not compare effect sizes or add reserve records to the 121-study frequency tables. All 53 packets mapped to at least one existing theme: 26 to evaluation or evaluator validity, 25 to context or grounding quality, two to annotation or dataset validity, 29 to human-review or workflow value, and 23 to trade-off or mitigation design. No new top-level component was required. Because the mapping was conducted by the same reviewer and 26 reserve candidates lack substantive extraction, this result provides a bounded robustness check rather than evidence that the reserve cannot alter lower-level categories or relative emphasis.

## Protocol Deviations and Amendments

The main deviation is retrospective protocol formalization: the baseline corpus was assembled before the complete search log was available. Evidence-tier assignment was added after full-text extraction to prevent indirect studies from receiving the same argumentative weight as direct code-review studies. The dated arXiv run is reported as an amendment and does not reconstruct the historical search. The external export is partial, and seven otherwise relevant records remain outside the frozen corpus because verified full text was unavailable. Any future database-search rerun must be dated and reported as a further amendment rather than described as if it preceded corpus assembly.
