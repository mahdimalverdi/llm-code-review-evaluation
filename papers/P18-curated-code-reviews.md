# P18 — Harnessing Large Language Models for Curated Code Reviews

> [!NOTE]
> Compact v2 analysis. P18 is central for the data-quality layer of our synthesis because it proposes a comment-quality framework, uses LLM-as-a-Judge with human sanity checks, curates noisy review comments, and shows that clearer/civil/concise comments improve both comment generation and code refinement.

## Status

- Paper ID: `P18`
- Analysis status: `First pass completed from PDF; needs citation/BibTeX cleanup`
- Priority: `Medium / High`
- Reading depth: `Read once from PDF`
- Confidence: `High`

## Bibliographic Information

| Field | Value |
|---|---|
| Title | Harnessing Large Language Models for Curated Code Reviews |
| Authors | Oussama Ben Sghaier, Martin Weyssow, Houari Sahraoui |
| Year | 2025 |
| Venue / Source | MSR 2025 / arXiv |
| DOI / arXiv | DOI: 10.1109/MSR66628.2025.00039; arXiv:2502.03425 |
| Artifact | CuREV replication package and Zenodo data |

```bibtex
% TODO: Add checked MSR/arXiv BibTeX.
```

## One-Sentence Summary

> P18 proposes CuRev, a curated code review dataset produced by filtering irrelevant comments and reformulating noisy comments to improve clarity, conciseness, and civility, then shows that the curated data improves comment generation and code refinement.

## Main Contribution

P18 shifts the focus from model architecture to input/reference quality. It argues that code review automation is limited by noisy datasets and demonstrates a practical LLM-based curation pipeline.

## Dataset / Study Context

| Field | Value |
|---|---|
| Source dataset | Largest publicly available CodeReviewer-style dataset |
| Original size | 176,613 samples |
| Languages | Nine programming languages |
| Curated size | 170,718 after filtering relevance < 4 |
| LLM used | Llama-3.1-70B |
| Downstream model | DeepSeek-Coder-6.7B-Instruct with LoRA |

## Evaluation / Curation Framework

| Dimension | Values / Criteria |
|---|---|
| Type | Refactoring, Bugfix, Testing, Logging, Documentation, Other |
| Nature | Prescriptive, Descriptive, Clarification, Other |
| Civility | Civil, Uncivil |
| Quality scores | Relevance, Clarity, Conciseness on 1–10 scale |

## LLM-as-a-Judge Reliability

The authors manually checked 100 comments with two human annotators and compared the consensus with Llama-3.1-70B judgments. Reported Cohen’s kappa values include civility 1.0, type 0.88, nature 0.82, relevance 0.85, conciseness 0.76, and clarity 0.64.

## Key Findings

| Finding | Summary |
|---|---|
| F1 | Dataset is dominated by refactoring and bugfix comments, with many prescriptive comments. |
| F2 | Original dataset contains uncivil, lengthy, unclear, and irrelevant comments. |
| F3 | 5,895 irrelevant samples were removed using relevance < 4. |
| F4 | Curated comments improve clarity from 6.89 to 8.96. |
| F5 | Curated comments improve conciseness from 7.71 to 8.05. |
| F6 | Civility improves from 98.8% to 100%. |
| F7 | Prescriptive/actionable comments increase from 62.6% to 90.2%. |
| F8 | Comment generation BLEU improves from 7.71 to 11.26 when training on curated comments. |
| F9 | Code refinement improves from CodeBLEU 0.36 to 0.44 and EM 408 to 445. |

## Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Relevance | High | Used for filtering. |
| Clarity | High | Reformulation target. |
| Conciseness | High | Reformulation target. |
| Civility | High | Reformulation target. |
| Actionability | Medium / High | Prescriptive comments increase. |
| Usefulness | Medium | Measured indirectly through code refinement. |
| Correctness | Medium | Downstream code refinement is a proxy. |
| LLM-as-Judge validity | High | Human sanity check with kappa. |
| Useful preservation | Medium | Reformulation preserves core intent, but loss risk remains. |

## Problematic Comment Types

- Irrelevant comments.
- Unclear comments.
- Verbose/lengthy comments.
- Uncivil comments.
- Vague conversational comments.
- Non-informative comments such as “Same here” or “Need some edit here?”
- Ambiguous comments that humans may understand socially but models cannot learn from.

## Context / Data-Quality Evidence

P18 shows that the review comment itself is part of the evaluation context. Even if the code diff is correct, a noisy reference comment can corrupt both training and evaluation. This strengthens our argument that reference quality must be modeled explicitly.

## Trade-offs

| Strategy | Benefit | Risk / Cost |
|---|---|---|
| Filtering low-relevance comments | Removes unlearnable examples. | May remove comments that require missing social/project context. |
| Reformulating comments | Improves clarity/civility/conciseness. | May subtly change reviewer intent. |
| LLM-as-a-Judge | Scales to large datasets. | Requires calibration and can encode judge bias. |
| Prescriptive transformation | Increases actionability. | May over-normalize diverse review discourse. |

## Relevance to Our RQs

| Our RQ | Relevance |
|---|---|
| RQ1 | Adds noisy, unclear, uncivil, irrelevant, verbose, non-informative comment types. |
| RQ2 | Shows reference/comment quality is part of context quality. |
| RQ3 | Adds relevance/clarity/conciseness/civility/actionability dimensions. |
| RQ4 | Filtering/reformulation improves learning but may remove or alter useful comments. |
| RQ5 | Strong support for data-quality layer and LLM-as-judge calibration. |

## Limitations from Our Perspective

- LLM reformulation may change intent even if prompted not to.
- Downstream improvements are measured with BLEU/CodeBLEU/EM, not direct developer usefulness.
- LLM-as-a-Judge agreement is checked on only 100 samples.
- Relevance filtering can discard context-dependent comments that would be useful in the original workflow.

## Follow-up TODOs

- [ ] Verify MSR BibTeX.
- [ ] Add clarity/relevance/conciseness/civility to `synthesis/evaluation-dimensions.md`.
- [ ] Add noisy-comment categories to taxonomy.
- [ ] Add LLM-as-judge calibration and reformulation risks to trade-off framework.
