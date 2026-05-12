# P16 — Context-Aware Code Review Automation: A Retrieval-Augmented Approach

> [!NOTE]
> Compact v2 analysis. P16 is important for the context-quality and RAG trade-off parts of our synthesis because it studies retrieval-augmented code review automation, context collapse, expert routing, hallucination/severity errors, and LLM-as-a-judge calibration against human experts.

## Status

- Paper ID: `P16`
- Analysis status: `First pass completed from PDF; needs citation/BibTeX cleanup`
- Priority: `Medium / High`
- Reading depth: `Read once from PDF`
- Confidence: `High`

## Bibliographic Information

| Field | Value |
|---|---|
| Title | Context-Aware Code Review Automation: A Retrieval-Augmented Approach |
| Authors | Büşra İçöz, Göksel Biricik |
| Year | 2026 |
| Venue / Source | Applied Sciences |
| DOI | 10.3390/app16041875 |
| Type | Journal article; RAG/context-aware code review |

```bibtex
% TODO: Add checked MDPI BibTeX.
```

## One-Sentence Summary

> P16 proposes a retrieval-augmented code review system that uses project memory, semantic categories, and hybrid expert routing, showing that retrieved context improves strong/specialized models but can degrade weaker models through context collapse.

## Main Contribution

P16 operationalizes context-aware review through a dynamic RAG pipeline: project-specific review history is indexed, similar prior reviews are retrieved, review category/subcategory is inferred, and specialized models are routed by category.

## Dataset / Study Context

| Field | Value |
|---|---|
| Domain | Python 3.13 projects |
| Source | GitHub PRs from trending/top Python repositories |
| Temporal split | Reviews after 1 June 2024 used to reduce contamination risk |
| Test setting | Home Assistant Core |
| Project memory | 3,739 historical review pairs |
| Test set | 1,625 unseen contributions |
| Categories | Functional, Refactoring, Documentation, Discussion, False Positive, with 17 subcategories |

## Method

- Qdrant vector store.
- `all-MiniLM-L6-v2` embeddings with 384 dimensions.
- Top-k retrieval over historical reviews.
- Retrieval-informed categorization by nearest-neighbor majority vote.
- Prompt includes code diff, retrieved exemplars, inferred category/subcategory.
- Hybrid expert routing chooses the best-performing model by review category.
- Offline LinearSVC with TF-IDF is used for category support and self-training.

## Models / Systems

DeepSeek-Coder-33B, Qwen2.5-Coder-32B, Codestral-22B, CodeLlama-13B, Mistral-Instruct-7B, Phi-3-Mini; local inference through Ollama.

## Evaluation

| Dimension | Evidence |
|---|---|
| Automatic metrics | BLEU-4, ROUGE-L, semantic similarity |
| LLM-as-a-judge | Llama-3-70B, 0–10 rubric |
| Human evaluation | 3 senior backend engineers, 105 samples, at least 5 per 17 subcategories |
| Quality risks | Hallucination rate and severity overestimation |
| Statistical evidence | Hybrid routing significantly outperforms baselines |

## Key Findings

| Finding | Summary |
|---|---|
| F1 | Retrieval helps large/specialized models more than small models. |
| F2 | DeepSeek-Coder-33B improves from judge score 4.45 to 5.24 at k=3. |
| F3 | Phi-3 degrades with more retrieved context, showing context collapse. |
| F4 | Hybrid expert routing achieves mean score 7.03, outperforming zero-shot and single best model baselines. |
| F5 | LLM judge aligns reasonably with human experts, with strong reported correlation/agreement. |
| F6 | Hallucination and severity overestimation remain important failure modes. |
| F7 | Lexical metrics do not reliably reflect human/judge quality. |

## Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Relevance | High | Human and judge ratings include practical fit. |
| Context quality | Very high | Main contribution. |
| Retrieval quality | High | Top-k and category-informed routing. |
| Hallucination | Medium / High | Hallucination rate tracked. |
| Severity calibration | High | Severity overestimation measured. |
| Human alignment | High | Expert evaluation and judge calibration. |
| Cost/latency | Medium | Local model routing implies operational cost but not fully modeled. |
| Useful-comment preservation | Low | Not a filter-focused study. |

## Problematic Comment Types

- Hallucinated comment.
- Severity-overestimated comment.
- Context-collapsed comment caused by excessive retrieved context.
- Category-misaligned comment.
- Lexically plausible but low-quality comment.
- False-positive review comment.

## Context-Quality Evidence

P16 is one of the clearest papers showing that context quality is model-dependent. Retrieved exemplars improve strong models but can overwhelm smaller models. Therefore, the framework should include both retrieval relevance and recipient-model capacity.

## Trade-offs

| Strategy | Benefit | Risk / Cost |
|---|---|---|
| More retrieved context | Better grounding for capable models. | Context collapse in smaller models. |
| Hybrid expert routing | Higher quality by category. | Requires monitoring and routing logic. |
| LLM-as-a-judge | Scalable evaluation. | Needs human calibration; judge bias risk. |
| Category-aware prompts | More targeted review. | Error propagation from wrong category. |

## Relevance to Our RQs

| Our RQ | Relevance |
|---|---|
| RQ1 | Adds hallucination, severity overestimation, false positives, and context collapse. |
| RQ2 | Strong evidence for context-quality model and retrieval-quality model. |
| RQ3 | Adds judge score, human score, hallucination rate, severity overestimation. |
| RQ4 | Strong trade-off: retrieval depth vs attention/model capacity; routing vs complexity. |
| RQ5 | Supports trade-off-aware RAG evaluation. |

## Follow-up TODOs

- [ ] Verify MDPI BibTeX.
- [ ] Extract exact human/judge alignment values carefully because the paper reports multiple correlation figures.
- [ ] Update `synthesis/context-quality.md` with context collapse and model-capacity dependency.
- [ ] Update `synthesis/trade-off-framework.md` with retrieval depth and expert routing trade-offs.
