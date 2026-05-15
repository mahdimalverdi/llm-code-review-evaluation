# Academic English for Scientific and Technical Writing

This guide defines the writing style for all English research drafts in this repository.

The project is about trade-off-aware evaluation of LLM-generated code review comments. Because the topic combines software engineering, empirical evaluation, LLM-based systems, and research synthesis, the writing must be precise, evidence-based, and careful about claim strength.

## Goal

The goal is to produce academic English that is clear, precise, and defensible.

The writing should help the reader understand:

- what problem is being studied;
- what prior work has already shown;
- what remains fragmented or underexplored;
- why the gap matters;
- and how the proposed taxonomy or framework addresses the gap.

The writing should not sound promotional, vague, inflated, or AI-generated.

## General Principles

- Write in clear, precise, and professional academic English.
- Prefer clarity over complexity.
- Do not use inflated or promotional language.
- Do not overstate claims beyond what the evidence supports.
- Avoid unnecessary jargon. Use technical terms only when they improve precision.
- Define important terms before using them repeatedly.
- Keep the argument explicit: problem → evidence → gap → implication.
- Each paragraph should have one main idea.
- Each sentence should contribute to the argument.
- Avoid long, overloaded sentences.
- Avoid overly short, fragmented sentences unless used intentionally for emphasis.
- Prefer active voice when it improves clarity.
- Use passive voice only when the actor is unknown, irrelevant, or less important than the process.

## Tone

The tone should be:

- academic;
- analytical;
- precise;
- measured;
- critical but fair;
- evidence-based.

The tone should not be:

- promotional;
- emotional;
- exaggerated;
- conversational;
- vague;
- defensive;
- overly confident without support.

Avoid phrases such as:

```text
This paper revolutionizes...
This study proves that...
It is obvious that...
Clearly, LLMs are the future of code review...
```

Prefer careful formulations:

```text
This paper argues that...
The results suggest that...
The evidence indicates that...
Prior work has shown that...
This limitation motivates the need for...
```

## Claim Strength

Match the strength of each claim to the strength of the evidence.

Use stronger claims only when the evidence is strong:

```text
The results show that...
The study demonstrates that...
```

Use cautious claims when the evidence is limited, indirect, or based on interpretation:

```text
The results suggest that...
This may indicate that...
This finding points to...
One possible interpretation is that...
```

Use interpretive framing when the claim is our synthesis rather than a direct claim from a source:

```text
From the perspective of this study, this suggests that...
We interpret this as evidence that...
Taken together, these studies indicate that...
```

## Technical Terminology

Use technical terms consistently.

When introducing a key term, define it briefly:

```text
We use context quality to refer to the relevance, completeness, consistency, and usability of the information provided to an LLM-based code review system.
```

Avoid using multiple terms for the same concept unless the distinction is meaningful.

For example, do not alternate between these terms unless each one is explicitly defined:

```text
context quality
context usefulness
context adequacy
context richness
```

## Paragraph Structure

Each paragraph should follow a clear structure.

Recommended pattern:

```text
Topic sentence.
Evidence or explanation.
Connection to the research problem.
Implication for our framework.
```

Example:

```text
Evaluation based only on lexical similarity is insufficient for generated code review comments. Code review comments are often semantically valid even when they differ substantially from a reference comment in wording. Prior work has therefore moved toward domain-specific evaluation dimensions such as usefulness, grounding, actionability, and developer value. This motivates an evaluation framework that treats comment quality as a multi-dimensional construct rather than a single similarity score.
```

## Related Work Writing

Do not write related work as a list of paper summaries.

Avoid:

```text
Paper A proposed X. Paper B proposed Y. Paper C proposed Z.
```

Prefer synthesis:

```text
Prior work has moved from lexical similarity metrics toward richer evaluation protocols. Early code review generation studies exposed the limitations of reference-based metrics, while later work introduced dimensions such as grounding, usefulness, actionability, and workflow impact. However, these dimensions remain fragmented across studies.
```

Related work should answer:

