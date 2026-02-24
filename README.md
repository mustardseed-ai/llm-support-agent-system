# llm-support-agent-system

A minimal, production-minded **LLM support agent** demo focused on reliability: structured outputs, validation, fallbacks, logging, and evaluation.

This project is intentionally small and practical.  
I build in iterations:

**learn → ship → observe failures → unlearn assumptions → improve**

---

## Problem

Customer support at scale requires systems that are:

- **Reliable** (do not break downstream tooling)
- **Safe** (reduce hallucinations and incorrect claims)
- **Resilient under real constraints** (ambiguous phrasing, poor connectivity, mixed language, low literacy)

For financial systems, incorrect confidence is worse than safe escalation.

---

## What this repository demonstrates

- An agent workflow:  
  **Intent → Retrieve → Generate → Validate → Fallback**
- Strict **JSON output contracts**
- Schema validation and defensive fallbacks
- Logging to `.jsonl` for monitoring
- Basic reliability metrics computation
- A repeatable batch test set simulating messy real-world inputs

---

## Architecture (v1)

1. **Intent classification** (rule-based baseline)
2. **Retrieval** from a lightweight knowledge base (RAG-lite)
3. **Structured response generation**
4. **Validation** (schema enforcement)
5. **Fallback** for unknown/ambiguous cases
6. **Logging + metrics computation**

This design intentionally separates logic into small, debuggable stages.

---

## Folder Structure

data/ → Knowledge base (RAG-lite)
examples/ → Realistic test inputs
logs/ → JSONL run logs (not version-controlled)
prompts/ → Prompt scaffolding (future extension)
utils/ → Validation helpers
main.py → Pipeline + batch runner
evaluation.md → Evaluation philosophy and failure modes
