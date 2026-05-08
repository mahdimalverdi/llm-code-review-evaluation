# Trade-off Framework

This file develops the trade-off-aware evaluation argument.

## Core Trade-offs

- Reducing hallucinated comments vs preserving useful comments
- Increasing context vs increasing noise and cost
- Higher precision vs lower review coverage
- Automated filtering vs human escalation
- Better quality gates vs higher latency
- Offline benchmark performance vs production workflow impact

## Working Claim

Current evaluations often ask whether an LLM-generated review comment is good, but they less often ask what is lost when we filter, suppress, or rewrite comments. A trade-off-aware framework should measure both error reduction and useful-feedback preservation.
