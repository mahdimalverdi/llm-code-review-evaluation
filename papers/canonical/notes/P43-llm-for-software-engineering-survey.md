# P43 — A Survey on Large Language Models for Software Engineering

> [!NOTE]
> Compact v2 analysis. P43 is a broad software-engineering survey. It is not code-review-specific, but it helps position LLM-based code review within the wider LLM-for-SE landscape and provides background on SE task taxonomy and evaluation limitations.

## Status

- Paper ID: `P43`
- Analysis status: `First pass completed from bibliographic metadata; needs PDF-level verification`
- Priority: `Medium`
- Reading depth: `Background / positioning`
- Last updated: `2026-05-14`
- Confidence in extraction: `Medium`

## Bibliographic Information

| Field | Value |
|---|---|
| Title | A survey on large language models for software engineering |
| Authors | Quanjun Zhang, Chunrong Fang, Yang Xie, Yaxin Zhang, Shengcheng Yu, Weisong Sun, Yun Yang, Zhenyu Chen |
| Year | 2026 |
| Venue / Source | Science China Information Sciences |
| Publication type | Peer-reviewed journal article / survey |
| Link | https://doi.org/10.1007/s11432-025-4670-0 |
| DOI / arXiv | 10.1007/s11432-025-4670-0 |
| Code / artifact | Not applicable |

```bibtex
```

## One-Sentence Summary

> This survey maps the broader use of large language models in software engineering, providing background for positioning LLM-based code review among SE tasks and evaluation challenges.

## Main Goal of the Paper

The paper aims to survey LLM applications, methods, benchmarks, and challenges across software engineering tasks.

## Relevance to Our Research Questions

| Our RQ | Relevance | Evidence / Use |
|---|---|---|
| RQ1 — problematic comments | `Low` | Broad survey may mention failure types but is not review-comment-specific. |
| RQ2 — context quality | `Medium` | Useful for general SE context and task-specific constraints. |
| RQ3 — evaluation dimensions | `Medium` | Helps position evaluation limitations across SE tasks. |
| RQ4 — trade-offs | `Low / Medium` | Broad challenges can support discussion of cost, reliability, and generalization. |
| RQ5 — framework design | `Medium` | Provides landscape framing and terminology. |

## Dataset / Study Context

| Field | Value |
|---|---|
| Dataset / study name | Literature survey |
| Dataset / study source | LLM-for-SE literature |
| Dataset / study size | Needs PDF-level verification |
| Repository type | Not applicable |
| Input context available | Surveyed SE tasks, models, benchmarks, and challenges |
| Output being evaluated | Research landscape |
| Data availability | Not applicable |

## Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Technical correctness | `Broadly` | Relevant to SE tasks, not review-specific. |
| Evaluation validity | `Medium` | Surveys benchmarks and evaluation challenges. |
| Context quality | `Partially` | SE tasks require project and artifact context. |
| Reproducibility | `Partially` | Broad survey challenge. |
| Generalization | `Medium` | Important across SE tasks and datasets. |
| Workflow impact | `Low / Medium` | Depends on coverage in the survey; needs verification. |

## Problematic Comment Types / Error Taxonomy

### Explicitly Defined Error Types

Not a generated-review-comment taxonomy paper.

### Inferred Error Types

- `Inferred`: Evaluation mismatch between benchmark tasks and real SE workflows.
- `Inferred`: Insufficient task-specific context for SE reasoning.
- `Inferred`: Overgeneralized LLM evaluation across heterogeneous SE tasks.

## Context-Quality Extraction

| Context Dimension | Coverage | Evidence / Notes |
|---|---|---|
| Relevance | `Medium` | SE tasks require task-specific artifacts. |
| Completeness | `Medium` | Many SE tasks require repository/project context. |
| Specificity / focus | `Medium` | Broad SE tasks need tailored context. |
| Groundability | `Medium` | Code-related outputs should be grounded in artifacts and constraints. |
| Cost / token budget | `Partially` | Large-context SE tasks face cost and scalability issues. |

## Trade-off Extraction

| Strategy / Mechanism | Benefit | Risk / Cost | Missing Metric for Our Work |
|---|---|---|---|
| Broad LLM-for-SE capability | Shows applicability across SE | May hide task-specific evaluation needs | Code-review-specific evaluation dimensions |
| General SE benchmarks | Enable comparison | May be too abstract for workflow tasks | Workflow validity |
| Larger/contextual models | Improve some SE tasks | Cost, latency, and context dilution | Context-quality and cost metrics |

## Key Findings for Our Synthesis

| Finding | Importance for us |
|---|---|
| LLM-based code review should be framed inside the broader LLM-for-SE research landscape. | Helps position related work. |
| SE tasks require task-specific evaluation and context. | Supports our argument for a review-specific framework. |
| General LLM-for-SE surveys are too broad to solve review-comment evaluation. | Helps identify our narrower contribution. |

## Limitations from Our Perspective

- Broad survey, not code-review-specific.
- Likely insufficient for fine-grained review-comment taxonomy.
- Useful mainly for background, positioning, and challenge framing.

## Final Assessment

| Field | Value |
|---|---|
| Overall relevance to our study | `Medium` |
| Should we cite this paper? | `Maybe / Yes for broad positioning` |
| Priority for deep reading | `Medium` |
| Confidence in this analysis | `Medium` |

