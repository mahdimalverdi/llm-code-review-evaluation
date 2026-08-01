# P34 — From Code to Courtroom: LLMs as the New Software Judges

> [!NOTE]
> Compact v2 analysis. P34 is the earlier, shorter vision/position version of the LLM-as-a-Judge-in-SE roadmap. P33 appears to be the expanded newer version with 42 primary studies, while P34 reviews 16 studies.

## Status

- Paper ID: `P34`
- Analysis status: `First pass completed from PDF; needs citation/BibTeX cleanup`
- Priority: `Medium / High`
- Reading depth: `Read once from PDF`
- Confidence: `High`

## Bibliographic Information

| Field | Value |
|---|---|
| Title | From Code to Courtroom: LLMs as the New Software Judges |
| Authors | Junda He, Jieke Shi, Terry Yue Zhuo, Christoph Treude, Jiamou Sun, Zhenchang Xing, Xiaoning Du, David Lo |
| Year | 2025 |
| Venue / Source | arXiv / SE 2030 forward-looking paper |
| DOI / arXiv | arXiv:2503.02246 |

```bibtex
```

## One-Sentence Summary

> P34 argues that LLM-as-a-Judge can become a scalable surrogate for human evaluation of software artifacts, but only if the community builds better benchmarks, bias analyses, SE-specialized judges, tool integration, human oversight, and adversarial defenses.

## Relationship to P33

P34 and P33 share authors, title, and core roadmap. P34 appears to be an earlier version:

| Aspect | P34 | P33 |
|---|---|---|
| Primary studies reviewed | 16 | 42 |
| Scope | Shorter roadmap and vision | Broader systematic review and more detailed taxonomy |
| Best use | Early vision/position citation | Main survey/roadmap citation |

For our paper, P33 should be treated as the stronger source. P34 is useful mainly for tracing the evolution of the argument and for the concise roadmap framing.

## Formal Definition

Like P33, P34 defines:

```text
E(T, C, X, R) -> (Y, E, F)
```

where `T` is evaluation type, `C` criteria, `X` evaluated item, `R` optional reference, `Y` result, `E` explanation, and `F` feedback.

P34 explicitly argues for a stricter LLM-as-a-Judge definition than broad LLM-based evaluation: embedding-based metrics such as BERTScore/CodeBERTScore should not be treated as true LLM-as-a-Judge because they do not independently judge, explain, or provide feedback.

## Reviewed SE Applications

| Task | Examples |
|---|---|
| Code generation | Evaluating generated code correctness and quality. |
| Code changes / patches | Static-analysis warning fixes, vulnerability fixes, test outcome prediction. |
| Software documentation summarization | Code summaries and bug report summaries. |
| Other SE tasks | Programming Q&A, code translation, requirements causality extraction. |

## Core Claims

| Claim | Summary |
|---|---|
| C1 | Human evaluation is ideal but costly, slow, and fatigue-prone. |
| C2 | Traditional metrics are scalable but weak for nuanced qualities such as usefulness/readability. |
| C3 | LLM-as-a-Judge can be execution-free, reference-free, and multi-faceted. |
| C4 | Current work is still early and inconsistent. |
| C5 | LLM judges need better SE expertise and external tool support. |
| C6 | Human-in-the-loop escalation is necessary for low-confidence/high-stakes cases. |
| C7 | Adversarial manipulation of judges is underexplored in SE. |

## Key Limitations Identified

| Limitation | Why It Matters |
|---|---|
| Small-scale human-alignment datasets | Limits external validity. |
| Inconsistent empirical findings | Different datasets/prompts/models lead to conflicting conclusions. |
| Limited bias studies | Position, verbosity, and egocentric bias remain insufficiently studied in SE. |
| Inadequate SE domain expertise | A model that generates code may not judge code well. |
| Reliance on internal LLM knowledge | Missing static-analysis, execution, formal-verification, and model-checking evidence. |
| Security/adversarial threats | Judge can be manipulated through comments, code layout, or deceptive context. |

## Roadmap

| Direction | Details |
|---|---|
| More empirical evaluation and benchmarking | Large, multi-dimensional, expert-annotated benchmarks. |
| Better internal judgment | Improve SE expertise and embed expert tacit knowledge. |
| Better external judgment | Integrate SE tools and human-in-the-loop workflows. |
| Security of LLM judges | Adversarial testing and defensive mechanisms. |

## Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Judge paradigm definition | High | Strict distinction from embedding metrics. |
| SE task mapping | Medium | 16 primary studies. |
| Benchmark gaps | High | Strong emphasis. |
| Bias/fairness | Medium / High | Calls for more empirical study. |
| Tool integration | High | Static analyzers, formal methods, IDE integration. |
| Human-in-the-loop | High | Low-confidence escalation. |
| Adversarial security | High | Judge manipulation threats. |

## Problematic Judge / Evaluation Types

- LLM judge treated as a drop-in human replacement.
- Small benchmark overgeneralization.
- Judge with hidden position/verbosity/egocentric bias.
- Judge without SE domain expertise.
- Judge relying only on internal reasoning when external evidence is available.
- Vulnerable judge that can be manipulated by comments, formatting, or deceptive context.

## Context-Quality Evidence

P34 stresses that evaluation quality depends on more than the candidate artifact: it also depends on criteria, references, SE tool outputs, human confidence thresholds, and adversarial robustness.

## Trade-off Extraction

