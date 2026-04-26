# Using Xskill

Xskill is a portable skill bundle. It does not require a CLI.

## Basic flow

```text
Use Xskill question-requirements for:
<task>
```

Then:

```text
Use Xskill delete-scope after question-requirements for:
<task>
```

For larger work:

```text
Use Xskill semantic-architecture after delete-scope for:
<task>
```

Then:

```text
Use Xskill optimize-path after scope and architecture are clear for:
<task>
```

If the selected route is too large:

```text
Use Xskill shorten-iteration to split the selected path into TDD micro-loops.
```

After execution:

```text
Use Xskill evidence-ledger to record the run.
```

If the run produced reusable evidence:

```text
Use Xskill adaptive-improvement to decide whether this should update schema memory, a checklist, a template, or become an automation candidate.
```

If a repeated pattern emerges:

```text
Use Xskill schema-memory to create or update a schema memory card.
```

## Rule of thumb

Do not run every skill for every task.

Use Xskill when the task is vague, risky, multi-module, likely to drift, or important enough to verify.

## Self-improvement rule

Xskill learns from evidence, not confidence.

Do not promote a lesson unless it reduces context, narrows scope, improves verification, prevents repeated failure, or stabilizes a repeated workflow.
