# P25 — Fine-Tuning Large Language Models to Improve Accuracy and Comprehensibility of Automated Code Review

> [!NOTE]
> Compact v2 analysis. P25 is central for our comprehensibility/evaluation framework because it defines comprehensible ACR as issue detection, localization, explanation, and repair suggestion, and fine-tunes LLMs on chain-of-thought style curated review data.

## Status

- Paper ID: `P25`
- Analysis status: `First pass completed from PDF; needs citation/BibTeX cleanup`
- Priority: `High`
- Reading depth: `Read once from PDF`
- Confidence: `High`

## Bibliographic Information

| Field | Value |
|---|---|
| Title | Fine-Tuning Large Language Models to Improve Accuracy and Comprehensibility of Automated Code Review |
| Authors | Yongda Yu, Guoping Rong, Haifeng Shen, He Zhang, Dong Shao, Min Wang, Zhao Wei, Yong Xu, Juhong Wang |
| Year | 2024 |
| Venue / Source | ACM TOSEM |
| DOI | 10.1145/3695993 |
| Artifact | GitHub: `aiopsplus/Carllm` |

```bibtex
% TODO: Add checked ACM BibTeX.
```

## One-Sentence Summary

> P25 proposes Carllm, a fine-tuned LLM for automated code review that uses curated chain-of-thought review data to improve both code issue detection and the comprehensibility of generated comments.

## Main Contribution

The paper argues that automated code review must optimize both **accuracy** and **comprehensibility**. It defines comprehensibility as a logical chain of four elements:

1. detecting whether an issue exists,
2. localizing the issue,
3. explaining the cause,
4. suggesting a concrete repair solution.

## Dataset / Study Context

| Field | Value |
|---|---|
| Projects | 1,793 GitHub projects |
| Inclusion | >1,000 stars, >1,000 PRs, MIT/Apache 2.0, popular languages |
| Languages | Go, Python, Java, C/C++, JavaScript |
| Annotated candidate data | 15,000 randomly selected review data pieces |
| Optimized high-quality data | 9,728 data pieces after filtering |
| Final training instances | 19,456 including 1:1 negative examples |
| Test set | 1,000 positive and 1,000 negative instances for issue detection |

## Method

| Component | Details |
|---|---|
| Data curation | ChatGPT restructures raw review discussions into CoT template. |
| Error filtering | Removes out-of-token, JSON-load, not-inline, and no-issue errors. |
| Manual quality check | 400 samples; >99.5% restructured, 87.25% enriched with context, 83.5% correct comments. |
| Fine-tuning | LoRA on LLaMA, LLaMA2, CodeLLaMA, Magicoder variants. |
| Balanced loss | Gives explicit weight to issue detection decision. |
| Decoding | Greedy decoding preferred for deterministic issue detection. |

## Evaluation Method

| RQ | Method |
|---|---|
| RQ1 | Issue detection using recall, precision, F1, accuracy over 1,000 positive/1,000 negative samples. |
| RQ2 | Manual comprehensibility assessment over 1,000 review comments using clear/neutral/unclear. |

## Key Findings

| Finding | Summary |
|---|---|
| F1 | CodeCarllm 13B achieves the best F1-Score: 0.7316. |
| F2 | Carllm 13B achieves highest recall: 0.8500. |
| F3 | MagicCarllm 7B achieves highest precision: 0.7500. |
| F4 | Carllm variants outperform CodeReviewer, CodeT5, LLaMA-Reviewer, base LLMs, ChatGPT, and GPT-4 on issue detection. |
| F5 | Balanced loss improves F1 and accuracy over original loss across Carllm variants. |
| F6 | Carllm comments have higher degree of clarity and fewer unclear comments than baselines. |
| F7 | Baselines often generate short comments without issue location, explanation, or solution. |
| F8 | High-temperature sampling degrades issue detection stability; greedy/beam search are more stable. |

## Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Issue detection | Very high | Core RQ1. |
| Localization | High | Part of comprehensibility template. |
| Explanation | High | Explicit component of review comment. |
| Repair suggestion | High | Explicit component of review comment. |
| Comprehensibility / clarity | Very high | Manual clear/neutral/unclear evaluation. |
| Determinism / stability | High | Decoding strategy evaluated. |
| Data quality | High | Curated CoT dataset and filtering. |
| Human evaluation | Medium | Manual clarity assessment and consistency check. |
| Workflow impact | Low | No production deployment. |

## Problematic Comment / Review Types

- Issue-free bias in general LLMs.
- Comment that only describes diff changes.
- Comment with wrong issue judgment.
- Comment with missing issue location.
- Comment with explanation but no solution.
- Comment with solution but no issue explanation.
- Unclear comment.
- Not-inline generated location.
- No-issue error for an actual issue.
- Test-request comments or re-submit-PR comments that do not directly explain a code issue.

## Context-Quality Evidence

P25 strongly supports treating context as a structured reasoning chain. The useful context is not only the diff, but also the issue decision, issue position, explanation, and suggested repair. It also shows that raw review comments are too sparse to support this structure, motivating data curation.

## Trade-off Extraction

| Strategy | Benefit | Risk / Cost |
|---|---|---|
| CoT review template | Improves logical structure and comprehensibility. | May force comments into a rigid schema. |
| ChatGPT data annotation | Scales construction of logic-rich data. | Can introduce wrong explanations or filtered artifacts. |
| Balanced loss | Improves issue detection. | Weight tuning may affect generation quality. |
| Greedy decoding | Stable and deterministic for issue detection. | May reduce diversity. |
| Manual clarity evaluation | Captures human comprehensibility better than BLEU. | Still subjective and sample-limited. |

## Relevance to Our Paper

P25 should be one of our main sources for the evaluation framework. It provides a concrete decomposition of review-comment comprehensibility and directly supports evaluating detection, localization, explanation, and repair suggestion separately.

## Limitations from Our Perspective

- Uses ChatGPT-generated annotations, so training data may contain model artifacts.
- Manual comprehensibility evaluation has only ternary labels.
- No live workflow/adoption evaluation.
- Issue categories and severity are not deeply separated.
- The method is heavily dependent on curated CoT data quality.

## Follow-up TODOs

- [ ] Add comprehensibility decomposition to `synthesis/evaluation-dimensions.md`.
- [ ] Add issue detection/localization/explanation/repair suggestion to framework.
- [ ] Add unclear/missing-location/wrong-judgment comment types to taxonomy.
- [ ] Add decoding stability to trade-off framework.
- [ ] Update `matrices/cross-paper-synthesis.md` with P25 evidence.
