# P29 — Can LLMs Replace Human Evaluators? An Empirical Study of LLM-as-a-Judge in Software Engineering

> [!NOTE]
> Compact v2 analysis. P29 is central for our evaluator-validity section because it empirically shows that LLM-as-a-judge performance in software engineering is highly task-dependent and that pairwise evaluation is unstable under response-order swaps.

## Status

- Paper ID: `P29`
- Analysis status: `First pass completed from PDF; needs citation/BibTeX cleanup`
- Priority: `High`
- Reading depth: `Read once from PDF`
- Confidence: `High`

## Bibliographic Information

| Field | Value |
|---|---|
| Title | Can LLMs Replace Human Evaluators? An Empirical Study of LLM-as-a-Judge in Software Engineering |
| Authors | Ruiqi Wang, Jiyu Guo, Cuiyun Gao, Guodong Fan, Chun Yong Chong, Xin Xia |
| Year | 2025 |
| Venue / Source | Proc. ACM Softw. Eng. / ISSTA 2025 |
| DOI | 10.1145/3728963 |
| Artifact | GitHub: `BackOnTruck/llm-judge-empirical` |

```bibtex
% TODO: Add checked ACM BibTeX.
```

## One-Sentence Summary

> P29 evaluates LLM-as-a-judge methods on code translation, code generation, and code summarization, finding that output-based large LLM judges can align with humans on some SE tasks but fail to generalize and perform poorly or inconsistently on others.

## Main Contribution

The paper conducts a meta-evaluation of LLM-as-a-judge methods for software engineering tasks by comparing judge scores with human scores. It categorizes judge methods into embedding-based, probability-based, and output-based approaches and tests individual scoring plus pairwise comparison.

## Dataset / Study Context

| Field | Value |
|---|---|
| Tasks | Code translation, code generation, code summarization |
| Source datasets | CodeTransOcean, ComplexCodeEval, CodeXGLUE |
| Human-scored samples | 450 instruction-response-score triplets |
| Response pairs | 900 pairs |
| Response generators | 12 code LLMs from 7 families |
| Human evaluators | Two evaluators; high inter-rater agreement reported |

## Method Categories

| Category | Examples | Key Characteristic |
|---|---|---|
| Conventional metrics | BLEU, ROUGE-L, METEOR, ChrF++, CrystalBLEU | Reference-based lexical/similarity metrics. |
| Embedding-based | BERTScore, MoverScore with UniXcoder | Reference-based semantic similarity. |
| Probability-based | GPTScore, FFLM | Uses generation probabilities/log probabilities. |
| Output-based | Vanilla, G-Eval, BatchEval | LLM outputs score or preference directly. |
| SFT judge models | Auto-J, Prometheus, base models | Fine-tuned for evaluation, mostly NLP-oriented. |

## Key Findings

| Finding | Summary |
|---|---|
| F1 | LLM-as-a-judge human alignment is highly task-dependent. |
| F2 | Output-based large LLMs perform best overall. |
| F3 | On code translation, BatchEval reaches near-human alignment: Pearson R = 81.32. |
| F4 | On code generation, DeepSeek-V2.5 reaches Pearson R = 68.51, comparable to conventional metrics. |
| F5 | On code summarization, LLM-as-a-judge methods are outperformed by conventional metrics and can show negative correlation. |
| F6 | Inference strategies such as G-Eval and BatchEval provide only marginal improvements in individual scoring but increase cost. |
| F7 | Pairwise comparison performs poorly and is inconsistent under answer-order swaps. |
| F8 | LLM judges show verbosity bias in code summarization, mistaking detailed explanation for good summary. |
| F9 | Embedding-based methods correlate strongly with conventional metrics, suggesting they are still mostly similarity metrics. |

## Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Human alignment | Very high | Correlation with human scores. |
| Task dependence | Very high | Three SE task types. |
| Judge-method comparison | High | Embedding/probability/output/SFT methods. |
| Pairwise order sensitivity | High | Pairwise comparisons tested with swapped positions. |
| Score distribution | High | Compares judge distributions to human distributions. |
| Verbosity bias | Medium / High | Case study shows summarization failure. |
| Cost | Medium | Inference strategies increase token/inference cost. |

## Problematic Judge / Evaluation Types

- Task-misaligned judge.
- Verbosity-biased judge.
- Pairwise judge with position/order bias.
- Judge that interprets “summary” as detailed explanation.
- Small/fine-tuned NLP judge transferred poorly to SE tasks.
- Embedding/probability judge that behaves like conventional similarity metric.
- Output-based judge with high cost but marginal gain.
- Reference-free judge that lacks task-specific understanding.

## Context-Quality Evidence

P29 shows that evaluator context and task definition matter. A judge can align with humans in code translation but fail in code summarization because it misunderstands the expected output style. Therefore, LLM-as-a-judge prompts must encode task-specific criteria rather than assume generic “quality.”

## Trade-off Extraction

| Strategy | Benefit | Risk / Cost |
|---|---|---|
| Output-based large LLM judge | Best human alignment in several tasks. | Expensive; task-dependent; can be biased. |
| Inference strategies | Slightly improve alignment in some cases. | Higher cost; not consistently worth it. |
| Pairwise comparison | Intuitive and common for preference tasks. | Poor accuracy and severe order inconsistency. |
| Conventional metrics | Sometimes surprisingly competitive. | Lexical/reference-bound and incomplete. |
| SFT judge models | Cheaper/open alternatives. | Poor transfer if trained on non-SE evaluation data. |

## Relevance to Our Paper

P29 gives strong support for treating LLM-as-a-judge as an imperfect evaluator, not ground truth. In our framework, any judge-based evaluation should include calibration, task-specific rubrics, order-bias checks, and possibly human spot checks.

## Limitations from Our Perspective

- Does not evaluate code review comment generation directly.
- Human-scored dataset is relatively small: 450 responses.
- Uses three SE tasks, but not PR-level review, security review, or human workflow outcomes.
- Pairwise tie threshold is derived from human-score differences, which may not map to all tasks.

## Follow-up TODOs

- [ ] Add task-dependence and order sensitivity to evaluator-validity section.
- [ ] Add verbosity bias to judge-failure taxonomy.
- [ ] Add human-calibration requirement for LLM-as-a-judge.
- [ ] Update `matrices/cross-paper-synthesis.md` with P29 evidence.
