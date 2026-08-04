# P120 — Fine-Tuning and Prompt Engineering for Large Language Models-based Code Review Automation

## 1. Identification

| Field | Value |
|---|---|
| Project ID | `P120` |
| Citation key | `p120_pornprasit2024_fine_tuning_and_prompt_enginee` |
| Authors | Chanathip Pornprasit; Chakkrit Tantithamthavorn |
| Year | 2024 |
| Source | Information and Software Technology 175, 107523; arXiv `2402.00905v4` |
| Study type | Comparative empirical study of fine-tuning and prompting |

## 2. Screening

- **Scope decision:** Include as core evidence for fine-tuning, few-shot prompting, cold-start trade-offs, and code-revision evaluation.
- **Task:** Generate revised code from submitted code and review comments across three code-review datasets.
- **Evidence boundary:** Exact-match/code-similarity metrics evaluate code refinement, not human usefulness or correctness of natural-language review comments.
- **Metadata note:** An external record maps this arXiv item to the published IST article; verify the final bibliographic entry and do not double-count.

## 3. Study overview

The study compares 12 configurations of GPT-3.5 and Magicoder using fine-tuning, zero-shot prompting, few-shot prompting, and persona prompts. It also compares Guo et al.’s GPT-3.5 baseline and three existing code-review automation approaches. Experiments use CodeReviewer, Tufano, and D-ACT datasets, containing submitted code, comments, and revised code. Exact Match (EM) measures identical revised code; CodeBLEU adds syntax/semantic structure beyond token overlap. Magicoder uses DoRA parameter-efficient fine-tuning. The study’s main practical recommendation is fine-tuning when data are available and few-shot prompting without persona for cold-start settings.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Fine-tuned GPT-3.5 with zero-shot inference is the strongest general configuration; it improves EM over Guo et al.’s baseline by 73.17–74.23%. | Reported | RQ1; Table 4 |
| RQ2 | Fine-tuning improves GPT-3.5 EM by 63.91–1,100% and CodeBLEU by approximately 5.91–63.9% over non-fine-tuned zero-shot variants. | Reported | RQ2 |
| RQ3 | Few-shot prompting improves non-fine-tuned GPT-3.5 by 46.38–659.09% EM over zero-shot; persona reduces EM by 1.02–54.17%. | Reported | RQ3 |
| RQ4 | The study compares zero-shot, few-shot, persona, fine-tuned, and PEFT settings across three datasets and two models. | Reported | Sections 3–4 |
| RQ5 | The design targets practical resource choices: fine-tuning for sufficient data, few-shot/no-persona for cold starts. | Reported/proposed | Conclusions |
| RQ6 | EM and CodeBLEU provide automated code-revision evaluation, but no human review-quality validation is reported. | Limitation | Evaluation design |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Incorrect revision | Generated code does not match the accepted revised code. | EM failure | RQ1–RQ2 |
| Semantically weak revision | Output has token overlap but incorrect structure/meaning. | CodeBLEU limitation | Section 3.5 |
| Persona degradation | Adding a role/persona prompt reduces revision performance. | Measured | RQ3 |
| Cold-start weakness | No fine-tuning and no examples produce poor revisions. | Measured | RQ2–RQ3 |
| Reference overfitting | Exact/reference similarity rewards one accepted revision and may penalize valid alternatives. | Metric limitation | Evaluation |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Exact correction | Exact Match between generated and dataset revised code | Fine-tuned GPT-3.5 strongly outperforms non-fine-tuned and prior baseline. | Table 4 |
| Structured code similarity | CodeBLEU combines n-gram, AST/data-flow, and semantic signals | Provides more information than EM, but remains reference-based. | Section 3.5 |
| Fine-tuning benefit | Compare same model with/without fine-tuning | Large EM and CodeBLEU gains for GPT-3.5. | RQ2 |
| Prompt benefit | Compare zero-shot and few-shot settings | Few-shot is especially useful when fine-tuning is unavailable. | RQ3 |
| Persona effect | Compare prompts with/without developer persona | Persona generally harms EM in the reported configurations. | RQ3 |
| Cross-dataset robustness | CodeReviewer, Tufano, and D-ACT datasets | Recommendations vary by dataset/model; no human workflow validation. | Section 3 |

