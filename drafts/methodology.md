# Methodology Draft

> [!NOTE]
> This is the working methodology for our paper. The method should be framed as a **focused evidence synthesis** that derives a taxonomy, evaluation framework, and trade-off matrix for LLM-generated code review comments.

## Method Type

We do not frame this work as a simple narrative review or as a benchmark/model paper. The method is a focused evidence synthesis of recent studies on LLM-based code review evaluation.

The purpose is to synthesize evidence from existing studies and derive:

1. a taxonomy of problematic LLM-generated code review comments;
2. a set of evaluation dimensions for generated review comments;
3. a context-quality model for code review automation;
4. a trade-off matrix for filtering, gating, aggregation, and human-in-the-loop decisions.

## Research Questions

| RQ | Question | Output |
|---|---|---|
| RQ1 | What types of problematic comments appear in LLM-generated code review? | Problematic-comment taxonomy |
| RQ2 | How is context quality defined, used, or ignored in current LLM-based code review evaluation? | Context-quality model |
| RQ3 | Which evaluation dimensions are covered or missing in current studies? | Evaluation-dimension matrix |
| RQ4 | What trade-offs arise when generated review comments are filtered, gated, aggregated, or enriched with context? | Trade-off matrix |
| RQ5 | What should a trade-off-aware evaluation framework for LLM-generated code review comments include? | Final framework |

## Paper Selection Strategy

We conduct a focused literature review of recent papers on LLM-based code review evaluation. We prioritize papers that include at least one of the following:

- evaluation of generated code review comments;
- hallucination, unsupported-claim, or context-alignment analysis;
- PR-level, benchmark-level, or production-level evaluation;
- human/user-study evaluation of generated review comments;
- cost, latency, reviewer-overhead, or workflow-related metrics;
- filtering, gating, aggregation, or LLM-as-a-Judge mechanisms;
- context selection, retrieval, or context-enrichment mechanisms for code review.

### Inclusion Criteria

A paper is included if it satisfies at least one of these criteria:

- It evaluates LLM-generated code review comments or review outputs.
- It proposes or evaluates a benchmark for code review automation.
- It studies hallucination, grounding, or context alignment in generated review comments.
- It reports human, user-study, or production signals for LLM-based code review.
- It discusses context, retrieval, or project-level information for code review.
- It evaluates filtering, gating, judging, or aggregation of generated comments.

### Exclusion Criteria

A paper is excluded if:

- it studies general code generation without code review evaluation;
- it studies program repair or bug fixing without review comments or review workflow;
- it only proposes a model without evaluation dimensions relevant to review comments;
- it is too far from LLM-based code review or automated code review;
- it provides no usable evidence for taxonomy, context quality, evaluation dimensions, or trade-offs.

## Coding Protocol

Each paper is coded using the repository paper-analysis template.

For each paper, we extract:

- bibliographic metadata;
- study type and contribution type;
- dataset/study context;
- input context available to the model or evaluator;
- output being evaluated;
- models, systems, prompts, and context strategies;
- evaluation metrics and methods;
- human annotation, user-study, or production-feedback protocol;
- covered and missing evaluation dimensions;
- explicitly defined and inferred problematic comment types;
- context-quality dimensions and context failure types;
- filtering, gating, aggregation, or escalation trade-offs;
- limitations from the paper’s perspective;
- limitations from our perspective;
- evidence relevant to our research questions.

## Coding Labels

We use the following labels to separate evidence from interpretation:

| Label | Meaning |
|---|---|
| `Reported` | Explicitly stated in the paper. |
| `Inferred` | Reconstructed from examples, tables, results, or implications. |
| `Our perspective` | Our critique, synthesis, or research positioning. |
| `Not reported` | The paper does not provide this information. |
| `Not applicable` | The field does not fit the paper. |
| `Partially` | The paper touches the dimension but does not operationalize it clearly. |

This distinction is important because our framework should not overclaim what individual papers actually report.

## Cross-Paper Synthesis Process

After coding individual papers, we synthesize them in three steps.

### Step 1 — Within-paper extraction

Each paper is analyzed using the template. Evidence is extracted for taxonomy, context quality, evaluation dimensions, and trade-offs.

### Step 2 — Cross-paper comparison

We compare papers across recurring dimensions:

- what they evaluate;
- what context they provide;
- what failure types they observe;
- what human or production signals they use;
- what costs or workflow effects they measure;
- which dimensions they omit.

