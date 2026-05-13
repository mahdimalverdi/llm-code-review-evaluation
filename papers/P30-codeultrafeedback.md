# P30 — CodeUltraFeedback: An LLM-as-a-Judge Dataset for Aligning Large Language Models to Coding Preferences

> [!NOTE]
> Compact v2 analysis. P30 is useful for our evaluator and preference-dimension sections because it operationalizes non-functional coding preferences and uses LLM-as-a-judge annotations for preference tuning.

## Status

- Paper ID: `P30`
- Analysis status: `First pass completed from PDF; needs citation/BibTeX cleanup`
- Priority: `Medium / High`
- Reading depth: `Read once from PDF`
- Confidence: `High`

## Bibliographic Information

| Field | Value |
|---|---|
| Title | CodeUltraFeedback: An LLM-as-a-Judge Dataset for Aligning Large Language Models to Coding Preferences |
| Authors | Martin Weyssow, Aton Kamanda, Xin Zhou, Houari Sahraoui |
| Year | 2024 |
| Venue / Source | arXiv / TOSEM candidate |
| DOI / arXiv | arXiv:2403.09032; DOI listed in sheet as 10.1145/3736407 |
| Artifact | GitHub: `martin-wey/CodeUltraFeedback` |

```bibtex
% TODO: Verify final publication metadata and BibTeX.
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
| F1 | GPT-4-Turbo and GPT-3.5-Turbo receive the highest average preference scores in the dataset. |
| F2 | Strong code models still underperform GPT-3.5/4 on preference alignment. |
| F3 | GPT-4/3.5 responses are not always best; another LLM response is preferred for about 73% of samples. |
| F4 | SFT+DPO improves CodeLlama-7B-Instruct alignment across preferences. |
| F5 | DPO and SFT+DPO significantly improve most preference dimensions except instruction following. |
| F6 | Alignment tuning can improve functional correctness versus the base model, though SFT alone gives the largest Pass@k gains. |
| F7 | Judge selection matters: GPT-3.5 and GPT-4 produce different rankings/scores. |
| F8 | GPT-3.5 aligns more closely with human evaluators than GPT-4 on the 100-sample manual check under their setup. |
| F9 | GPT-4 distinguishes test-passing from test-failing HumanEval+ solutions better than GPT-3.5. |

## Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Coding preferences | Very high | Five explicit non-functional dimensions. |
| LLM-as-a-judge dataset construction | High | GPT-3.5 ratings + rationales. |
| Judge-human agreement | Medium | 100 manually judged samples. |
| Judge selection sensitivity | High | GPT-3.5 vs GPT-4 differences. |
| Functional correctness | Medium / High | HumanEval/HumanEval+ Pass@k. |
| Preference tuning | High | SFT/DPO experiments. |
| Reference-guided judging | High | Bench uses reference response. |

## Problematic Judge / Evaluation Types

- Judge-specific preference ranking.
- GPT-3.5 judge that may not distinguish test-passing from test-failing code well.
- GPT-4 judge that may have different style preferences from humans/GPT-3.5.
- Preference-over-optimization that improves non-functional alignment but may not maximize functional correctness.
- Reference-dependent judging.
- Verbosity/length bias risk in coding preference evaluation.

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
- GPT-3.5-generated labels are treated as preference data, creating judge-dependence.
- Manual validation is limited to 100 samples.
- Reference-guided grading may not fit open-ended review-comment evaluation.
- The paper uses coding-preference tasks, not PR workflow or review comments.

## Follow-up TODOs

- [ ] Add coding preference dimensions to evaluation framework.
- [ ] Add judge-selection sensitivity to evaluator-validity synthesis.
- [ ] Add reference-guided judging trade-off to framework.
- [ ] Update `matrices/cross-paper-synthesis.md` with P30 evidence.
