# P36 — LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation Methods

> [!NOTE]
> Compact v2 analysis. P36 is a broad, cross-domain survey of LLM-as-Judge methods. It is less SE-specific than P33, but it provides a strong taxonomy of judge functionality, methodology, meta-evaluation metrics, bias categories, adversarial attacks, and future directions.

## Status

- Paper ID: `P36`
- Analysis status: `First pass completed from PDF; needs citation/BibTeX cleanup`
- Priority: `Medium / High`
- Reading depth: `Read once from PDF`
- Confidence: `High`

## Bibliographic Information

| Field | Value |
|---|---|
| Title | LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation Methods |
| Authors | Haitao Li, Qian Dong, Junjie Chen, Huixue Su, Yujia Zhou, Qingyao Ai, Ziyi Ye, Yiqun Liu |
| Year | 2024 |
| Venue / Source | arXiv / ACM-style preprint |
| DOI / arXiv | arXiv:2412.05579 |
| Artifact | Awesome list: `CSHaitao/Awesome-LLMs-as-Judges` |

```bibtex
% TODO: Add checked arXiv BibTeX.
```

## One-Sentence Summary

> P36 surveys LLM-as-Judge systems across functionality, methodology, applications, meta-evaluation, limitations, and future work, providing a broad taxonomy of how judges are used and why their reliability is fragile.

## Main Contribution

The paper organizes LLM-as-Judge research around five questions:

| Perspective | Question |
|---|---|
| Functionality | Why use LLM judges? |
| Methodology | How to use LLM judges? |
| Applications | Where to use LLM judges? |
| Meta-evaluation | How to evaluate LLM judges? |
| Limitations | What can go wrong? |

## Formal Definition

P36 uses the same general input-output form:

```text
(Y, E, F) = E(T, C, X, R)
```

| Symbol | Meaning |
|---|---|
| `E` | Evaluation function/system. |
| `T` | Evaluation type: pointwise, pairwise, listwise. |
| `C` | Evaluation criteria. |
| `X` | Evaluation item. |
| `R` | Optional references. |
| `Y` | Evaluation result. |
| `E` output | Explanation. |
| `F` | Feedback for improvement. |

## Functionality Taxonomy

| Function | Subtypes |
|---|---|
| Performance evaluation | Response evaluation, model evaluation. |
| Model enhancement | Reward modeling during training, verifier during inference, feedback for refinement. |
| Data construction | Data annotation, data synthesis. |

## Methodology Taxonomy

| Method Family | Examples / Notes |
|---|---|
| Single-LLM prompt-based | In-context learning, chain-of-thought, definition augmentation, multi-turn optimization. |
| Single-LLM tuning-based | Score-based tuning, preference-based learning. |
| Post-processing | Probability calibration, text reprocessing, task transformation. |
| Multi-LLM communication | Cooperation, competition, debate. |
| Multi-LLM aggregation | Voting, weighted scoring, Bayesian/graph aggregation, cascades. |
| Human-AI collaboration | Human refinement during or after automated evaluation. |

## Application Domains

| Domain | Examples |
|---|---|
| General NLP | Dialogue, summarization, translation, story generation. |
| Multimodal | Vision-language, image/audio/video evaluation. |
| Medical | Clinical notes, medical QA, counseling. |
| Legal | Law LLM evaluation, legal retrieval. |
| Financial | Risk assessment, credit scoring, benchmark construction. |
| Education | Assignment grading, essay scoring, math reasoning, debate judging. |
| Information retrieval | Relevance judgment, ranking, RAG evaluation. |
| Software engineering | Code generation, CodeUltraFeedback, bug report summarization. |

## Meta-Evaluation Metrics

| Metric | Use |
|---|---|
| Accuracy | Correct judgment proportion. |
| Pearson | Linear correlation with human scores. |
| Spearman | Rank correlation. |
| Kendall’s Tau | Ordinal consistency, handles ranking/ties. |
| Cohen’s Kappa | Chance-adjusted agreement for categorical labels. |
| ICC | Reliability across multiple raters. |

## Bias Taxonomy

