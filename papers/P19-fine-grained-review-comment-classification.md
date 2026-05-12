# P19 — Exploring the Potential of Large Language Models in Fine-Grained Review Comment Classification

> [!NOTE]
> Compact v2 analysis. P19 is useful for our taxonomy and evaluation-framework work because it studies LLM-based classification of review comments into 17 fine-grained categories linked to practitioner usefulness, exposing how comment type, usefulness, context, and class imbalance interact.

## Completion Checklist

- [x] Bibliographic fields are filled.
- [x] Dataset/study details are filled from the PDF.
- [x] Evaluation methods and metrics are described.
- [x] Evaluation dimensions are separated from problematic comment types.
- [x] Context-quality evidence is extracted.
- [x] Trade-offs are explicitly identified.
- [x] Mapping to our RQs is included.

## Status

- Paper ID: `P19`
- Analysis status: `First pass completed from PDF; needs citation/BibTeX cleanup and venue verification`
- Priority: `Low / Medium for core synthesis; useful for taxonomy`
- Reading depth: `Read once from PDF`
- Last updated: `2026-05-13`
- Confidence in extraction: `Medium / High`

## 1. Bibliographic Information

| Field | Value |
|---|---|
| Title | Exploring the Potential of Large Language Models in Fine-Grained Review Comment Classification |
| Authors | Linh Nguyen, Chunhua Liu, Hong Yi Lin, Patanamon Thongtanunam |
| Year | 2025 |
| Venue / Source | arXiv / preprint candidate |
| Publication type | Empirical classification study |
| DOI / arXiv | arXiv:2508.09832; DOI not verified in this pass |
| Artifact | Zenodo replication package reported in paper |

```bibtex
% TODO: Verify venue/DOI and add BibTeX.
```

## 2. One-Sentence Summary

> This paper evaluates whether LLMs can classify code review comments into 17 fine-grained categories linked to perceived usefulness, showing that large LLMs can outperform supervised CodeBERT+LSTM overall and can better identify rare but useful categories.

## 3. Main Goal of the Paper

The paper aims to classify code review comments into a 17-category taxonomy, moving beyond coarse useful/non-useful or five-group classifications to support code review analytics and prioritization.

### Focus Area

- [x] Review comment taxonomy
- [x] Fine-grained classification
- [x] Usefulness-linked categories
- [x] Context quality / code context
- [x] Prompting strategy
- [x] Class imbalance
- [ ] Review comment generation
- [ ] Production deployment

## 4. Research Questions of the Paper

| RQ | Summary |
|---|---|
| RQ1 | Can LLMs classify review comments into 17 fine-grained categories? |
| RQ2 | Do LLMs outperform the state-of-the-art supervised approach? |
| RQ3 | Which categories can LLMs classify accurately? |

## 5. Dataset / Study Context

| Field | Value |
|---|---|
| Dataset source | Turzo and Bosu / OpenStack Nova review-comment dataset |
| Initial labeled data | 2,500 annotated code review comments |
| Used data | 1,828 comments with associated code changes |
| Annotation source | Industry experts; original reported Cohen’s kappa 0.68 |
| Taxonomy | 17 categories mapped to practitioner usefulness ratings |
| Context variants | Comment-only; code + comment |

### 17 Categories

The taxonomy includes categories such as functional defect, validation, logical, resource, timing, support, interface, solution approach, code organization, alternate output, naming convention, visual representation, documentation, question, design discussion, praise, and false positive.

## 6. Methods / Models Studied

| Component | Notes |
|---|---|
| LLMs | Qwen 2-7B, Qwen 2-72B, Llama 3-8B, Llama 3-70B, Llama 3.1-405B |
| Strategies | Flat 17-way classification; hierarchical group-then-category classification |
| Context | Comment-only and code+comment prompts |
| Baseline | CodeBERT+LSTM adapted from prior work |
| Prompt format | Multiple choice with category definitions and `$` stopping marker |

## 7. Evaluation Method

| Metric | Notes |
|---|---|
| F1, precision, recall, accuracy | Per-category and weighted average across imbalanced classes |
| Cross-validation | Used for comparison with CodeBERT+LSTM |
| Statistical test | One-sided Wilcoxon signed-rank test |
| Runtime | Llama 405B ≈ 9h; 70B/72B ≈ 5h; 7B/8B ≈ 1h; CodeBERT+LSTM ≈ 5h |

