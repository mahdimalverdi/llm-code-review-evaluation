# Findings

<!-- TODO: This section is a placeholder until the empirical study is executed. Replace all planned findings below with actual findings supported by quantitative tables, uncertainty summaries where feasible, and qualitative examples. -->

This section will report the empirical findings after the mitigation strategies are implemented and annotated. It should present a small number of concrete, evidence-backed observations rather than a long list of descriptive statistics. The findings should be organized around trade-offs: which failure types are reduced, which useful comments are preserved or lost, and what cost or human effort is introduced.

The final findings must be based on the annotated empirical sample. Until the study is run, the following are hypotheses and planned analysis targets rather than results.

## Planned Finding 1: Mitigation Strategies Reduce Different Failure Types

The first expected finding concerns failure-type specificity. Robust prompting, context-quality gates, post-generation verification, and hybrid designs are unlikely to reduce the same categories of problematic comments equally.

For example, robust prompting may reduce vague or non-actionable comments, while post-generation verification may be more effective for unsupported or technically incorrect claims. A context-quality gate may be most useful for comments that cannot be judged because the available context is incomplete or inconsistent. The final analysis should report these differences in a strategy-by-failure-type table.

## Planned Finding 2: Error Reduction Can Hide Useful-Feedback Loss

A strategy that suppresses many comments may reduce the apparent rate of problematic comments while also removing useful feedback. This finding is central to the paper. The empirical results should therefore report useful comments retained, useful comments wrongly suppressed, and useful-but-not-directly-acceptable comments that would be better rewritten than removed.

The strongest version of this finding would show that a strategy with the best error-reduction score is not necessarily best under preservation and coverage metrics.

## Planned Finding 3: Context Quality Changes Mitigation Behavior

Context quality is expected to moderate mitigation success. Low-context or inconsistent-context instances may lead to more unsupported, context-dependent, or hard-to-judge comments. In such cases, a context-quality gate may reduce risky comments but also lower automatic review coverage.

The final results should compare high-context and low-context instances when feasible and report whether different strategies behave differently across these groups.

## Planned Finding 4: Hybrid Mitigation May Improve Safety but Increase Cost

A hybrid gate-plus-verifier strategy may reduce complementary failure types, but it may also add model calls, increase latency, raise the human escalation rate, or suppress more useful comments. The paper should not assume the hybrid strategy is best. It should evaluate whether the hybrid improves the trade-off profile compared with its individual components.

## Planned Finding 5: Rewrite and Escalate Decisions Capture a Gray Zone

Binary show/suppress decisions may miss comments that contain useful signals but are not safe or clear enough to show directly. The empirical results should therefore report rewrite and escalation rates. These decisions are important because they show when mitigation should preserve a comment in modified form or route it to a human rather than simply deleting it.

## Reporting Principles

Each final finding should include three elements:

1. a quantitative summary from the annotated sample;
2. one or more representative examples;
3. an interpretation of the trade-off and its implication for LLM-based code review tools.

The section should avoid overclaiming. If the sample is small, findings should be described as exploratory but still useful for designing larger evaluations.
