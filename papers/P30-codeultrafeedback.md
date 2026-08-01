# P30 — CodeUltraFeedback: An LLM-as-a-Judge Dataset for Aligning Large Language Models to Coding Preferences

> [!NOTE]
> Compact v2 analysis. P30 is useful for our evaluator and preference-dimension sections because it operationalizes non-functional coding preferences and uses LLM-as-a-judge annotations for preference tuning. Metadata has been aligned with the spreadsheet: the official ACM TOSEM DOI is retained, and arXiv remains the preprint/PDF source.

## Status

- Paper ID: `P30`
- Analysis status: `First pass completed from PDF; metadata aligned with spreadsheet; needs BibTeX cleanup`
- Priority: `Medium / High`
- Reading depth: `Read once from PDF`
- Last updated: `2026-05-15`
- Confidence: `High`

## Bibliographic Information

| Field | Value |
|---|---|
| Title | CodeUltraFeedback: An LLM-as-a-Judge Dataset for Aligning Large Language Models to Coding Preferences |
| Authors | Martin Weyssow, Aton Kamanda, Xin Zhou, Houari Sahraoui |
| Year | 2025 |
| Venue / Source | ACM Transactions on Software Engineering and Methodology |
| Publication type | Peer-reviewed journal article |
| Link | https://dl.acm.org/doi/abs/10.1145/3736407 |
| DOI / arXiv | DOI: 10.1145/3736407; arXiv:2403.09032 |
| Artifact | GitHub: `martin-wey/CodeUltraFeedback` |

```bibtex
```

## One-Sentence Summary

> P30 introduces CodeUltraFeedback, a 10,000-instruction / 40,000-response LLM-as-a-judge preference dataset for aligning code LLMs to five coding preferences: instruction following, explanation, complexity/efficiency, readability, and coding style.

## Main Contribution

The paper uses LLM-as-a-judge to create preference data and then uses that data to align a code model through SFT and DPO. It is not code-review-specific, but it is highly relevant because it formalizes non-functional coding preferences and shows how judge choice affects alignment scores.

## Dataset / Study Context

| Field | Value |
|---|---|
| Base instructions | 10,000 Magicoder Evol-Instruct samples |
| Responses | 40,000 responses |
| Response models | Four responses per instruction, sampled from 14 LLMs |
| Preferences | Instruction following, code explanation, complexity/efficiency, readability, coding style |
| Judge for dataset | GPT-3.5-Turbo |
| Benchmark subset | 500 instructions in CodeUltraFeedback-Bench |
| Alignment target | CodeLlama-7B-Instruct with SFT, DPO, SFT+DPO |

## Preference Dimensions

| Preference | Evaluation Meaning |
|---|---|
| Instruction following | Fidelity to user constraints and directives. |
| Code explanation | Clarity, depth, relevance, and accessibility of explanation. |
| Code complexity and efficiency | Time efficiency, resource efficiency, algorithm effectiveness, optimization. |
| Code readability | Clarity, conciseness, relevance of comments/docs, comprehensibility. |
| Coding style | Readability, maintainability, efficiency, idiomatic style. |

## Key Findings

| Finding | Summary |
|---|---|
| F1 | Strong code models still underperform GPT-3.5/4 on preference alignment. |
| F2 | GPT-4/3.5 responses are not always best; another LLM response can be preferred in many samples. |
| F3 | SFT+DPO improves CodeLlama-7B-Instruct alignment across preference dimensions. |
| F4 | Judge selection matters: GPT-3.5 and GPT-4 produce different rankings/scores. |
| F5 | Human agreement checks are necessary because LLM preference labels are judge-dependent. |

## Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Coding preferences | Very high | Five explicit non-functional dimensions. |
| LLM-as-a-judge dataset construction | High | GPT-based ratings and rationales. |
| Judge-human agreement | Medium | Manual validation subset. |
| Judge selection sensitivity | High | GPT-3.5 vs GPT-4 differences. |
| Functional correctness | Medium / High | Coding benchmark evaluation is included. |
| Preference tuning | High | SFT/DPO experiments. |
| Reference-guided judging | High | Benchmark uses reference responses. |

## Problematic Judge / Evaluation Types

- Judge-specific preference ranking.
- Preference-over-optimization that improves non-functional alignment but may not maximize functional correctness.
- Reference-dependent judging.
- Verbosity/length bias risk in coding preference evaluation.
- Closed-source judge drift and reproducibility risk.

## Context-Quality Evidence

P30 shows that high-quality evaluation for code generation requires explicit preference context. A generic judge score is not enough; the judge needs to know whether it is evaluating readability, explanation, efficiency, style, or instruction following.

## Trade-off Extraction

| Strategy | Benefit | Risk / Cost |
|---|---|---|
| LLM-as-a-judge annotations | Scales preference-data construction. | Depends on judge quality and biases. |
| Reference-guided grading | More consistent comparison point. | Requires reference responses and may favor reference style. |
| DPO alignment | Improves preference alignment. | May not optimize functional correctness as strongly as SFT. |
| Preference dimensions | Captures non-functional qualities. | Rubric design can shape results and miss project-specific preferences. |
| Closed-source judge | Strong evaluator capability. | Cost, reproducibility, and judge drift concerns. |

## Relevance to Our Paper

P30 supports adding non-functional and preference-based dimensions to code review evaluation: readability, explanation quality, style, efficiency, and instruction following. It also strengthens our caution that LLM judges need calibration and that judge choice changes conclusions.

