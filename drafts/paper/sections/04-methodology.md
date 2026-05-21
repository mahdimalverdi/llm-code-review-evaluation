# Methodology

This section specifies a bounded empirical protocol for evaluating mitigation strategies for problematic LLM-generated code review comments. The aim is narrower than a general survey of LLMs for software engineering and different from a leaderboard-style benchmark. Rather than ranking models, the study asks how different mitigation strategies change the fate of generated review comments that may be unsupported, irrelevant, non-actionable, low-value, or otherwise risky to show.

The central methodological concern is trade-off-aware evaluation. A mitigation strategy may reduce problematic comments, but it may also suppress weak yet useful feedback, reduce automatic review coverage, increase latency, or shift additional work to human reviewers. For this reason, the study evaluates mitigation not as a single success/failure outcome, but as a set of linked decisions involving error reduction, useful-feedback preservation, review coverage, human effort, computational cost, and evaluator validity.

The study follows a bounded empirical-software-engineering design. The research questions, units of analysis, comparison conditions, annotation constructs, reliability checks, scope limits, and reproducibility artifacts are specified before the final analysis [@m05_paulralph2020]. Because the evaluated systems use LLMs, the design treats model versions, prompts, context construction, verifier behavior, human validation, and limitations as methodological objects that must be reported rather than as incidental implementation details [@m06_sebastianbaltes2025].

The literature synthesis and taxonomy serve as design inputs for the empirical protocol. They define the failure categories, evaluation dimensions, and representative mitigation families used in the comparison. The main object of analysis is a paired comparison: the same review instances are processed under a bounded set of mitigation strategies, the resulting comments and decisions are annotated, and the strategies are compared through both error-reduction and useful-feedback-preservation measures.

At this draft stage, execution-specific fields such as dataset identity, search counts, prompt text, thresholds, annotator background, and agreement statistics are treated as protocol commitments. In the final manuscript, these placeholders must be replaced with executed-study details before the work is presented as a completed empirical study. If any of these fields cannot be completed, the corresponding claim is reported as exploratory and the limitation is stated before the results are interpreted.

## Study Design

The study is organized into six connected stages:

1. conducting a targeted literature review to identify failure categories, evaluation dimensions, mitigation families, and evaluator-validity risks;
2. constructing and pilot-refining an operational taxonomy of problematic generated review comments;
3. selecting a shared evaluation sample with enough code and textual context for human judgment;
4. fixing the generation, gating, verification, rewriting, and escalation rules before final execution;
5. applying the compared strategies to the same review instances wherever feasible;
6. annotating the resulting comments and decisions, then analyzing mitigation trade-offs.

Figure \ref{fig:methodology-protocol-overview} summarizes this sequence and shows how the design moves from evidence synthesis to a paired trade-off analysis on shared review instances.

<!-- figure: path="figures/methodology_protocol_overview.tex" caption="Overview of the bounded empirical protocol used to evaluate mitigation strategies for problematic LLM-generated code review comments." label="fig:methodology-protocol-overview" -->

The study uses two related units of analysis. The **review instance** is the unit for coverage, escalation, context-quality, and cost analysis. A review instance contains a code change and, where available, review-relevant textual context such as a commit message, pull-request description, issue description, previous discussion, surrounding code, or retrieved project context. The **generated review comment** is the unit for comment-quality, failure-type, usefulness, actionability, and grounding analysis. This distinction is necessary because some strategies may produce no comment for an instance and instead suppress, defer, or escalate it.

The same base review instances are used across strategies so that observed differences are attributable to the mitigation strategy rather than to different input distributions. This unit structure is consistent with prior work on generated review comments, pull-request-level review benchmarks, context-enriched review datasets, and code-review automation datasets [@p01_lu2025_deepcrceval; @p04_kumar2026_swe_prbench; @p05_zeng2025_swrbench; @p06_hu2025_contextcrbench; @p14_li2022_codereviewer; @p52_tufano2021_automating_code_review_activities].

The empirical scope is intentionally bounded. The initial version uses one primary dataset, one main generation model, fixed prompts and settings, a limited set of representative mitigation strategies, and a few hundred annotated comments. This scope is chosen to make the comparison interpretable. The study is not intended to rank all review models or generalize across all programming languages, repositories, or review workflows.

## Research Questions

The research questions follow the trade-off structure of the study. RQ1 defines the failure space. RQ2 compares mitigation effects by failure type. RQ3 measures the preservation, coverage, escalation, and cost side of mitigation. RQ4 treats context quality as an exploratory moderator rather than as a primary causal claim.