## 8. Key Findings

| Finding | Summary |
|---|---|
| F1 | Llama 3.1-405B with flat code+comment prompt achieves best weighted F1: 46.2. |
| F2 | Llama 3.1-405B flat improves over CodeBERT+LSTM by about 10%–11.3% F1. |
| F3 | Small and medium models benefit from hierarchical classification. |
| F4 | Large model performs better with flat strategy and code context. |
| F5 | LLMs outperform baseline on the five most useful categories: functional defect, validation, logical, interface, and solution approach. |
| F6 | LLMs handle low-frequency categories better than supervised models. |
| F7 | Category definitions and context length affect smaller models more strongly. |
| F8 | Support, Resource, and Interface remain challenging because they often require repository/API context. |

## 9. Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Comment type | Very high | Main contribution. |
| Usefulness | High | Categories are linked to practitioner usefulness ratings. |
| Class imbalance | High | Rare useful categories are central. |
| Code context | Medium / High | Comment-only vs code+comment. |
| Taxonomy validity | Medium | Depends on prior taxonomy and labels. |
| Actionability | Medium | Useful categories tend to be more actionable, but actionability is indirect. |
| Production impact | Low | Suggested uses, not deployed. |

## 10. Problematic Comment Types / Taxonomy Evidence

P19 is not a harmful-comment paper, but its categories help separate high-value from lower-value feedback:

- High-value / useful categories: functional defect, validation, logical, interface, solution approach.
- Lower-value categories: visual representation, praise, some documentation/style categories.
- Explicit false-positive category.
- Trivial or low-priority comments can be deprioritized by category.
- Interface/support/resource comments may be context-dependent and hard to classify.

## 11. Context-Quality Extraction

| Context Dimension | Evidence |
|---|---|
| Code context | Helps larger models in many settings. |
| Comment-only signal | Sometimes enough for large models; avoids added context complexity. |
| Category definitions | Refined definitions help some models but can overload others. |
| Task decomposition | Hierarchical strategy helps smaller models but can propagate errors. |
| Repository context | Missing repository/API context explains hard categories such as support/interface/resource. |

## 12. Trade-off Extraction

| Strategy | Benefit | Risk / Cost |
|---|---|---|
| Flat classification | Holistic view over all 17 categories. | Longer option space; harder for smaller models. |
| Hierarchical classification | Easier subtask for small/medium models. | High-level error propagates to category. |
| Code+comment context | Improves many larger models. | Increases context length and complexity. |
| Comment-only context | Cheaper and sometimes competitive. | May miss code-dependent categories. |
| LLM classification | Reduces manual labeling/training burden. | Runtime/cost and prompt sensitivity. |

## 13. Relevance to Our Paper

| Our RQ | Relevance |
|---|---|
| RQ1 — problematic comments | `Medium / High` because category-level usefulness helps distinguish low-value and high-value feedback. |
| RQ2 — context quality | `Medium` because code context helps but can also increase difficulty. |
| RQ3 — evaluation dimensions | `High` for comment type, usefulness category, classification validity. |
| RQ4 — trade-offs | `Medium / High` for flat vs hierarchical, code context vs cost, large vs small model. |
| RQ5 — framework design | `High` for taxonomy and prioritization layer. |

## 14. Limitations

- Uses one dataset from OpenStack Nova, so generalizability is limited.
- Original annotation agreement is moderate (kappa 0.68), indicating ambiguity.
- LLM outputs can be format-sensitive.
- No live deployment or developer-facing evaluation.
- Classification is useful for prioritization, but does not itself validate correctness of generated comments.

## 15. Follow-up TODOs

- [ ] Verify DOI/venue status.
- [ ] Add 17-category taxonomy to `synthesis/problematic-comment-taxonomy.md` as a usefulness-linked taxonomy layer.
- [ ] Add flat-vs-hierarchical classification to `synthesis/trade-off-framework.md`.
- [ ] Add comment-type/usefulness-category to `synthesis/evaluation-dimensions.md`.
