# Portable Install

Xskill does not require an Xskill CLI, npm package, npx command, pip package, database, or runtime.

Download the release zip and choose the ready-made install pack for your agent.

## Codex

Copy:

```text
install/codex/.agents
```

Into your repository root.

## Claude Code

Copy:

```text
install/claude-code/.claude
```

Into your repository root.

## Gemini CLI

Copy:

```text
install/gemini-cli/xskill
```

To:

```text
~/.gemini/extensions/xskill
```

Restart Gemini CLI.

## GitHub Copilot CLI

Copy:

```text
install/github-copilot-cli/.github
install/github-copilot-cli/xskill
```

Into your repository root.

## Generic agents

Keep `xskill/` in your project and ask the agent:

```text
Use the Xskill protocol in xskill/AGENTS.md. Read only the relevant Xskill module files. Compile this task into a bounded Execution Brief before editing code:
<task>
```
