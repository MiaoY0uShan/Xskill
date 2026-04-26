# Xskill Adapters

Xskill is agent-agnostic.

The core protocol is the same everywhere:

```text
task → brief → bounded execution → evidence → metrics → improvement
```

This directory explains how to use the same portable Xskill bundle with common coding agents.

The release zip includes ready-made install packs under `install/`:

```text
install/codex/.agents/skills/xskill/
install/claude-code/.claude/skills/xskill/
install/gemini-cli/xskill/
install/github-copilot-cli/.github/agents/xskill.agent.md
```

No Xskill CLI, npm package, pip package, database, or runtime is required.