## Limitations from Our Perspective

- Not code-review-specific.
- LLM-generated preference labels create judge-dependence.
- Manual validation is limited.
- Reference-guided grading may not fit open-ended review-comment evaluation.
- The paper uses coding-preference tasks, not PR workflow or review comments.

## Follow-up TODOs

- [ ] Add checked ACM BibTeX.
- [ ] Add coding preference dimensions to evaluation framework.
- [ ] Add judge-selection sensitivity to evaluator-validity synthesis.
- [ ] Add reference-guided judging trade-off to framework.
## Legacy proposal-aligned quality appraisal (superseded by the canonical record)

P30 is **Supporting/Core / High relevance**. It supports RQ2–RQ3 through preference dimensions and evaluator comparison; RQ4 through feedback quality, judge choice, and preference-coverage trade-offs; RQ5 through annotation validity; and RQ6 through evaluator and preference-data design. Its direct evidence for code-review-specific failure taxonomy is limited.

**Quality score: 20/24.** Q1–Q5=2, Q6=1, Q7=2, Q8=2, Q9=0, Q10=2, Q11=1, Q12=2. Preference data should not be equated with correctness or production usefulness.
## Canonical citation record

Use citation key `p30_weyssow2025_codeultrafeedback` from `references/references.bib`; do not duplicate its BibTeX entry in this note.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative; the compact block is provenance only.

- Identification/screening: `p30_weyssow2025_codeultrafeedback`; Supporting; Include; High relevance.
- Study overview: LLM-as-a-Judge preference dataset for aligning coding models to review/evaluation preferences.
- RQ1: Direct comment-failure taxonomy is limited; preference disagreement and low-quality outputs are relevant (Reported/Our perspective).
- RQ2: Preference dimensions, evaluator judgments, and coding context (Reported).
- RQ3: Preference data, judge quality, and alignment outcomes (Reported).
- RQ4: Preference alignment versus judge cost, bias, and generalization (Reported).
- RQ5: Annotation and evaluator-validity evidence (Reported).
- RQ6: Strong preference/evaluator methodology support.
- Failure taxonomy: preference disagreement; evaluator inconsistency; low-quality output; judge bias.
- Metrics: preference agreement, judge quality, alignment, and robustness.
- Mitigation/trade-off: preference optimization; may improve judged alignment while overfitting preferences.
- Validity: preference is not correctness, actionability, or production acceptance.
- Quality: 20/24; strong supporting evidence.
- Synthesis conclusion: supports proxy-validity analysis for preference-based evaluation.

### 1. Identification
- P30; `p30_weyssow2025_codeultrafeedback`; local full PDF; included; authoritative record.
### 2. Screening and proposal alignment
- Include as supporting. `p30_weyssow2025_codeultrafeedback`; Supporting; Include; High relevance.
### 3. Study overview
LLM-as-a-Judge preference dataset for aligning coding models to review/evaluation preferences.
### 4. Evidence mapped to proposal RQ1–RQ6
| RQ | Evidence | Type | Location |
|---|---|---|---|
| RQ1 | Direct comment-failure taxonomy is limited; preference disagreement and low-quality outputs are relevant (Reported/Our perspective). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ2 | Preference dimensions, evaluator judgments, and coding context (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ3 | Preference data, judge quality, and alignment outcomes (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ4 | Preference alignment versus judge cost, bias, and generalization (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ5 | Annotation and evaluator-validity evidence (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ6 | Strong preference/evaluator methodology support. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
### 5. Failure and problematic-comment categories
| Category | Type | Location |
|---|---|---|
| preference disagreement | Reported/Inferred | Full PDF |
| evaluator inconsistency | Reported/Inferred | Full PDF |
| low-quality output | Reported/Inferred | Full PDF |
| judge bias. | Reported/Inferred | Full PDF |
### 6. Evaluation dimensions and metrics
| Dimension/metric | Limitation | Location |
|---|---|---|
| preference agreement | Not an end-to-end outcome | Full PDF |
| judge quality | Not an end-to-end outcome | Full PDF |
| alignment | Not an end-to-end outcome | Full PDF |
| and robustness. | Not an end-to-end outcome | Full PDF |
### 7. Mitigation and trade-offs
- Mitigation/intervention: preference optimization; may improve judged alignment while overfitting preferences.
- Useful feedback potentially lost: not directly measured unless stated above.
- Coverage: partial; useful-issue retention after intervention is incomplete.
- Human escalation: no formal rate/policy reported unless stated above.
- Cost: paper-specific evidence above; otherwise Not reported.
### 8. Annotation and evaluator validity
- preference is not correctness, actionability, or production acceptance.
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
| Q7 | 2 | judging at scored depth. |
| Q8 | 2 | reliability at scored depth. |
| Q9 | 0 | intervention at scored depth. |
| Q10 | 2 | trade-offs at scored depth. |
| Q11 | 1 | threats at scored depth. |
| Q12 | 2 | SLR support at scored depth. |
- Total: 20/24; reporting-quality score.
### 10. Review-process reliability and bias
- Missing preservation/escalation evidence and selection/publication bias remain explicit; second-reviewer calibration is unavailable.
### 11. Synthesis-ready conclusion
- Contribution: LLM-as-a-Judge preference dataset for aligning coding models to review/evaluation preferences.
- Boundary: supports proxy-validity analysis for preference-based evaluation.
