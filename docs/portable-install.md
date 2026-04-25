# Portable Installation

Xskill is designed to work without a CLI or package manager.

## Install globally

Copy the `xskill/` folder to:

```text
~/.agents/skills/xskill
```

## Install inside one project

Copy the `xskill/` folder to:

```text
your-project/.agents/skills/xskill
```

Then copy `AGENTS.md` to your project root if your coding agent supports it.

## Verify structure

```text
.agents/skills/xskill/
  question-requirements/SKILL.md
  delete-scope/SKILL.md
  optimize-path/SKILL.md
  shorten-iteration/SKILL.md
  automate-after-stable/SKILL.md
  semantic-memory/SKILL.md
```

Restart your coding agent after copying files.
