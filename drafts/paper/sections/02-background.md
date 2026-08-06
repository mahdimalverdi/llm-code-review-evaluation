# Background and Motivation

A generated review comment can fail in several different ways. The comment may be wrong, the available context may be incomplete, the evaluation instance may be unjudgeable, or the evaluator may be unreliable. These failures should not be treated as the same problem. This section separates the concepts used in the review synthesis, taxonomy, annotation protocol, and evaluation framework.

The key distinction is between the comment, its context, the evaluation instance, the evaluator, and the subsequent workflow action. These objects can fail independently and therefore require separate definitions.

## Key Concepts

Modern code review is a lightweight, asynchronous, and tool-mediated process in which developers submit code changes, reviewers inspect them, and discussion continues until the change is accepted, revised, or abandoned [@p37_sadowski2018_google_mcr; @p38_bacchelli2013_expectations_mcr; @p51_davila2021_mcr_slr_taxonomy]. We treat it as a socio-technical practice, not only as a defect-detection activity. This matters because an automated review comment is not only judged as text; it is judged by how it affects that practice.

In this paper, a generated review comment is natural-language review feedback produced by an automated system, often an LLM-based or LLM-assisted one, for a code change under review. It may point to a defect, ask for clarification, suggest a fix, or raise a maintainability, design, testing, security, or process concern. The comment becomes problematic when it weakens the review process: for example, when it is incorrect, unsupported, irrelevant, linked to the wrong location, non-actionable, misleading, low-value, or useful only after rewriting or escalation. The taxonomy developed later turns this broad idea into concrete labels, decision rules, and examples.

Context quality asks whether we have enough relevant and coherent information to judge a comment fairly. A warning about a missing null check, for example, may look unsupported in the local diff but become reasonable once surrounding code, a runtime assumption, or a project convention is considered. The needed context may be local code, surrounding code, documentation, issue discussion, review history, runtime assumptions, or retrieved evidence.

A mitigation decision is an action taken before generated feedback reaches the user. The framework later specifies the available actions and the evidence needed to select among them.

Dataset validity asks whether the evaluation instance itself supports a fair judgment. Sometimes the problem is not the generated comment at all, but the target used to evaluate it. For example, if a mined reference comment is unclear from the provided context or linked to the wrong code, the model may look wrong even though the evaluation instance is the real problem. Prior code-review automation work shows that such cases occur in mined review data [@p52_tufano2021_automating_code_review_activities; @p53_tufano2024_code_review_automation_strengths_weaknesses].

Evaluator validity asks whether the evaluation method measures the intended dimension reliably. Human evaluators can disagree or apply labels inconsistently. LLM-based evaluators add another source of risk because their judgments can change with the prompt, answer order, verbosity, model choice, or task framing [@m04_zheng2023_llm_judge; @p29_wang2025_human_evaluators; @p31_jiang2025_codejudgebench; @p32_zhao2026_bias_loop; @p33_he2025_llmjudge_se].

Figure \ref{fig:evaluation-pipeline-concepts} locates these concepts in the evaluation pipeline. Its purpose is diagnostic: an observed error in the final score may originate in the generated comment, but it may also originate upstream in the instance or downstream in the judging procedure.

<!-- figure: path="figures/evaluation-pipeline-concepts.png" caption="Conceptual pipeline for evaluating LLM-generated code review comments. The generated comment is only one part of the evaluation problem: dataset validity, context quality, evaluator validity, and mitigation trade-offs can each affect the final decision." label="fig:evaluation-pipeline-concepts" width="0.95\linewidth" -->

## Why Generated Review Comments Are Difficult to Evaluate

Generated review comments are difficult to evaluate because there is rarely a single correct comment for a code change. Human reference comments are useful, but they are incomplete and noisy. Reviewers may focus on different issues, express feedback at different levels of detail, or leave no comment even when a change has reviewable concerns. A generated comment can therefore be useful without matching a reference comment in wording or location [@p01_lu2025_deepcrceval; @p08_liu2025_too_noisy; @p18_bensghaier2025_curated_reviews; @p52_tufano2021_automating_code_review_activities; @p53_tufano2024_code_review_automation_strengths_weaknesses].

There is also a quieter failure mode: a generated comment can sound fluent and relevant while having no support in the available context. It may infer a bug that is not present, assume a missing condition that is actually handled elsewhere, propose a fix that does not apply, or point the reviewer to the wrong location. Such comments can consume reviewer attention and reduce trust in the assistant [@p02_tantithamthavorn2026_hallujudge; @p35_mcaleese2024_llm_critics].

Usefulness and correctness describe different properties. Correct feedback can be too vague or minor to assist a reviewer, whereas an uncertain observation can still prompt a worthwhile check. Binary correct/incorrect or accepted/rejected labels obscure these cases [@p10_sun2025_bitsai_cr; @p19_nguyen2025_fine_grained_classification; @p39_bosu2015_useful_reviews; @p53_tufano2024_code_review_automation_strengths_weaknesses].

A third difficulty comes from the evaluation instance itself. In a generation failure, the model produces a poor comment for an otherwise valid instance. In a dataset-validity problem, the instance itself may not support a reliable judgment. Prior code-review automation work shows that mined review data can include comments that are unclear from the available context, comments that do not ask for a change, ignored comments, and comments linked to the wrong code [@p52_tufano2021_automating_code_review_activities; @p53_tufano2024_code_review_automation_strengths_weaknesses]. Such cases can distort both training and evaluation because the target itself may not represent a valid or judgeable review action.

Evaluator behavior introduces a fourth difficulty. LLM-based assessment reduces some manual effort, but reported judgments vary with prompts, answer order, model choice, verbosity, and task framing [@m04_zheng2023_llm_judge; @p29_wang2025_human_evaluators; @p31_jiang2025_codejudgebench; @p32_zhao2026_bias_loop; @p33_he2025_llmjudge_se]. These sensitivities become part of construct validity whenever judge outputs support a performance claim.

These distinctions provide the vocabulary used by the taxonomy and the evaluation framework developed later in the paper.
