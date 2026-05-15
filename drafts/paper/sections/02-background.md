# Background and Motivation

The introduction framed LLM-generated code review evaluation as a decision-oriented trade-off problem. This section defines the concepts needed for the taxonomy, framework, and empirical design. It focuses on the terms that recur throughout the paper: generated review comments, problematic comments, context quality, mitigation decisions, dataset validity, evaluator validity, and evaluation trade-offs.

## Key Concepts

We use **modern code review** to refer to the lightweight, asynchronous, and tool-mediated process in which developers submit code changes, reviewers inspect them, and discussion continues until the change is accepted, revised, or abandoned [@p37_sadowski2018_google_mcr; @p38_bacchelli2013_expectations_mcr; @p51_davila2021_mcr_slr_taxonomy]. We treat this process as a socio-technical practice, not only as a defect-detection activity.

A **generated review comment** is a natural-language review comment produced by an automated system, often an LLM-based or LLM-assisted review system, for a code change under review. It may point to a defect, request a refactoring, ask for clarification, suggest a fix, or raise a maintainability, design, testing, security, or process concern. In this paper, generated comments are treated as workflow interventions rather than merely as text outputs.

A **problematic generated review comment** is an umbrella concept for generated comments that may harm, weaken, or fail to support the review process. This includes comments that are incorrect, unsupported, irrelevant, linked to the wrong location, non-actionable, misleading, low-value, or useful only after rewriting or escalation. The operational taxonomy developed later turns this broad definition into concrete labels, decision rules, and examples.

**Context quality** refers to whether the information available to the generator, verifier, annotator, or evaluator is sufficient, relevant, and coherent enough to judge a comment. The relevant context may include the local diff, surrounding code, project-level conventions, specifications, documentation, issue descriptions, previous review discussion, runtime assumptions, or retrieved evidence.

A **mitigation decision** is the action taken before a generated comment reaches the user. We focus on four decision types: show the comment, suppress it, rewrite it, or escalate it for human review. These decisions create trade-offs because reducing noisy or unsupported comments can also remove weak but useful review signals.

**Dataset validity** refers to whether an evaluation instance contains a review-relevant, contextually judgeable, and correctly linked target. An instance can be invalid or weak if the reference comment is unclear from the provided context, does not ask for a code-review-relevant action, was ignored by the later code revision, or is linked to the wrong code [@p52_tufano2021_automating_code_review_activities; @p53_tufano2024_code_review_automation_strengths_weaknesses].

**Evaluator validity** refers to whether the evaluation method reliably measures the intended dimension. Human evaluators can disagree or apply labels inconsistently, while LLM-based evaluators can be sensitive to prompts, answer order, verbosity, model choice, and task framing [@m04_zheng2023_llm_judge; @p29_wang2025_human_evaluators; @p31_jiang2025_codejudgebench; @p32_zhao2026_bias_loop; @p33_he2025_llmjudge_se].

Together, these concepts separate four concerns that are often conflated: whether the evaluation instance is valid, whether the generated comment is grounded and useful, what action should be taken on the comment, and whether the evaluator is reliable. Table \ref{tab:key-concepts} summarizes these concepts and their role in the rest of the paper.

<!-- table: caption="Key concepts used in the proposed taxonomy and evaluation design." label="tab:key-concepts" -->
| Concept | Meaning in this paper | Why it matters for evaluation |
| --- | --- | --- |
| Generated review comment | Automated natural-language review feedback for a code change. | It is the artifact being judged and may affect the review workflow. |
| Problematic generated review comment | Umbrella term for comments that are wrong, unsupported, irrelevant, non-actionable, low-value, or uncertain. | It defines the scope that the operational taxonomy later makes concrete. |
| Context quality | Sufficiency, relevance, and coherence of the information available to judge a comment. | It determines whether a comment is grounded, unsupported, or impossible to judge. |
| Mitigation decision | The action taken on a generated comment: show, suppress, rewrite, or escalate. | It turns evaluation from passive scoring into a workflow decision. |
| Dataset validity | Whether an evaluation instance is review-relevant, judgeable, and correctly linked. | It separates model failures from invalid or misleading evaluation targets. |
| Evaluator validity | Whether the human or LLM-based evaluator reliably measures the intended dimension. | It keeps measurement bias separate from comment quality. |

