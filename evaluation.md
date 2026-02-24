\# Evaluation



This project treats reliability as a first-class requirement. The goal is not only to produce helpful outputs, but to ensure outputs are structured, safe, and resilient under messy real-world inputs.



\## What I measure (v1)



\### 1) Schema compliance rate

\- Definition: % of runs where output contains all required fields and passes validation.

\- Why it matters: downstream tooling breaks when schema is inconsistent.



\### 2) Fallback rate

\- Definition: % of runs that trigger fallback or escalation to human support.

\- Why it matters: a safe fallback is better than a confident wrong answer.



\### 3) Latency (if model calls are added)

\- Definition: response time distribution (p50/p95).

\- Why it matters: support automation must feel instant, especially under weak connectivity.



\### 4) Hallucination flags (rule-based in v1)

\- Definition: heuristics that detect when the agent invents unsupported facts (e.g., mentions a transaction reference that was not provided).

\- Why it matters: incorrect claims destroy trust in financial products.



\## Failure modes I expect

\- Ambiguous user intent (“it failed” without details)

\- Mixed language / low literacy phrasing

\- Poor connectivity leading to partial messages

\- Schema drift (missing fields / invalid JSON)

\- Retrieval mismatch (wrong KB article)

\- Overconfident answers on insufficient context



\## How I iterate (my learning loop)

1\. Ship a minimal version

2\. Observe failures from logs

3\. Unlearn assumptions (what I thought users would say vs what they actually say)

4\. Improve prompts / retrieval / validation

5\. Re-test using the same sample inputs + new edge cases



\## Next evaluation upgrades

\- Add a fixed test set in `examples/`

\- Add regression checks (fail the run if schema compliance drops)

\- Add multilingual test cases (English + Swahili/French-style strings)

\- Add groundedness scoring once real RAG is added

