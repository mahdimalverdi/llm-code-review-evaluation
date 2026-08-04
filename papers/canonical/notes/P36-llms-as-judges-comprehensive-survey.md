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
## Legacy proposal-aligned quality appraisal (superseded by the canonical record)

P36 is **Supporting / High relevance**. It supports RQ2–RQ3 through judge functionality, methodology, metrics, bias, and attack taxonomies; RQ4 through reliability/cost/robustness trade-offs; RQ5 through evaluator validity; and RQ6 through methodological vocabulary. It is broad rather than code-review-specific.

**Quality score: 20/24.** Q1–Q5=2, Q6=1, Q7–Q8=2, Q9=0, Q10=2, Q11=1, Q12=2. Use P33 for SE-specific claims and P36 for general judge taxonomy.
## Canonical citation record

Use citation key `p36_li2024_llms_as_judges` from `references/references.bib`; do not duplicate its BibTeX entry in this note.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative; the compact block is provenance only.

- Identification/screening: `p36_li2024_llms_as_judges`; Supporting; Include; High relevance.
- Study overview: Broad survey of LLM-as-a-Judge functionality, methodology, metrics, bias, attacks, and future work.
- RQ1: Evaluator failure and adversarial categories (Reported).
- RQ2: Judge functions, metrics, bias, uncertainty, and robustness (Reported).
- RQ3: Judge methodology and meta-evaluation (Reported).
- RQ4: Reliability, scalability, adversarial robustness, and cost trade-offs (Reported).
- RQ5: Strong evaluator-validity support.
- RQ6: Strong general judge taxonomy support; P33 remains more SE-specific.
- Failure taxonomy: position/verbosity/authority bias; prompt sensitivity; adversarial attacks; invalid output; calibration failure.
- Metrics: agreement, consistency, calibration, robustness, uncertainty, and attack success.
- Mitigation/trade-off: judge auditing and robustness; more checks increase cost and complexity.
- Validity: broad cross-domain survey and limited review-specific evidence.
- Quality: 20/24; strong supporting survey.
- Synthesis conclusion: provides vocabulary for evaluator failures and meta-evaluation.

### 1. Identification
- P36; `p36_li2024_llms_as_judges`; local full PDF; included; authoritative record.
### 2. Screening and proposal alignment
- Include as supporting. `p36_li2024_llms_as_judges`; Supporting; Include; High relevance.
### 3. Study overview
Broad survey of LLM-as-a-Judge functionality, methodology, metrics, bias, attacks, and future work.
### 4. Evidence mapped to proposal RQ1–RQ6
| RQ | Evidence | Type | Location |
|---|---|---|---|
| RQ1 | Evaluator failure and adversarial categories (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ2 | Judge functions, metrics, bias, uncertainty, and robustness (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ3 | Judge methodology and meta-evaluation (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ4 | Reliability, scalability, adversarial robustness, and cost trade-offs (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ5 | Strong evaluator-validity support. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ6 | Strong general judge taxonomy support; P33 remains more SE-specific. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
### 5. Failure and problematic-comment categories
| Category | Type | Location |
|---|---|---|
| position/verbosity/authority bias | Reported/Inferred | Full PDF |
| prompt sensitivity | Reported/Inferred | Full PDF |
| adversarial attacks | Reported/Inferred | Full PDF |
| invalid output | Reported/Inferred | Full PDF |
| calibration failure. | Reported/Inferred | Full PDF |
### 6. Evaluation dimensions and metrics
| Dimension/metric | Limitation | Location |
|---|---|---|
| agreement | Not an end-to-end outcome | Full PDF |
| consistency | Not an end-to-end outcome | Full PDF |
| calibration | Not an end-to-end outcome | Full PDF |
| robustness | Not an end-to-end outcome | Full PDF |
### 7. Mitigation and trade-offs
- Mitigation/intervention: judge auditing and robustness; more checks increase cost and complexity.
- Useful feedback potentially lost: not directly measured unless stated above.
- Coverage: partial; useful-issue retention after intervention is incomplete.
- Human escalation: no formal rate/policy reported unless stated above.
- Cost: paper-specific evidence above; otherwise Not reported.
### 8. Annotation and evaluator validity
- broad cross-domain survey and limited review-specific evidence.
- Q7–Q8 encode judging and reliability depth.
### 9. Quality appraisal
| Criterion | Score | Evidence note |
|---|---:|---|
| Q1 | 2 | goal at scored depth. |
| Q2 | 2 | artifact at scored depth. |
| Q3 | 2 | dataset/context at scored depth. |
| Q4 | 2 | procedure at scored depth. |
| Q5 | 2 | metrics at scored depth. |
| Q6 | 1 | failures at scored depth. |
| Q7 | 2 | judging at scored depth. |
| Q8 | 2 | reliability at scored depth. |
| Q9 | 0 | intervention at scored depth. |
| Q10 | 2 | trade-offs at scored depth. |
| Q11 | 1 | threats at scored depth. |
| Q12 | 2 | SLR support at scored depth. |
- Total: 20/24; reporting-quality score.
### 10. Review-process reliability and bias
- Missing preservation/escalation evidence and selection/publication bias remain explicit; second-reviewer calibration is unavailable.
### 11. Synthesis-ready conclusion
- Contribution: Broad survey of LLM-as-a-Judge functionality, methodology, metrics, bias, attacks, and future work.
- Boundary: provides vocabulary for evaluator failures and meta-evaluation.
