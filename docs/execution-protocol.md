# Xskill Execution Protocol

User-facing protocol:

```text
Xskill: <task or idea>
```

Internal protocol:

```text
task or idea
→ router
→ idea cards, if vague
→ brief
→ bounded execution
→ evidence
→ metrics
→ improvement
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

## Vague input

If the user gives an unclear idea, produce 3 Idea Cards.

Each card contains:

- interpretation
- MVP
- best for
- risk / tradeoff
- estimated Context Budget Contract
- recommended workflow

After the user chooses, continue the workflow.

## Clear task

If the task is already specific, produce a Compiled Execution Brief.

## Completion

After execution:

1. Create an Evidence Ledger.
2. Create a Metrics Report if measurement matters.
3. Use Adaptive Improvement only from evidence.
4. Update Schema Memory only for reusable repeated patterns.

## Boundary

Xskill is not a runtime.

It does not execute commands, edit files automatically, store database state, or run background loops.
