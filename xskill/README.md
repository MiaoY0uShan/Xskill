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
- `semantic-architecture`: after requirements are clarified, sketch the MVP slice, module map, coupling risks, and decoupling rules for larger tasks.
- `delete-scope`: remove unnecessary work and define boundaries.
- `optimize-path`: create an execution brief.
- `shorten-iteration`: split large or failed work into smaller tasks.
- `automate-after-stable`: automate only repeated stable workflows.
- `semantic-memory`: select relevant context and files to avoid.
- `learn-after-run`: extract reusable learning after a run without automatic self-modification.

## Templates

- `templates/question-requirements-report.md`
- `templates/semantic-architecture-report.md`
- `templates/execution-brief.md`
- `templates/context-budget.md`
- `templates/evidence-ledger.md`
- `templates/iteration-learning-note.md`

## Use

Ask your agent:

```text
Use Xskill question-requirements for:
<task>
```

For a project, system, feature, refactor, workflow, or multi-module task, ask:

```text
Use Xskill semantic-architecture after question-requirements for:
<task>
```

Then ask:

```text
Use Xskill to create an execution brief before editing code:
<task>
```

or:

```text
Use Xskill optimize-path for:
<task>
```

## Post-run learning

After a non-trivial task, ask your agent:

```text
Use Xskill learn-after-run to extract reusable learning from the evidence ledger.
```

Do not promote a lesson into a skill unless it is repeated, reduces context, narrows scope, improves verification, or prevents a recurring failure.
