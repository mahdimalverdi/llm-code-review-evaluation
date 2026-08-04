# P122 — The Right Prompts for the Job: Repair Code-Review Defects with Large Language Model

## 1. Identification

| Field | Value |
|---|---|
| Project ID | `P122` |
| Citation key | `p122_zhao2023_the_right_prompts_for_the_job_` |
| Authors | Zelin Zhao; Zhaogui Xu; Jialong Zhu; Peng Di; Yuan Yao; Xiaoxing Ma |
| Year | 2023 |
| Source | arXiv preprint, `2312.17485v1` |
| Study type | Prompt comparison and LLM-based code-repair evaluation |

## 2. Screening

- **Scope decision:** Include as core evidence for review-comment context, repair correctness, prompt design, and human/checker dataset trade-offs.
- **Task:** Repair code defects identified by human reviewers or automated checkers using LLM-generated patches.
- **Evidence boundary:** The study measures whether generated code matches/repairs reference fixes; it does not evaluate developer acceptance or the quality of generated review prose.
- **Metadata caveat:** Publisher/duplicate status and the provisional BibTeX record require verification.

## 3. Study overview

The study evaluates ChatGPT-3.5, ChatGPT-4, LLaMA, CodeLLaMA, CodeGen-2, CodeFuse, and CodeReviewer under seven prompt designs. Prompts progressively add bug location, review comments, buggy-code context, and fix range. Two datasets represent human reviewer comments and PMD automated-checker defects; the datasets contain comparable training/evaluation instances and are cross-validated. Fine-tuning and zero-shot/few-shot settings are compared. Exact code match (ECM) and CodeBLEU evaluate repaired code, with defect-type analysis and model-size comparisons.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | CodeLLaMA performs best among fine-tuned systems, reaching up to 72.97% exact repair match. | Reported | RQ1; Table 2 |
| RQ2 | Adding review comments and fix-range information produces the strongest prompt configuration; bug location alone gives smaller gains. | Reported | RQ2; Tables 2, 4 |
| RQ3 | Models around 6–7B parameters often provide a strong performance/cost balance; larger size is not always better. | Reported | RQ3 |
| RQ4 | Models trained on human-review data perform best on human-review defects, while checker-trained models transfer imperfectly across datasets. | Reported | RQ4; Table 5 |
| RQ5 | Prompts should include actionable review feedback and the target fix range; dataset diversity and source alignment are important. | Reported/proposed | Discussion |
| RQ6 | ECM, CodeBLEU, defect-type analysis, and cross-dataset validation provide evidence; no human assessment of patch safety or usefulness is included. | Limitation | Evaluation |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Wrong repair | Generated code does not match the expected repaired code or fails to correct the defect. | ECM failure | RQ1 |
| Incomplete repair | Model addresses only part of a review comment or defect. | Qualitative failure | Prompt analysis |
| Scope overreach | Generated patch modifies unrelated code or exceeds the requested fix range. | Target risk | Prompt design |
| Formatting contamination | ChatGPT output includes explanations/comments around code, complicating evaluation and deployment. | Reported | Evaluation discussion |
| Dataset transfer failure | Model trained on human comments performs worse on checker defects, or vice versa. | Cross-validation result | RQ4 |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Exact repair | Exact Code Match (ECM) with reference fixed snippet | Best CodeLLaMA configuration reaches 72.97%. | RQ1/Table 2 |
| Structural/semantic repair | CodeBLEU | Captures code structure beyond string matching, but remains reference-based. | Section 3.5 |
| Prompt contribution | Compare seven prompts P1–P7 | Review comments and fix range yield largest incremental improvement. | RQ2/Table 4 |
| Model scaling | Compare LLM families and parameter sizes | 6–7B models often balance performance and cost; size alone is insufficient. | RQ3 |
| Dataset transfer | Train/test on reviewer-data (RD) and PMD-data (PD) combinations | Same-source training/testing gives best performance; cross-source transfer is weaker. | RQ4/Table 5 |
| Defect coverage | ECM by 30 PMD defect categories | Performance varies substantially by defect type. | Section 4.1.3 |

