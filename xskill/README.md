# Xskill Bundle

This folder is the portable Xskill skill bundle.

Xskill is a task compiler for AI coding agents. Its primary output is a compiled **Execution Brief**.

The brief tells the agent:

```text
what to do
why it matters
what not to do
which files to read
which files to touch
which files to avoid
how to verify
when to stop
what evidence is required
```

## Skills

```text
question-requirements/     find the real goal, Five Whys, failure paths
delete-scope/              reduce to MVP using first principles and Occam's Razor
semantic-architecture/     sketch MVP module boundaries and coupling risks
optimize-path/             select the smallest stable route and compile the brief
shorten-iteration/         split large or failed routes into TDD micro-loops
evidence-ledger/           record proof after execution
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
adaptive-improvement
  ↓
schema-memory
```

## Primary templates

```text
templates/compiled-execution-brief.md
templates/execution-brief.md
templates/context-budget.md
templates/evidence-ledger.md
templates/adaptive-improvement-report.md
templates/schema-memory-card.md
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
Use Xskill end to end: question, delete, architecture if needed, optimize, shorten if needed, then produce one compiled Execution Brief.
```

## Rule

Do not use Xskill to create long planning documents. Use it to create the shortest safe execution contract.
