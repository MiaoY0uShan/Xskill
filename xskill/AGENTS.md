# AGENTS.md

This repository uses Xskill.

Xskill is a portable task compiler for AI coding agents. Its primary output is a compiled Execution Brief, not a long plan.

## Core rules

1. For non-trivial work, create a compiled Execution Brief before editing code.
2. Respect the Context Budget Contract.
3. Use the Context Diet Map to decide what not to read.
4. Do not touch files outside the declared scope unless the contract is revised.
5. Run the required checks.
6. Do not claim completion without an Evidence Ledger.
7. If the task fails, blocks, or exceeds budget, use the Failure-to-Smaller-Task Protocol instead of retrying blindly.
8. If measurement matters, create a Metrics Report after the Evidence Ledger.
9. Use adaptive improvement only from evidence-backed patterns.
10. Store reusable patterns as schema memory, not raw context.

## Workflow

```text
question-requirements
→ delete-scope
→ semantic-architecture, when needed
→ optimize-path
→ shorten-iteration, when needed
→ compiled execution brief
→ execution
→ evidence-ledger
→ metrics, when needed
→ adaptive-improvement
→ schema-memory
```

## Required artifacts for meaningful tasks

- Compiled Execution Brief
- Context Budget Contract
- Context Diet Map
- Evidence Ledger

If the run fails or exceeds budget, also produce:

- Failure-to-Smaller-Task Protocol

If the run is being measured, also produce:

- Metrics Report

## Do not

- Do not load long context by default.
- Do not read unrelated files just because they may be useful.
- Do not expand MVP scope without evidence.
- Do not automate confusion.
- Do not turn one-off experience into a schema.
- Do not claim success without checks or explicit evidence.