| Bias Family | Biases |
|---|---|
| Presentation-related | Position bias, verbosity bias. |
| Social-related | Authority bias, bandwagon-effect bias, compassion-fade bias, diversity bias. |
| Content-related | Sentiment bias, token bias, contextual bias. |
| Cognitive-related | Overconfidence bias, self-enhancement bias, refinement-aware bias, distraction bias, fallacy-oversight bias. |

## Adversarial Attack Categories

| Category | Examples |
|---|---|
| Text-level manipulation | Typos, word order, irrelevant additions, paraphrases. |
| Structural/semantic distortion | Syntactic rewrites and semantic-preserving perturbations. |
| Optimization-based attacks | Gradient/search/black-box adversarial strings. |
| Judge-specific attacks | Prompt injection and universal phrases to inflate scores or force biased choices. |

## Future Work Directions

| Goal | Directions |
|---|---|
| More efficient | Automated criteria/task construction, scalable evaluation systems, faster evaluation. |
| More effective | Reasoning+judge integration, collective judgment, stronger domain knowledge, cross-domain/language transfer, multimodal evaluation. |
| More reliable | Interpretability/transparency, bias/fairness mitigation, robustness. |

## Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| General judge taxonomy | Very high | Strongest contribution. |
| Bias taxonomy | Very high | Useful vocabulary for our evaluator section. |
| Meta-evaluation metrics | High | Standard statistical measures. |
| Application breadth | Very high | Cross-domain survey. |
| SE specificity | Low / Medium | Only a small SE subsection. |
| Adversarial robustness | High | General LLM and judge-specific attacks. |
| Human-AI collaboration | Medium / High | Surveyed as methodology. |

## Problematic Judge / Evaluation Types

- Position-biased judge.
- Verbosity-biased judge.
- Authority-biased judge.
- Bandwagon-biased judge.
- Sentiment-biased judge.
- Token-biased judge.
- Self-enhancing judge.
- Refinement-aware biased judge.
- Distracted judge.
- Judge overlooking logical fallacies.
- Judge vulnerable to universal adversarial score inflation.
- Judge relying on stale knowledge or hallucinated facts.
- Domain-knowledge-deficient judge.

## Context-Quality Evidence

P36 shows that LLM judge outputs are affected by many non-semantic factors: position, verbosity, authority markers, majority cues, identity markers, sentiment, token frequency, irrelevant context, refinement history, and adversarial strings. Therefore, evaluator context must be treated as a controlled variable.

## Trade-off Extraction

| Strategy | Benefit | Risk / Cost |
|---|---|---|
| Single LLM judge | Simple and scalable. | Single-model bias and limited domain expertise. |
| Multi-LLM debate/aggregation | Can reduce single-model bias and improve robustness. | Higher compute, coordination, and possible groupthink. |
| Human-AI collaboration | Improves high-stakes reliability. | Less scalable and needs human calibration. |
| Pairwise evaluation | Good for subtle preferences. | Position bias and many comparisons. |
| Listwise evaluation | Holistic ranking. | Transitivity and consistency issues. |
| Reference-free judging | Flexible for open-ended tasks. | Depends on judge knowledge and bias. |
| Reference-based judging | Anchors evaluation. | Reference quality and style bias. |
| Criteria automation | More scalable adaptation. | Criteria drift and hidden misalignment. |

## Relevance to Our Paper

P36 is a vocabulary and taxonomy source. It helps us name evaluator failure modes and justify why LLM-as-a-Judge validity should include bias, adversarial robustness, meta-evaluation metrics, and human-AI collaboration.

## Limitations from Our Perspective

- Very broad and not focused on software engineering.
- Software engineering section is brief and mostly code generation / bug report summarization.
- Many claims are survey-level summaries rather than direct empirical results.
- Because P33 is SE-specific, use P36 mostly for general judge taxonomy and bias terminology.

## Follow-up TODOs

- [ ] Add P36 bias taxonomy to evaluator-validity framework.
- [ ] Add adversarial judge attacks to threat model.
- [ ] Add meta-evaluation metric table to methodology notes.
- [ ] Use P33 as SE-specific source and P36 as general LLM-as-Judge taxonomy source.
