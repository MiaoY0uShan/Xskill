# Xskill bundle

This folder contains the Xskill portable skill bundle.

Users should not call internal skills manually.

Default trigger:

```text
Xskill: <task or idea>
```

The top-level router is:

```text
SKILL.md
```

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

The agent should produce a Compiled Execution Brief before editing code.

If the user input is vague, the agent should produce 3 Idea Cards first.