## Why Generated Review Comments Are Difficult to Evaluate

Generated review comments are difficult to evaluate because there is rarely a single correct comment for a code change. Human reference comments are useful, but they are incomplete and noisy. Reviewers may focus on different issues, express feedback at different levels of detail, or leave no comment even when a change has reviewable concerns. A generated comment can therefore be useful without matching a reference comment in wording or location [@p01_lu2025_deepcrceval; @p08_liu2025_too_noisy; @p18_bensghaier2025_curated_reviews; @p52_tufano2021_automating_code_review_activities; @p53_tufano2024_code_review_automation_strengths_weaknesses].

The reverse is also true. A generated comment can look fluent and relevant while being unsupported by the available context. It may infer a bug that is not present, cite a missing condition that is actually handled elsewhere, suggest an invalid fix, or point to the wrong location. Such comments can consume reviewer attention and reduce trust in the assistant [@p02_tantithamthavorn2026_hallujudge; @p35_mcaleese2024_llm_critics].

Usefulness is not identical to correctness. A correct comment can be too vague, too minor, or too hard to act on. A partially grounded comment may still be useful if it highlights a real uncertainty that should be checked. A comment may be unsuitable to show directly but useful after rewriting, routing, or escalation to a human reviewer. These cases are difficult to capture with binary labels such as correct/incorrect or accepted/rejected [@p10_sun2025_bitsai_cr; @p19_nguyen2025_fine_grained_classification; @p39_bosu2015_useful_reviews; @p53_tufano2024_code_review_automation_strengths_weaknesses].

Dataset validity adds another difficulty. In a generation failure, the model produces a poor comment for an otherwise valid evaluation instance. In a dataset-validity problem, the instance itself may not support a reliable judgment. Prior code review automation work shows that mined review data can contain comments that are unclear from the available context, comments that do not ask for a change, comments that were ignored by the later code revision, and comments linked to the wrong code [@p52_tufano2021_automating_code_review_activities; @p53_tufano2024_code_review_automation_strengths_weaknesses]. Such cases can distort both training and evaluation because the target itself may not represent a valid or judgeable review action.

Evaluator validity is also a concern. Manual evaluation is expensive, but LLM-as-a-Judge is not a neutral replacement for human judgment. LLM-based evaluators can scale assessment and reduce manual effort, yet their judgments can depend on prompts, answer order, model choice, verbosity, and task framing. For this reason, LLM-as-a-Judge should be treated as a measurement instrument that needs calibration and validation, not as ground truth [@m04_zheng2023_llm_judge; @p29_wang2025_human_evaluators; @p31_jiang2025_codejudgebench; @p32_zhao2026_bias_loop; @p33_he2025_llmjudge_se].

## Evaluation Trade-Offs

The concepts above lead to a set of recurring trade-offs. A filter that removes unsupported comments may reduce hallucinations, but it may also remove uncertain comments that would have been useful to a reviewer. A retrieval component may improve grounding, but it can increase latency, cost, and context noise. A relevance filter may reduce reviewer burden, but it may also reduce review coverage. A context-quality gate may avoid unreliable automatic review in low-context cases, but it can also increase human escalation.

Evaluation should therefore ask three linked questions. First, is the instance valid and judgeable under the available context? Second, is the generated comment useful enough to preserve in some form? Third, what mitigation decision should follow: show, suppress, rewrite, or escalate? These questions connect error reduction to useful-feedback preservation, cost, workflow impact, dataset validity, and evaluator validity.

This framing leads to the two core artifacts developed in the next sections: an operational taxonomy of problematic generated review comments, and a trade-off-aware evaluation design for comparing mitigation strategies on shared review instances.
