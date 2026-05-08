# Context Quality

This file tracks how papers treat context in LLM-based code review.

## Initial Questions

- What context is provided to the model?
- Is the context relevant, complete, and consistent?
- Does more context improve or degrade review quality?
- Can low-quality context cause hallucination or irrelevant comments?
- Should context quality be evaluated before generation, after generation, or both?

## Working Hypothesis

Context should not be treated as a simple quantity. More context can help, but it can also add noise, increase cost, and reduce review quality. A useful framework should evaluate context quality, not just context size.
