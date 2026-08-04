# ARXIV-0007 extraction packet

- Title: Cross-Model LLM Code Review: Should you use Claude to review Codex or vice versa?
- arXiv: 2607.21656v1
- Authors: Zuodong Xiang; Yike Zhang; YueMing Zhang; Hailu Xu
- Full text: `data/search/provisional-extraction/supporting/ARXIV-0007.txt`
- Screening tier: supporting

## Required extraction

1. Purpose: evaluates whether assigning different LLMs to writing and reviewing improves the final program.
2. System/context: Claude Opus 4.7 and Codex GPT-5.5; reviewer receives the problem and writer draft but cannot execute tests.
3. Study design: controlled experiment on 116 medium and hard LiveCodeBench tasks across solo, cross-model, and same-model conditions.
4. Problematic risks: regressions, worse revisions, and added cost/latency are identified as risks; a full comment-level taxonomy is not reported.
5. Metrics/results: Claude reviewing Codex raises pass rate from 71.6% to 89.7%; Codex reviewing Claude lowers pass rate from 91.4% to 82.8%; reported significance uses BH-adjusted tests.
6. Trade-off: cross-model review is asymmetric; a second review pass can improve correctness in one direction but reduce it in another while adding cost and latency.
7. Limitations: benchmark tasks, no test execution during review, and final-program pass rate do not directly measure comment grounding, usefulness, or developer workflow. Quality score: provisional, medium.
8. Synthesis claim: supporting evidence for reviewer-model assignment, asymmetric mitigation effects, and cost-aware evaluation of multi-agent review.
