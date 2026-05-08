# Research Gap

> [!NOTE]
> This file collects the emerging research gap from the paper notes. It should become the basis for the introduction, related-work critique, and contribution statement.

## Current Literature Movement

The first four analyzed papers show a clear movement in LLM-based code review evaluation:

1. **From lexical similarity to quality rubrics**  
   DeepCRCEval argues that BLEU/ROUGE-like metrics are weak because they depend on imperfect reference comments and do not capture real review-comment quality.

2. **From generated text to grounded claims**  
   HalluJudge reframes hallucination as context misalignment and checks whether generated review comments are supported by the code diff.

3. **From offline benchmarks to production workflow impact**  
   RovoDev Code Reviewer evaluates a deployed system using code resolution, PR cycle time, reduction in human-written comments, and developer feedback.

4. **From generic coding benchmarks to PR-level review feedback**  
   SWE-PRBench evaluates whether models catch issues that human reviewers flagged in real pull requests and shows that adding more context can degrade performance.

## Core Gap

Recent work improves evaluation along several dimensions, but these dimensions remain fragmented. Existing studies do not yet provide a unified framework that jointly evaluates:

- **context quality**, not just context size or number of retrieved files;
- **problematic comment types**, not just aggregate model performance;
- **grounding and hallucination**, not just fluency or relevance;
- **actionability and practical usefulness**, not just semantic similarity to human comments;
- **preservation of useful feedback**, especially when filters or gates are applied;
- **false-positive and false-negative consequences** of automated quality gates;
- **human annotation validity**, including annotator expertise, agreement, and conflict resolution;
- **cost, latency, escalation, and workflow impact** in realistic review settings.

## Why the Gap Matters

A code review assistant can fail in several different ways that are easy to collapse under a single “quality” score:

- It can produce a hallucinated comment.
- It can produce a technically grounded but useless comment.
- It can produce a correct but non-actionable comment.
- It can miss the actual issue human reviewers would flag.
- It can be filtered too aggressively and suppress useful comments.
- It can require more context while performing worse because the added context increases noise.
- It can improve benchmark scores while failing to improve developer workflow.

These failures imply that evaluation should not only ask whether a generated comment is good. It should also ask what kind of failure occurred, what caused it, and what trade-off a mitigation strategy introduces.

## Candidate Research Problem

Current LLM-based code review evaluation lacks a trade-off-aware framework for assessing generated review comments under varying context quality and filtering decisions.

More specifically, current work lacks a systematic way to answer:

- Which problematic comment types occur in LLM-generated code review?
- Which failures are caused or amplified by poor context quality?
- How should we evaluate comments that are grounded but low-value?
- How much useful feedback is lost when stricter hallucination or quality filters are applied?
- When should a generated comment be shown, suppressed, rewritten, or escalated to a human?
- How should controlled annotation results be combined with production/workflow signals?

## Possible Contribution

A strong contribution direction is:

> A taxonomy and trade-off-aware evaluation framework for LLM-generated code review comments, with special attention to context quality and the consequences of filtering, suppressing, or escalating generated comments.

This contribution can include:

- a taxonomy of problematic code review comments;
- a context-quality dimension for code review automation;
- an evaluation matrix separating correctness, grounding, usefulness, actionability, and workflow impact;
- a trade-off model for filtering/gating decisions;
- guidelines for human annotation and agreement reporting;
- a mapping from current papers to missing evaluation dimensions.

## What This Is Not

To avoid weak positioning, the contribution should **not** be framed as:

- just another comparison of LLMs for code review;
- just another benchmark leaderboard;
- just another hallucination detector;
- just another rubric like DeepCRCEval;
- just another RAG/context expansion method.

The stronger framing is that existing methods each cover one part of the evaluation problem, but the field still lacks a framework for reasoning about the trade-offs between quality, context, filtering, cost, and developer value.

## Evidence from the First Four Papers

| Evidence | Supporting Papers | Interpretation |
|---|---|---|
| Text-similarity metrics are insufficient | P01, P03 | Evaluation needs task-specific and developer-facing criteria. |
| Hallucination can be framed as context misalignment | P02 | Generated comments should be checked against available review context. |
| Production metrics matter | P03 | Offline quality does not fully capture workflow impact. |
| More context can hurt | P04 | Context quality must be evaluated, not assumed. |
| Human feedback is useful but noisy | P03, P04 | Human review comments and reactions are realistic but imperfect ground truth. |
| Gates exist but trade-offs are under-modeled | P02, P03 | We need to evaluate both caught errors and lost useful comments. |

## Working Research Questions

- **RQ1:** What types of problematic comments appear in LLM-generated code review, and how can they be organized into a taxonomy?
- **RQ2:** How does context quality affect the likelihood and type of problematic generated review comments?
- **RQ3:** How do different mitigation strategies trade off between reducing problematic comments and preserving useful feedback?
- **RQ4:** Which evaluation dimensions are necessary to assess LLM-based code review beyond correctness or similarity?
- **RQ5:** How should human annotation and production feedback be combined to produce reliable evaluation results?

## Next Steps

- [ ] Add evidence from additional papers about hallucination, RAG, and context selection.
- [ ] Add evidence from papers about human annotation protocols and inter-rater reliability.
- [ ] Add evidence from industrial deployment studies beyond Atlassian if available.
- [ ] Convert this gap into a concise introduction paragraph.
- [ ] Convert this gap into a related-work critique section.
- [ ] Refine the candidate research questions after 8–10 papers.
