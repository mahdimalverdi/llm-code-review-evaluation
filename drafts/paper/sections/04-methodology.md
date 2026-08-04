# Review Method

## Review Design

We conducted a targeted structured literature review inspired by software-engineering SLR guidance. The review follows question definition, study identification, eligibility assessment, quality appraisal, data extraction, thematic synthesis, and reporting. Taxonomy construction and reliability planning additionally draw on established taxonomy and agreement methods [@m01_nickerson2013_taxonomy; @m02_cohen1960_kappa; @m03_krippendorff2018_content_analysis]. The work is not presented as a fully reproducible SLR because the original database-specific search dates, queries, retrieval counts, deduplication counts, and title/abstract screening history were not preserved.

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

The proposal defined ACM Digital Library, IEEE Xplore, ScienceDirect, SpringerLink, arXiv, Semantic Scholar, Google Scholar, and Scopus where available, with a primary focus on work from 2021 onward and earlier foundational modern-code-review studies. Query families covered LLM code review, automated review, generated comments, evaluation metrics, hallucination and grounding, context-aware review, LLM-as-a-Judge, and human--AI review.

The local corpus contains 121 unique full-text records. It combines a 71-record baseline with 50 unique core studies admitted through a dated supplementary amendment. The baseline cannot be treated as the output of a reproducible search flow because its original retrieval and exclusion counts are unavailable. We therefore report verified corpus and amendment counts and do not infer missing historical identification-stage counts from the PDF directory.

### Dated supplementary amendment and freeze

The amendment searched arXiv using documented query families and produced 293 unique title/abstract records after pooled deduplication. Full text was assessed for 140 records: 132 were retained for consideration and eight were excluded. The retained set comprised 53 core-classified records and 79 supporting candidates. Of the 53 core records, one mapped to baseline P05, two were duplicate/version identities, and 50 unique studies were admitted to the canonical corpus. Of the 79 supporting candidates, 69 currently have aligned extraction packets and ten remain queued for extraction; none contributes to the 121-study denominator. A stale packet created before the exclusion of ARXIV-0051 is retained only as provenance and is not included in these counts.

An external 30-record export was screened separately after the canonical freeze. Reconciliation found 20 duplicates, including EXT-0006/P06; two full-text candidates retained outside the frozen denominator; seven access-limited metadata-only candidates; and one exclusion. The external export therefore contributes no additional study to the 121-study denominator. The freeze decision and provenance are recorded in `data/search/final-corpus-freeze-register.csv` and the associated screening ledgers.

<!-- table: caption="Auditable accounting of the baseline corpus and dated search amendments." label="tab:corpus-flow-audit" -->
| Source | Identified | Full text assessed | Canonical additions | Reserve or post-freeze | Duplicates | Access-limited |
|---|---:|---:|---:|---:|---:|---:|
| Historical baseline | NR | 71 | 71 | 0 | NR | NR |
| Dated arXiv amendment | 293 | 140 | 50 | 79 supporting: 69 extracted, 10 queued | 3 core identities | 0 |
| External cross-check export | 30 | 3 | 0 | 2 full-text candidates | 20 | 7 |

The rows are not additive identification stages: the external export is a post-freeze cross-check and overlaps the baseline and arXiv records. The canonical arithmetic is therefore `71 + 50 = 121`.

## Eligibility and Evidence Tiers

Core eligibility covered LLM-based, AI-assisted, or automated code review; generated review comments or PR feedback; code-review benchmarks and rubrics; relevant failure types; and mitigation through prompting, filtering, retrieval, verification, tool support, rewriting, or escalation. Supporting eligibility covered evaluator validity, human review, workflow value, annotation, context quality, and methodological foundations. General code generation or repair without a review connection was excluded unless retained as explicitly bounded peripheral evidence.

The frozen synthesis assigns 91 records to the core tier, 24 to supporting evidence, and six to peripheral evidence. The tiers indicate argumentative role, not methodological quality. Direct code-review evidence can support review-specific findings; supporting evidence defines constructs or qualifications; peripheral evidence is used only for bounded transfer claims. The 79 supplementary supporting candidates are outside these counts because they were not promoted through the canonical-note and freeze rule; 69 have aligned extraction packets and ten remain queued.

## Quality Appraisal

The proposal specified eight 0--2 criteria. The extraction workflow expanded these into 12 items covering artifact clarity, context, data, metrics, judging, reliability, limitations, relevance to the review questions, preservation, coverage/escalation, cost/workflow, and evaluator validity. The expanded instrument improves extraction consistency but is not presented as the proposal's original rubric. Total scores do not determine inclusion; criterion-level evidence, confidence, and evidence tier guide interpretation.

## Data Extraction

Each paper has one authoritative Markdown record derived from the local full text. Records contain bibliographic identity, screening decision, study design, RQ1--RQ5 evidence, a framework-traceability field, Q1--Q12 appraisal, trade-off fields, evaluator-validity fields, evidence locations, and unresolved verification items. All 121 records pass the same eleven-section structural validator. This validation establishes completeness of form, not independent reviewer agreement.

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

The complete field definitions and controlled labels are provided in the replication artifact `method/slr-data-dictionary.md`.

## Synthesis

We used tabulation, thematic grouping, and framework mapping. We did not pool incompatible metrics. Initial categories were derived during cross-paper synthesis and normalized into controlled vocabularies for failure types, evaluation dimensions, mitigation families, and context types. A deterministic script then projected the authoritative notes into one study-level CSV row per paper. The script searches the canonical numbered sections, records multi-valued controlled labels, and uses `NR` when the note does not contain enough evidence. The generated counts therefore describe coded evidence in the notes, not the prevalence of failures in deployed systems.

The script validates that the canonical note set occurs exactly once, baseline evidence tiers do not overlap, promoted supplementary records receive the core tier, bibliography keys resolve, and quality scores are available. Findings were organized by research question. Paper IDs provide internal traceability, while bibliography keys support publication-facing claims. Every reported count uses the 121-record evidence pool as its denominator unless another denominator is stated.

## Protocol Deviations and Amendments

The main deviation is retrospective protocol formalization: the baseline corpus was assembled before the complete search log was available. Evidence-tier assignment was added after full-text extraction to prevent indirect studies from receiving the same argumentative weight as direct code-review studies. The dated arXiv run is reported as an amendment and does not reconstruct the historical search. The external export is partial, and seven otherwise relevant records remain outside the frozen corpus because verified full text was unavailable. Any future database-search rerun must be dated and reported as a further amendment rather than described as if it preceded corpus assembly.
