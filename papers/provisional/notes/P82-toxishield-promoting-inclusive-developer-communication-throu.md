# P82 — ToxiShield: Promoting Inclusive Developer Communication through Real-Time Toxicity Filtering

## 1. Identification

- Project ID: `P82` (provisional)
- Citation key: `p82_anindya2026_toxishield_promoting_inclusive`
- Full reference: Md Awsaf Alam Anindya; Showvik Biswas; Anindya Iqbal; Jaydeb Sarker; Amiangshu Bosu. “ToxiShield: Promoting Inclusive Developer Communication through Real-Time Toxicity Filtering.” Proc. ACM Softw. Eng., FSE 2026, Article FSE123.
- DOI/URL: `https://doi.org/10.1145/3808130`; `https://arxiv.org/abs/2604.14408v1`
- Review date: 2026-08-04
- Source/database: arXiv/full-text screening
- Selection stage: included for reconciliation; canonical corpus integration pending
- Duplicate or companion publication: Publisher record appears available; reconcile final metadata.

## 2. Screening

- Decision: `Include`
- Relevance: `High`
- Decision rationale: Directly detects and reframes toxic code-review comments in real time while evaluating toxicity classification, content preservation, and developer acceptance.
- Protocol deviation or amendment: None reported.
- Inclusion group: `Core`
- Proposal deliverable supported: taxonomy / annotation protocol / mitigation design / trade-off framework
- Exact inclusion criterion: Core inclusion: problematic-comment detection, mitigation, and human workflow evaluation.

## 3. Study overview

- Purpose: Promote constructive communication through a GitHub PR browser extension.
- Research questions: Evaluate binary toxicity detection, fine-grained toxicity categorization/reasoning, detoxification quality, and perceived usefulness/ease of adoption.
- Method: Three-module system: BERT Toxicity Filter, LLM Communication Coach, and LLM Reframer; model comparisons plus a 10-developer Technology Acceptance Model study.
- Evaluated system/artifact: Browser extension integrated with GitHub pull requests; toxic text is categorized and rewritten into a constructive alternative.
- Dataset/benchmark: Binary dataset of 38,761 comments (10,120 toxic, 28,641 non-toxic); multiclass set of 1,200 comments; reframing dataset of 10,120 toxic comments.
- Input context: Draft code-review text; the tool flags toxicity, provides category/reason explanation, then proposes a non-toxic rewrite.
- Main findings: BERT reaches 98% accuracy and 0.97 toxic-class F1; Claude 3.5 Sonnet reaches macro F1 0.42/MCC 0.39 for 12-class toxicity; fine-tuned Llama 3.2 reaches 95.27% style transfer, 97.03% fluency, 67.07% content preservation, and 84% J-score.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Toxicity is operationalized as binary and 12-category/multi-label classification of code-review comments. | Reported | Sections 2–4 |
| RQ2 | Toxicity categories include profanity, insult, threat, hostility, obscenity, and other nuanced antisocial behaviors; sparse classes remain difficult. | Reported | Sections 2.2–3 |
| RQ3 | Reframer performs style transfer from toxic to constructive text with explicit content-preservation metrics. | Reported | Section 4 |
| RQ4 | Detoxification trades toxicity reduction and fluency against content preservation; J-score summarizes the balance. | Inferred | Section 4 |
| RQ5 | Ten professional developers evaluate perceived usefulness, ease of use, and behavioral intention via TAM. | Reported | Section 5 |
| RQ6 | Direct mitigation evidence, but no downstream review-quality or acceptance outcome is measured. | Inferred | Sections 4–5 |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Explicit toxicity | Profanity, insult, threat, or obscenity in review text. | Taxonomy | Sections 2–3 |
| Implicit/nuanced toxicity | Hostility, deprecation, sarcasm, or technical frustration requiring context. | Taxonomy/result | Sections 2–3 |
| Toxicity misclassification | Sparse or ambiguous categories produce low multiclass performance. | Reported failure | Section 3 |
| Meaning/style distortion | Reframed text loses technical content while becoming non-toxic. | Trade-off category | Section 4 |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Binary detection | Accuracy, precision, recall, toxic-class F1. | BERT: 98% accuracy, F1 0.97. | Section 2.1 |
| Fine-grained classification | Exact match, precision, recall, F1, macro MCC across 12 categories. | Claude: macro F1 0.42, MCC 0.39. | Section 3 |
| Style transfer | Style transfer accuracy and fluency. | Llama 3.2: 95.27% and 97.03%. | Section 4 |
| Content preservation | Preservation of technical meaning. | 67.07%, leaving substantial loss risk. | Section 4 |
| Overall reframing | J-score combines trade-offs. | 84%. | Section 4 |
| User acceptance | TAM perceived usefulness/ease of use/behavioral intention. | 10 professional developers; perceived acceptance reported. | Section 5 |

