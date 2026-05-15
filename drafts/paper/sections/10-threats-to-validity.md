# Threats to Validity

This section discusses threats to the validity of the empirical comparison and the steps used to reduce them. Because the study is intentionally bounded, the main risk is overgeneralizing from a small controlled evaluation. The paper should therefore match its claims to the size, diversity, and reliability of the final annotated sample.

## Construct Validity

The study measures problematic generated review comments using an operational taxonomy. The taxonomy may not capture all possible failure modes, and some labels may overlap. For example, a comment can be both unsupported and technically incorrect, or both non-actionable and low-value. To reduce this threat, the annotation guideline should define primary and secondary labels, provide inclusion and exclusion criteria, and preserve disagreement notes for ambiguous cases.

Useful-feedback preservation is also difficult to measure. A comment may be useful to one reviewer but not another, or useful only after rewriting. The study reduces this threat by separating usefulness, actionability, grounding, and mitigation decision rather than collapsing them into one score.

## Internal Validity

Differences between strategies may be caused by prompt wording, model settings, verifier design, or threshold choices rather than by the strategy family itself. To reduce this threat, prompts, model versions, decoding settings, gating rules, verifier rules, and thresholds should be fixed before the final evaluation run. Any pilot tuning should be separated from the final sample.

A paired evaluation design helps internal validity because the same review instances are processed across strategies where feasible. This reduces the chance that observed differences are caused by different input distributions.

## External Validity

The results may not generalize across programming languages, repositories, organizations, review cultures, model families, or code-change types. A study using one dataset and one main model can still provide useful evidence about trade-offs, but it should not claim universal superiority of one strategy.

To reduce this threat, the paper should describe the dataset, sampling strategy, model, prompts, and review context clearly. Future work can then replicate the evaluation on other datasets, languages, and review workflows.

## Annotation Validity

Human annotators may disagree on usefulness, severity, actionability, and whether a comment should be rewritten or escalated. These disagreements are not only noise; they may reveal genuinely ambiguous review situations. The study should report inter-annotator agreement where feasible and preserve disagreement reasons for analysis.

If only a subset is double-annotated, the paper should state this clearly and avoid overclaiming annotation reliability for the full dataset.

## Dataset and Reference Validity

The selected dataset may contain instances that are not review-relevant, not judgeable under the available context, or linked to incomplete references. Such cases can make a good generated comment appear wrong or make a bad comment appear unsupported only because the necessary context is missing.

The study mitigates this by labeling context quality and dataset validity separately from generated-comment quality. Instances that cannot be judged should be marked as context-dependent or dataset-validity concerns rather than treated as ordinary model failures.

## Evaluator Validity

If LLM-as-a-Judge is used as part of verification or auxiliary evaluation, its outputs may be sensitive to prompt wording, answer order, model choice, and response format. The study should not treat LLM judgments as ground truth unless validated against human labels. When LLM judges are used, their role should be reported explicitly as a mitigation component, an auxiliary measurement instrument, or both.

## Cost and Workflow Validity

Cost proxies such as token count, number of model calls, latency estimates, and human escalation rate may not directly match real deployment cost. Different providers, infrastructure, review workflows, and organizational policies can change these costs. The study should therefore report cost measures transparently and interpret them as proxies rather than exact deployment estimates.

## Literature and Framing Validity

The targeted literature review may miss relevant papers, especially because LLM-based code review research is changing quickly. Some recent papers may be preprints or may change before publication. The paper mitigates this by documenting inclusion criteria, maintaining a transparent paper pool, and separating reported evidence from inferred interpretation and our own perspective.

## Summary

The main validity strategy is transparency: fixed settings, explicit labels, pilot annotation, agreement reporting, preserved disagreement notes, separate context-quality labels, and conservative interpretation. The study should present its empirical findings as evidence about mitigation trade-offs under a controlled design, not as universal claims about all LLM-based code review tools.
