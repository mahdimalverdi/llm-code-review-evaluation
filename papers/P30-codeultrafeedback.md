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
% TODO: Add checked ACM BibTeX.
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