## 7. Mitigation and trade-offs

- Mitigation family: Real-time toxicity filtering, explanation, and constructive reframing.
- Intervention point: While a developer drafts a PR review comment, before submission.
- What it reduces: Toxic, exclusionary, hostile, or uncivil communication.
- Useful feedback potentially lost: Reframing may remove emotional or direct wording and can alter technical intent; content preservation is only 67.07%.
- Coverage effect: Binary detection is strong, but nuanced/sparse toxicity categories are poorly covered.
- Human escalation effect: Communication Coach explanations support reflection; escalation is not measured.
- Computational/operational cost: Browser integration and multi-stage LLM calls are required; latency/cost is not reported.
- New failure modes: False positives on technical frustration, hallucinated rewrites, semantic drift, and over-sanitization.

## 8. Annotation and evaluator validity

- Judge/annotator: Manually annotated binary and multiclass datasets; LLMs evaluate/rewrite; 10 developers participate in TAM study.
- Rubric: Binary toxicity, 12-category labels, style transfer, fluency, content preservation, J-score, and TAM constructs.
- Agreement/reliability: Quadratic-weighted Cohen’s kappa is reported for reframing dimensions; multiclass validation includes author review of 100 predictions. Exact aggregate reliability varies by dimension.
- Validity checks: Stratified toxic sampling, two-stage manual validation, model comparisons, teacher-dataset evaluation, replication package, and user study.
- Possible bias: Small TAM sample, synthetic/teacher-generated reframing pairs, cultural variation in toxicity, and model-based evaluation.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Three-module system and workflow are explicit. |
| Q2 | 2 | Binary, multiclass, and reframing datasets are reported. |
| Q3 | 2 | BERT/LLM candidates and human study are described. |
| Q4 | 2 | Detection, classification, transfer, preservation, and TAM metrics are explicit. |
| Q5 | 2 | Toxicity taxonomy and reframing criteria are specified. |
| Q6 | 1 | Kappa is reported, but multiclass label reliability is limited. |
| Q7 | 2 | Stratification, manual validation, and model comparisons are described. |
| Q8 | 1 | User study is small and synthetic evaluation remains a concern. |
| Q9 | 2 | Real-time filtering/reframing is explicit intervention. |
| Q10 | 1 | Real-time intent is stated, but latency/cost is not measured. |
| Q11 | 2 | Nuance, sparsity, semantic drift, and user-study limits are discussed. |
| Q12 | 2 | Directly addresses problematic review communication and mitigation. |

- Total: `21/24` provisional
- Quality interpretation: Strong detection/mitigation engineering evidence, but limited downstream and human-scale validation.

## 10. Review-process reliability and bias

- Missing data: Developer behavioral outcomes, long-term adoption, review correctness, latency, and false-positive costs are not measured.
- Publication-bias concern: Not assessed; model-selected results and positive TAM framing may bias interpretation.
- Selection uncertainty: Included by full-text screening; final publisher record should be reconciled.
- Extraction uncertainty: Moderate for content-preservation judgments and small user study.
- Second-reviewer agreement: Not available for this note.
- Duplicate-publication handling: Pending final-version reconciliation.

## 11. Synthesis-ready conclusion

- Contribution to the SLR: Provides an end-to-end mitigation pipeline for toxic code-review communication, including detection, explanation, and reframing.
- What the paper does not establish: It does not establish improved review correctness, developer behavior, or safe semantic preservation in production.
- Research gap supported: Communication mitigation should measure toxicity reduction jointly with technical-intent preservation, false positives, latency, and developer outcomes.
- Candidate synthesis claims: Real-time detoxification can make feedback more constructive, but strong style/fluency scores do not guarantee preservation of actionable technical content.
- Follow-up verification needed: Inspect released data/prompts and obtain detailed TAM and kappa tables before corpus integration.