## 7. Mitigation and trade-offs

- **Mitigation family:** Fine-tuning, few-shot demonstrations, DoRA/PEFT, and prompt selection.
- **Intervention point:** Model adaptation and inference prompt.
- **What it reduces:** Weak cold-start performance and mismatch between general LLM knowledge and code-review refinement.
- **Useful feedback potentially lost:** Optimizing for exact revised code may suppress valid alternative repairs or explanatory review comments.
- **Coverage:** Multiple datasets broaden task coverage, but all are code/comment/revision benchmarks rather than live review workflows.
- **Human escalation:** No escalation policy or expert validation is evaluated; generated revisions require human/test verification.
- **Cost:** Fine-tuning is resource-intensive; few-shot inference consumes context and can be used when training data are insufficient.
- **New failure modes:** Persona-induced degradation, prompt sensitivity, hallucinated edits, and exact-reference bias.

## 8. Annotation and evaluator validity

- **Dataset oracle:** Existing revised-code targets supply reference outputs across three datasets.
- **Metrics:** EM and CodeBLEU capture exactness and structured similarity but not developer acceptance or semantic adequacy in all cases.
- **Statistical evidence:** The study compares many configurations, but the extracted record does not indicate human inter-rater evaluation.
- **Open science:** Fine-tuned models, scripts, and results are reported as publicly available.
- **Threats:** Dataset artifacts, leakage/overlap, reference-repair bias, model/API drift, and lack of human review assessment.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Three research questions and configuration scope are explicit. |
| Q2 | 2 | Three code-review datasets and task inputs/outputs are described. |
| Q3 | 2 | Models, prompting, fine-tuning, DoRA, and settings are detailed. |
| Q4 | 2 | EM and CodeBLEU are reported across configurations. |
| Q5 | 1 | Reference revisions provide an oracle, but no human rubric. |
| Q6 | 0 | No inter-rater or human review-quality agreement. |
| Q7 | 2 | 12 variants, two models, prior baseline, and existing approaches are compared. |
| Q8 | 2 | Multiple datasets improve breadth, though benchmark-based. |
| Q9 | 2 | Fine-tuning and prompting interventions are directly isolated. |
| Q10 | 1 | Resource/cold-start trade-offs discussed, but costs are not fully measured. |
| Q11 | 2 | Persona degradation, prompt effects, fine-tuning gains, and metric limitations are discussed. |
| Q12 | 1 | Relevant refinement evidence, but weak alignment with human comment usefulness. |

**Total: 19/24 — moderate-high confidence for adaptation/configuration evidence; limited for human review quality.**

## 10. Review-process reliability and bias

- **Duplicate risk:** Reconcile the arXiv record with the published IST article and count once.
- **Construct validity:** Code refinement success is not equivalent to good review feedback or accepted developer change.
- **Reference bias:** EM and CodeBLEU favor the single dataset revision and can penalize valid alternatives.
- **Prompt/model bias:** Results depend on GPT-3.5/Magicoder versions, prompt templates, and selected demonstrations.
- **Dataset bias:** CodeReviewer/Tufano/D-ACT distributions may not represent private repositories or complex review workflows.
- **Missing outcomes:** No expert correctness, applicability, review time, trust, or production adoption is measured.

## 11. Synthesis-ready conclusion

- P120 provides clear evidence that fine-tuning can substantially improve code-review refinement performance when suitable data are available.
- Few-shot prompting without persona is a practical cold-start mitigation, while persona prompts can unexpectedly degrade results.
- EM and CodeBLEU quantify code similarity but do not establish that generated changes are safe, useful, or preferred by developers.
- The study supports a resource-aware adaptation roadmap: fine-tune when data exist; use carefully selected demonstrations when they do not.
- Deduplicate against the published IST record before final synthesis integration.