| Strategy | Benefit | Risk / Cost |
|---|---|---|
| LLM-as-a-Judge | Scalable and multi-faceted. | Bias, inconsistency, and hidden invalidity. |
| Execution-free judging | Works when execution is costly or unavailable. | May miss behavioral correctness. |
| Tool-integrated judging | Adds stronger objective evidence. | Operational complexity. |
| Human-in-the-loop | Improves high-stakes reliability. | Reduces automation gains. |
| Adversarial hardening | Protects judge integrity. | Requires attack models and extra testing. |

## Relevance to Our Paper

P34 supports the high-level claim that LLM-based evaluation must be treated as a first-class research problem. It is especially useful for a concise roadmap quote/summary, but P33 should be the primary survey evidence.

## Limitations from Our Perspective

- Earlier/shorter version of P33; avoid over-weighting both as separate evidence.
- Roadmap is conceptual, not empirically validated.
- Not code-review-comment-specific.
- Does not operationalize useful-feedback preservation.

## Follow-up TODOs

- [ ] Use only where the concise early vision is helpful.
- [ ] Prefer P33 for detailed survey claims.
- [ ] Add strict LLM-as-a-Judge vs LLM-based metric distinction to evaluator section.
## Legacy proposal-aligned quality appraisal (superseded by the canonical record)

P34 is **Supporting / Medium–High relevance**. It supports RQ2–RQ4 through evaluator validity, human oversight, high-stakes review, and escalation arguments; RQ5 through threats to validity; and RQ6 through roadmap/methodology design. Direct evidence for comment taxonomy is limited.

**Quality score: 18/24.** Q1–Q5=2, Q6=1, Q7=1, Q8=1, Q9=1, Q10=2, Q11=1, Q12=2. Treat its roadmap claims as interpretation rather than measured deployment results.
## Canonical citation record

Use citation key `p34_he2025_code_courtroom` from `references/references.bib`; do not duplicate its BibTeX entry in this note.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative; the compact block is provenance only.

- Identification/screening: `p34_he2025_code_courtroom`; Supporting; Include; Medium–High relevance.
- Study overview: Roadmap/vision for LLMs as software judges, with emphasis on trust, accountability, and high-stakes oversight.
- RQ1: Judge reliability and harmful evaluation outcomes (Reported/Our perspective).
- RQ2: Validity, context, uncertainty, and human oversight (Reported).
- RQ3: Evaluator roles and evaluation dimensions (Reported).
- RQ4: Human escalation, accountability, and automation risk (Reported).
- RQ5: Threats to validity and socio-technical concerns (Reported).
- RQ6: Roadmap support for evaluator and escalation framework.
- Failure taxonomy: over-trust; unsupported judgment; miscalibration; accountability loss.
- Metrics: proposed/roadmap dimensions; limited new empirical metrics.
- Mitigation/trade-off: human-in-the-loop escalation; reliability gains versus cost and delay.
- Validity: vision/roadmap claims must not be reported as measured outcomes.
- Quality: 18/24; supporting conceptual evidence.
- Synthesis conclusion: motivates escalation and accountability dimensions.

### 1. Identification
- P34; `p34_he2025_code_courtroom`; local full PDF; included; authoritative record.
### 2. Screening and proposal alignment
- Include as supporting. `p34_he2025_code_courtroom`; Supporting; Include; Medium–High relevance.
### 3. Study overview
Roadmap/vision for LLMs as software judges, with emphasis on trust, accountability, and high-stakes oversight.
### 4. Evidence mapped to proposal RQ1–RQ6
| RQ | Evidence | Type | Location |
|---|---|---|---|
| RQ1 | Judge reliability and harmful evaluation outcomes (Reported/Our perspective). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ2 | Validity, context, uncertainty, and human oversight (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ3 | Evaluator roles and evaluation dimensions (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ4 | Human escalation, accountability, and automation risk (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ5 | Threats to validity and socio-technical concerns (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ6 | Roadmap support for evaluator and escalation framework. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
### 5. Failure and problematic-comment categories
| Category | Type | Location |
|---|---|---|
| over-trust | Reported/Inferred | Full PDF |
| unsupported judgment | Reported/Inferred | Full PDF |
| miscalibration | Reported/Inferred | Full PDF |
| accountability loss. | Reported/Inferred | Full PDF |
### 6. Evaluation dimensions and metrics
| Dimension/metric | Limitation | Location |
|---|---|---|
| proposed/roadmap dimensions | Not an end-to-end outcome | Full PDF |
| limited new empirical metrics. | Not an end-to-end outcome | Full PDF |
### 7. Mitigation and trade-offs
- Mitigation/intervention: human-in-the-loop escalation; reliability gains versus cost and delay.
- Useful feedback potentially lost: not directly measured unless stated above.
- Coverage: partial; useful-issue retention after intervention is incomplete.
- Human escalation: no formal rate/policy reported unless stated above.
- Cost: paper-specific evidence above; otherwise Not reported.
### 8. Annotation and evaluator validity
- vision/roadmap claims must not be reported as measured outcomes.
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
| Q9 | 1 | intervention at scored depth. |
| Q10 | 2 | trade-offs at scored depth. |
| Q11 | 1 | threats at scored depth. |
| Q12 | 2 | SLR support at scored depth. |
- Total: 19/24; reporting-quality score.
### 10. Review-process reliability and bias
- Missing preservation/escalation evidence and selection/publication bias remain explicit; second-reviewer calibration is unavailable.
### 11. Synthesis-ready conclusion
- Contribution: Roadmap/vision for LLMs as software judges, with emphasis on trust, accountability, and high-stakes oversight.
- Boundary: motivates escalation and accountability dimensions.
