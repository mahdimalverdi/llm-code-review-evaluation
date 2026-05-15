# Background and Motivation

TODO: Write this section before expanding the framework.

This section should prepare the reader without jumping directly into the proposed taxonomy.

Suggested structure:

## Modern Code Review

- Code review as defect detection, maintainability, knowledge sharing, and coordination.
- Why review comments are not only technical assertions.
- Key citations: [@p37_sadowski2018_google_mcr; @p38_bacchelli2013_expectations_mcr; @p39_bosu2015_useful_reviews].

## LLM-Based Code Review Assistance

- Generated review comments.
- Review-comment classification.
- Retrieval/context-augmented review.
- Specification-grounded review.
- Industrial systems and user studies.

## Why Evaluation Is Difficult

- Multiple valid comments may exist for the same change.
- Human reference comments are incomplete and noisy.
- A comment can be correct but low value.
- A comment can be useful but not directly acceptable.
- A comment can be plausible but unsupported.

## Trade-Offs as the Main Motivation

- Error reduction vs useful-feedback preservation.
- More context vs noise and cost.
- Filtering vs review coverage.
- LLM-as-a-Judge scalability vs evaluator validity.
