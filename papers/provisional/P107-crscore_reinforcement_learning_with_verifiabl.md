# P107 — CRScore++: Reinforcement Learning with Verifiable Tool and AI Feedback for Code Review

## 1. Identification

| Field | Value |
|---|---|
| Project ID | `P107` |
| Citation key | `p107_kapadnis2025_crscore_reinforcement_learning` |
| Authors | Manav Nitin Kapadnis; Atharva Naik; Carolyn Rose |
| Year | 2025 |
| Source | arXiv preprint, `2506.00296v1` |
| Study type | Training-method study with automated and human evaluation |

## 2. Screening

- **Scope decision:** Include as core evidence for verifiable tool grounding, evaluator design, and quality trade-offs in generated code reviews.
- **Task:** Generate review comments for Python, Java, and JavaScript code changes.
- **Evidence boundary:** The study evaluates comprehensiveness, conciseness, relevance, and tool-signal use; it does not directly measure accepted fixes or downstream developer productivity.
- **Metadata caveat:** Publisher/duplicate status and the provisional BibTeX record require verification before final submission.

## 3. Study overview

CRScore++ combines reinforcement learning from AI feedback with verifiable signals from linters, security analyzers, and code-smell detectors. The pipeline uses GPT-4o-mini to produce tool-augmented demonstrations and pseudo-references, fine-tunes Qwen2.5-Coder 3B/7B models, and applies preference optimization to candidate reviews. Training uses 20,888 Python CodeReviewer examples, with a 5,000-example subset for preference optimization. Evaluation compares zero-shot, tool-guided, supervised fine-tuned (Stage 1), and DPO (Stage 2) variants on Python and on out-of-domain Java and JavaScript changes. A human study covers 100 changes, with five graduate-student annotators and 5-point ratings.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | The system generates code-review comments using Qwen2.5-Coder models trained with static-analysis feedback and AI preference signals. | Reported | Sections 3–4 |
| RQ2 | Comprehensiveness, conciseness, relevance, tool-use accuracy, and tool-use coverage are measured; human ratings use the same three quality dimensions. | Reported | Tables 1–4 |
| RQ3 | Directly trained-on-human-review baselines are described as noisy and perform below zero-shot variants; the study highlights irrelevance, incompleteness, and loss of conciseness as risks. | Reported/inferred | Sections 4–5 |
| RQ4 | Inputs include code diffs, full source context for human rating, and outputs from Ruff, PyScent, PMD, DesigniteJava, and a JavaScript linter. | Reported | Sections 3, Appendix B |
| RQ5 | Tool-augmented SFT improves balance; DPO increases comprehensiveness and relevance while reducing conciseness. | Reported | Tables 1–4 |
| RQ6 | Automated GPT-4o-mini judging is cross-checked with human ratings; overlapping annotations yield reported Cohen’s kappa of 0.7. | Reported | Section 5.4; Appendix B |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Incomplete coverage | Review omits topics surfaced by static analysis or the topic list. | Measured by coverage/comprehensiveness | Sections 4–5 |
| Irrelevance | Comment is not pertinent to the changed code or target issue. | Measured by relevance | Tables 1–4 |
| Excessive verbosity | Review covers more issues but loses concise focus. | Reported trade-off | Sections 4–5 |
| Noisy human-review supervision | Comments scraped from online discussions can be irrelevant or noisy for direct training. | Reported finding | Section 5.1 |
| Tool-grounding error | Model fails to use, or misrepresents, linter/code-smell signals. | Measured by tool accuracy/coverage | Table 3 |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Comprehensiveness | 5-point human rating and automated score for covered review topics | Qwen 7B Stage 2 reaches 0.69 in-domain and human ratings favor Stage 2. | Tables 1, 4 |
| Relevance | 5-point human rating and automated score for pertinence | Qwen 7B Stage 2 reaches 0.65 in-domain; gains transfer to Java/JavaScript. | Tables 1–4 |
| Conciseness | 5-point human rating and automated score for appropriate focus | DPO decreases conciseness relative to SFT/zero-shot. | Tables 1, 4 |
| Tool accuracy | GPT-4o-mini judge score for correctly using tool findings | Stage 1 generally improves accuracy over zero-shot; DPO adds little accuracy. | Table 3 |
| Tool coverage | GPT-4o-mini judge score for surfacing relevant tool findings | Coverage improves substantially after SFT/DPO, with variation by language/model. | Table 3 |
| Human agreement | Cohen’s kappa on overlapping annotations | Reported agreement is 0.7; human sample remains limited to 100 changes. | Appendix B |
| Compute/operational cost | A100 training, API calls, and model scale | Approximately 450 GPU hours and about 40,000 GPT-4o-mini calls are reported. | Appendix B.4 |

