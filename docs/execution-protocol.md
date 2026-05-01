# Xskill Execution Protocol

User-facing protocol:

```text
Xskill: <task or idea>
```

Internal protocol:

```text
task or idea
-> router
-> smallest useful brief
-> bounded execution
-> evidence
-> optional metrics or improvement
```

## Router behavior

The router decides which internal Xskill files are needed.

The user should not have to call:

```text
question-requirements
delete-scope
semantic-architecture
optimize-path
shorten-iteration
```

directly.

## Small clear change

Use a 3-5 line brief:

- task
- read/touch
- verification
- result

Do not produce a full Execution Brief or Evidence Ledger unless risk appears.

## Medium clear task

Use a compact Execution Brief before editing and a compact Evidence Ledger after verification.

## Vague, large, architectural, or risky input

Use Idea Cards or requirements clarification first. Add delete-scope, semantic-architecture, optimize-path, and shorten-iteration only when they reduce risk or scope.

## Protocol or agent-behavior change

Before editing Xskill itself, trigger rules, install boundaries, memory policy, or the default workflow:

- restate the inferred goal
- challenge unclear or risky assumptions
- list proposed files or areas
- ask for confirmation

Skip this only when the user explicitly says to implement already-discussed feedback.

## Completion

Match evidence weight to task weight:

- small change -> validation result
- medium task -> Evidence Ledger
- large/risky task -> Evidence Ledger plus metrics or learning only when useful

## Boundary

Xskill is not a runtime.

It does not execute commands, edit files automatically, store database state, or run background loops.
