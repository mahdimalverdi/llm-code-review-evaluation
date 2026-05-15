# P44 — A Survey on Large Language Models for Code Generation

> [!NOTE]
> Compact v2 analysis. P44 is a code-generation survey rather than a code-review paper. It is useful for background on LLM coding evaluation, benchmark limitations, and the relationship between generation, repair, and downstream software-engineering tasks.

## Status

- Paper ID: `P44`
- Analysis status: `First pass completed from bibliographic metadata; needs PDF-level verification`
- Priority: `Low`
- Reading depth: `Background`
- Last updated: `2026-05-14`
- Confidence in extraction: `Medium`

## Bibliographic Information

| Field | Value |
|---|---|
| Title | A Survey on Large Language Models for Code Generation |
| Authors | Juyong Jiang, Fan Wang, Jiasi Shen, Sungju Kim, Sunghun Kim |
| Year | 2025 |
| Venue / Source | ACM Transactions on Software Engineering and Methodology |
| Publication type | Peer-reviewed journal article / survey |
| Link | https://dl.acm.org/doi/full/10.1145/3747588 |
| DOI / arXiv | DOI: 10.1145/3747588; arXiv:2406.00515 |
| Code / artifact | Not applicable |

```bibtex
% TODO: Add checked ACM BibTeX.
```

## One-Sentence Summary

> This survey reviews large language models for code generation and provides background on coding benchmarks, evaluation practices, and limitations relevant to LLM-based software-engineering tools.

## Main Goal of the Paper

The paper aims to survey LLM-based code generation research, including models, tasks, datasets, benchmarks, evaluation metrics, and future challenges.

## Relevance to Our Research Questions

| Our RQ | Relevance | Evidence / Use |
|---|---|---|
| RQ1 — problematic comments | `Low` | Not about generated review comments. |
| RQ2 — context quality | `Low / Medium` | Code generation shares context and prompt-quality issues with code review. |
| RQ3 — evaluation dimensions | `Medium` | Useful for general critique of coding benchmarks and automatic metrics. |
| RQ4 — trade-offs | `Medium` | Code generation trade-offs around benchmark validity, cost, and repair are relevant background. |
| RQ5 — framework design | `Low / Medium` | Helps avoid reinventing generic code-generation evaluation concerns. |

## Dataset / Study Context

| Field | Value |
|---|---|
| Dataset / study name | Literature survey |
| Dataset / study source | LLM code-generation literature |
| Dataset / study size | Needs PDF-level verification |
| Repository type | Not applicable |
| Input context available | Surveyed code-generation tasks, benchmarks, and models |
| Output being evaluated | Research landscape |
| Data availability | Not applicable |

## Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Technical correctness | `High in general code tasks` | Correctness is central to code generation. |
| Evaluation validity | `Medium / High` | Surveys benchmarks and metrics. |
| Test-based validation | `Medium` | Code generation often uses executable tests. |
| Semantic equivalence | `Partially` | Relevant to generated code and repair. |
| Context quality | `Partially` | Prompt and task context matter. |
| Cost / scalability | `Partially` | Large coding models can be expensive. |
| Workflow impact | `Low` | Less central than in code review work. |

## Problematic Comment Types / Error Taxonomy

### Explicitly Defined Error Types

Not applicable; this is not a review-comment taxonomy paper.

### Inferred Error Types for Our Work

- `Inferred`: Benchmark-metric mismatch between generated artifacts and real developer value.
- `Inferred`: Overreliance on automated metrics that do not capture human usefulness.
- `Inferred`: Code-generation success does not imply review-comment usefulness.

## Context-Quality Extraction

| Context Dimension | Coverage | Evidence / Notes |
|---|---|---|
| Relevance | `Medium` | Code-generation prompts need task-relevant information. |
| Completeness | `Medium` | Missing specification or tests can produce wrong code. |
| Groundability | `Low / Medium` | Generated code should satisfy specification/tests; review comments need different grounding. |
| Cost / token budget | `Medium` | Large context and large models raise cost concerns. |
| Context availability vs usability | `Medium` | General lesson transfers to code review. |

## Trade-off Extraction

| Strategy / Mechanism | Benefit | Risk / Cost | Missing Metric for Our Work |
|---|---|---|---|
| Benchmark-driven evaluation | Enables reproducible comparison | May not reflect workflow usefulness | Review-comment workflow validity |
| Larger models | Better coding performance | Cost and latency | Value per cost |
| Automated metrics/tests | Scalable evaluation | Partial proxy for human value | Human-centered review quality |
| Code generation framing | Broad coding capability | Not enough for review rationale/actionability | Review-specific dimensions |

## Key Findings for Our Synthesis

| Finding | Importance for us |
|---|---|
| LLM coding tasks need careful benchmark and metric design. | Supports our metric-validity argument. |
| Code generation and code review share some evaluation problems but have different goals. | Helps distinguish our contribution from generic coding surveys. |
| Automatic metrics are useful but incomplete. | Reinforces the need for human-centered and workflow-aware dimensions. |

## Limitations from Our Perspective

- Not focused on code review.
- Does not directly address comment usefulness, actionability, or reviewer workflow.
- Should be used only for background on coding-task evaluation, not as core evidence.

## Final Assessment

| Field | Value |
|---|---|
| Overall relevance to our study | `Low / Medium` |
| Should we cite this paper? | `Maybe` |
| Priority for deep reading | `Low` |
| Confidence in this analysis | `Medium` |

### Short Justification

P44 is useful for broad LLM coding evaluation background but should not carry the main argument of our code-review evaluation framework.

## Follow-up TODOs

- [ ] Verify exact taxonomy and benchmark discussion from PDF.
- [ ] Add checked ACM BibTeX.
- [ ] Extract only the parts relevant to evaluation limitations.
- [ ] Decide whether this belongs in related work or background footnote only.