## 7. Mitigation and trade-offs

- **Mitigation family:** Tool-augmented knowledge distillation, supervised fine-tuning, and preference optimization using pseudo-references and verifier signals.
- **Intervention point:** Training reward and demonstration construction, rather than only inference-time prompting.
- **What it reduces:** Missing tool-detected issues, weak relevance, and noisy preference-only supervision.
- **Useful feedback potentially lost:** DPO improves comprehensiveness at the cost of conciseness, so longer reviews may impose additional reviewer burden.
- **Coverage:** Static analyzers broaden observable defect categories, but their language/tool coverage determines what can be surfaced.
- **Human escalation:** The framework supports human review but does not test a concrete escalation or acceptance workflow.
- **Cost:** Training and GPT-4o-mini data-generation/judging require substantial compute and API expenditure.
- **New failure modes:** Proprietary LLM-judge bias, pseudo-reference errors, tool blind spots, and cross-language transfer failures remain possible.

## 8. Annotation and evaluator validity

- **Annotators:** Five graduate students with programming experience; they received training and calibration.
- **Rubric:** Comprehensiveness, conciseness, and relevance on 5-point Likert scales, using code diffs, source context, and topic lists.
- **Agreement:** Cohen’s kappa is reported as 0.7 on an overlapping subset; the paper also reports an earlier 0.65 agreement description, which should be reconciled.
- **Automated judge:** GPT-4o-mini scores structured topic coverage and quality dimensions; human ratings are used as a validity check.
- **Blinding and ethics:** Annotators were not told model identities, consent/compensation are described, and IRB review is reported.
- **Bias risks:** The judge is proprietary, topics are generated by an LLM, and the human sample is relatively small and limited to three languages.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Objective and training stages are explicit. |
| Q2 | 2 | Dataset, languages, and evaluation sets are described. |
| Q3 | 2 | Models, tools, prompts, and training procedure are detailed. |
| Q4 | 2 | Automated and human metrics cover several review-quality dimensions. |
| Q5 | 2 | Human rubric and topic-based evaluation are specified. |
| Q6 | 2 | Agreement statistic and annotator overlap are reported. |
| Q7 | 2 | Multiple baselines, model sizes, and languages are compared. |
| Q8 | 1 | Three languages are tested, but repositories and domains remain limited. |
| Q9 | 2 | Tool grounding, SFT, and DPO interventions are clearly described. |
| Q10 | 1 | Compute and API costs are reported, but deployment latency is not central. |
| Q11 | 2 | Quality trade-offs and statistical comparisons are discussed. |
| Q12 | 2 | Human evaluation directly addresses generated-review quality. |

**Total: 22/24 — high confidence for synthesis, with judge and sample-size caveats.**

## 10. Review-process reliability and bias

- **Missing/uncertain data:** Full repository diversity, long-term adoption, accepted fixes, and production impact are not evaluated.
- **Judge dependence:** GPT-4o-mini supplies much of the training and automated evaluation signal, creating possible shared-model bias.
- **Selection uncertainty:** The human test set contains only 100 changes and three programming languages.
- **Attribution uncertainty:** Tool augmentation, SFT, and DPO are compared, but their individual causal contributions are not fully isolated.
- **Reproducibility:** Detailed tools and training sizes are reported, while proprietary API behavior and generated pseudo-references limit exact replication.
- **Extraction note:** The reported kappa values (0.65 in the main discussion and 0.7 in the appendix) need reconciliation before final use.

## 11. Synthesis-ready conclusion

- P107 provides strong evidence that static-analysis signals can serve as partial verifiers for training code-review generators.
- The central trade-off is explicit: preference optimization increases comprehensiveness and relevance while reducing conciseness.
- Human ratings broadly support the automated metric trends, and Python-trained models show promising transfer to Java and JavaScript.
- The study does not establish accepted-fix rates, developer productivity, or production reliability; use it for context grounding, evaluation design, and quality trade-offs.
- Before final submission, verify the preprint/venue relationship and reconcile the agreement-statistic discrepancy.

