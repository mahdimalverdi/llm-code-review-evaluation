# P32 — Bias in the Loop: Auditing LLM-as-a-Judge for Software Engineering

> [!NOTE]
> Compact v2 analysis. P32 is a high-priority evaluator-validity paper because it directly audits prompt-induced bias, consistency, answer rate, and A/B-order sensitivity for LLM-as-a-Judge in software engineering tasks.

## Status

- Paper ID: `P32`
- Analysis status: `First pass completed from PDF; needs citation/BibTeX cleanup`
- Priority: `High`
- Reading depth: `Read once from PDF`
- Confidence: `High`

## Bibliographic Information

| Field | Value |
|---|---|
| Title | Bias in the Loop: Auditing LLM-as-a-Judge for Software Engineering |
| Authors | Zixiao Zhao, Amirreza Esmaeili, Fatemeh Fard |
| Year | 2026 |
| Venue / Source | arXiv / TOSEM draft metadata in PDF |
| DOI / arXiv | arXiv:2604.16790 |

```bibtex
```

## One-Sentence Summary

> P32 shows that LLM judges for code are highly sensitive to prompt-injected presentation biases, and that reported judge accuracy can reflect prompt artifacts rather than stable evaluation ability.

## Main Contribution

The paper treats LLM-as-a-Judge as a measurement instrument. It evaluates not only accuracy but also bias sensitivity, consistency, and answer-rate reliability under controlled prompt perturbations for code generation, code repair, and unit-test generation.

## Dataset / Study Context

| Field | Value |
|---|---|
| Benchmark | CodeJudgeBench |
| Total pairs | 5,352 good/bad pairs |
| Tasks | Code generation, code repair, unit-test generation |
| Difficulty labels | Easy, medium, hard from CodeJudgeBench |
| Judges | Qwen3-4B, Qwen2.5-Coder-3B, GPT |
| Evaluation setup | Pairwise A/B judging with original and swapped order |

## Bias Suite

| Bias | Meaning in Code Judging |
|---|---|
| Position | Candidate order affects verdict. |
| Authority | Standards/provenance cues over-credited. |
| Bandwagon | Prior reviewer preference shifts judgment. |
| Chain-of-thought | Visible reasoning attached to one option shifts attention. |
| Distraction | Non-target cues such as rich formatting/trivia divert attention. |
| Diversity / style | Style or paradigm preference substitutes for correctness. |
| Final-only | Confident final answer can bias judge. |
| Model-name | Model/source provenance creates halo effect. |
| Refined | “Refined version” label biases toward that answer. |
| Self-enhance | Judge favors same model family. |
| Sentiment | Confident/constructive tone affects selection. |
| Verbosity | Longer explanations/comments are treated as stronger evidence. |

## Metrics / Reliability Measures

| Metric | Purpose |
|---|---|
| Accuracy | Whether judge selects the benchmark-labeled good response. |
| Robustness / bias sensitivity | Deviation from no-bias condition under prompt perturbations. |
| A/B order comparison | Detects whether same content is judged differently by position. |
| Consistency rate | Test-retest reliability across repeated runs with fixed prompt. |
| Answer rate | Fraction of cases where judge emits a valid structured A/B verdict. |
| Token-level confidence | Explains how prompt cues shift decision confidence, not only final answer. |

## Key Findings

| Finding | Summary |
|---|---|
| F1 | Judge decisions are highly sensitive to prompt-level presentation cues even when the underlying code is unchanged. |
| F2 | Some biases improve accuracy when they favor the correct option and severely reduce accuracy when they favor the incorrect option. |
| F3 | Biases can alter task-level conclusions and model rankings. |
| F4 | CoT, authority, refined, and sentiment cues often act as A-favoring priors. |
| F5 | Verbosity often creates the opposite direction, acting like a B-favoring cue in their setup. |
| F6 | TestGen is the most fragile task; CodeRepair is generally more stable. |
| F7 | Qwen2.5-Coder-3B has very high answer rate (~99%), while Qwen3-4B only emits valid structured verdicts about 44% overall. |
| F8 | High consistency can be misleading: a judge may consistently repeat a biased decision. |
| F9 | GPT has stronger baseline accuracy/consistency than smaller open models, but still shifts under prompt biases. |
| F10 | Token-level confidence shows bias can move internal probability mass even when the final answer does not change. |

## Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Prompt-induced bias | Very high | Central contribution. |
| Position/order sensitivity | Very high | Original vs swapped A/B. |
| Consistency / test-retest reliability | Very high | Repeated runs under identical settings. |
| Answer-format reliability | High | Answer rate as first-class metric. |
| Task difficulty | High | Easy/medium/hard splits. |
| Closed/open judge comparison | Medium / High | Qwen and GPT comparison. |
| Token confidence | Medium | Used for explainability. |
| Human calibration | Low | Uses benchmark labels, not new human study. |

## Problematic Judge / Evaluation Types

- Prompt-biased judge.
- Position-sensitive judge.
- Verbosity-sensitive judge.
- Authority/provenance-biased judge.
- CoT-overtrusting judge.
- Refined-version halo effect.
- Sentiment/tone-biased judge.
- Judge with low answer rate or invalid structured outputs.
- Consistently wrong judge.
- Judge whose ranking conclusions flip under prompt perturbations.

## Context-Quality Evidence

P32 shows that evaluator context is itself a major source of measurement error. The code can stay unchanged while prompt framing, candidate order, tone, model-name, or “refined” labels change the verdict. Therefore, evaluator prompts are not neutral wrappers; they are part of the experimental condition.

## Trade-off Extraction

| Strategy / Check | Benefit | Risk / Cost |
|---|---|---|
| A/B order swapping | Detects position effects. | Doubles evaluation cost and may require aggregation rules. |
| Controlled prompt perturbations | Reveals bias sensitivity. | Adds protocol complexity. |
| Repeated runs | Measures test-retest reliability. | Higher cost; two runs may still under-estimate variance. |
| Answer-rate reporting | Catches non-judgment failures. | Requires strict output parsing and missing-data policy. |
| Token confidence analysis | Explains hidden decision shifts. | Model/tool dependent; not always available. |
| Escalation to tests/static analysis/humans | Protects high-stakes decisions. | Slower and less scalable. |

## Relevance to Our Paper

P32 is directly useful for the evaluator-validity section. It supports our claim that a code-review evaluation framework must audit the judge itself. For our work, LLM-as-a-Judge should be reported with accuracy, answer rate, repeated-run consistency, A/B swap consistency, and prompt-bias sensitivity.

## Limitations from Our Perspective

- Focuses on code generation/repair/test generation rather than review comments.
- Pairwise A/B setting may not capture open-ended multi-comment code review.
- Only two repeated runs for consistency estimates.
- Bias suite is controlled and reproducible but not exhaustive.
- Human judgment is not newly collected; benchmark labels provide the oracle.

## Follow-up TODOs

- [ ] Add answer rate as evaluator-validity metric.
- [ ] Add prompt-bias sensitivity to LLM-as-a-judge protocol checklist.
- [ ] Add “high consistency can be consistently biased” to validity discussion.
- [ ] Add A/B swap and controlled perturbation requirements to final framework.
## Legacy proposal-aligned quality appraisal (superseded by the canonical record)

P32 is **Supporting/Core / High relevance**. It supports RQ2–RQ3 through evaluator bias, reliability, and robustness measures; RQ4 through bias-mitigation cost and validity trade-offs; RQ5 through annotation/evaluator validity; and RQ6 through judge-audit protocol design.

**Quality score: 21/24.** Q1–Q8=2, Q9=0, Q10=2, Q11=1, Q12=2. Bias findings concern evaluators and should not be conflated with generated-comment failures.
## Canonical citation record

Use citation key `p32_zhao2026_bias_loop` from `references/references.bib`; do not duplicate its BibTeX entry in this note.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative; the compact block is provenance only.

