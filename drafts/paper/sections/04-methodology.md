# Methodology

This study uses a framework-oriented focused evidence synthesis, supported by an illustrative empirical evaluation of representative mitigation strategies. The goal is not to conduct an exhaustive systematic literature review, build a new leaderboard benchmark, or identify a universally best code-review assistant. Instead, the method is designed to answer a narrower question: how can problematic LLM-generated code review comments be identified, categorized, and evaluated together with the costs and trade-offs of reducing them?

The study has two connected layers. The first layer synthesizes evidence from prior work to derive an operational taxonomy of problematic comments and a trade-off-aware evaluation framework. The second layer applies the taxonomy and framework to a small annotated evidence layer in which several representative mitigation strategies are compared on the same sample. This empirical layer is intended to make the framework concrete and test whether the labels and trade-off dimensions can be applied consistently. It should not be interpreted as a broad claim about model superiority.

This framing follows the initial research goal of comparing error-reduction strategies while keeping the scope controlled. The comparison is not a search for one winning strategy across all conditions. Rather, it asks which kinds of problematic comments each strategy reduces, which useful comments it may remove, how much review coverage it preserves, and what human or computational cost it introduces.

## Study Design

The methodology consists of four parts:

1. a focused evidence synthesis over a curated paper pool;
2. construction of an operational taxonomy of problematic generated review comments;
3. design of a trade-off-aware evaluation framework;
4. an illustrative annotated study comparing representative mitigation strategies.

The evidence synthesis provides the conceptual basis for the taxonomy, evaluation dimensions, and mitigation categories. The annotated study provides a concrete test of the framework on generated review comments. The two layers are intentionally connected: the literature synthesis identifies what should be measured, while the annotated study shows how these dimensions can be measured and where trade-offs appear in practice.

The unit of analysis is a generated review comment for a code change under review. Each instance may include the code diff, surrounding code or project context where available, textual context such as a commit message or pull-request description, the generated comment, and any mitigation output produced before the comment is shown to a developer.

## Research Questions

The study is guided by five research questions.

<!-- table: caption="Research questions and expected outputs." label="tab:methodology-rqs" -->
| RQ | Question | Expected output |
| --- | --- | --- |
| RQ1 | What types of problematic comments occur in LLM-generated code review? | Operational taxonomy and label definitions. |
| RQ2 | Which mitigation strategies reduce which types of problematic comments? | Strategy-by-failure-type comparison. |
| RQ3 | What trade-offs do mitigation strategies introduce in useful-feedback preservation, review coverage, human effort, and computational cost? | Trade-off matrix and metric definitions. |
| RQ4 | How does context quality affect the occurrence, detection, and mitigation of problematic comments? | Context-quality layer and context-failure analysis. |
| RQ5 | How can these signals be integrated into a framework for show, suppress, rewrite, or escalate decisions? | Trade-off-aware evaluation framework. |

RQ1 and RQ4 are primarily supported by the evidence synthesis and annotation labels. RQ2 and RQ3 require the illustrative empirical comparison. RQ5 integrates both layers into the final framework.

## Paper Selection and Coding

The evidence synthesis is based on a curated paper pool maintained in `matrices/paper-pool.md`. The pool includes core work on LLM-based code review, automated review-comment generation, hallucination and grounding, context-aware review, production review assistants, benchmark construction, data curation, human-centered code review, static-analysis-guided feedback, secure review, and LLM-as-a-Judge evaluation.

A paper is included when it provides evidence for at least one of the following concerns: evaluation of generated review comments, problematic comment types, context quality, review-comment usefulness, mitigation or filtering mechanisms, human or production feedback, data and reference quality, cost and workflow impact, or evaluator validity. A paper is excluded when it focuses only on general code generation, program repair, or model performance without evidence relevant to review-comment evaluation.

Each paper is coded using the repository analysis template in `templates/paper-analysis-template.md`. For each paper, we extract the study type, contribution type, dataset or evaluation setting, input context, generated or evaluated artifact, evaluation metrics, human or automated judging protocol, reported limitations, observed or implied failure types, context-quality assumptions, mitigation strategies, cost or workflow indicators, and evidence relevant to the research questions.

To avoid overstating the evidence, extracted claims are marked using interpretation labels. `Reported` means the paper states the claim explicitly. `Inferred` means the claim is reconstructed from examples, tables, results, or study design. `Our perspective` means the claim is part of our synthesis or critique. This distinction is important because the framework combines evidence reported by prior work with analytical interpretation across studies.

