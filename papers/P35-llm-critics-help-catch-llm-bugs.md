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
% TODO: Add checked arXiv BibTeX.
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