### Short Justification

P43 helps place our work within LLM-for-SE but should not be overused as evidence for code-review-specific claims.

## Follow-up TODOs

- [ ] Verify survey taxonomy and exact code-review coverage from PDF.
- [ ] Add checked Springer BibTeX.
- [ ] Extract 1–2 positioning sentences for related work.
- [ ] Check whether it discusses evaluation limitations relevant to our framework.
## Legacy proposal-aligned quality appraisal (superseded by the canonical record)

P43 is **Supporting / Medium relevance**. It supports RQ2–RQ4 through broader LLM-for-SE evaluation dimensions, reliability, cost, and generalization; RQ5 through methodological limitations; and RQ6 through background positioning. It is not code-review-specific.

**Quality score: 14/24.** Q1–Q3=2, Q4–Q5=1, Q6=1, Q7=1, Q8=1, Q9=0, Q10=1, Q11=1, Q12=2.
## Canonical citation record

Use citation key `p43_zhang2026_llm_se_survey` from `references/references.bib`; do not duplicate its BibTeX entry in this note.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative; the compact block is provenance only.

- Identification/screening: `p43_zhang2026_llm_se_survey`; Supporting; Include; Medium relevance.
- Study overview: Broad survey of LLMs across software-engineering tasks and evaluation practices.
- RQ1: General hallucination, reliability, and task-failure categories; review-specific evidence is limited.
- RQ2: Evaluation, grounding, generalization, and context dimensions (Reported).
- RQ3: SE task/model/metric landscape (Reported).
- RQ4: Reliability, cost, generalization, and operational trade-offs (Reported).
- RQ5: Dataset and evaluator validity (Reported).
- RQ6: Background and framework-positioning support.
- Failure taxonomy: broad LLM/SE failures; not a complete review-comment taxonomy.
- Metrics: task-specific quality, correctness, robustness, and resource metrics.
- Mitigation/trade-off: prompting, retrieval, fine-tuning, and tool use; review-specific consequences are indirect.
- Validity: broad survey synthesis, not a primary review experiment.
- Quality: 14/24; supporting evidence.
- Synthesis conclusion: use for background, not core review-comment claims.

### 1. Identification
- P43; `p43_zhang2026_llm_se_survey`; local full PDF; included as supporting unless explicitly marked core; authoritative record.
### 2. Screening and proposal alignment
- Include as supporting. `p43_zhang2026_llm_se_survey`; Supporting; Include; Medium relevance.
### 3. Study overview
Broad survey of LLMs across software-engineering tasks and evaluation practices.
### 4. Evidence mapped to proposal RQ1–RQ6
| RQ | Evidence | Type | Location |
|---|---|---|---|
| RQ1 | General hallucination, reliability, and task-failure categories; review-specific evidence is limited. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ2 | Evaluation, grounding, generalization, and context dimensions (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ3 | SE task/model/metric landscape (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ4 | Reliability, cost, generalization, and operational trade-offs (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ5 | Dataset and evaluator validity (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ6 | Background and framework-positioning support. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
### 5. Failure and problematic-comment categories
| Category | Type | Location |
|---|---|---|
| broad LLM/SE failures | Reported/Inferred | Full PDF |
| not a complete review-comment taxonomy. | Reported/Inferred | Full PDF |
### 6. Evaluation dimensions and metrics
| Dimension/metric | Limitation | Location |
|---|---|---|
| task-specific quality | Indirect/supporting evidence only | Full PDF |
| correctness | Indirect/supporting evidence only | Full PDF |
| robustness | Indirect/supporting evidence only | Full PDF |
| and resource metrics. | Indirect/supporting evidence only | Full PDF |
### 7. Mitigation and trade-offs
- Mitigation/intervention: prompting, retrieval, fine-tuning, and tool use; review-specific consequences are indirect.
- Useful feedback potentially lost: not directly measured unless stated above.
- Coverage: indirect/task-specific; retained useful-review coverage is incomplete.
- Human escalation: no formal rate/policy reported unless stated above.
- Cost: paper-specific evidence above; otherwise Not reported.
### 8. Annotation and evaluator validity
- broad survey synthesis, not a primary review experiment.
- Q7–Q8 encode judging and reliability depth.
### 9. Quality appraisal
| Criterion | Score | Evidence note |
|---|---:|---|
| Q1 | 2 | goal at scored depth. |
| Q2 | 2 | artifact at scored depth. |
| Q3 | 2 | dataset/context at scored depth. |
| Q4 | 1 | procedure at scored depth. |
| Q5 | 1 | metrics at scored depth. |
| Q6 | 1 | failures at scored depth. |
| Q7 | 1 | judging at scored depth. |
| Q8 | 1 | reliability at scored depth. |
| Q9 | 0 | intervention at scored depth. |
| Q10 | 1 | trade-offs at scored depth. |
| Q11 | 1 | threats at scored depth. |
| Q12 | 2 | SLR support at scored depth. |
- Total: 15/24; reporting/relevance score; supporting status is unchanged.
### 10. Review-process reliability and bias
- Indirect transfer, missing preservation/escalation evidence, and selection/publication bias remain explicit; second-reviewer calibration is unavailable.
### 11. Synthesis-ready conclusion
- Contribution: Broad survey of LLMs across software-engineering tasks and evaluation practices.
- Boundary: use for background, not core review-comment claims.
