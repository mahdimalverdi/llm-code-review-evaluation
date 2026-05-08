# Research Gap

> [!NOTE]
> This file collects the emerging research gap from the paper notes. It should become the basis for the introduction, related-work critique, contribution statement, and methodology.

## Current Literature Movement

The analyzed papers show a clear movement in LLM-based code review evaluation:

1. **From lexical similarity to quality rubrics**  
   DeepCRCEval argues that BLEU/ROUGE-like metrics are weak because they depend on imperfect reference comments and do not capture real review-comment quality.

2. **From generated text to grounded claims**  
   HalluJudge reframes hallucination as context misalignment and checks whether generated review comments are supported by the code diff.

3. **From offline benchmarks to production workflow impact**  
   RovoDev Code Reviewer evaluates a deployed system using code resolution, PR cycle time, reduction in human-written comments, and developer feedback.

4. **From generic coding benchmarks to PR-level review feedback**  
   SWE-PRBench evaluates whether models catch issues that human reviewers flagged in real pull requests and shows that adding more context can degrade performance.

5. **From fine-grained snippets to PR-centric and project-aware benchmarks**  
   SWRBench and ContextCRBench argue that realistic automated code review evaluation needs PR-level tasks, project context, semantic context, and data-quality filtering.

6. **From offline labels to live reviewer behavior**  
   The RevMate user study shows that acceptance, perceived value, reviewer overhead, and downstream patch revision are distinct evaluation signals.

## Core Gap

Recent work improves evaluation along several dimensions, but these dimensions remain fragmented. Existing studies do not yet provide a unified framework that jointly evaluates:

- **context quality**, not just context size, full-project availability, or number of retrieved files;
- **data quality**, especially in benchmarks built from noisy review data;
- **problematic comment types**, not just aggregate model performance;
- **grounding and hallucination**, not just fluency or relevance;
- **actionability and practical usefulness**, not just semantic similarity to human comments;
- **acceptance and perceived value**, without collapsing them into correctness;
- **preservation of useful feedback**, especially when filters, gates, or aggregation strategies are applied;
- **false-positive and false-negative consequences** of automated quality gates;
- **human annotation and user-study validity**, including expertise, agreement, protocol, and conflict resolution;
- **cost, latency, reviewer overhead, escalation, and workflow impact** in realistic review settings.

## Why the Gap Matters

A code review assistant can fail in several different ways that are easy to collapse under a single “quality” score:

- It can produce a hallucinated comment.
- It can produce a technically grounded but useless comment.
- It can produce a correct but non-actionable comment.
- It can miss the actual issue human reviewers would flag.
- It can be filtered too aggressively and suppress useful comments.
- It can use more context while performing worse because the added context increases noise or attention load.
- It can improve benchmark scores while failing to improve developer workflow.
- It can be rejected by a reviewer but still provide useful development insight.
- It can reduce visible noise while hiding the cost of wrong removals.

These failures imply that evaluation should not only ask whether a generated comment is good. It should also ask what kind of failure occurred, what caused it, and what trade-off a mitigation strategy introduces.

## Candidate Research Problem

Current LLM-based code review evaluation lacks a trade-off-aware framework for assessing generated review comments under varying context quality, problematic comment types, and filtering/gating decisions.

More specifically, current work lacks a systematic way to answer:

- Which problematic comment types occur in LLM-generated code review?
- Which failures are caused or amplified by poor context quality?
- How should we evaluate comments that are grounded but low-value?
- How much useful feedback is lost when stricter hallucination, relevance, or actionability filters are applied?
- When should a generated comment be shown, suppressed, rewritten, aggregated, or escalated to a human?
- How should controlled annotation, benchmark issue coverage, and live reviewer feedback be combined?

## Research Questions

| RQ | Question | Expected Output |
|---|---|---|
| RQ1 | What types of problematic comments appear in LLM-generated code review? | Problematic-comment taxonomy |
| RQ2 | How is context quality defined, used, or ignored in current LLM-based code review evaluation? | Context-quality model |
| RQ3 | Which evaluation dimensions are covered or missing in current studies? | Evaluation-dimension matrix |
| RQ4 | What trade-offs arise when generated review comments are filtered, gated, aggregated, or enriched with context? | Trade-off matrix |
| RQ5 | What should a trade-off-aware evaluation framework for LLM-generated code review comments include? | Final evaluation framework |

## Possible Contribution

A strong contribution direction is:

> A taxonomy and trade-off-aware evaluation framework for LLM-generated code review comments, with special attention to context quality and the consequences of filtering, aggregating, suppressing, rewriting, or escalating generated comments.

This contribution can include:

- a taxonomy of problematic code review comments;
- a context-quality model for code review automation;
- an evaluation matrix separating correctness, grounding, usefulness, actionability, acceptance, coverage, and workflow impact;
- a trade-off matrix for filtering/gating/aggregation decisions;
- guidelines for human annotation, user-study design, and agreement reporting;
- a mapping from current papers to missing evaluation dimensions.

## What This Is Not

To avoid weak positioning, the contribution should **not** be framed as:

- just another comparison of LLMs for code review;
- just another benchmark leaderboard;
- just another hallucination detector;
- just another rubric like DeepCRCEval;
- just another RAG/context expansion method;
- just a generic survey of LLMs for software engineering.

The stronger framing is that existing methods each cover one part of the evaluation problem, but the field still lacks a framework for reasoning about the trade-offs between quality, context, filtering, cost, and developer value.

## Evidence from Current Papers

| Evidence | Supporting Papers | Interpretation |
|---|---|---|
| Text-similarity metrics are insufficient | P01, P03 | Evaluation needs task-specific and developer-facing criteria. |
| Hallucination can be framed as context misalignment | P02 | Generated comments should be checked against available review context. |
| Production metrics matter | P03 | Offline quality does not fully capture workflow impact. |
| More context can hurt | P04 | Context quality must be evaluated, not assumed. |
| Full project context improves benchmark realism | P05 | Realistic evaluation needs project-level information, but still needs context-quality controls. |
| Semantic and code context enrichment can help | P06 | Context is useful when selected, filtered, and structured carefully. |
| Human feedback is useful but noisy | P03, P04, P05, P07 | Human review comments, structured ground truth, acceptance, and value signals are realistic but imperfect. |
| Gates and filters exist but trade-offs are under-modeled | P02, P03, P07 | We need to evaluate both caught errors and lost useful comments. |
| Acceptance is not usefulness | P07 | A comment can be valuable even if not directly accepted. |

## Methodological Implication

The method should be described as a **focused evidence synthesis**, not as a simple literature summary. The analysis pipeline is:

```text
Paper selection
  → structured coding using the template
  → extraction of evaluation dimensions
  → extraction of problematic comment types
  → extraction of context-quality dimensions
  → extraction of trade-offs
  → cross-paper synthesis
  → taxonomy + framework + trade-off matrix
```

## Next Steps

- [ ] Add more evidence from papers about hallucination, RAG, and context selection.
- [ ] Add more evidence from papers about human annotation protocols and inter-rater reliability.
- [ ] Add more evidence from industrial deployment studies beyond Atlassian and Mozilla/Ubisoft if available.
- [ ] Convert this gap into a concise introduction paragraph.
- [ ] Convert this gap into a related-work critique section.
- [ ] Refine the candidate research questions after 8–10 papers.
- [ ] Decide whether to add a small illustrative mini-validation.