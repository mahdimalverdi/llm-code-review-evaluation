# P113 — Distilling Desired Comments for Enhanced Code Review with Large Language Models

## 1. Identification

| Field | Value |
|---|---|
| Project ID | `P113` |
| Citation key | `p113_yu2024_distilling_desired_comments_fo` |
| Authors | Yongda Yu; Lei Zhang; Guoping Rong; Haifeng Shen; Jiahao Zhang; Haoxiang Yan; Guohao Shi; Dong Shao; Ruiqi Pan; Yuan Li; Qiushi Wang; Zhao Tian |
| Year | 2024 |
| Source | arXiv preprint, `2412.20340v2` |
| Study type | Dataset distillation, fine-tuning, alignment, and human evaluation |

## 2. Screening

- **Scope decision:** Include as core evidence for desired-comment labeling, training-data quality, and comment-level evaluation.
- **Task:** Identify review comments that correspond to subsequent code fixes and train LLaMA models to generate such comments.
- **Evidence boundary:** “Desired” is operationalized primarily as comments associated with later code changes; this does not cover all useful review purposes.
- **Metadata caveat:** Publisher/duplicate status and the provisional BibTeX record require verification.

## 3. Study overview

Desiview distills desired review comments (DRCs) from the 150,406-entry CodeReviewer dataset. It computes a desiredness score from the change in perplexity of the subsequent code fix with versus without the review comment, then uses four LLMs in a voting mechanism to label comments. The authors manually annotate 600 entries to evaluate the labeling method. LLaMA-3/3.1 8B models are fine-tuned on the distilled data (Desiview4FT) and then KTO-aligned using undesired comments (Desiview4FA). Automated evaluation uses 5,727 entries; human evaluation uses 300 entries and rates issue localization and issue description.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Desiview identifies comments that lead to meaningful subsequent code fixes; Desiview achieves 86.67% accuracy in DRC identification. | Reported | Table III |
| RQ2 | Desiview4FT/FA outperform original-data LLaMA-Reviewer on BLEU-4, issue localization, and issue-description ratings. | Reported | Table IV |
| RQ3 | Non-DRCs include comments unrelated to subsequent fixes, redundant suggestions, already-resolved issues, and comments that produce no meaningful change. | Reported | Figure 1; threats |
| RQ4 | The method uses original commits, comments, subsequent fixes, perplexity, and multi-model voting as training context. | Reported | Section III |
| RQ5 | Dataset distillation, fine-tuning, KTO alignment, and filtering low-quality comments are used to reduce hallucination/noise. | Reported | Sections III–IV |
| RQ6 | Manual labels, duplicated annotations, automated metrics, and human evaluation validate the method; BLEU remains a limited proxy for semantic quality. | Reported/limitation | Section IV |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Non-actionable comment | Comment does not trigger a meaningful subsequent fix. | Labeling criterion | Section III |
| Mislocalized issue | Comment does not identify the location of the real defect. | Human Position metric | Section IV |
| Incorrect issue description | Comment fails to describe the actual issue or solution. | Human Perfect metric | Section IV |
| Redundant/irrelevant suggestion | Comment proposes stylistic or unrelated changes without useful repair effect. | Dataset examples | Figure 1 |
| Already-resolved issue | Comment addresses a change already present in the diff. | Dataset example | Figure 1 |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| DRC identification | Accuracy, precision, recall, F1 | Desiview: 86.67 accuracy, 88.93 precision, 80.37 recall, 84.44 F1. | Table III |
| Text similarity | BLEU-4 against reference comments | Desiview4FA improves over LLaMA-Reviewer, but BLEU is not semantic correctness. | Table IV |
| Issue localization | Human Position: same issue location as reference | LLaMA-3 Desiview4FA reaches 80.00; LLaMA-3.1 reaches 79.00. | Table IV |
| Issue description | Human Perfect: same issue/solution description | LLaMA-3 Desiview4FA reaches 18.67; LLaMA-3.1 reaches 16.67. | Table IV |
| Human consistency | Duplicated evaluations and chi-squared tests | p=0.965 for labeling and p=0.887 for generation evaluation. | Section IV |
| Dataset quality prediction | RoBERTa/CodeBERT classify whether comments lead to fixes | Accuracy/F1 around 79–82, suggesting a possible quality filter. | Table VI |

