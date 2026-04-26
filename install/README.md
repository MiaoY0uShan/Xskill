# Xskill install packs

Pick one folder. Copy it. Restart your agent. Use one sentence.

```text
Use Xskill to compile this task before editing code:
<task>
```

## Available packs

| Agent | Folder to copy/install | Destination |
|---|---|---|
| Codex | `install/codex/.agents` | project root |
| Claude Code | `install/claude-code/.claude` | project root |
| Gemini CLI | `install/gemini-cli/xskill` | `~/.gemini/extensions/xskill` |
| GitHub Copilot CLI | `install/github-copilot-cli/.github` and `install/github-copilot-cli/xskill` | project root |

## Notes

- You do not need to copy a separate root `AGENTS.md`.
- The agent contract lives inside the pack.
- Xskill does not require an installer, package manager, server, database, or runtime.
- If your agent is not listed, use `adapters/generic.md`.