## 7. Mitigation and trade-offs

- **Mitigation family:** Prompt enrichment with review comments, bug location, code context, and fix range; fine-tuning on aligned datasets.
- **Intervention point:** Input context and model adaptation.
- **What it reduces:** Under-specified repairs, wrong locations, and incomplete use of human/checker feedback.
- **Useful feedback potentially lost:** A narrow fix range can constrain broader but necessary repairs; exact-reference optimization may reject valid alternatives.
- **Coverage:** Combining human and automated-checker datasets broadens defect coverage, but source mismatch can reduce transfer.
- **Human escalation:** Generated patches require tests and human review before application; no operational escalation protocol is tested.
- **Cost:** Fine-tuning and larger LLMs are expensive; 6–7B models offer a practical compromise.
- **New failure modes:** Prompt overloading, malformed output, context truncation, dataset-specific overfitting, and unsafe code edits.

## 8. Annotation and evaluator validity

- **Datasets:** Human-review and PMD-checker datasets provide complementary defect/comment sources; checker examples are manually reviewed for quality.
- **Evaluation:** ECM and CodeBLEU are supplemented by defect-type and cross-dataset analyses.
- **Human validation:** No developer/expert rating of patch correctness, safety, or applicability is reported.
- **Metric limitation:** Exact match penalizes semantically equivalent repairs; CodeBLEU still relies on a reference patch.
- **Reproducibility:** Prompt templates, models, datasets, and scripts are described/reported as available, but API/model versions may drift.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Four research questions and prompt objective are explicit. |
| Q2 | 2 | Human-review/checker datasets and defect types are described. |
| Q3 | 2 | Models, seven prompts, fine-tuning, and evaluation are detailed. |
| Q4 | 2 | ECM, CodeBLEU, defect categories, and transfer results are reported. |
| Q5 | 1 | Dataset quality checks are reported, but no human patch rubric. |
| Q6 | 0 | No inter-rater agreement or expert validation of generated patches. |
| Q7 | 2 | Many models, prompts, dataset conditions, and sizes are compared. |
| Q8 | 2 | Two complementary data sources and cross-validation improve breadth. |
| Q9 | 2 | Context/prompt and fine-tuning interventions are directly evaluated. |
| Q10 | 1 | Model-size cost trade-off is discussed, not fully measured. |
| Q11 | 2 | Prompt, defect-type, transfer, and formatting failures are analyzed. |
| Q12 | 1 | Strong repair evidence, but limited alignment with human review outcomes. |

**Total: 19/24 — moderate-high confidence for prompt/context and repair evidence; limited human validity.**

## 10. Review-process reliability and bias

- **Construct bias:** Exact repair to a reference patch is not equivalent to a safe or preferred repair.
- **Dataset bias:** Human comments and PMD defects represent different distributions and may not cover repository-level failures.
- **Prompt bias:** Results are sensitive to the chosen seven templates and information ordering.
- **Model/API drift:** ChatGPT behavior can change across versions and access modes.
- **Transfer uncertainty:** Cross-dataset performance may reflect domain mismatch rather than general repair capability.
- **Missing outcomes:** No test-passing rate, accepted-patch rate, developer trust, or production regression analysis is reported.

## 11. Synthesis-ready conclusion

- P122 shows that review comments and explicit fix-range context materially improve LLM-based repair of code-review defects.
- The best prompt is not merely more verbose: useful, localized reviewer feedback and target scope are the key additions.
- Human-review and automated-checker data are complementary but not freely interchangeable; source-aligned fine-tuning performs best.
- Repair metrics must go beyond exact match and include tests, safety, semantic equivalence, and human acceptance.
- Use as core evidence for context grounding and repair-oriented prompt design, with human verification required before patch application.

