# Start here

Use this file if you do not want to understand the whole project first.

## What Xskill does

Xskill makes your coding agent do this before editing code:

```text
turn a vague task into a small, bounded, verifiable Execution Brief
```

You install Xskill by copying one ready-made folder for your agent.

No Xskill CLI. No npm. No npx. No pip. No database. No runtime.

---

## Step 1: Pick your agent

### Codex

Copy this folder into your repository root:

```text
install/codex/.agents
```

After copying, your project should contain:

```text
.agents/skills/xskill/SKILL.md
```

### Claude Code

Copy this folder into your repository root:

```text
install/claude-code/.claude
```

After copying, your project should contain:

```text
.claude/skills/xskill/SKILL.md
```

### Gemini CLI

Copy this folder:

```text
install/gemini-cli/xskill
```

To:

```text
~/.gemini/extensions/xskill
```

Or install from the local path:

```bash
gemini extensions install install/gemini-cli/xskill
```

### GitHub Copilot CLI

Copy both of these into your repository root:

```text
install/github-copilot-cli/.github
install/github-copilot-cli/xskill
```

After copying, your project should contain:

```text
.github/agents/xskill.agent.md
xskill/
```

---

## Step 2: Restart your agent

Restart the agent or reload the project so it can discover the new instructions.

---

## Step 3: Use one sentence

Ask your agent:

```text
Use Xskill to compile this task before editing code:
<your task>
```

For Claude Code, you can also use:

```text
/xskill Compile this task before editing code: <your task>
```

---

## What you should get

The agent should produce a **Compiled Execution Brief** with:

```text
- real goal
- MVP scope
- must not do
- context budget contract
- context diet map
- files to read
- files to avoid
- checks
- evidence required
- stop condition
```

If it starts editing code before producing the brief, tell it:

```text
Stop. Use Xskill first. Produce the Execution Brief before editing code.
```
