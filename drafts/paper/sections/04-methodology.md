# Review Method

## Review Design

We conducted a targeted structured literature review inspired by software-engineering SLR guidance. The review follows question definition, study identification, eligibility assessment, quality appraisal, data extraction, thematic synthesis, and reporting. Taxonomy construction and reliability planning additionally draw on established taxonomy and agreement methods [@m01_nickerson2013_taxonomy; @m02_cohen1960_kappa; @m03_krippendorff2018_content_analysis]. The work is not presented as a fully reproducible SLR because the original database-specific search dates, queries, retrieval counts, deduplication counts, and title/abstract screening history were not preserved.

## Review Questions

| RQ | Question |
|---|---|
| RQ1 | Which problematic-comment types and failure categories have been reported? |
| RQ2 | Which evaluation dimensions have been used for correctness, grounding, relevance, usefulness, actionability, context quality, and evaluator validity? |
| RQ3 | Which mitigation families have been proposed or evaluated, and where do they intervene? |
| RQ4 | What evidence exists about error reduction versus useful-feedback preservation, coverage, escalation, and cost? |
| RQ5 | How are context quality, dataset validity, and annotation difficulty treated? |
| RQ6 | Which studies directly or indirectly support the taxonomy, annotation protocol, and framework? |

## Search Scope and Corpus Assembly

The proposal defined ACM Digital Library, IEEE Xplore, ScienceDirect, SpringerLink, arXiv, Semantic Scholar, Google Scholar, and Scopus where available, with a primary focus on work from 2021 onward and earlier foundational modern-code-review studies. Query families covered LLM code review, automated review, generated comments, evaluation metrics, hallucination and grounding, context-aware review, LLM-as-a-Judge, and human--AI review.

The local corpus contains 71 unique full-text records. These records cannot be treated as the output of a reproducible search flow because the original retrieval and exclusion counts are unavailable. We therefore report verified local-corpus counts and do not infer missing identification-stage counts from the PDF directory.

## Eligibility and Evidence Tiers

Core eligibility covered LLM-based, AI-assisted, or automated code review; generated review comments or PR feedback; code-review benchmarks and rubrics; relevant failure types; and mitigation through prompting, filtering, retrieval, verification, tool support, rewriting, or escalation. Supporting eligibility covered evaluator validity, human review, workflow value, annotation, context quality, and methodological foundations. General code generation or repair without a review connection was excluded unless retained as explicitly bounded peripheral evidence.

The synthesis assigns 41 records to the core tier, 24 to supporting evidence, and six to peripheral evidence. The tiers indicate argumentative role, not methodological quality. Direct code-review evidence can support review-specific findings; supporting evidence defines constructs or qualifications; peripheral evidence is used only for bounded transfer claims.

## Quality Appraisal

The proposal specified eight 0--2 criteria. The extraction workflow expanded these into 12 items covering artifact clarity, context, data, metrics, judging, reliability, limitations, relevance to the review questions, preservation, coverage/escalation, cost/workflow, and evaluator validity. The expanded instrument improves extraction consistency but is not presented as the proposal's original rubric. Total scores do not determine inclusion; criterion-level evidence, confidence, and evidence tier guide interpretation.

## Data Extraction

Each paper has one authoritative Markdown record derived from the local full text. Records contain bibliographic identity, screening decision, study design, RQ1--RQ6 evidence, Q1--Q12 appraisal, trade-off fields, evaluator-validity fields, evidence locations, and unresolved verification items. All 71 records pass the same eleven-section structural validator. This validation establishes completeness of form, not independent reviewer agreement.

## Synthesis

We used tabulation, thematic grouping, and framework mapping. We did not pool incompatible metrics. Findings were organized by failure type, evaluation dimension, mitigation intervention point, preservation and cost evidence, context and dataset validity, and evaluator risk. Paper IDs provide internal traceability; bibliography keys support publication-facing claims. Denominators are stated when counts are reported.

## Protocol Deviations and Amendments

The main deviation is retrospective protocol formalization: the corpus was assembled before the complete search log was available. Evidence-tier assignment was added after full-text extraction to prevent indirect studies from receiving the same argumentative weight as direct code-review studies. Any future database-search rerun must be dated and reported as an amendment rather than described as if it preceded corpus assembly.