<!-- table: caption="Research questions, priority, and expected outputs." label="tab:methodology-rqs" -->
| RQ | Priority | Question | Expected output |
| --- | --- | --- | --- |
| RQ1 | Primary | What types of problematic comments occur in LLM-generated code review under the selected evaluation setting? | Distribution of problematic-comment types, examples, and refined taxonomy labels. |
| RQ2 | Primary | Which mitigation strategies reduce or reroute which types of problematic comments? | Strategy-by-failure-type comparison and decision-confusion analysis. |
| RQ3 | Primary | How do mitigation strategies affect useful-feedback preservation, review coverage, human escalation, and execution cost? | Trade-off matrix and preservation, coverage, escalation, and cost metrics. |
| RQ4 | Exploratory | How does context quality or context inconsistency appear to affect mitigation behavior and annotation difficulty? | Context-quality subgroup summaries, disagreement patterns, and qualitative examples. |

RQ1 is analyzed before comparing strategies so that the study first establishes what kinds of failures appear in the sample. RQ2 and RQ3 form the core paired comparison. The hybrid strategy, if included, is evaluated under RQ2 and RQ3 rather than promoted to a separate primary research question. RQ4 is interpreted conservatively, especially if the number of low-context or inconsistent-context instances is small.

## Targeted Literature Review and Initial Operationalization

The empirical comparison starts from a targeted review of closely related work. This review is not presented as a full systematic literature review. Its purpose is more specific: to make the empirical design traceable by identifying the failure types, evaluation dimensions, mitigation families, and methodological risks that the study must operationalize. The procedure therefore uses explicit search and selection records, but it is scoped to the design needs of this study rather than to exhaustive coverage of all LLM-for-software-engineering research [@m08_claeswohlin2020; @m09_claeswohlin2023].

The review begins from seed studies that directly inform the study design. One group contributes review-specific evaluation rubrics and benchmarks [@p01_lu2025_deepcrceval; @p04_kumar2026_swe_prbench; @p05_zeng2025_swrbench; @p06_hu2025_contextcrbench]. A second group informs grounding, context use, retrieval, specification grounding, and static-analysis-guided review [@p02_tantithamthavorn2026_hallujudge; @p11_zhang2025_laura; @p12_wang2025_sgcr; @p16_icoz2026_context_aware; @p20_hong2025_rag_reviewer; @p22_jaoua2025_static_analyzers]. A third group informs workflow value, industrial filtering, human-AI review interaction, data quality, reference quality, and evaluator validity [@p03_tantithamthavorn2026_rovodev; @p07_olewicki2024_revmate; @p10_sun2025_bitsai_cr; @p26_zhong2026_human_ai_synergy; @p28_heander2025_support_not_automation; @p08_liu2025_too_noisy; @p18_bensghaier2025_curated_reviews; @p29_wang2025_human_evaluators; @p31_jiang2025_codejudgebench; @p33_he2025_llmjudge_se; @p36_li2024_llms_as_judges].

Additional studies are added only when they contribute evidence to at least one design component: a failure category, context-quality dimension, mitigation decision, annotation label, evaluation metric, workflow cost, or evaluator-validity risk. Studies are excluded when they address general code generation, program repair, or model performance without evidence relevant to generated review-comment evaluation.

To keep this targeted review auditable, the executed study records the metadata in Table \ref{tab:methodology-review-protocol}. These fields are not intended to turn the review into a full systematic mapping study; they make the design choices inspectable and reduce the risk of cherry-picking.

<!-- table: caption="Targeted-review reporting fields." label="tab:methodology-review-protocol" -->
| Field | Required report in the executed study |
| --- | --- |
| Search sources | Digital libraries, search engines, and seed-paper snowballing sources used for the targeted review. |
| Search date | Date or date range when the search was last executed. |
| Seed papers | Initial studies used to start the targeted review, grouped by design role. |
| Search strings | Query strings or keyword families used for LLM code review, review-comment evaluation, hallucination, grounding, context, filtering, and LLM-as-a-Judge. |
| Inclusion criteria | Evidence relevance to failure types, context quality, mitigation strategies, annotation labels, metrics, workflow cost, or evaluator validity. |
| Exclusion criteria | Generic code generation, program repair, or model-performance papers without review-comment evaluation evidence. |
| Selection counts | Number of initially identified, screened, excluded, and included studies. |
| Stopping rule | Saturation point or snowballing rule used to stop adding papers. |

The final manuscript reports the actual values for all fields in Table \ref{tab:methodology-review-protocol}. If a field cannot be reconstructed, the review is described as a transparent targeted review rather than as systematic evidence, and the missing field is reported as a threat to validity. No paper is added to the evidence base after final annotation begins unless the addition is logged and the affected design choice is explicitly rechecked.

For each included paper, the extraction records the evaluated artifact, input context, model or system setting, evaluation dimensions, failure types, mitigation mechanisms, human or automated judging protocol, cost or workflow indicators, and stated limitations. During extraction, reported evidence is separated from study interpretation. This distinction matters because some constructs used in this paper, such as useful-feedback preservation or decision-level mitigation, are synthesized across papers rather than always named directly by the original studies.

