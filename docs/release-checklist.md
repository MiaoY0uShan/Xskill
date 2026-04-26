# Release checklist

## Before release

- [ ] `README.md` starts with the 30-second start path.
- [ ] `START_HERE.md` exists.
- [ ] `INSTALL.md` exists.
- [ ] `install/README.md` exists.
- [ ] Codex pack exists: `install/codex/.agents/skills/xskill/SKILL.md`.
- [ ] Claude Code pack exists: `install/claude-code/.claude/skills/xskill/SKILL.md`.
- [ ] Gemini CLI pack exists: `install/gemini-cli/xskill/gemini-extension.json`.
- [ ] GitHub Copilot CLI pack exists: `install/github-copilot-cli/.github/agents/xskill.agent.md`.
- [ ] No root `AGENTS.md` is required.
- [ ] `xskill/AGENTS.md` is bundled.
- [ ] `xskill/templates/compiled-execution-brief.md` exists.
- [ ] `xskill/templates/context-budget-contract.json` exists.
- [ ] `xskill/templates/evidence-ledger.md` exists.
- [ ] `docs/case-studies.md` exists.

## Release title

Recommended:

```text
v0.2.0 — Dumb-simple install
```

## Release note

```text
- Added START_HERE.md for the shortest possible install path
- Added INSTALL.md with copy-only instructions for Codex, Claude Code, Gemini CLI, and GitHub Copilot CLI
- Added install/README.md to make release zip usage clearer
- Simplified README around a 30-second start path
- Moved complex protocol details lower in the README
- Kept Xskill portable: no CLI, npm, npx, pip, database, runtime, or automatic executor
```
