---
name: xskill
description: Use before non-trivial coding work to compile a vague task into a bounded, verifiable Execution Brief with a Context Budget Contract, Context Diet Map, Failure-to-Smaller-Task Protocol, Evidence Ledger, Metrics Report, Adaptive Improvement, and Schema Memory handoff.
---

# Xskill

Xskill is an agent-agnostic execution discipline layer.

Use it to compile vague coding tasks into a short, bounded, verifiable **Compiled Execution Brief**.

Do not use Xskill to create long planning documents. Use it to create the shortest safe execution contract.

## Primary protocol

```text
user task
→ question-requirements
→ delete-scope
→ semantic-architecture, when needed
→ optimize-path
→ shorten-iteration, when needed
→ compiled execution brief
→ bounded execution
→ evidence-ledger
→ metrics, when measurement matters
→ adaptive-improvement
→ schema-memory
```

## Core artifacts

Always produce these for meaningful tasks:

1. **Compiled Execution Brief**
2. **Context Budget Contract**
3. **Context Diet Map**
4. **Evidence Ledger**

When a task fails, blocks, or exceeds budget, also produce:

5. **Failure-to-Smaller-Task Protocol**

When measuring quality, also produce:

6. **Metrics Report**

## How to use the bundled references

The detailed Xskill modules live under `references/xskill/`:

- `question-requirements/` — Five Whys, inversion, true goal, decision gate
- `delete-scope/` — first principles, Occam's Razor, MVP nucleus
- `semantic-architecture/` — MVP module boundaries and coupling risks
- `optimize-path/` — small-batch path, agile increment, lean waste removal, compiled brief
- `shorten-iteration/` — TDD micro-loops and failure-to-smaller-task protocol
- `evidence-ledger/` — evidence audit after execution
- `metrics/` — TVP, scope creep, verification rate, rework, context load
- `adaptive-improvement/` — evidence-backed improvement loop
- `schema-memory/` — reusable task patterns, not raw context

Use only the modules needed for the current task. Do not load every reference by default.

## Start here

When the user says "Use Xskill" or the task is non-trivial, do this:

1. Use `references/xskill/question-requirements/SKILL.md` to identify the real goal.
2. Use `references/xskill/delete-scope/SKILL.md` to reduce the work to an MVP nucleus.
3. Use `references/xskill/semantic-architecture/SKILL.md` only if the MVP spans multiple modules.
4. Use `references/xskill/optimize-path/SKILL.md` to select the smallest stable path and compile the final brief.
5. Use `references/xskill/shorten-iteration/SKILL.md` only if the route is too large or has already failed.
6. Execute only after the Compiled Execution Brief is complete.
7. Use `references/xskill/evidence-ledger/SKILL.md` after execution.
8. Use `references/xskill/metrics/SKILL.md` if quality is being measured.
9. Use `references/xskill/adaptive-improvement/SKILL.md` and `references/xskill/schema-memory/SKILL.md` only after evidence exists.

## Hard rules

- Do not read broad context by default.
- Do not expand scope without revising the Context Budget Contract.
- Do not touch files outside the declared scope unless the brief is revised.
- Do not claim completion without evidence.
- If the run fails, split smaller instead of retrying blindly.
- Xskill learns from evidence, not confidence.
