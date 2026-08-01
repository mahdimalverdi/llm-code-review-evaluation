# P38 — Expectations, Outcomes, and Challenges of Modern Code Review

> [!NOTE]
> Compact v2 analysis. P38 is a foundational empirical study of modern code review. It helps us avoid treating code review as only defect detection and supports a broader definition of useful review feedback.

## Status

- Paper ID: `P38`
- Analysis status: `First pass completed from bibliographic metadata and known study framing; needs PDF-level verification`
- Priority: `High`
- Reading depth: `Deep / foundational background`
- Last updated: `2026-05-14`
- Confidence in extraction: `Medium`

## Bibliographic Information

| Field | Value |
|---|---|
| Title | Expectations, Outcomes, and Challenges of Modern Code Review |
| Authors | Alberto Bacchelli, Christian Bird |
| Year | 2013 |
| Venue / Source | ICSE / TU Delft |
| Publication type | Foundational empirical study |
| Link | https://research.tudelft.nl/en/publications/expectations-outcomes-and-challenges-of-modern-code-review |
| DOI / arXiv | 10.1109/ICSE.2013.6606617 |
| Code / artifact | Not applicable |

```bibtex
```

## One-Sentence Summary

> This paper shows that modern code review is expected to produce outcomes beyond defect detection, including knowledge transfer, alternative solution discovery, team awareness, and maintainability improvement.

## Main Goal of the Paper

The paper investigates what practitioners expect from modern code review, what outcomes they actually observe, and what challenges arise in real review practice.

## Relevance to Our Research Questions

| Our RQ | Relevance | Evidence / Use |
|---|---|---|
| RQ1 — problematic comments | `Medium` | Helps define problematic comments as comments that fail to support expected review outcomes. |
| RQ2 — context quality | `Medium` | Review depends on understanding rationale, surrounding code, and design alternatives. |
| RQ3 — evaluation dimensions | `High` | Supports evaluation dimensions beyond correctness, especially usefulness and knowledge transfer. |
| RQ4 — trade-offs | `High` | Review benefits are balanced against reviewer effort, delay, and communication costs. |
| RQ5 — framework design | `High` | Provides baseline human-review goals that LLM review evaluation should preserve. |

## Dataset / Study Context

| Field | Value |
|---|---|
| Dataset / study name | Modern code review empirical study |
| Dataset / study source | Practitioner study / software development setting |
| Dataset / study size | Needs PDF-level verification |
| Number of repositories / projects | Not verified in this pass |
| Programming languages | Not central to this pass |
| Repository type | Mixed / industrial and practitioner context; needs verification |
| Input context available | Human review practice, expectations, challenges |
| Output being evaluated | Code review outcomes and developer expectations |
| Data availability | Summarized in paper |

## Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Technical correctness | `Yes` | Defect detection is one expected outcome. |
| Usefulness | `Yes` | The whole study helps define useful review outcomes. |
| Actionability | `Partially` | Feedback should help authors improve changes. |
| Specificity | `Partially` | Review comments need to refer to concrete issues or alternatives. |
| Review coverage / issue coverage | `Partially` | Review can miss concerns depending on reviewer attention and context. |
| Reviewer time overhead | `Yes` | Review effort and delay are part of the challenge space. |
| Workflow impact | `Yes` | Review process challenges are central. |
| Developer trust | `Partially` | Review value depends on social and team expectations. |
| Trade-off analysis | `Partially` | Not a formal matrix, but review benefit vs cost is implicit. |

## Problematic Comment Types / Error Taxonomy

### Explicitly Defined Error Types

Not a taxonomy paper for generated comments.

### Inferred Error Types

- `Inferred`: Comment that only nitpicks without supporting meaningful review outcomes.
- `Inferred`: Comment that is too vague to support knowledge transfer or improvement.
- `Inferred`: Comment that ignores design alternatives or broader maintainability concerns.
- `Inferred`: Comment that consumes review effort without improving correctness, maintainability, or shared understanding.

## Context-Quality Extraction

| Context Dimension | Coverage | Evidence / Notes |
|---|---|---|
| Relevance | `High` | Review feedback should relate to meaningful change concerns. |
| Completeness | `Medium` | Reviewers need enough surrounding context to evaluate alternatives and consequences. |
| Consistency | `Medium` | Review practice depends on team norms and expectations. |
| Groundability | `Medium` | Comments should be grounded in code, design rationale, or project practice. |
| Attention load | `High` | Human review is limited by reviewer effort and cognitive load. |

## Trade-off Extraction

| Strategy / Mechanism | Benefit | Risk / Cost | Missing Metric for LLM Review |
|---|---|---|---|
| Human review | Rich outcomes: defect detection, knowledge transfer, maintainability | Time, delay, and communication cost | Which outcomes LLM comments preserve or degrade |
| Automated review support | Potentially reduces workload | May optimize for shallow defect-like comments only | Non-defect usefulness and developer value |
| Broader review goals | Captures real value of review | Harder to measure consistently | Multi-dimensional evaluation rubric |

## Key Findings for Our Synthesis

| Finding | Importance for us |
|---|---|
| Code review has multiple expected outcomes. | We should not evaluate LLM review only by bug-detection or reference overlap. |
| Review outcomes include knowledge and awareness. | LLM-generated comments should be evaluated for explanation, context, and value. |
| Review practice has challenges and costs. | Trade-off-aware evaluation must include reviewer overhead and workflow friction. |

## Limitations from Our Perspective

- Not about LLMs or generated review comments.
- Does not provide metrics for automated comment evaluation.
- Needs careful mapping from human-review goals to LLM-review evaluation dimensions.

