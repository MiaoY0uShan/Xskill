# Release Checklist

## v0.1.11 — Agent-agnostic adapters

Check that the release zip contains:

```text
xskill/AGENTS.md
xskill/*/SKILL.md
xskill/templates/
xskill/examples/
adapters/
docs/execution-protocol.md
install/codex/.agents/skills/xskill/
install/claude-code/.claude/skills/xskill/
install/gemini-cli/xskill/gemini-extension.json
install/gemini-cli/xskill/GEMINI.md
install/github-copilot-cli/.github/agents/xskill.agent.md
```

Confirm that root `AGENTS.md` is no longer required for users.

Suggested release title:

```text
v0.1.11 — Agent-agnostic adapters
```

Suggested notes:

```text
- Added ready-made install packs for Codex, Claude Code, Gemini CLI, and GitHub Copilot CLI
- Moved the agent contract into xskill/AGENTS.md so users do not copy a separate root AGENTS.md
- Added agent-agnostic adapter docs
- Added docs/execution-protocol.md
- Added single-folder Xskill skill packs for Codex and Claude Code
- Added Gemini CLI extension pack
- Added GitHub Copilot CLI custom agent pack
- Kept Xskill portable: no Xskill CLI, npm, npx, pip, database, runtime, or automatic executor
```
