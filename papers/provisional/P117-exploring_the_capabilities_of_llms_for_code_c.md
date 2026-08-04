# P117 — Exploring the Capabilities of LLMs for Code Change Related Tasks

## 1. Identification

| Field | Value |
|---|---|
| Project ID | `P117` |
| Citation key | `p117_fan2024_exploring_the_capabilities_of_` |
| Authors | Lishui Fan; Jiakun Liu; Zhongxin Liu; David Lo; Xin Xia; Shanping Li |
| Year | 2024 |
| Source | arXiv preprint, `2407.02824v1` |
| Study type | Broad empirical comparison of LLM prompting and PEFT |

## 2. Screening

- **Scope decision:** Include as supporting evidence for code-change representation, prompting, parameter-efficient fine-tuning, and model-size trade-offs.
- **Tasks:** Code-review generation, commit-message generation, and just-in-time comment update.
- **Evidence boundary:** The primary code-review metric is BLEU-4 against a reference comment; human evaluation is reported for commit-message generation rather than review comments.
- **Metadata caveat:** Publisher/duplicate status and the provisional BibTeX record require verification.

## 3. Study overview

The study compares open LLMs including InCoder, CodeGen, Llama 2, and Code Llama with CodeT5 and change-oriented CCT5 baselines. It evaluates in-context learning (ICL), LoRA, prefix-tuning, input formats, model size, and code-change categories across three tasks. Code-review generation uses 138,127 diff–review pairs from nine languages; commit-message generation uses 2.25 million commits across five languages; just-in-time comment update uses 98,622 Java instances. Paired bootstrap resampling is used for metric significance tests.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Without examples, LLM performance is poor; one example generally improves results, while additional examples do not always help. | Reported | RQ1 |
| RQ2 | LoRA generally outperforms prefix-tuning, and PEFT improves over ICL across code-change tasks. | Reported | RQ2 |
| RQ3 | LLM-PEFT can match or approach small change-oriented models, but comparisons depend on task and change type. | Reported | RQ3 |
| RQ4 | Diff inputs help ICL on JIT comment update; PEFT is less sensitive to input format. | Reported | RQ4 |
| RQ5 | Llama 2/Code Llama are consistently strong; LLM-PEFT benefits especially on documentation-only changes, while code changes remain harder. | Reported | RQ5 |
| RQ6 | Paired bootstrap tests and task metrics support model comparison, but review-comment usefulness is not directly human-validated. | Reported/limitation | Study design |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| No-example weakness | LLM produces poor review comments without demonstrations. | Measured | RQ1 |
| Example overload | More in-context examples do not consistently improve performance. | Measured | RQ1 |
| Change-understanding gap | General code pretraining does not fully capture differences between versions. | Motivation/finding | Introduction |
| Documentation bias | Models perform relatively better on comment/documentation-only changes than substantive code changes. | Reported | RQ5 |
| Reference mismatch | BLEU rewards overlap with a single review comment and may penalize valid alternatives. | Metric limitation | CRG evaluation |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Review-comment generation | BLEU-4 on diff–review pairs | Useful for comparison but weakly aligned with one-to-many review validity. | Section 2.1.1 |
| Commit-message generation | B-Norm/BLEU and human expressiveness/conciseness/adequacy | LLM-PEFT messages are reported as expressive and concise without large adequacy loss. | RQ5 |
| Comment update | GLEU and exact accuracy | Measures similarity to updated-comment references. | Section 2.1.3 |
| Prompt adaptation | ICL with varying example counts | One example often provides large gains; more examples can degrade or plateau. | RQ1 |
| Parameter adaptation | LoRA versus prefix-tuning | LoRA generally performs better. | RQ2 |
| Generalization | Language, input format, model size, and change-type comparisons | Larger models are not always better; code-specific changes remain difficult. | RQs 3–5 |

## 7. Mitigation and trade-offs

- **Mitigation family:** In-context examples, LoRA/PEFT, change-aware input formatting, and code-change-oriented pretraining.
- **Intervention point:** Prompt context, model parameters, and input representation.
- **What it reduces:** Weak zero-shot performance and mismatch between general code knowledge and code-change reasoning.
- **Useful feedback potentially lost:** Reference-overlap optimization may favor familiar wording over novel, correct review concerns.
- **Coverage:** Nine-language review data broaden scope, but substantive code-change reasoning remains weaker than documentation changes.
- **Human escalation:** The study does not define a reviewer escalation policy; human validation is still required for generated review comments.
- **Cost:** PEFT reduces trainable parameters, while long prompts and repeated examples increase context and inference cost.
- **New failure modes:** Prompt sensitivity, context-length limits, model-size misconceptions, and dataset/reference bias.

## 8. Annotation and evaluator validity

- **Datasets:** Large open-source datasets cover multiple languages and code-change tasks.
- **Metrics:** Paired bootstrap resampling supports statistical comparison across configurations.
- **Human evaluation:** Reported human evaluation focuses on commit-message quality, not the main code-review generation task.
- **Agreement:** No central inter-rater agreement statistic is reported in the extracted evidence.
- **Validity risks:** BLEU/GLEU/B-Norm and exact match are limited proxies for review correctness, issue coverage, and actionability.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Five research questions and task scope are explicit. |
| Q2 | 2 | Large multi-language datasets and task definitions are described. |
| Q3 | 2 | Models, ICL, PEFT, formats, and comparisons are detailed. |
| Q4 | 2 | Multiple automated metrics and bootstrap tests are reported. |
| Q5 | 1 | Human validation is limited and not centered on code-review comments. |
| Q6 | 0 | No formal review-comment agreement statistic. |
| Q7 | 2 | Broad model, tuning, format, and task comparisons. |
| Q8 | 2 | Multi-language, multi-dataset design supports breadth. |
| Q9 | 2 | Prompt and PEFT interventions are directly compared. |
| Q10 | 1 | PEFT/resource implications discussed, but operational cost is limited. |
| Q11 | 2 | Example count, input format, model size, and change-type effects analyzed. |
| Q12 | 1 | Relevant capability evidence, but weak alignment with human review utility. |

**Total: 19/24 — moderate-high confidence for capability and adaptation comparisons; limited for review quality.**

## 10. Review-process reliability and bias

- **Metric bias:** Reference-based text metrics can undercount valid alternative comments and overvalue lexical overlap.
- **Dataset bias:** Open-source datasets and existing review comments may not represent private repositories or modern reviewer workflows.
- **Task transfer:** Results from commit messages and comment updates do not automatically transfer to defect-oriented review.
- **Prompt confounding:** Example number, prompt length, and input format interact with context limits and model architecture.
- **Model comparison:** Parameter count alone is not a reliable proxy for code-change competence; family/pretraining differences matter.
- **Missing outcomes:** No reviewer acceptance, correctness judgment, latency, or downstream fix measurement for generated review comments.

## 11. Synthesis-ready conclusion

- P117 shows that code-change tasks require specialized adaptation beyond general code pretraining.
- One-shot examples and LoRA can substantially improve performance, but more context and larger models do not guarantee better results.
- Models perform relatively better on documentation-only changes than substantive code changes, supporting a gap around semantic change reasoning.
- The study is useful for capability and configuration trade-offs, but reference-based metrics cannot establish review-comment correctness or usefulness.
- Use as supporting evidence for prompt/PEFT design and code-change representation, not as human-validated review-quality evidence.

