# Problematic Comment Taxonomy

> [!NOTE]
> This file defines failure types for LLM-generated code review comments. It should stay separate from evaluation dimensions. Evaluation dimensions tell us what to measure; taxonomy tells us what kind of failure occurred.

## Purpose

A single label such as “bad comment” is too coarse. A generated review comment may be bad because it is hallucinated, irrelevant, vague, non-actionable, low-value, or because it misses the actual issue. These failures have different causes and require different mitigation strategies.

## Core Distinction

| Concept | Example |
|---|---|
| Evaluation dimension | actionability, correctness, grounding, usefulness |
| Problematic comment type | non-actionable comment, hallucinated comment, irrelevant comment |
| Mitigation strategy | filter, rewrite, add context, escalate to human |
| Trade-off | fewer bad comments vs lost useful comments |

## Taxonomy Overview

| Category | Failure Type | Definition | Typical Cause | Possible Mitigation |
|---|---|---|---|---|
| Grounding failures | Hallucinated or unsupported claim | Comment makes a claim not supported by available context. | Model inference beyond diff/context. | Hallucination gate; claim-to-context grounding. |
| Grounding failures | Context-misaligned comment | Comment does not align with diff, PR intent, or available context. | Wrong or incomplete context. | Context-quality check; diff-grounded judge. |
| Grounding failures | Technically plausible but unsupported comment | Comment may be true, but cannot be verified from provided context. | Partial context; overconfident reasoning. | Require evidence span; human escalation. |
| Correctness failures | Factually incorrect comment | Comment is technically wrong. | Wrong API/type/language assumption. | Factuality judge; static/context checks. |
| Correctness failures | Wrong API/type assumption | Comment assumes incorrect return type, API behavior, or language semantics. | Missing framework/version context. | Add semantic/project context; type-aware checks. |
| Localization failures | Wrong-location comment | Comment is attached to the wrong line/hunk/file. | Poor localization or context matching. | Line-level localization check. |
| Relevance failures | Irrelevant comment | Comment does not matter for the reviewed change. | Noisy retrieval; generic generation. | Relevance filter. |
| Relevance failures | Out-of-scope comment | Comment discusses something outside the review scope. | Broad context; PR intent ignored. | Scope-aware judge; PR-intent alignment. |
| Clarity failures | Vague or generic comment | Comment is too vague to guide action. | Generic prompting; weak context. | Specificity rubric; rewrite. |
| Actionability failures | Non-actionable comment | Comment does not tell the developer what to do. | Missing fix suggestion; unclear issue. | Actionability gate; rewrite. |
| Value failures | Redundant comment | Comment repeats existing information or obvious facts. | Duplicate retrieval; low novelty. | Deduplication; reviewer-feedback learning. |
| Value failures | Low-value nitpick | Comment is technically valid but not worth reviewer attention. | Over-sensitive review style. | Severity/value threshold. |
| Value failures | Style-only low-value comment | Comment focuses on style with little practical value. | Style-biased prompt/model. | Team policy; severity filtering. |
| Coverage failures | Comment misses the actual issue | Generated review fails to identify a human-relevant issue. | Weak reasoning; missing context; attention dilution. | Coverage evaluation; multi-review aggregation. |
| Context failures | Comment depends on missing project context | Comment cannot be judged without project/framework/version context. | Insufficient context selection. | Context enrichment; escalation. |
| Human-value failures | Comment with poor value-to-time ratio | Comment requires reviewer time but provides little benefit. | Low-value or noisy generation. | Value gate; reviewer-overhead metric. |

## Relationship to Context Quality

Several failure types are context-related:

- unsupported claim;
- context-misaligned comment;
- wrong API/type assumption;
- comment depending on missing project context;
- wrong-location comment;
- missed issue due to missing context;
- low-value comment caused by irrelevant retrieved context.

This means context quality should be evaluated before or alongside comment quality.

## Relationship to Trade-offs

Each failure type implies a different trade-off.

| Failure Type | Naive Mitigation | Risk |
|---|---|---|
| Hallucinated claim | Strict hallucination filter | Useful but weakly grounded comments may be removed. |
| Irrelevant comment | Relevance filter | Novel but unexpected useful comments may be removed. |
| Non-actionable comment | Actionability gate | High-level design concerns may be suppressed. |
| Low-value nitpick | Severity threshold | Small but important issues may be missed. |
| Missed issue | More context / aggregation | Cost, latency, and attention dilution may increase. |
| Wrong API/type assumption | Add project context | Context size and complexity increase. |

## Evidence Sources from Papers

| Paper | Useful Failure Types |
|---|---|
| P01 — DeepCRCEval | Vague, non-actionable, low-quality, context-inadequate comments. |
| P02 — HalluJudge | Hallucinated, unsupported, context-misaligned, wrong API/type assumption. |
| P03 — RovoDev | Noisy, vague, non-specific, non-actionable, factually incorrect, context-missing comments. |
| P04 — SWE-PRBench | Missed human-flagged issues, fabricated issues, context-induced failures. |
| P05 — SWRBench | Missed functional/non-functional issues, uncovered ground-truth issues, invalid review points. |
| P06 — ContextCRBench | Missing semantic context, outdated/malformed/low-value samples, coarse-grained failures. |
| P07 — RevMate | Rejected comments, valuable-but-not-accepted comments, irrelevant filtered comments, poor value-to-time comments. |

## Open Taxonomy Questions

- [ ] Should hallucination and unsupported claim be one category or separate categories?
- [ ] Should low-value nitpicks be treated as harmful, or only harmful under time pressure?
- [ ] How should we classify a comment that is incorrect but points to a useful area?
- [ ] Should “missed issue” be part of comment taxonomy or review-level coverage taxonomy?
- [ ] How should we distinguish “grounded but useless” from “ungrounded but plausible”?
- [ ] How should we classify comments that are useful as internal tips but not accepted directly?

## Working Claim

A good evaluation framework should not only decide whether a generated comment is good or bad. It should identify the failure type because different failure types imply different causes, metrics, and mitigation trade-offs.