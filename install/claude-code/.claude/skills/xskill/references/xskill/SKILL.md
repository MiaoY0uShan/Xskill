---
name: xskill
description: Use proactively before non-trivial coding tasks to create a bounded, evidence-backed Execution Brief. Do not wait for the user to say "Xskill". Manual override: "Xskill: <task or idea>".
---

# Xskill

Xskill is the proactive execution discipline layer for AI coding agents.

Use Xskill **before editing code** when the user asks for non-trivial coding work.

Do **not** wait for the user to say `Xskill`.

`Xskill: <task or idea>` is only a manual override when the user wants to force Xskill.

## Default behavior

When the user asks for a non-trivial coding task, activate Xskill and produce the right planning artifact before code is edited.

For a clear task, first respond with:

```text
I’ll use Xskill to create a bounded Execution Brief before editing code.
```

Then produce a **Compiled Execution Brief**.

For a vague idea, first respond with:

```text
This idea is broad. I’ll use Xskill Idea Cards first.
```

Then produce **3 Idea Cards**.

## Automatic trigger

Use Xskill proactively when the user asks you to:

- modify code
- fix a bug
- add a feature
- refactor
- change repository structure
- change installation flow
- change agent instructions
- write or update tests
- touch multiple files
- make an architecture decision
- perform work that needs verification
- perform a task where scope, context, or evidence matters

If unsure whether to use Xskill, run a **lightweight Xskill pass** instead of skipping it.

## Do not trigger for

Do not run the full Xskill flow for:

- trivial typo fixes
- obvious one-line formatting edits
- pure explanation or Q&A
- casual discussion
- throwaway experiments
- tasks where the user explicitly says not to use Xskill

For tiny edits, use a minimal brief with only:

```text
Task
Scope boundary
Files to touch
Check
Evidence required
```

## Manual trigger

The user may still write:

```text
Xskill: <task or idea>
```

Treat this as an explicit instruction to use Xskill even if the task looks small.

If the user writes only:

```text
Xskill
```

ask:

```text
What task should I compile with Xskill?
```

## Router

### A. Vague idea or unclear requirement

Use this when the user gives a broad, partial, emotional, or exploratory idea.

Action:

1. Generate **3 Idea Cards**.
2. Each card should be close to the user's likely intent.
3. Each card must include interpretation, MVP, best for, tradeoff / risk, estimated Context Budget Contract, and recommended workflow.
4. Ask the user to choose `A`, `B`, `C`, `merge A+B`, or `none, generate 3 new cards`.

Do not continue into implementation until the user selects a path, unless one path is overwhelmingly obvious and low risk.

### B. Clear small implementation task

Use `optimize-path`, estimate a Context Budget Contract, and produce a Compiled Execution Brief.

### C. Clear but non-trivial task

Use `question-requirements` if the real goal or success criteria are uncertain, then `delete-scope`, `optimize-path`, and `shorten-iteration` if needed. Produce a Compiled Execution Brief.

### D. Large or multi-module task

Use `question-requirements` → `delete-scope` → `semantic-architecture` → `optimize-path` → `shorten-iteration`, then produce a Compiled Execution Brief.

### E. Failed or blocked task

Use `evidence-ledger` if evidence exists, then the `Failure-to-Smaller-Task Protocol`, then `shorten-iteration`, then produce a smaller Compiled Execution Brief with a new verification command.

### F. Completed task

Use `evidence-ledger`, `metrics` if measurement matters, `adaptive-improvement`, and `schema-memory` only if there is a reusable pattern backed by evidence.

## Context Budget estimation

The user should not have to fill out a budget manually.

Estimate the Context Budget Contract yourself using task type and risk.

Always mark:

```text
budget_type: estimated
confidence: low | medium | high
```

If the task needs a larger budget, split it instead of expanding the first contract.

## Default output

For vague ideas, output **Idea Cards** first.

For selected or clear tasks, output a **Compiled Execution Brief** with Task, Real Goal, MVP Scope, Must Not Do, Estimated Context Budget Contract, Context Diet Map, Files To Read, Files To Touch, Files To Avoid, Checks, Evidence Required, Max Scope, Stop Condition, and Handoff.

## Hard rules

- Do not edit code before producing the brief.
- Do not load every internal Xskill module by default.
- Use only the modules required by the task.
- Estimate the Context Budget Contract yourself.
- Respect files to read, files to touch, and files to avoid.
- If the task is vague, generate Idea Cards before asking many questions.
- If blocked or over budget, split the work smaller instead of retrying the same task.
- No evidence, no done.
- Xskill learns from evidence, not confidence.
