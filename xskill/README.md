# Xskill Bundle

This folder is the portable Xskill skill bundle.

Copy this `xskill/` folder into your agent skills directory.

Recommended locations:

```text
~/.agents/skills/xskill
```

or project-local:

```text
your-project/.agents/skills/xskill
```

## Skills

- `question-requirements`: run Five Whys and inversion before coding to reveal the real goal, failure paths, success criteria, and a continue/reduce/ask/stop decision.
- `delete-scope`: after requirements are clarified, use first-principles reasoning and Occam's Razor to cut the request down to the smallest verifiable MVP.
- `semantic-architecture`: after scope is deleted, sketch the MVP module map, coupling risks, and decoupling rules for larger tasks.
- `optimize-path`: select the smallest stable route using small-batch, agile, lean, and minimal safety-buffer filters, then create an execution brief.
- `shorten-iteration`: split large or failed selected paths into TDD micro-loops.
- `evidence-ledger`: record what actually happened, what was verified, what remains unverified, and whether scope was violated.
- `adaptive-improvement`: turn post-run evidence into feedback, schema updates, checklist improvements, or automation candidates.
- `schema-memory`: store reusable task patterns, failure modes, context budget patterns, verification patterns, and stop conditions.

## Templates

- `templates/question-requirements-report.md`
- `templates/delete-scope-report.md`
- `templates/semantic-architecture-report.md`
- `templates/optimize-path-report.md`
- `templates/shorten-iteration-report.md`
- `templates/execution-brief.md`
- `templates/context-budget.md`
- `templates/evidence-ledger.md`
- `templates/adaptive-improvement-report.md`
- `templates/schema-memory-card.md`
- `templates/automation-candidate.md`

## Use

Ask your agent:

```text
Use Xskill question-requirements for:
<task>
```

Then cut scope:

```text
Use Xskill delete-scope after question-requirements for:
<task>
```

For a project, system, feature, refactor, workflow, or multi-module MVP, ask:

```text
Use Xskill semantic-architecture after delete-scope for:
<task>
```

Then ask:

```text
Use Xskill optimize-path after scope and architecture are clear for:
<task>
```

If the selected path is still too large or a previous attempt failed, ask:

```text
Use Xskill shorten-iteration to split the selected path into TDD micro-loops:
<task>
```

After execution, ask:

```text
Use Xskill evidence-ledger to record what changed and what was verified.
```

After a non-trivial run with evidence, ask:

```text
Use Xskill adaptive-improvement to extract reusable improvement from the evidence ledger.
```

If a repeated task pattern emerges, ask:

```text
Use Xskill schema-memory to create or update a schema memory card.
```

## Adaptive improvement

Xskill learns from evidence, not confidence.

Do not promote a lesson into a schema, checklist, template, or automation candidate unless it reduces context, narrows scope, improves verification, prevents a repeated failure, or stabilizes a repeated workflow.