- What has been studied?
- What has been measured?
- What has been overlooked?
- How does this motivate our work?

## Citation Style

Every factual or literature-based claim should be supported by citations.

Use citation keys from:

```text
references/references.bib
```

Use Pandoc/Quarto-style citations:

```markdown
Prior work has shown that lexical similarity metrics are insufficient for evaluating generated code review comments [@p14_li2022_codereviewer; @p01_lu2025_deepcrceval].
```

For multiple related studies:

```markdown
Recent benchmarks have moved toward PR-level and project-aware evaluation [@p04_kumar2026_swe_prbench; @p05_zeng2025_swrbench; @p06_hu2025_contextcrbench].
```

Do not use citations as a substitute for explanation. A citation should support a claim, not replace the reasoning.

## Handling Prior Work

When discussing prior work, be fair and specific.

Avoid vague criticism:

```text
Existing work is limited.
```

Prefer precise criticism:

```text
Existing benchmarks improve realism by incorporating pull-request-level context, but they do not systematically evaluate whether the added context is relevant, consistent, or usable by the model.
```

When making a gap claim, show the contrast:

```text
While prior work studies hallucination, context enrichment, production deployment, and LLM-as-a-judge evaluation separately, it does not provide a unified framework that connects these dimensions through explicit trade-offs.
```

## Writing the Research Gap

A strong research gap should have this structure:

```text
Prior work has done X.
However, Y remains underexplored.
This matters because Z.
Therefore, this study focuses on W.
```

Example:

```text
Prior work has proposed richer metrics, PR-level benchmarks, hallucination detectors, and production evaluation signals for LLM-based code review. However, these efforts remain fragmented and rarely model the trade-offs introduced by filtering, gating, retrieval, or LLM-based judging. This matters because reducing harmful comments may also suppress useful feedback, increase reviewer overhead, or hide evaluator bias. Therefore, this study develops a trade-off-aware evaluation framework for LLM-generated code review comments.
```

## Writing Contributions

Contributions should be concrete and modest.

Avoid:

```text
This paper solves the problem of LLM code review evaluation.
```

Prefer:

```text
This paper makes three contributions. First, it synthesizes evaluation dimensions used in recent LLM-based code review studies. Second, it proposes a taxonomy of problematic generated review comments. Third, it introduces a trade-off-aware framework for evaluating filtering, gating, and human-in-the-loop decisions.
```

## Things to Avoid

Do not:

- overclaim;
- use promotional language;
- write paper-by-paper summaries without synthesis;
- introduce terms without defining them;
- mix too many concepts in one paragraph;
- cite papers without explaining their relevance;
- use “prove” unless the evidence truly proves something;
- use “significant” unless referring to statistical significance or clearly explained practical significance;
- use “novel” unless the novelty is carefully justified;
- say “no prior work” unless this has been carefully verified.

## Preferred Expressions

Use:

```text
This suggests that...
This motivates...
This highlights the need for...
This provides evidence that...
This paper argues that...
This study focuses on...
Prior work has examined...
However, these studies do not fully address...
Taken together, these findings indicate that...
```

Avoid:

```text
This obviously shows...
This completely solves...
This is very important...
Many researchers say...
LLMs are transforming everything...
```

## Final Review Checklist

Before finalizing any English academic text, check:

- Is every major claim supported by evidence or citation?
- Are all important terms defined?
- Is the claim strength appropriate?
- Is the paragraph structure clear?
- Does each paragraph advance the argument?
- Is the text analytical rather than descriptive?
- Are prior works synthesized rather than listed?
- Are limitations stated fairly?
- Are citations placed where they support specific claims?
- Is there any vague, inflated, or promotional language?
- Does the text sound like a careful research paper rather than a blog post or AI-generated summary?

## Repository Rule

All English research drafts in this repository should follow this guide. This includes:

- `drafts/*.md`
- `synthesis/*.md` when written as prose
- introductory and related-work material
- contribution and methodology sections

Internal matrices can remain compact, but any prose intended for a report, paper, proposal, or thesis should follow this guide.