The review produces the initial operational vocabulary used in the rest of the study. Candidate failure labels include unsupported or hallucinated comments, irrelevant comments, wrong-location comments, incorrect technical claims, invalid fix suggestions, false positives, non-actionable comments, low-value comments, and context-dependent cases. These labels are grounded in prior review-comment evaluation, hallucination, data-quality, and comment-classification work [@p01_lu2025_deepcrceval; @p02_tantithamthavorn2026_hallujudge; @p08_liu2025_too_noisy; @p18_bensghaier2025_curated_reviews; @p19_nguyen2025_fine_grained_classification; @p41_widyasari2025_explaining_explanations]. The same review also identifies strategy families by intervention point: before generation, during generation, after generation, and before display to the user.

## Operational Taxonomy Construction

The taxonomy is built as an annotation instrument, not only as a conceptual classification. Its purpose is to help annotators decide whether a generated comment is problematic, what kind of problem it contains, which context condition affects the judgment, and which mitigation decision is appropriate. This practical purpose shapes the taxonomy: labels must be clear enough for coding, but still expressive enough to capture the trade-offs that matter for review assistance.

Taxonomy construction follows an empirical-to-conceptual iteration. The study starts with dimensions derived from the targeted review, prior code-review taxonomies, evaluation rubrics, and examples of generated comments. These dimensions are refined during pilot annotation until the labels are clear, non-redundant, and useful for the decision task. This follows the general logic of taxonomy development: categories should be grounded in empirical observations, connected to a clear purpose, and refined until they satisfy explicit ending conditions such as label clarity, mutual usefulness, and sufficient coverage for the intended analysis [@m01_nickerson2013_taxonomy].

The coding guide for the taxonomy follows content-analysis practice. Each category defines the coding unit, inclusion criteria, exclusion criteria, and decision notes so that annotators can apply the labels consistently across comments and instances [@m03_krippendorff2018_content_analysis]. The initial review-specific labels draw on modern-code-review taxonomies, automated code-review analyses, fine-grained comment classification, and explanation-oriented review studies [@p51_davila2021_mcr_slr_taxonomy; @p52_tufano2021_automating_code_review_activities; @p53_tufano2024_code_review_automation_strengths_weaknesses; @p19_nguyen2025_fine_grained_classification; @p41_widyasari2025_explaining_explanations].

The taxonomy separates four related layers rather than mixing them into one flat label set:

<!-- table: caption="Layered taxonomy structure." label="tab:methodology-taxonomy-layers" -->
| Layer | Role in annotation | Examples |
| --- | --- | --- |
| Evaluation dimensions | Cross-cutting properties scored for each comment. | Technical correctness, grounding, relevance, usefulness, actionability, severity, annotator confidence. |
| Comment-level failure type | Primary label for what is wrong with the generated comment. | Unsupported claim, incorrect technical claim, irrelevant comment, wrong location, invalid fix, false positive, non-actionable comment, low-value nitpick. |
| Context condition | Modifier that explains whether the available evidence supports reliable judgment. | Sufficient context, insufficient context, inconsistent context, stale context, overly broad context. |
| Mitigation decision | Human reference decision used for strategy comparison. | `show`, `rewrite`, `suppress`, `escalate`. |

This separation is needed because a comment can be correct but low-value, useful but weakly grounded, relevant but not directly actionable, or impossible to judge because the context is insufficient. It also reduces overlap between failure labels and context labels. For example, an unsupported claim is a property of the comment relative to the available evidence, while insufficient context is a property of the instance that may make judgment or safe display difficult.

Pilot refinement ends when the main labels can be applied without persistent overlap between major categories, when recurring ambiguities have been turned into decision notes, and when the pilot does not reveal an important failure type missing from the taxonomy. The executed study reports the pilot size, annotator count, label changes, merged or removed categories, added decision notes, and unresolved ambiguity.

## Dataset and Sample Selection

The evaluation sample is selected for judgeability and paired comparison, not for dataset size alone. Each retained instance must contain a code change and enough review-relevant context to judge grounding, relevance, usefulness, and actionability. This requirement is important because mitigation strategies can only be compared fairly when the same underlying instance can be assessed across baseline generation, filtering, rewriting, suppression, and escalation decisions.

The dataset is chosen from sources that support review-comment evaluation: existing code-review comment generation datasets, pull-request-level review benchmarks, or code changes paired with commit messages, pull-request descriptions, issue descriptions, and review discussion. This choice is guided by the differences among reference-comment generation datasets, PR-level review benchmarks, context-enriched benchmarks, and comprehension-oriented review tasks [@p14_li2022_codereviewer; @p52_tufano2021_automating_code_review_activities; @p04_kumar2026_swe_prbench; @p05_zeng2025_swrbench; @p06_hu2025_contextcrbench; @p17_lin2025_codereviewqa]. The selected source is documented with its version, license constraints, instance definition, and available context fields so that the comparison can be reproduced.

