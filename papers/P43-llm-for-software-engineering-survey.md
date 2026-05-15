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
% TODO: Add checked Springer BibTeX.
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
