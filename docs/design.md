# Xskill design

Xskill is a portable execution discipline layer for AI coding agents.

It is not a CLI, runtime, database, package manager, or automatic executor.

## Product principle

Users should only need to say:

```text
Xskill: <task or idea>
```

Xskill should decide the workflow and keep the process weight proportional to the task.

## Main loop

```text
Xskill trigger
-> router
-> smallest useful brief
-> bounded execution
-> evidence
-> optional metrics or learning
```

## Routing levels

- Small change -> 3-5 line brief plus validation result.
- Medium task -> compact Execution Brief plus Evidence Ledger.
- Large, vague, architectural, or risky task -> Idea Cards or full chain, then compact Execution Brief and Evidence Ledger.
- Protocol or agent-behavior change -> confirm intent and boundaries before editing.

## Why a router exists

Earlier versions required the user to know the internal workflow.

That is too hard.

The router hides the internal skill structure and decides what to use.

## Idea Cards

Idea Cards are used when the user does not know the real requirement yet.

They prevent the agent from asking a long questionnaire too early.

They give the user three close implementation paths to choose from.

## Estimated budgets

Use explicit budgets only when the task is medium or large enough for budget risk to matter.

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
