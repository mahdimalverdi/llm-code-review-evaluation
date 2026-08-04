# P35 — LLM Critics Help Catch LLM Bugs

> [!NOTE]
> Compact v2 analysis. P35 is not a conventional LLM-as-a-judge benchmark. It is a scalable-oversight paper about critic models that help humans evaluate model-written code by producing natural-language critiques.

## Status

- Paper ID: `P35`
- Analysis status: `First pass completed from PDF; needs citation/BibTeX cleanup`
- Priority: `High`
- Reading depth: `Read once from PDF`
- Confidence: `High`

## Bibliographic Information

| Field | Value |
|---|---|
| Title | LLM Critics Help Catch LLM Bugs |
| Authors | Nat McAleese, Rai (Michael Pokorny), Juan Felipe Cerón Uribe, Evgenia Nitishinskaya, Maja Trębácz, Jan Leike |
| Year | 2024 |
| Organization | OpenAI |
| DOI / arXiv | arXiv:2407.00215 |

```bibtex
```

## One-Sentence Summary

> P35 trains LLM critic models to write code critiques that help humans catch bugs in model-written code, showing that critics improve bug detection and comprehensiveness but also introduce hallucinated bugs and nitpicks.

## Main Contribution

The paper demonstrates scalable oversight for code: instead of asking an LLM judge to directly score an answer, it trains a critic model to produce natural-language feedback that assists human evaluators. The main idea is that human+critic teams may overcome weaknesses of both humans and models.

## Study Context

| Field | Value |
|---|---|
| Input format | `(question, answer)` pairs where the answer contains code. |
| Data source | OpenAI RLHF pipeline / ChatGPT training data. |
| Code filter | Examples where model response is at least 50% Python by line count. |
| Evaluation distributions | Human Inserted Bugs and Human Detected Bugs. |
| Human reviewers | Contractors from ChatGPT/CriticGPT training pool; median ~5 years Python experience. |
| Human critique time | Median around 50 minutes per example. |
| Decline rate | Around 4% of tasks. |

## Critique Attributes

| Attribute | Meaning |
|---|---|
| Comprehensiveness | Whether the critique omits clear and severe issues. |
| Critique-Bug Inclusion (CBI) | Whether the critique catches a known reference bug. |
| Hallucinated bug / fake problem | Whether the critique claims a non-existent problem. |
| Nitpick | Whether the critique contains low-value quibbles. |
| Conciseness | Whether the critique avoids unnecessary verbosity. |
| Overall helpfulness | Subjective quality considering correctness, completeness, style, and usefulness. |

## Method

| Component | Details |
|---|---|
| Critic model | GPT-4-family model trained to output structured natural-language critiques. |
| Training | RLHF on critique comparison data. |
| Tampering | Contractors insert subtle bugs into model-written code and write reference bug descriptions. |
| Reward model | Trained from human rankings of critiques. |
| Policy optimization | PPO. |
| FSBS | Force Sampling Beam Search balances more highlighted issues against reward-model score. |
| Human+critic setup | Contractor critique is prefilled with critic output; humans can keep, remove, edit, or add comments. |

## Key Findings

| Finding | Summary |
|---|---|
| F1 | Model-written critiques are often preferred over human-written critiques on model-written code with known bugs. |
| F2 | On naturally occurring LLM errors, model-written critiques are preferred over human critiques in 63% of cases. |
| F3 | LLM critics catch more inserted bugs than human contractors in the study setup. |
| F4 | Human+CriticGPT teams write more comprehensive critiques than humans alone. |
| F5 | LLM critics hallucinate and nitpick more than humans. |
| F6 | Human+CriticGPT teams hallucinate/nitpick less than LLM-only critics while retaining much of the comprehensiveness benefit. |
| F7 | CriticGPT reduces hallucinated bugs and nitpicks compared with prompted ChatGPT, but the absolute rate remains non-trivial. |
| F8 | FSBS provides a controllable precision/recall-like frontier between comprehensiveness and spurious claims. |
| F9 | Tampered data with known reference bugs improves agreement and training signal compared with unmodified data. |
| F10 | A negative experiment on difficult competition-code pairs shows critics did not significantly help humans choose passing over failing solutions under that setup. |

## Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Bug detection | Very high | CBI and comprehensiveness. |
| Hallucination / fake problems | Very high | Explicitly measured. |
| Nitpicking | Very high | Explicitly measured. |
| Human+AI collaboration | Very high | Human+critic teams evaluated. |
| Precision/recall trade-off | High | FSBS controls critique length/claims. |
| Inter-rater agreement | Medium / High | Higher agreement with reference bug descriptions. |
| Workflow utility | Medium | Critiques support RLHF/human evaluation, not production PR review. |
| Repository/multi-file context | Low | Limitation: short snippets, no repo navigation. |

## Problematic Critique / Review Types

- Hallucinated bug / fake problem.
- Nitpick-heavy critique.
- Overly long critique with low precision.
- High-recall but low-precision critique.
- Missing severe known bug.
- Overstated severity.
- Single-step critique unable to handle distributed or multi-file bug.
- Critique that helps on inserted bugs but generalizes weakly to natural bugs.
- Critic output that biases human reviewers into false positives.

## Context-Quality Evidence

P35 shows that known reference bugs dramatically improve evaluation quality and inter-rater agreement. Without a concrete reference issue, humans disagree more on which critique is better. This supports the idea that code-review evaluation needs explicit issue targets or structured subclaims rather than only free-form overall preference.

## Trade-off Extraction

| Strategy | Benefit | Risk / Cost |
|---|---|---|
| LLM critic assistance | Helps humans catch more bugs and write more comprehensive critiques. | Can introduce hallucinated bugs and nitpicks. |
| Human+critic teaming | Balances LLM recall with human precision. | Human still needs time to verify/edit/remove suggestions. |
| Tampered-bug data | Provides hard known-bug supervision and better agreement. | Inserted bugs differ from natural model errors. |
| FSBS | Tunes comprehensiveness vs hallucination/nitpick rate at inference time. | Requires reward model and extra sampling cost. |
| Critique-only oversight | Provides actionable feedback, not just scalar score. | Does not itself prove final policy improvement. |

## Relevance to Our Paper

P35 is valuable because it gives a rigorous language for evaluating review-like comments: comprehensiveness, known-bug inclusion, hallucinated bug, nitpick, conciseness, and helpfulness. It also supports our argument that human+AI review should be evaluated as a workflow, not only as model-only accuracy.

## Limitations from Our Perspective

- Focuses on LLM-written code, not human PRs or production code review.
- Code snippets are short and mostly single-file; no repository navigation or multi-file context.
- Inserted bugs may not match natural LLM error distribution.
- Assumes catching more bugs improves downstream RLHF labels; final policy improvement is not directly tested.
- Critics still hallucinate and nitpick at meaningful rates.
- Not a code-review-comment generation benchmark in the usual ACR sense.

## Follow-up TODOs

- [ ] Add CBI/comprehensiveness/hallucinated-bug/nitpick to review-comment evaluation dimensions.
- [ ] Add human+critic workflow to human-AI review synthesis.
- [ ] Add FSBS-like precision/recall trade-off to mitigation strategies.
- [ ] Add known-issue/reference-bug evaluation design to final framework.
## Legacy proposal-aligned quality appraisal (superseded by the canonical record)

P35 is **Core/Supporting / High relevance**. It supports RQ1 through hallucinated bugs, nitpicks, and incomplete or incorrect critiques; RQ2–RQ3 through critique quality dimensions; RQ4 through critic benefit versus human/compute cost; and RQ6 through critic-assisted mitigation design.

**Quality score: 20/24.** Q1–Q7=2, Q8=1, Q9=2, Q10=1, Q11=1, Q12=2. The task concerns generated-code critique and should be transferred to code review cautiously.
## Canonical citation record

Use citation key `p35_mcaleese2024_llm_critics` from `references/references.bib`; do not duplicate its BibTeX entry in this note.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative; the compact block is provenance only.