Table \ref{tab:methodology-dataset-protocol} records the sample-selection decisions that must be fixed before final evaluation. Its purpose is to make the dataset choice auditable: the reader should be able to see what was included, what was excluded, how pilot instances were separated from the final sample, and why the sample size supports the level of claim made in the paper.

<!-- table: caption="Dataset and sample-selection protocol." label="tab:methodology-dataset-protocol" -->
| Design element | Required specification in the executed study |
| --- | --- |
| Dataset name and source | The selected dataset or benchmark, with version, URL or release identifier, and license constraints. |
| Instance definition | Whether one instance corresponds to a pull request, code change, hunk, file-level change, or existing review-comment context. |
| Included context | Diff, surrounding code, commit message, pull-request description, issue text, review discussion, retrieved files, or other context used by strategies. |
| Inclusion criteria | Instances with enough code and textual context to judge grounding, relevance, usefulness, and actionability. |
| Exclusion criteria | Instances that cannot be legally reused, cannot be judged from available context, are duplicates, are non-code-only changes, or contain insufficient language/context support. |
| Sampling plan | Random or stratified sampling by repository, language, change size, context availability, or baseline-problem likelihood. |
| Pilot/final separation | Pilot instances are not reused for final evaluation after prompt, taxonomy, or threshold tuning. |
| Sample-size rationale | Number of review instances, generated comments, double-annotated comments, per-failure-type counts, and rationale for descriptive or inferential analysis. |

For every retained instance, the study records the code diff or changed region, available surrounding code, textual context such as commit message or pull-request description, and any additional context supplied to a strategy. Instances are excluded when the available material is insufficient to judge the generated comment, when the change is not review-relevant code, when reuse is not allowed by the dataset license, or when duplicate instances would distort the paired comparison.

If the selected dataset already contains generated review comments from prior systems, those comments may be used as input artifacts when they match the study's unit of analysis. Otherwise, baseline comments are generated using a fixed model and fixed prompt. In both cases, prompt or strategy tuning is limited to the pilot stage. The final evaluation sample is processed only after the dataset split, model configuration, decoding settings, prompts, thresholds, and strategy rules have been fixed.

The planned initial setup uses one primary dataset, one main generation model, four or five representative strategies, and approximately 100--300 annotated generated comments. This sample size is intended to support interpretable descriptive and paired trade-off analysis rather than broad model-ranking claims. Failure-type subgroups with small counts are treated as qualitative or exploratory evidence rather than as stable estimates. The executed study reports the count of generated comments and retained decisions for each strategy, each major failure type, each context-quality group, and the double-annotated subset. If the executed study uses a smaller sample, the results are reported as exploratory and the claims are narrowed accordingly.

## Compared Mitigation Strategies

The study compares a limited number of representative strategies. These strategies are chosen to represent different intervention points rather than to exhaust all possible systems. The strategy set reflects common intervention families in recent work: prompt- or generation-time control, context enrichment or context gating, post-generation verification, static-analysis or specification grounding, reward or preference-based filtering, and human-centered escalation [@p02_tantithamthavorn2026_hallujudge; @p03_tantithamthavorn2026_rovodev; @p10_sun2025_bitsai_cr; @p11_zhang2025_laura; @p12_wang2025_sgcr; @p20_hong2025_rag_reviewer; @p22_jaoua2025_static_analyzers; @p24_bensghaier2025_reward_models; @p28_heander2025_support_not_automation].

The default comparison includes five conditions. If implementation constraints require dropping a condition, the executed study reports the change before the results section and narrows the corresponding claims.

<!-- table: caption="Representative mitigation strategies for the empirical comparison." label="tab:methodology-strategies" -->
| Strategy | Intervention point | Operational rule | Main risk measured |
| --- | --- | --- | --- |
| Baseline LLM reviewer | Generation | Generate a review comment using a fixed base prompt and available context; generated comments are treated as shown candidates unless no comment is produced. | Exposes unsupported, irrelevant, non-actionable, or low-value comments. |
| Robust prompting | Generation | Generate using a constrained prompt that requires explicit grounding, actionability, and abstention from low-confidence or low-value feedback. | May still hallucinate or may reduce useful feedback by over-abstaining. |
| Context-quality gate | Before generation or before display | Assign a context-quality label before generation or display; sufficient-context cases continue, insufficient or inconsistent cases are escalated or skipped according to a fixed rule. | May reduce unsafe exposure but increase escalation and reduce coverage. |
| Post-generation verification | After generation | Check the generated comment against the available context; map the verifier result to `show`, `rewrite`, `suppress`, or `escalate`. | May falsely suppress useful comments or over-trust weakly grounded comments. |
| Hybrid gate plus verifier | Before and after generation | Apply the context-quality gate first, then verify generated comments for the instances that continue past the gate. | May improve safety but compound cost, false suppression, and escalation. |

The final implementation of each strategy is documented using the operational template in Table \ref{tab:methodology-strategy-spec}. A strategy is not considered comparable unless these fields are fixed before the final sample is processed.

