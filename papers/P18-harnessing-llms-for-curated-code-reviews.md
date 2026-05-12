# P18 — Harnessing Large Language Models for Curated Code Reviews

> [!NOTE]
> Compact v2 analysis. P18 is central for the data-quality and LLM-as-a-judge parts of our work because it proposes a comment-quality evaluation framework, uses Llama-3.1-70B to judge and reformulate review comments, validates judgments with humans, and shows curated comments improve comment generation and code refinement.

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
| Artifacts | CuREV GitHub replication package; Zenodo data/models/results |

```bibtex
% TODO: Add checked IEEE/arXiv BibTeX.
```

## One-Sentence Summary

> P18 proposes CuRev, an LLM-curated code review dataset that filters irrelevant comments and reformulates comments for clarity, conciseness, and civility, improving downstream comment generation and code refinement performance.

## Main Contribution

P18 treats code-review dataset quality as a first-class evaluation object. It defines a framework with comment type, nature, civility, relevance, clarity, and conciseness, then uses LLM-as-a-judge and LLM-based reformulation to improve dataset quality.

## Dataset / Study Context

| Field | Value |
|---|---|
| Base dataset | CodeReviewer dataset |
| Original size | 176,613 samples |
| Languages | PHP, Ruby, C#, C, Java, Python, C++, Go, JavaScript |
| Curated dataset size | 170,718 after filtering irrelevant comments |
| Judge/reformulator | Llama-3.1-70B |
| Downstream model | DeepSeek-Coder-6.7B-Instruct |
| Fine-tuning method | LoRA |

## Evaluation Framework

| Aspect | Categories / Criteria |
|---|---|
| Type | Refactoring, Bugfix, Testing, Logging, Documentation, Other |
| Nature | Prescriptive, Descriptive, Clarification, Other |
| Civility | Civil, Uncivil |
| Scores | Relevance, Clarity, Conciseness on 1–10 scale |

## LLM-as-a-Judge Validation

100 randomly selected review comments were manually evaluated by two authors and compared to Llama-3.1-70B judgments.

| Dimension | Cohen’s kappa |
|---|---|
| Civility | 1.00 |
| Type | 0.88 |
| Nature | 0.82 |
| Relevance | 0.85 |
| Conciseness | 0.76 |
| Clarity | 0.64 |

## Key Findings

| Finding | Summary |
|---|---|
| F1 | Original dataset is dominated by refactoring and bugfix comments. |
| F2 | 98.77% of comments are civil, but uncivil comments still exist and can teach undesirable patterns. |
| F3 | 5,895 comments with relevance score below 4 were filtered out. |
| F4 | Curated comments improve clarity from 6.89 to 8.96. |
| F5 | Curated comments improve conciseness from 7.71 to 8.05. |
| F6 | Prescriptive comments increase from 62.6% to 90.2%. |
| F7 | Civil comments become 100% after curation. |
| F8 | Comment generation BLEU improves from 7.71 to 11.26 when trained on curated comments. |
| F9 | Code refinement improves from CodeBLEU 0.36 to 0.44 and EM 408 to 445 with curated comments. |

## Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Relevance | High | Used for filtering. |
| Clarity | High | Main reformulation target. |
| Conciseness | High | Main reformulation target. |
| Civility | High | Main reformulation target. |
| Actionability | Medium / High | Prescriptive comments become dominant. |
| Data quality | Very high | Main contribution. |
| LLM-as-a-judge reliability | High | Human sanity check. |
| Downstream usefulness | High | Tested on generation and refinement. |
| Correctness | Medium | Indirect through downstream metrics. |

## Problematic Comment Types

- Irrelevant comments.
- Unclear comments.
- Verbose/lengthy comments.
- Uncivil comments.
- Descriptive but non-prescriptive comments.
- Vague low-information comments such as “Need some edit here?”
- Harsh/uncivil comments that may teach undesirable style.
- Comments whose form obscures useful intent.

## Context-Quality Evidence

P18 focuses less on code context and more on comment quality as input context for later tasks. It shows that a comment can contain useful intent but still be hard for models to learn from if it is unclear, verbose, or uncivil.

## Trade-offs

| Strategy | Benefit | Risk / Cost |
|---|---|---|
| Filtering low-relevance comments | Removes unhelpful training samples. | May remove context-dependent comments that humans understand. |
| Reformulating comments | Improves clarity/civility/conciseness. | May change nuance or over-prescribe. |
| LLM-as-a-judge | Scales dataset assessment. | Depends on judge reliability and prompt design. |
| LLM curation | Improves downstream metrics. | Could homogenize review style and reduce natural diversity. |

## Relevance to Our RQs

| Our RQ | Relevance |
|---|---|
| RQ1 | Strong evidence for problematic dataset/comment types. |
| RQ2 | Comment quality as context quality for generation/refinement. |
| RQ3 | Adds relevance, clarity, conciseness, civility, type, nature. |
| RQ4 | Filtering/reformulation trade-off and useful-intent preservation. |
| RQ5 | Strong support for data-quality layer and LLM-as-judge validation. |

## Follow-up TODOs

- [ ] Verify IEEE BibTeX.
- [ ] Add CuRev dimensions to `synthesis/evaluation-dimensions.md`.
- [ ] Add curation/reformulation trade-offs to `synthesis/trade-off-framework.md`.
- [ ] Add LLM-as-a-judge sanity-check example to methodology discussion.
