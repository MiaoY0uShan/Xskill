---
name: xskill
description: Use proactively before non-trivial coding tasks to create a bounded, evidence-backed Execution Brief. Do not wait for explicit "Xskill" invocation. Manual override: "Xskill: <task or idea>".
---

# Xskill

Xskill is the proactive execution discipline layer for AI coding agents.

Use Xskill **before editing code** when the user asks for non-trivial coding work.

Do **not** wait for the user to say `Xskill`.

`Xskill: <task or idea>` is only a manual override.

Bundled references are under:

```text
references/xskill/
```

## Automatic trigger

Use Xskill when the user asks you to modify code, fix a bug, add a feature, refactor, change repository structure, change installation flow, change agent instructions, write tests, touch multiple files, make an architecture decision, or perform work that needs verification.

## Default behavior

- Clear task → produce a Compiled Execution Brief before editing code.
- Vague idea → produce 3 Idea Cards first.
- Failed task → use Failure-to-Smaller-Task Protocol.
- Completed task → produce Evidence Ledger before claiming done.

## Manual override

```text
Xskill: <task or idea>
```

## Hard rules

1. Do not edit code before producing the brief.
2. Estimate the Context Budget Contract yourself.
3. Mark budget confidence as low, medium, or high.
4. Respect files to read, files to touch, and files to avoid.
5. If vague, generate Idea Cards before asking many questions.
6. If blocked or over budget, split smaller instead of retrying.
7. No evidence, no done.
8. Xskill learns from evidence, not confidence.