<!-- table: caption="Operational specification required for each mitigation strategy." label="tab:methodology-strategy-spec" -->
| Field | Required specification |
| --- | --- |
| Input | Code, textual context, retrieved context, static-analysis signal, generated comment, or strategy-specific metadata. |
| Output | Generated comment, revised comment, verification label, context-quality label, or no-comment decision. |
| Decision labels | One of `show`, `suppress`, `rewrite`, or `escalate`, with strategy-specific mapping rules. |
| Prompt or rule | Exact prompt, rule set, verifier criterion, static-analysis mapping, retrieval setting, or threshold. |
| Fixed settings | Model name, model version, temperature, decoding settings, retrieval depth, analyzer version, and threshold values. |
| Cost unit | Number of generation calls, verifier calls, retrieval calls, analyzer calls, token count, or latency proxy. |
| Failure mode | Known way the strategy may remove useful feedback, expose unsafe feedback, or increase human effort. |

Thresholds, prompts, and routing rules are calibrated only on the pilot subset and then locked before the final sample is processed. Any post-hoc change is reported as a protocol deviation and the affected comparison is labeled exploratory. For the context-quality gate, the executed study reports the exact context labels, the rule that maps those labels to continue, skip, or escalate, and whether the gate is applied before generation or only before display. For post-generation verification, the executed study reports the verifier prompt or rule, the evidence fields inspected by the verifier, and the mapping from verifier output to `show`, `rewrite`, `suppress`, or `escalate`.

A retrieval-augmented context strategy may be added only if the dataset supports retrieval and the retrieval setting can be fixed before final execution. If included, it is treated as a context-enrichment strategy and evaluated with the same trade-off metrics, including cost and added context noise [@p11_zhang2025_laura; @p16_icoz2026_context_aware; @p20_hong2025_rag_reviewer].

The baseline is not expected to be the best strategy. It provides the reference point for measuring how many problematic comments appear without additional mitigation. Robust prompting tests whether generation-time constraints are enough. The context-quality gate tests whether preventing or routing low-context cases reduces problematic comments. Post-generation verification tests whether checking comments after generation improves quality before display. The hybrid strategy tests whether pre-generation and post-generation controls complement each other.

## Paired Comparison Design

The empirical comparison uses a paired design: each strategy is evaluated on the same underlying review instances wherever feasible. This design is important because generated review comments vary strongly by change type, code context, and available textual context. Comparing strategies on different samples would confound mitigation behavior with input difficulty.

For each review instance, the study records the baseline output and the outputs or decisions produced by each mitigation strategy. The paired structure allows the analysis to ask instance-level questions: did the verifier suppress a comment that annotators considered useful? Did the context-quality gate route an instance that produced an unsupported baseline comment? Did robust prompting improve actionability for the same underlying change? Did the hybrid strategy preserve useful feedback that a single-stage filter would have removed?

When a strategy cannot produce an output for a specific instance, the missing output is recorded as part of the strategy behavior rather than silently removed from the analysis. For example, a context-quality gate that escalates an instance instead of generating a comment affects both coverage and human effort.

The paired structure is also reflected in the analysis. Comment-level quality measures are computed over generated comments, while coverage, escalation, and cost measures are computed over review instances. If multiple comments are produced for one instance, comment-level results are reported with the instance identifier preserved so that the analysis can avoid treating nested comments as fully independent observations.

## Generation and Mitigation Procedure

For each code-review instance, the baseline strategy generates a review comment using the fixed model and base prompt. Other strategies either change the generation prompt, add a pre-generation or pre-display context-quality decision, verify the generated comment, or combine these interventions.

Each strategy produces both an output artifact and a mitigation decision. The output artifact may be a generated comment, a rewritten comment, a verification label, a context-quality label, or an escalation decision. The four decision labels are:

- `show`: the comment is suitable to present as review feedback;
- `suppress`: the comment should not be shown because it is unsupported, incorrect, irrelevant, too low-value, or harmful;
- `rewrite`: the comment contains a useful signal but needs clarification, grounding, softening, or actionability improvements;
- `escalate`: the comment raises a potentially important issue that requires human judgment or additional context.

The decision labels are assigned by strategy rules during mitigation and by annotators during human reference labeling. The analysis compares these two sources rather than assuming the strategy decision is correct.

All prompts, model settings, gating rules, verifier prompts or rules, static-analysis settings, retrieval settings, and thresholds are fixed before processing the final sample. Reporting also identifies the role played by the LLM in each stage: generation, verification, rewriting, judging, or annotation support. This distinction is needed because an LLM used as a generator and an LLM used as a judge create different validity risks [@m06_sebastianbaltes2025; @m04_zheng2023_llm_judge; @p29_wang2025_human_evaluators; @p31_jiang2025_codejudgebench; @p33_he2025_llmjudge_se; @p36_li2024_llms_as_judges].

