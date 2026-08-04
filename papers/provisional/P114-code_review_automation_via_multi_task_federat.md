# P114 — Code Review Automation Via Multi-task Federated LLM: An Empirical Study

## 1. Identification

| Field | Value |
|---|---|
| Project ID | `P114` |
| Citation key | `p114_kumar2024_code_review_automation_via_mul` |
| Authors | Jahnavi Kumar; Sridhar Chimalakonda |
| Year | 2024 |
| Source | arXiv preprint, `2412.15676v1` |
| Study type | Federated fine-tuning and multi-task empirical study |

## 2. Screening

- **Scope decision:** Include as supporting evidence for privacy-preserving training, task coupling, and multi-task trade-offs.
- **Tasks:** Review-necessity prediction (RNP), review-comment generation (RCG), and code refinement (CR).
- **Evidence boundary:** The study evaluates model metrics on a simulated federated split; it does not evaluate human usefulness, privacy leakage, or production adoption.
- **Metadata caveat:** Publisher/duplicate status and the provisional BibTeX record require verification.

## 3. Study overview

The study fine-tunes an open LLaMA-3 8B model with LoRA in a federated-learning simulation over the CodeReviewer multi-language dataset. Clients share adapters rather than source code. RQ1 trains separate FedLLMs for RNP, RCG, and CR; RQ2 compares five multi-task strategies: sequential, parallel, and cumulative variants. Metrics include precision/recall/F1 for RNP and C-BLEU, METEOR, and ROUGE-L for generation/refinement. The study reports more than 2,600 wall-clock GPU hours and investigates performance on heterogeneous unseen-project splits.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Federated fine-tuning improves task-specific models, especially for low-data clients; reported gains include 18% F1 for RNP, 3% ROUGE-L for RCG, and 53% ROUGE-L for CR. | Reported | RQ1; conclusion |
| RQ2 | Sequential multi-task training suffers catastrophic forgetting, while cumulative fine-tuning performs better than several alternatives. | Reported | RQ2; Tables 7–12 |
| RQ3 | The three tasks are coupled conceptually, but generation/refinement quality and classification performance can interfere during shared training. | Inferred | RQ2 analysis |
| RQ4 | Federated clients retain local code and exchange LoRA adapter weights; task data are separated by client/project. | Reported | Sections 2–3 |
| RQ5 | Federated aggregation, LoRA, cumulative training, and separate task models mitigate privacy and data-silo constraints. | Reported | Method/results |
| RQ6 | Unseen-project splits and task metrics provide model evaluation, but privacy guarantees and human comment evaluation are not measured. | Limitation | Experimental design |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Catastrophic forgetting | Later task training degrades performance on earlier tasks. | Measured/observed | RQ2 |
| Weak comment generation | Generated comment has low lexical/semantic metric scores or fails to identify a useful issue. | Measured by C-BLEU/METEOR/ROUGE-L | RQ1–RQ2 |
| Failed refinement | Model outputs unchanged or incorrect code rather than implementing the review. | Anecdotal/evaluated | T3 examples |
| Review-necessity error | Model incorrectly predicts whether a patch needs review. | Measured by precision/recall/F1 | T1 |
| Privacy assumption gap | Sharing model weights may still leave unmeasured leakage or inference risks. | Threat | Federated design |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Review necessity | Precision, recall, and F1 for binary RNP | Best federated round reaches 49% precision, 62% recall, 55% F1 in reported analysis. | Table 3/Section 5.1 |
| Comment generation | C-BLEU, METEOR, ROUGE-L | Best RCG federated round reports 0.6 C-BLEU, 9.2 METEOR, 10.9 ROUGE-L. | Table 3 |
| Code refinement | C-BLEU, METEOR, ROUGE-L | Best CR federated round reports 74.58 C-BLEU, 84.54 METEOR, 87.47 ROUGE-L. | Table 3 |
| Multi-task stability | Compare sequential, parallel, and cumulative models | Sequential training exhibits catastrophic forgetting; cumulative variants are stronger. | Tables 7–12 |
| Generalization | Heterogeneous client/project split and unseen-project test | Supports silo/generalization analysis, but does not prove cross-organization robustness. | Section 3.1 |
| Privacy/efficiency | Federated data locality, adapter exchange, and wall-clock training | Privacy is architectural rather than empirically audited; training exceeds 2,600 wall-clock hours. | Sections 1–3 |