## Cross-Paper Synthesis

After individual coding, papers are compared across recurring dimensions rather than summarized one by one. The synthesis asks what each line of work evaluates, what context it assumes, what failure types it exposes, what mitigation decision it supports, what cost or workflow effect it measures, and what validity risks remain.

The cross-paper synthesis proceeds in three steps. First, we identify recurring evaluation dimensions such as correctness, relevance, grounding, usefulness, actionability, specificity, review coverage, cost, human effort, workflow impact, and evaluator validity. Second, we identify recurring problematic-comment types such as unsupported claims, hallucinated issues, irrelevant comments, wrong-location comments, incorrect technical assumptions, invalid fix suggestions, non-actionable comments, low-value comments, and context-dependent cases. Third, we identify missing links between dimensions, especially cases where prior work measures error reduction but not useful-feedback preservation, or evaluates generated comments without evaluating context quality or evaluator reliability.

The output of this synthesis is a set of framework layers that connect input and context quality, generated-comment quality, problematic-comment type, usefulness and actionability, mitigation decision, cost and workflow impact, dataset validity, and evaluator validity.

## Taxonomy Construction

The operational taxonomy is derived from three sources: failure types explicitly reported in prior work, failure types inferred from examples and evaluation rubrics, and failure types needed to analyze mitigation trade-offs. The taxonomy is operational because each category is intended to support annotation, not only conceptual discussion.

Each taxonomy category should include a definition, inclusion criteria, exclusion criteria, ambiguous cases, and likely mitigation decisions. For example, an unsupported comment may be suppressed if it makes a strong claim without evidence, rewritten if it contains a useful but overstated concern, or escalated if it raises a potentially important issue that cannot be judged with the available context. Similarly, a low-value comment may be technically correct but still not worth showing if it consumes reviewer attention without improving the review outcome.

The taxonomy separates problematic-comment types from evaluation dimensions. Grounding, correctness, usefulness, and actionability are evaluation dimensions. Unsupported claims, incorrect technical assumptions, wrong-location comments, and non-actionable comments are failure types. This separation allows the analysis to capture cases where a comment is correct but low-value, useful but weakly grounded, or relevant but not directly actionable.

## Mitigation Strategies

The empirical layer compares a small set of representative mitigation strategies. The set is intentionally limited so that the study remains feasible and the same samples can be evaluated across strategies. The initial strategies are:

<!-- table: caption="Representative mitigation strategies used in the illustrative comparison." label="tab:methodology-strategies" -->
| Strategy | Intervention point | Role in the study |
| --- | --- | --- |
| Baseline LLM reviewer | Generation time | Produces review comments using a fixed base prompt and the available input context. |
| Robust prompting | Generation time | Uses a more constrained prompt that asks the model to avoid unsupported claims and provide actionable comments. |
| Context-quality gate | Before generation or before evaluation | Skips, downgrades, or routes instances whose available context is insufficient, inconsistent, or difficult to judge. |
| Post-generation verification | After generation and before display | Checks generated comments for support, relevance, actionability, or risk before they are shown. |
| Hybrid gate plus verifier | Before and after generation | Combines context-quality gating with post-generation verification to examine whether the trade-off improves. |

Depending on data and implementation feasibility, a retrieval-augmented context strategy may be added as an optional strategy. If added, it should be treated as a context-enrichment strategy rather than as a separate model-comparison track. The study should keep the number of strategies small enough to support careful annotation and trade-off analysis.

## Data and Sample Selection

The study should use a dataset that contains, or can be linked to, code changes and review-relevant textual context. Candidate data sources include existing code review comment generation datasets, pull-request-level code review benchmarks, or code changes paired with commit messages, pull-request descriptions, and review discussions. The minimum requirement is that each instance should contain a code change and enough surrounding information to generate or evaluate a review comment.

If the selected dataset already includes generated comments, those comments may be used as candidate artifacts. If it does not, comments are generated using a fixed model, fixed decoding settings, and documented prompts. The same base sample should be used across mitigation strategies so that differences can be attributed to the strategy rather than to different input distributions.

A feasible initial study can use one primary dataset, one main generation model, a small number of representative strategies, and approximately 100--300 generated comments for human annotation. A smaller pilot sample should be labeled first to refine the taxonomy and annotation guideline. Any claims based on this sample should be framed as illustrative rather than broadly generalizable.

## Generation and Mitigation Procedure