Human annotation is the primary reference for final evaluation. If an LLM judge is used, its output is treated either as a mitigation-strategy component or as an auxiliary measurement signal, not as ground truth. LLM-judge results are therefore compared against human annotation rather than replacing it.

## Human Annotation Protocol

The annotation protocol evaluates generated comments, available context, and mitigation decisions. Annotators see the code change, available context, generated comment, and any strategy-specific decision needed for the current annotation phase. The annotation guideline defines the labels and decision rules.

The main annotation labels include:

- problematic-comment type;
- technical correctness;
- grounding or evidential support;
- relevance to the change;
- usefulness;
- actionability;
- value or severity;
- context quality;
- dataset validity;
- recommended mitigation decision;
- annotator confidence.

The protocol distinguishes correctness, usefulness, and actionability. A comment can be technically correct but practically low-value. A comment can be useful but not directly acceptable as a review comment. A comment can be impossible to judge because the available context is insufficient. These distinctions are consistent with review-specific evaluation rubrics, curated-review studies, comment-classification work, and human-centered review-assistance studies [@p01_lu2025_deepcrceval; @p18_bensghaier2025_curated_reviews; @p19_nguyen2025_fine_grained_classification; @p07_olewicki2024_revmate; @p28_heander2025_support_not_automation].

The human reference decision is derived from the annotation labels using the mapping in Table \ref{tab:methodology-human-decision-map}. Annotators may override the default mapping only when they record a rationale and the case is reviewed during adjudication. All overrides are flagged in the annotation dataset and analyzed separately from rule-conforming decisions. Figure \ref{fig:human-annotation-decision-mapping} shows how comment-level judgments flow into the human reference decision and then into decision-confusion analysis.

<!-- table: caption="Human annotation mapping from labels to mitigation decisions." label="tab:methodology-human-decision-map" -->
| Human reference decision | Default conditions |
| --- | --- |
| `show` | The comment is technically correct, grounded in the available evidence, relevant to the change, useful enough for review attention, and sufficiently actionable. |
| `rewrite` | The comment contains a useful signal, but the wording, scope, grounding, severity, or actionability must be improved before display; no new unverified factual claim is required to make it acceptable. |
| `suppress` | The comment is incorrect, unsupported, irrelevant, harmful, too low-value, misleading, or not worth preserving even through rewriting. |
| `escalate` | The comment may point to an important issue, but safe judgment requires human expertise, additional project context, security/performance validation, or resolution of low annotator confidence. |

<!-- figure: path="figures/human_annotation_decision_mapping.tex" caption="Human annotation flow from comment-level judgments to reference mitigation decisions and decision-confusion outcomes." label="fig:human-annotation-decision-mapping" -->

Annotation is performed in two phases to reduce bias. In the first phase, annotators judge comment quality, failure type, usefulness, actionability, grounding, and context quality while being blinded to the mitigation strategy whenever feasible. In the second phase, annotators evaluate or resolve the appropriate mitigation decision. Strategy identifiers and model-generated verifier labels are not shown during initial quality labeling unless they are required for the specific decision task. If full blinding is not feasible, the executed study reports what information was visible to annotators.

Before full annotation, annotators label a pilot subset. The pilot is used to refine taxonomy labels, clarify ambiguous cases, calibrate mitigation decisions, and revise the annotation guideline. At least two annotators with software-engineering experience label the pilot and a substantial subset of the final sample when feasible. The planned minimum is double annotation for all pilot items and for at least 30\% of final-sample comments, or for all final-sample comments when the sample contains 150 comments or fewer. If this minimum cannot be met, the executed study reports agreement descriptively and narrows claims that depend on reliability. The final paper reports annotator background in terms of software-engineering experience, code-review experience, programming-language familiarity, and prior exposure to LLM-based tools.

Inter-annotator agreement is reported separately for key label groups when possible. Cohen's kappa can be used for two annotators and categorical labels [@m02_cohen1960_kappa]. Krippendorff's alpha is appropriate when there are missing labels, more than two annotators, or variable annotation coverage, and software-engineering qualitative research provides practical guidance for using such agreement measures in coding studies [@m07_angelgonzalezprieto2020]. Percentage agreement is reported as a descriptive supplement because chance-corrected agreement can be unstable when labels are rare or highly imbalanced.

Agreement is not reported as a single global number. The executed study reports agreement separately for at least the main problematic type, usefulness, actionability, grounding, context quality, and final mitigation decision when sample size allows. It also reports labels with low agreement, frequent disagreement pairs, and examples of ambiguous cases. Disagreements are resolved through discussion or adjudication. The adjudication procedure identifies whether the adjudicator is one of the original annotators or a third reviewer. The final dataset preserves the initial annotator labels, resolved labels, override flags, adjudication notes, and disagreement notes where useful.

## Operational Measures