## 7. Mitigation and trade-offs

- **Mitigation family:** Perplexity-based dataset distillation, multi-LLM voting, fine-tuning, and KTO alignment with undesired examples.
- **Intervention point:** Training-data construction and model alignment.
- **What it reduces:** Noisy supervision, irrelevant comments, hallucination, and weak issue localization/description.
- **Useful feedback potentially lost:** Defining quality as “leading to a code fix” can exclude explanatory, preventive, acknowledgment, or knowledge-sharing comments.
- **Coverage:** The method depends on observable subsequent fixes and may miss valuable comments whose effect is not recorded in code.
- **Human escalation:** A quality classifier could filter comments before developers see them, but human review remains necessary for ambiguous judgments.
- **Cost:** Four-model voting and perplexity computation add preprocessing cost, while 8B low-parameter training reduces resource demands.
- **New failure modes:** Perplexity may misclassify useful comments, voting can share model bias, and distilled-label noise can leak into training/test sets.

## 8. Annotation and evaluator validity

- **Manual labeling:** Two software-engineering graduate students annotate overlapping entries; duplicated cases assess consistency.
- **Sample sizes:** 600 entries for DRC identification and 300 entries for human generation evaluation.
- **Agreement checks:** Chi-squared tests report p=0.965 and p=0.887, interpreted by the authors as consistent annotation/evaluation.
- **Human rubric:** Localization and issue description are judged separately, which distinguishes finding the right place from explaining the right problem.
- **Validity threats:** Code-fix linkage is an incomplete proxy for comment usefulness; BLEU and reference matching may underrepresent semantic variation.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | DRC definition and dataset/model objectives are explicit. |
| Q2 | 2 | CodeReviewer dataset and entry counts are described. |
| Q3 | 2 | Distillation, voting, fine-tuning, KTO, and evaluation procedures are detailed. |
| Q4 | 2 | Identification and generation metrics are reported. |
| Q5 | 2 | Manual labels and two human quality dimensions are specified. |
| Q6 | 1 | Consistency tests are reported, though agreement reporting is limited. |
| Q7 | 2 | Rule, GPT, original-data, distilled, and aligned baselines are compared. |
| Q8 | 1 | Large multi-language dataset, but one benchmark source. |
| Q9 | 2 | Training-data filtering and alignment are directly evaluated. |
| Q10 | 1 | Resource constraints and low-parameter training are discussed, not operational cost. |
| Q11 | 2 | Localization, description, noise, and dataset-quality issues are separated. |
| Q12 | 2 | Directly targets useful review-comment generation. |

**Total: 21/24 — high confidence for training-data quality and comment-generation evidence, with construct-validity caveats.**

## 10. Review-process reliability and bias

- **Construct bias:** DRCs are defined by subsequent code changes, privileging fix-triggering comments over other legitimate review outcomes.
- **Label leakage risk:** The same CodeReviewer source and fix relationships underpin distillation and evaluation, so residual noise or overlap may inflate results.
- **Metric bias:** BLEU and reference matching penalize valid alternative wording and do not fully capture correctness or usefulness.
- **Model bias:** Four voting models and LLaMA-specific training may not transfer to other architectures or closed models.
- **Annotation limitation:** Graduate-student judgments and chi-squared consistency checks do not establish expert validity.
- **External validity:** CodeReviewer is large and multilingual, but it may not represent repository-scale context or modern production review workflows.

## 11. Synthesis-ready conclusion

- P113 shows that training-data quality is a central determinant of LLM code-review performance.
- Linking comments to subsequent fixes is a practical way to distill desired examples, but it is only one dimension of review usefulness.
- Distillation and KTO alignment improve issue localization and description over noisy original-data training, with modest gains from alignment beyond fine-tuning.
- Evaluation should separate finding the correct location from accurately describing the issue, and should supplement text similarity with human or behavioral validation.
- Use as core evidence for desired-comment taxonomy, supervision quality, and the trade-off between fix-triggering precision and broader review value.

