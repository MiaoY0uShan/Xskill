# Xskill bundle

This folder contains the Xskill portable skill bundle.

Users should not call internal skills manually.

Default behavior:

```text
For coding tasks, activate Xskill proactively before editing code and choose the lightest useful path.
```

Manual override:

```text
Xskill: <task or idea>
```

The top-level router is `SKILL.md`.

It decides whether to use a tiny brief, a compact Execution Brief plus Evidence Ledger, Idea Cards, or the full chain.

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
Tiny Brief
Execution Brief
Evidence Ledger
Idea Cards
Failure-to-Smaller-Task Protocol
Metrics Report
Adaptive Improvement Report
Schema Memory Card
```

## Rule

Small changes should get a 3-5 line brief and validation result.

Medium changes should get an Execution Brief and Evidence Ledger.

Large, vague, architectural, or risky tasks should use the full chain.

Protocol or agent-behavior changes should confirm intent and boundaries before editing, unless the user explicitly says to implement already-discussed feedback.
