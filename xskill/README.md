# Xskill Bundle

This folder is the portable Xskill skill bundle.

Xskill is a task compiler for AI coding agents. Its primary output is a compiled **Execution Brief** with a Context Budget Contract, Context Diet Map, and Evidence Ledger handoff.

## Skills

```text
question-requirements/     find the real goal, Five Whys, failure paths
delete-scope/              reduce to MVP using first principles and Occam's Razor
semantic-architecture/     sketch MVP module boundaries and coupling risks
optimize-path/             select the smallest stable route and compile the brief
shorten-iteration/         split large or failed routes into TDD micro-loops and failure protocol
evidence-ledger/           record proof after execution
metrics/                   measure TVP, context load, scope creep, verification, and rework
adaptive-improvement/      improve only from evidence-backed patterns
schema-memory/             store reusable work schemas, not raw context
```

## Main workflow

```text
user task
  ↓
question-requirements
  ↓
delete-scope
  ↓
semantic-architecture, when needed
  ↓
optimize-path
  ↓
shorten-iteration, when needed
  ↓
compiled execution brief
  ↓
agent execution
  ↓
evidence-ledger
  ↓
metrics, when measurement matters
  ↓
adaptive-improvement
  ↓
schema-memory
```

## Primary templates

```text
templates/compiled-execution-brief.md
templates/context-budget-contract.md
templates/context-budget-contract.json
templates/context-diet-map.md
templates/failure-to-smaller-task-protocol.md
templates/evidence-ledger.md
templates/metrics-report.md
templates/adaptive-improvement-report.md
templates/schema-memory-card.md
```

## Four differentiators

```text
Context Budget Contract       hard limits on reading, touching, notes, and scope
Evidence Ledger               every agent claim needs evidence
Failure-to-Smaller Protocol   failed work shrinks into smaller verified tasks
Context Diet Map              memory used to remove context, not add it
```

## Recommended use

Ask your agent:

```text
Use Xskill to compile this task into an Execution Brief before editing code:
<task>
```

The agent should produce one final brief before touching code.

If the task is large, ask:

```text
Use Xskill end to end: question, delete, architecture if needed, optimize, shorten if needed, then produce one compiled Execution Brief with a Context Budget Contract and Context Diet Map.
```

## Rule

Do not use Xskill to create long planning documents. Use it to create the shortest safe execution contract.
