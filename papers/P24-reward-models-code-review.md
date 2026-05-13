# P24 — Leveraging Reward Models for Guiding Code Review Comment Generation

> [!NOTE]
> Compact v2 analysis. P24 is important for our trade-off framework because it treats review-comment generation as a reinforcement-learning problem and defines rewards based on semantic similarity and downstream code-refinement usefulness.

## Status

- Paper ID: `P24`
- Analysis status: `First pass completed from PDF; needs citation/BibTeX cleanup`
- Priority: `Medium / High`
- Reading depth: `Read once from PDF`
- Confidence: `High`

## Bibliographic Information

| Field | Value |
|---|---|
| Title | Leveraging Reward Models for Guiding Code Review Comment Generation |
| Authors | Oussama Ben Sghaier, Rosalia Tufano, Gabriele Bavota, Houari Sahraoui |
| Year | 2025 |
| Venue / Source | arXiv / manuscript |
| DOI / arXiv | arXiv:2506.04464 |
| Artifact | GitHub: `OussamaSghaier/RL4CR` |

```bibtex
% TODO: Add checked arXiv BibTeX.
```

## One-Sentence Summary

> P24 proposes CoRAL, a reinforcement-learning framework for review comment generation that rewards generated comments for semantic similarity to human comments and for their usefulness in downstream code refinement.

## Main Contribution

The paper moves beyond supervised learning with lexical targets by using reward models for code review comment generation. It evaluates whether comments are meaningful not only because they resemble references, but also because they help a code-refinement model produce the expected code edit.

## Dataset / Study Context

| Field | Value |
|---|---|
| Dataset | 176,616 code review rounds from prior code review automation dataset |
| Data format | `(code submitted for review, review comment, refined code)` |
| Split | 85% train, 7.5% validation, 7.5% test |
| Base model | CodeLlama-7B |
| Hardware | Four NVIDIA RTX A5000 GPUs for SFT; three GPUs for RL plus one reward-model GPU |
| Replication | Public replication package |

## Method

| Component | Details |
|---|---|
| SFT baseline | CodeLlama-7B fine-tuned for review comment generation. |
| Reward strategy 1 | Semantic similarity using SBERT cosine similarity between generated and human comments. |
| Reward strategy 2 | Downstream code-refinement usefulness using a refinement model and either loss or CrystalBLEU. |
| RL algorithm | PPO via HuggingFace TRL. |
| Stability control | KL penalty against the base model distribution. |
| Best variant | CoRAL_crystal, using CrystalBLEU of downstream refinement as reward. |

## Evaluation Method

| RQ | Method |
|---|---|
| RQ1 | Compare SFT and RL variants using BLEU. |
| RQ2 | Compare reward strategies: semantic, loss, CrystalBLEU. |
| RQ3 | Compare best CoRAL against DISCOREV with CodeLlama-7B. |
| RQ4 | o3-mini pairwise usefulness judgment against baselines; human sanity check on 100 pairs. |

## Key Findings

| Finding | Summary |
|---|---|
| F1 | RL improves comment generation over SFT for all reward strategies. |
| F2 | CoRAL_crystal achieves median BLEU 8.67 vs 7.05 for CodeLlama_sft. |
| F3 | CoRAL_crystal significantly outperforms semantic and loss rewards. |
| F4 | CoRAL_crystal significantly outperforms DISCOREV retrained on CodeLlama-7B. |
| F5 | Semantic reward improves average reward from 0.18 to 0.29. |
| F6 | CrystalBLEU downstream reward improves from 0.77 to 0.84. |
| F7 | o3-mini agrees with human usefulness judgments in 76% of 100 samples; Cohen’s kappa = 0.62. |
| F8 | o3-mini prefers CoRAL over CodeLlama_sft in 70% of comparisons and over DISCOREV in 55%. |

## Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Semantic equivalence | High | SBERT reward and BLEU evaluation. |
| Downstream usefulness | High | Code refinement reward is central. |
| Usefulness | Medium / High | o3-mini pairwise judgment with human sanity check. |
| Actionability | Medium | Downstream refinement reward approximates actionability. |
| LLM-as-judge calibration | Medium | kappa 0.62 on 100 pairs. |
| Correctness | Medium | Indirectly through refinement. |
| Human evaluation | Low / Medium | Sanity check only. |
| Workflow impact | Low | No live deployment. |

## Problematic Comment / Review Types

- Non-actionable comment.
- Semantically valid but lexically different comment penalized by exact-match learning.
- Comment that identifies a problem but does not guide refinement.
- Comment that is useful to humans but not to a downstream model.
- Reward-overoptimized comment that scores well but may be unnatural.
- Generic comment that lacks concrete repair guidance.

## Context / Quality Evidence

P24 frames useful review comments as comments that support a downstream code-refinement task. This is useful for our framework because it links comment quality to downstream action rather than only to textual similarity or human preference.

## Trade-off Extraction

| Strategy | Benefit | Risk / Cost |
|---|---|---|
| Semantic reward | Encourages meaning-preserving paraphrases. | May still reward comments that do not lead to fixes. |
| Downstream refinement reward | Optimizes for practical actionability. | Depends on the refinement model and code-similarity metric. |
| CrystalBLEU reward | Best observed reward strategy. | Code-similarity metric may not equal semantic correctness. |
| RL/PPO | Can optimize non-differentiable/usefulness objectives. | Expensive and sensitive to reward design. |
| LLM-as-judge usefulness | Scales qualitative comparison. | Requires calibration and may inherit judge bias. |

## Relevance to Our Paper

P24 supports a key dimension of our trade-off-aware framework: evaluation should ask whether a generated comment is useful for downstream repair/refinement, not only whether it resembles a reference.

## Limitations from Our Perspective

- BLEU remains a dominant quantitative metric.
- o3-mini usefulness judgment is calibrated only on 100 pairs.
- Downstream refinement reward depends on a model that may itself be imperfect.
- No live developer acceptance or actual human repair outcome.
- Reward overoptimization risk is acknowledged generally but not deeply analyzed.

## Follow-up TODOs

- [ ] Add downstream usefulness/reward-model dimension to `synthesis/evaluation-dimensions.md`.
- [ ] Add reward-overoptimization and model-dependent reward to trade-off framework.
- [ ] Add non-actionable-but-detecting comment type to taxonomy.
- [ ] Update `matrices/cross-paper-synthesis.md` with P24 evidence.
