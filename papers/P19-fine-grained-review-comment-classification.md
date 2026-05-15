# P19 — Exploring the Potential of Large Language Models in Fine-Grained Review Comment Classification

> [!NOTE]
> Compact v2 analysis. P19 is useful for our taxonomy and evaluation-framework work because it studies LLM-based classification of review comments into 17 fine-grained categories linked to practitioner usefulness. Metadata has been aligned with the spreadsheet: the official SCAM 2025 / IEEE DOI is retained, and arXiv remains the preprint/PDF source.

## Status

- Paper ID: `P19`
- Analysis status: `First pass completed from PDF; metadata aligned with spreadsheet; needs BibTeX cleanup`
- Priority: `Low / Medium for core synthesis; useful for taxonomy`
- Reading depth: `Read once from PDF`
- Last updated: `2026-05-15`
- Confidence in extraction: `Medium / High`

## Bibliographic Information

| Field | Value |
|---|---|
| Title | Exploring the Potential of Large Language Models in Fine-Grained Review Comment Classification |
| Authors | Linh Nguyen, Chunhua Liu, Hong Yi Lin, Patanamon Thongtanunam |
| Year | 2025 |
| Venue / Source | SCAM 2025 / IEEE |
| Publication type | Peer-reviewed conference paper |
| Link | https://ieeexplore.ieee.org/abstract/document/11190200 |
| DOI / arXiv | DOI: 10.1109/SCAM67354.2025.00012; arXiv:2508.09832 |
| Artifact | Zenodo replication package reported in paper |

```bibtex
% TODO: Add checked IEEE BibTeX.
```

## One-Sentence Summary

> This paper evaluates whether LLMs can classify code review comments into 17 fine-grained categories linked to perceived usefulness, showing that LLMs can support taxonomy-aware analysis of review comments.

## Main Goal of the Paper

The paper aims to classify code review comments into a 17-category taxonomy, moving beyond coarse useful/non-useful or five-group classifications to support code review analytics and prioritization.

## Focus Area

- [x] Review comment taxonomy
- [x] Fine-grained classification
- [x] Usefulness-linked categories
- [x] Context quality / code context
- [x] Prompting strategy
- [x] Class imbalance
- [ ] Review comment generation
- [ ] Production deployment

## Research Questions of the Paper

| RQ | Summary |
|---|---|
| RQ1 | Can LLMs classify review comments into 17 fine-grained categories? |
| RQ2 | Do LLMs outperform the state-of-the-art supervised approach? |
| RQ3 | Which categories can LLMs classify accurately? |

## Dataset / Study Context

| Field | Value |
|---|---|
| Dataset source | Turzo and Bosu / OpenStack Nova review-comment dataset |
| Initial labeled data | 2,500 annotated code review comments |
| Used data | 1,828 comments with associated code changes |
| Annotation source | Industry experts; original reported Cohen’s kappa 0.68 |
| Taxonomy | 17 categories mapped to practitioner usefulness ratings |
| Context variants | Comment-only; code + comment |

## Evaluation Method

| Metric | Notes |
|---|---|
| F1, precision, recall, accuracy | Per-category and weighted average across imbalanced classes. |
| Cross-validation | Used for comparison with supervised baseline. |
| Statistical test | One-sided Wilcoxon signed-rank test. |
| Runtime | Runtime varies by model size; large models are substantially slower. |

## Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Comment type | Very high | Main contribution. |
| Usefulness | High | Categories are linked to practitioner usefulness ratings. |
| Class imbalance | High | Rare useful categories are central. |
| Code context | Medium / High | Comment-only vs code+comment. |
| Taxonomy validity | Medium | Depends on prior taxonomy and labels. |
| Actionability | Medium | Useful categories tend to be more actionable, but actionability is indirect. |
| Production impact | Low | Suggested uses, not deployed. |

## Problematic Comment Types / Taxonomy Evidence

P19 is not a harmful-comment paper, but its categories help separate high-value from lower-value feedback:

- High-value / useful categories include functional defect, validation, logical, interface, and solution approach.
- Lower-value categories include visual representation, praise, and some documentation/style categories.
- It includes a false-positive category.
- Trivial or low-priority comments can be deprioritized by category.
- Interface/support/resource comments may be context-dependent and hard to classify.

## Context-Quality Extraction

| Context Dimension | Evidence |
|---|---|
| Code context | Helps models in many settings. |
| Comment-only signal | Sometimes enough, and cheaper than including code context. |
| Category definitions | Refined definitions can help but may overload smaller models. |
| Task decomposition | Hierarchical strategy can help smaller models but may propagate errors. |
| Repository context | Missing repository/API context explains hard categories such as support/interface/resource. |

## Trade-off Extraction

| Strategy | Benefit | Risk / Cost |
|---|---|---|
| Flat classification | Holistic view over all 17 categories. | Longer option space; harder for smaller models. |
| Hierarchical classification | Easier subtask for small/medium models. | High-level error propagates to category. |
| Code+comment context | Improves many larger models. | Increases context length and complexity. |
| Comment-only context | Cheaper and sometimes competitive. | May miss code-dependent categories. |
| LLM classification | Reduces manual labeling/training burden. | Runtime/cost and prompt sensitivity. |

## Relevance to Our Paper

| Our RQ | Relevance |
|---|---|
| RQ1 — problematic comments | `Medium / High` because category-level usefulness helps distinguish low-value and high-value feedback. |
| RQ2 — context quality | `Medium` because code context helps but can also increase difficulty. |
| RQ3 — evaluation dimensions | `High` for comment type, usefulness category, classification validity. |
| RQ4 — trade-offs | `Medium / High` for flat vs hierarchical, code context vs cost, large vs small model. |
| RQ5 — framework design | `High` for taxonomy and prioritization layer. |

## Limitations

- Uses one dataset from OpenStack Nova, so generalizability is limited.
- Original annotation agreement is moderate, indicating ambiguity.
- LLM outputs can be format-sensitive.
- No live deployment or developer-facing evaluation.
- Classification helps prioritization, but does not itself validate correctness of generated comments.

## Follow-up TODOs

- [ ] Add checked IEEE BibTeX.
- [ ] Add 17-category taxonomy to `synthesis/problematic-comment-taxonomy.md` as a usefulness-linked taxonomy layer.
- [ ] Add flat-vs-hierarchical classification to `synthesis/trade-off-framework.md`.
- [ ] Add comment-type/usefulness-category to `synthesis/evaluation-dimensions.md`.