## Final Assessment

| Field | Value |
|---|---|
| Overall relevance to our study | `High` |
| Should we cite this paper? | `Yes` |
| Priority for deep reading | `High` |
| Confidence in this analysis | `Medium` |

### Short Justification

P38 is a core background source for arguing that useful code review feedback is multi-dimensional. It helps justify our framework’s focus on usefulness, actionability, context, and workflow impact.

## Follow-up TODOs

- [ ] Verify exact methodology and study size from PDF.
- [ ] Add checked IEEE BibTeX.
- [ ] Extract cite-worthy claims about review outcomes beyond defect detection.
- [ ] Map human-review outcomes to `synthesis/evaluation-dimensions.md`.
## Legacy proposal-aligned quality appraisal (superseded by the canonical record)

P38 is **Supporting / High relevance**. It supports RQ2–RQ3 through reviewer expectations, outcomes, usefulness, and challenge dimensions; RQ4 through review benefits versus cost and burden; RQ5 through human/context validity; and RQ6 through workflow-oriented framework design. It is not an LLM mitigation experiment.

**Quality score: 18/24.** Q1–Q5=2, Q6=1, Q7=1, Q8=1, Q9=0, Q10=2, Q11=1, Q12=2.
## Canonical citation record

Use citation key `p38_bacchelli2013_expectations_mcr` from `references/references.bib`; do not duplicate its BibTeX entry in this note.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative; the compact block is provenance only.

- Identification/screening: `p38_bacchelli2013_expectations_mcr`; Supporting; Include; High relevance.
- Study overview: Empirical study of expectations, outcomes, and challenges in modern code review.
- RQ1: Unclear, low-value, or mismatch feedback and process challenges (Reported/Our perspective).
- RQ2: Reviewer/author context, expectations, and interaction (Reported).
- RQ3: Review outcomes, usefulness, communication, and process dimensions (Reported).
- RQ4: Review benefit versus effort, delay, and coordination cost (Reported).
- RQ5: Strong human-centered validity support.
- RQ6: Supports workflow and evaluation-dimension design.
- Failure taxonomy: unclear; low-value; expectation-mismatch; coordination-friction feedback.
- Metrics: expectations, outcomes, challenges, review effort, and interaction.
- Mitigation/trade-off: human review/process improvements; no LLM mitigation.
- Validity: foundational context rather than generated-comment evidence.
- Quality: 18/24; supporting evidence.
- Synthesis conclusion: supports socio-technical dimensions often missed by model metrics.

### 1. Identification
- P38; `p38_bacchelli2013_expectations_mcr`; local full PDF; included; authoritative record.
### 2. Screening and proposal alignment
- Include as supporting. `p38_bacchelli2013_expectations_mcr`; Supporting; Include; High relevance.
### 3. Study overview
Empirical study of expectations, outcomes, and challenges in modern code review.
### 4. Evidence mapped to proposal RQ1–RQ6
| RQ | Evidence | Type | Location |
|---|---|---|---|
| RQ1 | Unclear, low-value, or mismatch feedback and process challenges (Reported/Our perspective). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ2 | Reviewer/author context, expectations, and interaction (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ3 | Review outcomes, usefulness, communication, and process dimensions (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ4 | Review benefit versus effort, delay, and coordination cost (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ5 | Strong human-centered validity support. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ6 | Supports workflow and evaluation-dimension design. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
### 5. Failure and problematic-comment categories
| Category | Type | Location |
|---|---|---|
| unclear | Reported/Inferred | Full PDF |
| low-value | Reported/Inferred | Full PDF |
| expectation-mismatch | Reported/Inferred | Full PDF |
| coordination-friction feedback. | Reported/Inferred | Full PDF |
### 6. Evaluation dimensions and metrics
| Dimension/metric | Limitation | Location |
|---|---|---|
| expectations | Not an end-to-end outcome | Full PDF |
| outcomes | Not an end-to-end outcome | Full PDF |
| challenges | Not an end-to-end outcome | Full PDF |
| review effort | Not an end-to-end outcome | Full PDF |
### 7. Mitigation and trade-offs
- Mitigation/intervention: human review/process improvements; no LLM mitigation.
- Useful feedback potentially lost: not directly measured unless stated above.
- Coverage: partial; useful-issue retention after intervention is incomplete.
- Human escalation: no formal rate/policy reported unless stated above.
- Cost: paper-specific evidence above; otherwise Not reported.
### 8. Annotation and evaluator validity
- foundational context rather than generated-comment evidence.
- Q7–Q8 encode judging and reliability depth.
### 9. Quality appraisal
| Criterion | Score | Evidence note |
|---|---:|---|
| Q1 | 2 | goal at scored depth. |
| Q2 | 2 | artifact at scored depth. |
| Q3 | 2 | dataset/context at scored depth. |
| Q4 | 2 | procedure at scored depth. |
| Q5 | 2 | metrics at scored depth. |
| Q6 | 1 | failures at scored depth. |
| Q7 | 1 | judging at scored depth. |
| Q8 | 1 | reliability at scored depth. |
| Q9 | 0 | intervention at scored depth. |
| Q10 | 2 | trade-offs at scored depth. |
| Q11 | 1 | threats at scored depth. |
| Q12 | 2 | SLR support at scored depth. |
- Total: 18/24; reporting-quality score.
### 10. Review-process reliability and bias
- Missing preservation/escalation evidence and selection/publication bias remain explicit; second-reviewer calibration is unavailable.
### 11. Synthesis-ready conclusion
- Contribution: Empirical study of expectations, outcomes, and challenges in modern code review.
- Boundary: supports socio-technical dimensions often missed by model metrics.