The study operationalizes each construct through explicit labels, counts, or ratios. Table \ref{tab:methodology-operational-measures} summarizes the main constructs used in the analysis. The selected measures combine review-comment quality dimensions, production or workflow signals, data-quality concerns, and evaluator-validity risks reported in prior work [@p01_lu2025_deepcrceval; @p03_tantithamthavorn2026_rovodev; @p08_liu2025_too_noisy; @p10_sun2025_bitsai_cr; @p29_wang2025_human_evaluators; @p30_weyssow2025_codeultrafeedback; @p33_he2025_llmjudge_se].

<!-- table: caption="Operational measures used in the empirical comparison." label="tab:methodology-operational-measures" longtable="true" -->
| Construct | Operational measure | Source |
| --- | --- | --- |
| Problematic-comment rate | `# comments with at least one problematic label / # generated comments`. | Human annotation. |
| Failure-type rate | `# comments with a given failure type / # generated comments`. | Human annotation. |
| Useful-feedback preservation | `# useful comments retained as show or rewrite / # useful candidate comments`. | Human annotation plus strategy decision. |
| Wrongly suppressed useful comments | `# useful comments suppressed / # useful candidate comments`. | Human annotation plus strategy decision. |
| Review coverage | `# instances with at least one shown or rewritten useful comment / # review instances`. | Strategy output plus annotation. |
| Unsafe exposure | `# shown comments judged suppress or escalate / # shown comments`. | Strategy decision compared with resolved annotation. |
| Recoverable feedback loss | `# comments suppressed by a strategy but judged rewrite / # comments judged rewrite`. | Strategy decision compared with resolved annotation. |
| Human escalation rate | `# instances routed to human review or additional context / # review instances`. | Strategy decision. |
| Context-quality effect | Difference in primary and secondary strategy metrics between high-context, low-context, and inconsistent-context instances. | Context-quality label plus strategy metrics. |
| Computational cost | Model calls, verifier calls, retrieval calls, analyzer calls, approximate token count, or latency proxy per instance. | Execution log or cost proxy. |
| Evaluator reliability | Agreement on key labels such as problematic type, usefulness, actionability, grounding, context quality, and mitigation decision. | Annotator labels and agreement statistics. |

A **useful candidate comment** is any generated comment whose resolved human annotation marks it as useful or potentially useful, including comments assigned the reference decision `show` or `rewrite`. This definition intentionally includes recoverable comments because one purpose of the study is to distinguish feedback that should be removed from feedback that should be preserved through rewriting. Context-quality effects are computed only for metrics that have enough instances in each subgroup; otherwise, they are reported as qualitative patterns.

These measures make the trade-off explicit. A strategy can improve the problematic-comment rate while worsening useful-feedback preservation or review coverage. Conversely, a strategy can preserve more useful comments while requiring more escalation or computational cost.

## Decision-Confusion Analysis

The study compares each strategy's decision with the resolved human annotation decision. This creates a decision-confusion view over the four actions: show, suppress, rewrite, and escalate. Similar decision-oriented concerns appear in industrial filtering, human-AI review support, reward-guided comment generation, and LLM-as-a-Judge evaluation, where the relevant question is not only whether a score improves, but also which comments are exposed, removed, rewritten, escalated, or misjudged [@p03_tantithamthavorn2026_rovodev; @p10_sun2025_bitsai_cr; @p24_bensghaier2025_reward_models; @p28_heander2025_support_not_automation; @p29_wang2025_human_evaluators].

Several error types are especially important:

- **Unsafe exposure**: the strategy shows a comment that annotators judge should be suppressed or escalated.
- **False suppression**: the strategy suppresses a comment that annotators judge should be shown.
- **Recoverable feedback loss**: the strategy suppresses a comment that annotators judge should be rewritten.
- **Unnecessary escalation**: the strategy escalates a comment that annotators judge could be shown or rewritten.
- **Missed escalation**: the strategy shows or rewrites a comment that annotators judge requires escalation.

This analysis is important because it captures costs that are invisible in a binary quality score. For example, false suppression and recoverable feedback loss both remove useful information, but recoverable feedback loss is especially important because a rewrite strategy could have preserved the signal.

## Metrics

The study reports primary, secondary, and exploratory metrics so that the strength of each claim matches the amount of evidence available.

<!-- table: caption="Metric priority and interpretation." label="tab:methodology-metric-priority" -->
| Metric group | Metrics | Interpretation |
| --- | --- | --- |
| Primary | Problematic-comment rate, useful-feedback preservation, review coverage, unsafe exposure. | Used to answer the main trade-off questions in RQ2 and RQ3. |
| Secondary | Failure-type rates, recoverable feedback loss, false suppression, human escalation rate, computational cost. | Used to explain how and why strategy trade-offs differ. |
| Exploratory | Context-quality effects, low-frequency failure-type comparisons, hybrid-strategy subgroup effects. | Interpreted conservatively and reported with qualitative examples when counts are small. |

Error-reduction metrics include:

- overall problematic-comment rate;
- rate of each problematic-comment type;
- unsupported or hallucinated comment rate;
- irrelevant comment rate;
- wrong-location or wrong-cause rate;
- invalid fix suggestion rate;
- non-actionable comment rate;
- low-value comment rate.