- Identification/screening: `p35_mcaleese2024_llm_critics`; Supporting/Core; Include; High relevance.
- Study overview: Critic models help humans detect bugs in LLM-generated code.
- RQ1: Hallucinated bugs, nitpicks, incomplete critiques, and incorrect critiques (Reported).
- RQ2: Critique grounding, comprehensiveness, functionality, and human usefulness (Reported).
- RQ3: Critic-assisted evaluation and human oversight (Reported).
- RQ4: Critic benefit versus compute, false alarms, and human verification cost (Reported).
- RQ5: Human evaluation and evaluator validity (Reported).
- RQ6: Strong critic-assisted mitigation support.
- Failure taxonomy: hallucinated bug; nitpick; incomplete critique; incorrect critique; unsupported suggestion.
- Metrics: comprehensiveness, hallucination/false-alarm rate, human detection benefit, and critique quality.
- Mitigation/trade-off: critic-assisted human oversight; catches errors but adds model and verification cost.
- Validity: generated-code snippets differ from PR-level review; transfer is bounded.
- Quality: 20/24; strong supporting/core evidence.
- Synthesis conclusion: supports critic-plus-human workflows and false-alarm measurement.

### 1. Identification
- P35; `p35_mcaleese2024_llm_critics`; local full PDF; included; authoritative record.
### 2. Screening and proposal alignment
- Include as supporting. `p35_mcaleese2024_llm_critics`; Supporting/Core; Include; High relevance.
### 3. Study overview
Critic models help humans detect bugs in LLM-generated code.
### 4. Evidence mapped to proposal RQ1–RQ6
| RQ | Evidence | Type | Location |
|---|---|---|---|
| RQ1 | Hallucinated bugs, nitpicks, incomplete critiques, and incorrect critiques (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ2 | Critique grounding, comprehensiveness, functionality, and human usefulness (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ3 | Critic-assisted evaluation and human oversight (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ4 | Critic benefit versus compute, false alarms, and human verification cost (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ5 | Human evaluation and evaluator validity (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ6 | Strong critic-assisted mitigation support. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
### 5. Failure and problematic-comment categories
| Category | Type | Location |
|---|---|---|
| hallucinated bug | Reported/Inferred | Full PDF |
| nitpick | Reported/Inferred | Full PDF |
| incomplete critique | Reported/Inferred | Full PDF |
| incorrect critique | Reported/Inferred | Full PDF |
| unsupported suggestion. | Reported/Inferred | Full PDF |
### 6. Evaluation dimensions and metrics
| Dimension/metric | Limitation | Location |
|---|---|---|
| comprehensiveness | Not an end-to-end outcome | Full PDF |
| hallucination/false-alarm rate | Not an end-to-end outcome | Full PDF |
| human detection benefit | Not an end-to-end outcome | Full PDF |
| and critique quality. | Not an end-to-end outcome | Full PDF |
### 7. Mitigation and trade-offs
- Mitigation/intervention: critic-assisted human oversight; catches errors but adds model and verification cost.
- Useful feedback potentially lost: not directly measured unless stated above.
- Coverage: partial; useful-issue retention after intervention is incomplete.
- Human escalation: no formal rate/policy reported unless stated above.
- Cost: paper-specific evidence above; otherwise Not reported.
### 8. Annotation and evaluator validity
- generated-code snippets differ from PR-level review; transfer is bounded.
- Q7–Q8 encode judging and reliability depth.
### 9. Quality appraisal
| Criterion | Score | Evidence note |
|---|---:|---|
| Q1 | 2 | goal at scored depth. |
| Q2 | 2 | artifact at scored depth. |
| Q3 | 2 | dataset/context at scored depth. |
| Q4 | 2 | procedure at scored depth. |
| Q5 | 2 | metrics at scored depth. |
| Q6 | 2 | failures at scored depth. |
| Q7 | 2 | judging at scored depth. |
| Q8 | 1 | reliability at scored depth. |
| Q9 | 2 | intervention at scored depth. |
| Q10 | 1 | trade-offs at scored depth. |
| Q11 | 1 | threats at scored depth. |
| Q12 | 2 | SLR support at scored depth. |
- Total: 21/24; reporting-quality score.
### 10. Review-process reliability and bias
- Missing preservation/escalation evidence and selection/publication bias remain explicit; second-reviewer calibration is unavailable.
### 11. Synthesis-ready conclusion
- Contribution: Critic models help humans detect bugs in LLM-generated code.
- Boundary: supports critic-plus-human workflows and false-alarm measurement.
