# Trade-Off-Aware Evaluation Framework

Mitigation changes the review stream. A filter decides which candidate comments disappear; retrieval changes the evidence available to the generator; verification adds another judgment; and referral transfers work to a reviewer. Studies of these mechanisms report losses in coverage, shifts in intent, and additional latency or effort [@p04_kumar2026_swe_prbench; @p07_olewicki2024_revmate; @p10_sun2025_bitsai_cr; @p18_bensghaier2025_curated_reviews; @p35_mcaleese2024_llm_critics; @p65_ameen2026_qasecclaw].

This review integrates six layers: input and context quality, comment quality, failure type, handling decision, preservation and coverage, and cost and evaluator validity. Prior studies report the individual constructs and intervention families. Their organization into one framework and the four-way handling policy are proposed here and require empirical validation.

## Framework Overview

<!-- table: caption="Layers of the trade-off-aware evaluation framework." label="tab:framework-layers" -->
| Layer | Evaluation question | Example measurements |
| --- | --- | --- |
| Input and context quality | Is the instance judgeable under the available evidence? | context sufficiency, consistency, freshness, reviewability |
| Comment quality | Is the comment technically sound, grounded, relevant, useful, and actionable? | correctness, grounding, relevance, usefulness, actionability |
| Failure type | What kind of failure, if any, explains why the comment is problematic? | unsupported, irrelevant, wrong cause, invalid fix, low-value |
| Mitigation decision | What should happen before the comment reaches the user? | show, suppress, rewrite, escalate |
| Preservation and coverage | What useful feedback or review coverage is preserved or lost? | useful comments retained, useful comments wrongly suppressed, coverage retained |
| Cost and evaluator validity | What effort, computation, latency, or measurement risk is introduced? | model calls, human escalation, annotation agreement, judge robustness |

The table is meant to be read from left to right for a particular review instance. It begins with the evidence available to the system and ends with the reliability and cost of the resulting assessment.

## Layer 1: Input and Context Quality

Context quality covers relevance, completeness, specificity, consistency, freshness, reviewability, provenance, behavioral evidence, attention load, and cost. Consider a warning about an API contract that is absent from the diff. The warning is difficult to judge until the contract is retrieved; contradictory versions of that contract make the instance harder still. A context-quality gate can detect such cases before generation or display and route them for more evidence or human review.

## Layer 2: Comment Quality

Comment quality covers technical correctness, grounding, relevance, specificity, explanation quality, usefulness, and actionability. These labels answer different questions about the same text. A precise comment about the changed line, for example, can still rest on a false account of runtime behavior. In the proposed annotation record, it would receive high localization and specificity ratings alongside a low correctness rating.

## Layer 3: Failure Type

Failure labels supply a diagnosis that quality ratings alone cannot provide. Verification is relevant to an unsupported claim, whereas vague wording points toward revision and a misplaced diagnosis requires correction of its target or cause. Strategy comparisons can then show the distribution of affected failure types instead of reporting only an overall change in problematic comments.

## Layer 4: Mitigation Decision

This review proposes four mitigation decisions.

- `show`: the comment is suitable to present as review feedback.
- `suppress`: the comment should not be shown because it is harmful, unsupported, irrelevant, incorrect, or too low-value.
- `rewrite`: the comment contains a useful signal but needs clarification, grounding, softening, or actionability improvements.
- `escalate`: the comment may matter but requires human judgment or additional context.

These decisions preserve an important distinction. Some comments contain no defensible review signal and can be suppressed. Others contain a concern worth retaining, although the original wording is unsuitable for display.

## Layer 5: Preservation and Coverage

Preservation concerns comments that remain useful after intervention and useful candidates that are wrongly withheld. Coverage uses a different denominator: the review issues or changes for which the system still provides useful feedback. Both should be measured after filtering, gating, rewriting, or escalation.

## Layer 6: Cost and Evaluator Validity

The final layer records model and verifier calls, retrieval operations, latency, human escalation, and annotation effort. It also concerns the reliability of the measurement itself. Human annotators may disagree on usefulness, actionability, or severity, while LLM-as-a-Judge results may be sensitive to prompts, output order, model choice, and verbosity.

An empirical study should report inter-annotator agreement and the role of any LLM-as-a-Judge procedure. A judge may support screening or provide auxiliary evidence, but mitigation claims still need comparison with a defined annotation protocol.

## Empirical Use

Empirical use starts with paired records for the unmitigated and mitigated outputs. The comparison retains the failure diagnosis, handling decision, issue coverage, and resource fields. This makes a familiar production result—higher precision after aggressive filtering—inspectable: researchers can trace whether the gain came from removing unsupported comments, discarding low-value comments, or losing difficult but useful concerns. A second strategy may reach a similar displayed-comment precision through verification and referral, yet impose a different reviewer workload.

We have not executed that comparison in the present review. A future study will need to determine which fields annotators can apply reliably and which resource measures can be recovered from operational logs.