### Step 3 — Framework construction

We derive a framework that connects:

```text
Context Quality
      ↓
Generated Review Comment
      ↓
Problematic Comment Type
      ↓
Evaluation Dimension
      ↓
Mitigation Strategy
      ↓
Trade-off / Cost / Workflow Impact
```

## Main Analytical Distinctions

### Evaluation dimensions vs problematic comment types

We keep evaluation dimensions and failure types separate.

Examples of evaluation dimensions:

- correctness;
- relevance;
- grounding;
- usefulness;
- actionability;
- specificity;
- coverage;
- cost;
- latency;
- workflow impact.

Examples of problematic comment types:

- hallucinated comment;
- unsupported claim;
- irrelevant comment;
- non-actionable comment;
- vague comment;
- low-value nitpick;
- wrong API/type assumption;
- missed issue;
- technically plausible but unsupported comment.

### Context quantity vs context quality

We distinguish context quantity from context quality.

More context can increase available evidence, but it can also increase:

- noise;
- token cost;
- latency;
- attention dilution;
- irrelevant retrieved material;
- inconsistent signals.

Therefore, context is treated as an evaluation object, not just an input configuration.

### Acceptance vs usefulness

We distinguish reviewer acceptance from usefulness.

A generated comment may be:

- accepted directly;
- edited before acceptance;
- rejected but still useful as a development or review tip;
- correct but low-priority;
- incorrect but still draws attention to a valid area;
- irrelevant and harmful.

This distinction is necessary for human-centered evaluation.

### Filtering success vs useful-feedback preservation

A filter or gate should not only be evaluated by how many problematic comments it removes. It should also be evaluated by:

- how many useful comments it wrongly removes;
- how much cost or latency it adds;
- how it affects review coverage;
- whether it creates reviewer trust or overreliance issues;
- when it should escalate to a human.

## Candidate Framework Components

The final framework should include:

1. **Context-quality assessment**
   - relevance;
   - completeness;
   - specificity;
   - consistency;
   - groundability;
   - locality;
   - freshness;
   - attention load;
   - cost.

2. **Problematic-comment taxonomy**
   - hallucination/unsupported claim;
   - context misalignment;
   - factual incorrectness;
   - non-actionability;
   - vagueness;
   - low-value nitpick;
   - missed issue;
   - wrong-location/wrong-type assumption;
   - poor value-to-time ratio.

3. **Evaluation dimensions**
   - correctness;
   - relevance;
   - grounding;
   - usefulness;
   - actionability;
   - specificity;
   - issue coverage;
   - acceptance;
   - downstream revision;
   - reviewer overhead;
   - cost/latency;
   - workflow impact.

4. **Trade-off matrix**
   - context enrichment;
   - RAG/retrieval;
   - hallucination gate;
   - actionability gate;
   - LLM-as-a-Judge;
   - human escalation;
   - multi-review aggregation;
   - live reviewer inspection.

## Optional Mini-Validation

If we decide to strengthen the paper, we can add a small validation step.

Possible design:

- sample 20–50 generated review comments from available papers or benchmarks;
- label them using our taxonomy;
- map each label to evaluation dimensions and likely mitigation strategies;
- show that a single quality score is insufficient to explain the different failure modes and trade-offs.

This should be framed as an illustrative validation, not a large empirical benchmark.

## Threats to Validity

Potential threats:

- paper selection may be incomplete;
- recent papers may change quickly;
- some analyzed papers are preprints;
- industrial studies may use proprietary data;
- inferred taxonomy items may depend on our interpretation;
- human feedback and benchmark ground truth are imperfect;
- LLM-as-a-Judge results may introduce evaluator bias.

Mitigation:

- use explicit inclusion/exclusion criteria;
- label claims as `Reported`, `Inferred`, or `Our perspective`;
- separate paper limitations from our critique;
- keep a transparent paper pool and cross-paper synthesis matrix;
- update synthesis files after every 3–5 papers.

## Current Methodological Positioning

The paper should be positioned as:

> a framework-oriented evidence synthesis of LLM-based code review evaluation, focused on context quality, problematic comment types, and trade-off-aware evaluation.

It should not be positioned as:

- a new LLM model;
- a new leaderboard benchmark;
- only a hallucination detector;
- only a RAG/context retrieval method;
- a generic survey of LLMs for software engineering.
