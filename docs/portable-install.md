# Portable Install

Xskill does not require npm, npx, pip, Python, or a command-line tool.

## Install

1. Download the latest release zip.
2. Unzip it.
3. Copy the `xskill/` folder into your agent skills directory.

Recommended global location:

```text
~/.agents/skills/xskill
```

Recommended project-local location:

```text
your-project/.agents/skills/xskill
```

Optional: copy `AGENTS.md` into your project root.

## Validate

Your final folder should include:

```text
xskill/
  question-requirements/SKILL.md
  delete-scope/SKILL.md
  semantic-architecture/SKILL.md
  optimize-path/SKILL.md
  shorten-iteration/SKILL.md
  evidence-ledger/SKILL.md
  adaptive-improvement/SKILL.md
  schema-memory/SKILL.md
  templates/
  examples/
```

Restart your coding agent after copying.