Preservation and workflow metrics include:

- useful comments retained;
- useful comments wrongly suppressed;
- review coverage retained after filtering;
- comments rewritten rather than suppressed;
- human escalation rate;
- context-dependent comments routed correctly;
- human annotation or verification effort;
- number of model calls;
- approximate token cost;
- latency proxy where measurable.

The study does not report only a single quality score. A strategy that removes many comments may look good under an error-rate metric but bad under useful-feedback preservation or coverage. Conversely, a strategy that preserves many useful comments may still require too much human escalation or computational cost.

## Analysis Plan

The analysis compares strategies along four axes.

First, it compares the distribution of problematic-comment types produced or retained by each strategy. This answers which strategies are effective for unsupported claims, irrelevant comments, non-actionable comments, invalid fix suggestions, and low-value comments.

Second, it compares preservation and coverage. This asks how many useful comments each strategy keeps, how many useful comments it wrongly suppresses, and how much automatic review coverage remains after filtering or escalation.

Third, it compares strategy decisions against resolved annotation decisions using the decision-confusion analysis. This identifies unsafe exposure, false suppression, recoverable feedback loss, unnecessary escalation, and missed escalation.

Fourth, it compares cost and effort. This includes additional model calls, verifier calls, retrieval cost if applicable, human escalation rate, and annotation or verification effort. These measures are used to avoid presenting a high-cost strategy as better only because it reduces more problematic comments.

The primary analysis is the paired comparison of strategy decisions and outcomes on the shared evaluation sample. Primary metrics are always reported with counts and denominators. Secondary and exploratory metrics are reported only when their denominators are visible and their uncertainty or sparsity is acknowledged.

If the sample size permits, paired comparisons use uncertainty estimates such as confidence intervals or bootstrap intervals. For paired binary outcomes, tests such as McNemar's test or paired bootstrap comparisons may be used when their assumptions are reasonable. If the sample is small or a failure-type subgroup has few observations, the analysis remains primarily descriptive and pairs quantitative summaries with qualitative examples.

If the hybrid strategy is included, it is analyzed as a secondary trade-off case rather than as an assumed improvement. The analysis asks whether combining a context-quality gate with post-generation verification reduces complementary failure types or merely increases cost, false suppression, and escalation.

Context quality is analyzed as an exploratory moderator. The study compares high-context and low-context instances where possible, and examines whether certain failures occur more often when the available context is incomplete, inconsistent, stale, or too broad. This moderator analysis is motivated by prior evidence that review quality depends on available context, reviewability, retrieved evidence, specifications, static-analysis signals, and possible documentation-code inconsistencies [@p06_hu2025_contextcrbench; @p11_zhang2025_laura; @p12_wang2025_sgcr; @p22_jaoua2025_static_analyzers; @p40_ram2018_reviewability; @p49_lee2025_metamon].

Qualitative examples are selected using explicit criteria rather than as anecdotal support. The executed study reports at least one example for each common failure type, each major decision-confusion error, and each low-agreement label where licensing permits. Examples are selected from resolved annotations after metric computation, and the selection rule is reported before the examples are interpreted. Examples are used to explain mechanisms behind the metrics, not to replace the quantitative comparison.

## Reproducibility and Scope Control

To support reproducibility, the final replication package includes the study corpus where licensing permits, coding form, annotation guideline, evaluation schema, prompts, model settings, generated outputs where licensing permits, strategy decisions, resolved annotations, and scripts for computing metrics. If closed models or restricted datasets are used, the study still documents prompts, settings, sampling decisions, and annotation procedures as precisely as possible. This reporting covers not only the final prompt text, but also the model role, model version, temperature or decoding settings, context construction, tool use, and any human validation or adjudication steps [@m06_sebastianbaltes2025].

The main scope risk is that the work becomes too broad: too many datasets, too many models, too many strategies, or too many evaluation dimensions. The initial study therefore keeps the design limited. It is designed to use a bounded set of representative strategies and a sample size that supports careful annotation.

The main threats to validity are incomplete literature coverage, possible changes in recent preprints, dataset limitations, sample size limits, annotator disagreement, sensitivity to prompts and model settings, and possible evaluator bias if LLM-as-a-Judge is used. These threats are mitigated by transparent inclusion criteria, fixed evaluation settings, pilot annotation, agreement reporting, preserved disagreement notes, and conservative interpretation of results. The study reports these threats as design constraints rather than as after-the-fact caveats, following empirical software-engineering reporting expectations [@m05_paulralph2020]. Evaluator-related threats are especially important because recent work shows that LLM judges can be useful but sensitive to task framing, judge choice, bias, and calibration [@p29_wang2025_human_evaluators; @p31_jiang2025_codejudgebench; @p32_zhao2026_bias_loop; @p33_he2025_llmjudge_se; @p36_li2024_llms_as_judges].