# Xskill Design

Xskill is a portable skill bundle for context-budgeted AI coding.

It is intentionally not a CLI, package manager workflow, autonomous runtime, database, or multi-agent system.

## Core thesis

AI coding agents usually fail by expanding context, expanding scope, and claiming completion without evidence.

Xskill counters this with:

- requirement challenge
- first-principles scope deletion
- MVP semantic architecture
- small-batch implementation path
- TDD micro-loops
- evidence ledger
- adaptive improvement
- schema memory

## Workflow

```text
question-requirements
→ delete-scope
→ semantic-architecture
→ optimize-path
→ shorten-iteration
→ evidence-ledger
→ adaptive-improvement
→ schema-memory
```

Small tasks do not need the full chain.

## Skill boundaries

### question-requirements

Find the real goal with Five Whys and inversion. Do not plan implementation.

### delete-scope

Use first principles and Occam's Razor to reduce the real goal to an MVP nucleus. Do not design the full system.

### semantic-architecture

Sketch module boundaries from the MVP. Do not expand scope or build a graph database.

### optimize-path

Select the smallest stable implementation path using small-batch, agile, lean, and minimal safety-buffer filters. Do not slice every task.

### shorten-iteration

Split large or failed selected paths into TDD micro-loops. Do not redefine product goals.

### evidence-ledger

Record what happened. It is the source of truth for completion and later learning.

### adaptive-improvement

Turn evidence into feedback, schema updates, checklist improvements, or automation candidates. Do not modify skills automatically.

### schema-memory

Store reusable task patterns, not raw context. Schema memory should make future work smaller, safer, and easier to verify.

## Adaptive improvement loop

```text
evidence ledger
→ adaptive improvement report
→ schema memory card
→ future execution brief
```

Promotion requires evidence.

Rules:

1. No evidence, no learning.
2. One run is usually not enough to promote a rule.
3. Repetition before automation.
4. Stability before automation.
5. Prefer schema memory over raw memory.
6. Prefer small checklist improvements over new skills.
7. Do not add process unless it reduces context, narrows scope, improves verification, or prevents repeated failure.

## Memory model

Xskill uses schema memory instead of semantic memory.

Semantic memory stores facts and context.

Schema memory stores reusable patterns:

- task trigger
- common failure modes
- recommended path
- context budget pattern
- verification pattern
- files or modules usually avoided
- stop conditions

This keeps Xskill aligned with its main goal: less context, smaller changes, verified progress.
