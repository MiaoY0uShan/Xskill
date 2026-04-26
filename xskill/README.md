# Xskill bundle

This folder contains the Xskill portable skill bundle.

Users should not call internal skills manually.

Default behavior:

```text
For non-trivial coding tasks, activate Xskill proactively before editing code.
```

Manual override:

```text
Xskill: <task or idea>
```

The top-level router is `SKILL.md`.

It decides whether to produce Idea Cards, question requirements, delete scope, sketch architecture, optimize path, shorten iteration, or request evidence.

## Internal skills

```text
question-requirements/
delete-scope/
semantic-architecture/
optimize-path/
shorten-iteration/
evidence-ledger/
metrics/
adaptive-improvement/
schema-memory/
```

## Key artifacts

```text
Idea Cards
Compiled Execution Brief
Context Budget Contract
Context Diet Map
Failure-to-Smaller-Task Protocol
Evidence Ledger
Metrics Report
Adaptive Improvement Report
Schema Memory Card
```

## Rule

The agent should produce a Compiled Execution Brief before non-trivial code edits.

If the user input is vague, the agent should produce 3 Idea Cards first.
