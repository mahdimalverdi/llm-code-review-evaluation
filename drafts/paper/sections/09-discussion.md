# Discussion

## Interpretation of the Evidence

The expanded corpus supports a shift from evaluating generated text in isolation
to evaluating review decisions within a workflow. A review comment is produced
from a change, selected context, a model or agent trajectory, and an evaluation
instrument. Failure can occur at any of these points. Training references may be
ambiguous, retrieval may supply misleading context, an otherwise plausible
comment may identify the wrong cause, and a judge may prefer a fluent explanation
without reliable evidence [@p08_liu2025_too_noisy;
@p31_jiang2025_codejudgebench; @p72_centellas_claros2026_rethinking_training_data_for_g;
@p93_meng2025_when_more_retrieval_hurts_retr;
@p101_jin2025_uncovering_systematic_failures]. The resulting evaluation problem
is therefore wider than hallucination detection or comment-reference similarity.

The corpus also reveals a difference between evidence coverage and evidence
comparability. Many studies discuss correctness, usefulness, coverage, cost, or
human involvement, but they operationalize these constructs with different
artifacts, denominators, and evaluators. The generated study-level counts show
where evidence is present; they do not justify pooling heterogeneous effect
sizes. The framework therefore treats dimensions as a reporting structure and
decision aid rather than as a validated universal scoring function.

## Evaluation as a Decision Problem

Evaluation should connect measurement to action. Correctness or groundedness
alone does not determine whether a comment should be shown. A weakly grounded
but potentially important concern may require escalation; a valid but vague
concern may require rewriting; and a correct but low-value nitpick may justify
suppression. The show, suppress, rewrite, and escalate decisions expose
trade-offs hidden by binary quality labels.

This decision framing also changes the relevant denominator. A precision value
over displayed comments cannot reveal useful comments that a filter removed. A
coverage value over known reference issues cannot reveal valid issues absent
from the reference. An escalation rate is uninterpretable without escalation
precision, reviewer effort, and the consequences of non-escalation. Evaluation
should therefore preserve the relationship between generated candidates,
displayed comments, suppressed comments, escalated cases, and developer action.

## Implications for Tool Builders

Tool builders should report both harmful-comment reduction and useful-feedback
preservation. Context expansion should be evaluated for marginal utility,
freshness, integrity, latency, and model capacity. More retrieval or a larger
model does not consistently imply better review performance
[@p83_kumar2026_bigger_isn_t_always_better_a_c;
@p93_meng2025_when_more_retrieval_hurts_retr]. Verification and filtering should
expose suppressed outputs to audit so that wrong removals can be measured.
Human escalation should be treated as a cost and coverage outcome, not as a free
fallback.

Agentic systems additionally require trajectory-level observability. Reporting
only the final comment hides which context was selected, which tools were used,
which candidate issues were discarded, and where unsupported claims entered the
trajectory [@p74_charoenwet2026_agentic_code_review_in_the_ter;
@p76_wang2026_swe_review_closing_the_loop_on;
@p85_zhang2026_reporeviewer_a_local_first_mul]. At minimum, deployments should
retain auditable provenance for context retrieval, tool evidence, suppression,
rewriting, and escalation decisions.

## Implications for Benchmarks

Benchmarks should distinguish reference incompleteness from model failure, record
input reviewability, and support multiple valid comments. Acceptance, adoption,
or lexical similarity should not be treated as complete proxies for usefulness.
Specialized security, static-analysis, repair, and performance claims require
task-specific evidence rather than a generic quality score.

Benchmark reporting should also identify the unit of analysis. Comment-level,
issue-level, change-level, pull-request-level, and trajectory-level evaluations
answer different questions. A model may localize issues well but produce poor
explanations, or generate plausible comments without improving review outcomes.
Multi-task and multidimensional benchmarks help expose these differences, but
their aggregate scores should remain decomposable
[@p91_zhang2026_sphinx_benchmarking_and_modeli;
@p98_yu2025_fine_tuning_llms_to_analyze_mu].

## Implications for Evaluators

LLM-based judges can support scale but should be treated as measurement instruments. At minimum, judge studies should report the rubric, answer rate, order swaps, repeated-run consistency, prompt perturbation, judge and source-model sensitivity, preprocessing, human comparison, adversarial robustness, and cost [@p29_wang2025_human_evaluators; @p31_jiang2025_codejudgebench; @p32_zhao2026_bias_loop; @p33_he2025_llmjudge_se; @p36_li2024_llms_as_judges].

Consistency alone is insufficient. A judge can be consistently biased, sensitive
to source cues, or unreliable under semantically equivalent prompts. Human
evaluation is not an error-free gold standard either; expertise, task context,
rubric interpretation, and disagreement procedure affect the resulting labels.
Evaluator validation should therefore combine repeated measurements, human
calibration, disagreement analysis, and bounded claims about the constructs the
instrument can measure.

## Limits of the Proposed Framework

The framework is literature-derived and operationally specified, but it has not
yet been validated as a complete annotation or deployment instrument. The
taxonomy may require revision when annotators encounter comments that combine
multiple failures. The proposed decision thresholds depend on project risk and
review capacity. The trade-off fields do not imply that preservation, coverage,
escalation, and cost can always be reduced to one scalar utility value. These
limits are intentional: the framework provides a common reporting and reasoning
structure while preserving context-specific decisions.

## Research Agenda

The most useful next step is not another single-score leaderboard. Future work
should measure preservation under filters and gates, validate the proposed
taxonomy with independent annotators, compare context quantity with context
quality, test defensive mechanisms against adversarial review context, and
report workflow and cost effects alongside quality. Longitudinal field studies
are needed to determine whether apparently useful comments change developer
behavior, reviewer workload, defect outcomes, or trust over time
[@p77_lin2026_is_agentic_code_review_helpful;
@p100_sun2025_does_ai_code_review_lead_to_co;
@p110_a_alsteinsson2025_rethinking_code_review_workflo]. A controlled mitigation
study can use the annotation protocol and framework derived here, but its
findings should be presented separately from this literature review.