## 7. Mitigation and trade-offs

- **Mitigation family:** Federated learning, LoRA/PEFT, cumulative fine-tuning, and task-specific models.
- **Intervention point:** Data-sharing architecture and training schedule.
- **What it reduces:** Direct exposure of proprietary code and weak performance from isolated low-data clients.
- **Useful feedback potentially lost:** Multi-task optimization can sacrifice task-specific comment quality when shared representations forget prior tasks.
- **Coverage:** Collaborative clients can broaden training data, but the study simulates clients and does not test real organizational heterogeneity.
- **Human escalation:** No human review or escalation policy is evaluated; generated comments/refinements require external checking.
- **Cost:** Federated rounds, repeated fine-tuning, and multi-task experiments are computationally expensive.
- **New failure modes:** Adapter aggregation conflicts, catastrophic forgetting, client imbalance, and privacy leakage through model updates.

## 8. Annotation and evaluator validity

- **Dataset:** CodeReviewer data span nine programming languages and are partitioned by project/client to approximate siloed data.
- **Evaluation:** Automated task metrics are used; no new human labeling of generated comment quality is reported.
- **Metric limitation:** BLEU, METEOR, and ROUGE-L are proxies for generation similarity and may not capture defect correctness or actionability.
- **Generalization check:** Unseen-project splits are useful, but real private repositories and institutional privacy attacks are absent.
- **Reproducibility:** LLaMA-3, LoRA, federated aggregation, task definitions, and substantial compute are described; exact operational settings still require verification.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Two research questions and three tasks are explicit. |
| Q2 | 2 | Multi-language CodeReviewer data and client split are described. |
| Q3 | 2 | LoRA, FedAvg, task schedules, and baselines are detailed. |
| Q4 | 2 | Classification and generation metrics are reported. |
| Q5 | 1 | Automated reference metrics only; no human comment rubric. |
| Q6 | 0 | No inter-rater agreement or privacy audit. |
| Q7 | 2 | Individual, sequential, parallel, and cumulative strategies are compared. |
| Q8 | 1 | Unseen projects help, but federated setup is simulated. |
| Q9 | 2 | Privacy-aware architecture and training mitigations are explicit. |
| Q10 | 1 | Compute cost is reported, but deployment efficiency is limited. |
| Q11 | 2 | Catastrophic forgetting and task interference are analyzed. |
| Q12 | 1 | Relevant automation evidence, but limited alignment with human review outcomes. |

**Total: 18/24 — moderate confidence for federated/multi-task training evidence; weak for privacy and review usefulness.**

## 10. Review-process reliability and bias

- **Privacy claim limitation:** Federated training avoids direct data sharing but does not by itself establish formal privacy or resistance to update leakage.
- **Simulation bias:** Two-client/project partitioning may not reflect real organizations, client imbalance, or network constraints.
- **Metric bias:** Text-overlap metrics can reward reference imitation without detecting useful or correct comments.
- **Task interference:** The best schedule is data/model-dependent; catastrophic forgetting makes a single universal model unreliable.
- **Compute bias:** More than 2,600 wall-clock hours limits practical replication and may favor resource-rich settings.
- **Missing outcomes:** No expert review, accepted fixes, developer trust, or production latency/adoption is measured.

## 11. Synthesis-ready conclusion

- P114 supports federated fine-tuning as a plausible way to learn from siloed code without directly centralizing source data.
- Task-specific federated models can outperform vanilla models, but multi-task training introduces a clear stability–integration trade-off.
- Sequential training is vulnerable to catastrophic forgetting; cumulative or separate-task strategies are safer in the reported setting.
- Privacy architecture must be evaluated separately from model performance, and automated text metrics are insufficient for comment usefulness.
- Use as supporting evidence for privacy-aware training and multi-task trade-offs, not as evidence of secure or human-validated review automation.

