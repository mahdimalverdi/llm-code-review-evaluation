# Conclusion

This targeted structured review synthesized 121 full-text studies relevant to
trade-off-aware evaluation of LLM-based code review. The evidence shows that
problematic feedback cannot be reduced to hallucination alone. Failures include
unsupported and incorrect claims, irrelevant or low-value feedback, wrong
localization or causality, invalid fixes, missing issues, context dependence,
communication harms, adversarial influence, and evaluator error. These failures
arise not only in the final comment but also in training data, context selection,
agent trajectories, reference construction, and judging.

Review quality likewise cannot be represented by a single similarity,
correctness, relevance, usefulness, acceptance, or judge score. The review
derives an operational taxonomy, separates evaluation dimensions from failure
types and mitigation decisions, and proposes a framework spanning context
quality, comment quality, useful-feedback preservation, issue coverage, human
escalation, workflow outcomes, cost, and evaluator validity. It identifies
context integrity and evaluator robustness as first-class concerns, particularly
for agentic, security-oriented, and LLM-judged settings.

The central implication is asymmetric evaluation. A mitigation should not be
credited only for reducing visible errors. Evaluation should also measure useful
comments wrongly removed, issues no longer covered, cases redirected to humans,
changes in developer action, and additional computational or review effort. The
framework therefore connects measured properties to four operational decisions:
show, suppress, rewrite, and escalate. It is intended as a reproducible reporting
and decision structure rather than a universal scalar score.

The findings are bounded by the assembled corpus. The dated supplementary search
and freeze improve traceability, but the original database search and screening
history was not preserved. The work should therefore not be described as a fully
reproducible systematic review. The proposed taxonomy and framework also remain
literature-derived rather than empirically validated. Independent annotation,
calibration, controlled mitigation studies, and longitudinal deployment evidence
are needed to test category reliability, threshold choices, preservation,
coverage, escalation, and operational value.
