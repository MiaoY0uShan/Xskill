# Xskill design

Xskill is a portable execution discipline layer for AI coding agents.

It is not a CLI, runtime, database, package manager, or automatic executor.

## Product principle

Users should only need to say:

```text
Xskill: <task or idea>
```

Xskill should decide the workflow.

## Main loop

```text
Xskill trigger
→ router
→ Idea Cards, if needed
→ Compiled Execution Brief
→ bounded execution
→ Evidence Ledger
→ Metrics Report
→ Adaptive Improvement
→ Schema Memory
```

## Why a router exists

Earlier versions required the user to know the internal workflow.

That is too hard.

The router hides the internal skill structure and decides what to use.

## Idea Cards

Idea Cards are used when the user does not know the real requirement yet.

They prevent the agent from asking a long questionnaire too early.

They give the user three close implementation paths to choose from.

## Estimated budgets

Xskill estimates the Context Budget Contract instead of asking the user to fill it out.

Every estimate must include confidence and assumptions.

## Portable boundary

Xskill remains portable:

```text
No CLI
No npm
No npx
No pip
No database
No runtime
No automatic executor
```
