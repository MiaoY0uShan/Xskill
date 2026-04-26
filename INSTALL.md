# Install Xskill

This file is intentionally short.

Xskill is a portable skill bundle. Install it by copying the ready-made folder for your agent.

No Xskill CLI. No npm. No npx. No pip. No database. No runtime.

---

## Codex

Copy this folder into your repository root:

```text
install/codex/.agents
```

Expected result:

```text
your-project/
  .agents/
    skills/
      xskill/
        SKILL.md
        references/
```

Use:

```text
Use Xskill to compile this task before editing code:
<task>
```

---

## Claude Code

Copy this folder into your repository root:

```text
install/claude-code/.claude
```

Expected result:

```text
your-project/
  .claude/
    skills/
      xskill/
        SKILL.md
        references/
```

Use:

```text
/xskill Compile this task before editing code: <task>
```

Or:

```text
Use Xskill to compile this task before editing code:
<task>
```

---

## Gemini CLI

Copy this folder:

```text
install/gemini-cli/xskill
```

To:

```text
~/.gemini/extensions/xskill
```

Or run:

```bash
gemini extensions install install/gemini-cli/xskill
```

Use:

```text
Use Xskill to compile this task before editing code:
<task>
```

---

## GitHub Copilot CLI

Copy both of these into your repository root:

```text
install/github-copilot-cli/.github
install/github-copilot-cli/xskill
```

Expected result:

```text
your-project/
  .github/
    agents/
      xskill.agent.md
  xskill/
```

Use the `xskill` custom agent and ask:

```text
Compile this task before editing code:
<task>
```

---

## Generic manual use

If your agent does not support skills, open:

```text
xskill/AGENTS.md
```

Paste it into your agent as project instructions.

Then ask:

```text
Use Xskill to compile this task before editing code:
<task>
```

For task-specific depth, paste only the relevant `xskill/*/SKILL.md` file.
