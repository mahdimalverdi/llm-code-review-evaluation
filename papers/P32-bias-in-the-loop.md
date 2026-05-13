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
% TODO: Add checked arXiv/ACM BibTeX.
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