- Identification/screening: `p32_zhao2026_bias_loop`; Supporting; Include; High relevance.
- Study overview: Bias suite and audit protocol for LLM-as-a-Judge in software engineering.
- RQ1: Evaluator failures rather than generated-comment failures: authority, sentiment, position, verbosity, and prompt-perturbation effects (Reported).
- RQ2: Judge validity and robustness dimensions (Reported).
- RQ3: Bias and reliability metrics (Reported).
- RQ4: Bias mitigation versus evaluation cost and residual uncertainty (Reported).
- RQ5: Direct evaluator/annotation validity support.
- RQ6: Strong judge-audit protocol support.
- Failure taxonomy: position; verbosity; authority; sentiment; prompt sensitivity; answer-rate instability.
- Metrics: agreement, consistency, perturbation sensitivity, answer rate, confidence/token shifts.
- Mitigation/trade-off: bias auditing/mitigation; additional runs and cost may improve validity.
- Validity: evaluator bias must be separated from comment-generation failure.
- Quality: 21/24; high-quality supporting evidence.
- Synthesis conclusion: every LLM judge used in the SLR framework requires bias and robustness checks.

### 1. Identification
- P32; `p32_zhao2026_bias_loop`; local full PDF; included; authoritative record.
### 2. Screening and proposal alignment
- Include as supporting. `p32_zhao2026_bias_loop`; Supporting; Include; High relevance.
### 3. Study overview
Bias suite and audit protocol for LLM-as-a-Judge in software engineering.
### 4. Evidence mapped to proposal RQ1–RQ6
| RQ | Evidence | Type | Location |
|---|---|---|---|
| RQ1 | Evaluator failures rather than generated-comment failures: authority, sentiment, position, verbosity, and prompt-perturbation effects (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ2 | Judge validity and robustness dimensions (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ3 | Bias and reliability metrics (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ4 | Bias mitigation versus evaluation cost and residual uncertainty (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ5 | Direct evaluator/annotation validity support. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ6 | Strong judge-audit protocol support. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
### 5. Failure and problematic-comment categories
| Category | Type | Location |
|---|---|---|
| position | Reported/Inferred | Full PDF |
| verbosity | Reported/Inferred | Full PDF |
| authority | Reported/Inferred | Full PDF |
| sentiment | Reported/Inferred | Full PDF |
| prompt sensitivity | Reported/Inferred | Full PDF |
| answer-rate instability. | Reported/Inferred | Full PDF |
### 6. Evaluation dimensions and metrics
| Dimension/metric | Limitation | Location |
|---|---|---|
| agreement | Not an end-to-end outcome | Full PDF |
| consistency | Not an end-to-end outcome | Full PDF |
| perturbation sensitivity | Not an end-to-end outcome | Full PDF |
| answer rate | Not an end-to-end outcome | Full PDF |
### 7. Mitigation and trade-offs
- Mitigation/intervention: bias auditing/mitigation; additional runs and cost may improve validity.
- Useful feedback potentially lost: not directly measured unless stated above.
- Coverage: partial; useful-issue retention after intervention is incomplete.
- Human escalation: no formal rate/policy reported unless stated above.
- Cost: paper-specific evidence above; otherwise Not reported.
### 8. Annotation and evaluator validity
- evaluator bias must be separated from comment-generation failure.
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
| Q8 | 2 | reliability at scored depth. |
| Q9 | 0 | intervention at scored depth. |
| Q10 | 2 | trade-offs at scored depth. |
| Q11 | 1 | threats at scored depth. |
| Q12 | 2 | SLR support at scored depth. |
- Total: 21/24; reporting-quality score.
### 10. Review-process reliability and bias
- Missing preservation/escalation evidence and selection/publication bias remain explicit; second-reviewer calibration is unavailable.
### 11. Synthesis-ready conclusion
- Contribution: Bias suite and audit protocol for LLM-as-a-Judge in software engineering.
- Boundary: every LLM judge used in the SLR framework requires bias and robustness checks.
