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

- `question-requirements`: challenge assumptions before coding.
- `delete-scope`: remove unnecessary work and define boundaries.
- `optimize-path`: create an execution brief.
- `shorten-iteration`: split large or failed work into smaller tasks.
- `automate-after-stable`: automate only repeated stable workflows.
- `semantic-memory`: select relevant context and files to avoid.

## Use

Ask your agent:

```text
Use Xskill to create an execution brief before editing code:
<task>
```

or:

```text
Use Xskill optimize-path for:
<task>
```