For each selected code-change instance, the baseline system generates a review comment using a fixed prompt and input context. The robust-prompting strategy uses the same input but adds constraints intended to reduce unsupported, vague, or non-actionable comments. The context-quality gate evaluates whether the available input context is sufficient and coherent enough for review-comment generation or judgment. The post-generation verifier evaluates the generated comment before display. The hybrid strategy applies both context gating and post-generation verification.

The output of each strategy is mapped to one of the mitigation decisions used in the framework: show, suppress, rewrite, or escalate. `Show` means the comment is suitable to present as review feedback. `Suppress` means it should not be shown because it is harmful, unsupported, irrelevant, or too low-value. `Rewrite` means the comment contains a useful signal but should be clarified, softened, grounded, or made more actionable before display. `Escalate` means the comment raises a potentially important issue that requires human judgment or additional context.

All prompts, model settings, verifier rules, gating criteria, and retrieval settings, if any, should be documented. The settings should be fixed before running the final evaluation sample to avoid tuning on the evaluation data.

## Annotation Protocol

The annotation protocol is designed to evaluate both generated comments and mitigation decisions. The unit of annotation is a generated review comment together with the code change and available context. Annotators label the comment, the context, and the recommended mitigation decision.

The main labels include problematic-comment type, technical correctness, grounding, relevance, usefulness, actionability, value or severity, context quality, dataset validity, evaluator confidence, and mitigation decision. Labels should allow annotators to distinguish comments that are incorrect, unsupported, irrelevant, non-actionable, low-value, useful but not directly acceptable, or impossible to judge with the available context.

Before full annotation, annotators should label a pilot subset. The pilot is used to refine definitions, identify ambiguous cases, calibrate decision rules, and improve the annotation guideline. At least two annotators with software-engineering experience should label the pilot and a substantial subset of the final sample when feasible. Inter-annotator agreement should be reported for categorical labels using Cohen's kappa for two annotators or Krippendorff's alpha when the design includes missing labels or more than two annotators. Percentage agreement may be reported as a descriptive supplement, but it should not replace chance-corrected agreement.

Disagreements should be resolved through discussion or adjudication. The final annotation table should preserve the initial labels, resolved label, and disagreement reason where useful. This is especially important for borderline cases such as comments that are technically plausible but weakly grounded, correct but low-value, useful but not directly acceptable, or dependent on missing context.

## Metrics and Trade-Off Analysis

The study reports both error-reduction metrics and preservation metrics. Error-reduction metrics include the overall rate of problematic comments, the rate of each problematic-comment type, the rate of unsupported or hallucinated comments, the rate of irrelevant comments, the rate of non-actionable comments, and the rate of invalid fix suggestions. Preservation metrics include useful comments retained, useful comments wrongly suppressed, review coverage retained after filtering, comments rewritten rather than suppressed, and comments escalated to humans.

Cost and workflow metrics should also be reported where feasible. These include the number of model calls, approximate token cost, latency proxies, human verification effort, escalation rate, and the amount of review feedback removed by each strategy. These metrics are important because a strategy that reduces problematic comments may still be undesirable if it removes too much useful feedback, reduces coverage, or shifts too much effort to humans.

The analysis compares strategies by failure type and by trade-off dimension. A strategy should not be described as simply better because it removes more comments. It should be described in terms of what it removes, what it preserves, what it wrongly suppresses, what it escalates, and what cost it adds. This is the main reason the study separates technical correctness, usefulness, actionability, context quality, and mitigation decision.

## Reproducibility and Scope Control

To support reproducibility, the repository should include the paper pool, coding template, annotation guideline, evaluation schema, prompts, model settings, generated outputs where licensing permits, and metric-computation scripts. If proprietary models or closed datasets are used, the study should still document prompts, settings, sampling decisions, and annotation procedures as precisely as possible.

Several scope limits are intentional. The empirical layer is small and illustrative. It uses a limited number of datasets, models, and mitigation strategies. It is not designed to establish broad model rankings. Its purpose is to evaluate whether the taxonomy and framework reveal trade-offs that would be hidden by simple correctness, acceptance, or hallucination metrics.

The main threats to validity are incomplete paper selection, rapidly changing recent work, possible preprint changes, limited annotation sample size, annotator disagreement, sensitivity to prompt and model settings, and evaluator bias if LLM-as-a-Judge is used. These threats are mitigated by transparent inclusion criteria, explicit coding labels, pilot annotation, agreement reporting, preserved disagreement notes, fixed evaluation settings, and careful separation between reported evidence, inferred interpretation, and our own synthesis.
