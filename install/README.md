# Xskill install packs

Pick the package for your agent.

After installation, use your agent normally. Xskill should activate automatically for coding tasks and choose the lightest useful path.

Manual override:

```text
Xskill: <task or idea>
```

## Packages

| Agent | Folder | Release asset |
|---|---|---|
| Codex | `install/codex/` | `xskill-codex-{version}.zip` |
| Claude Code | `install/claude-code/` | `xskill-claude-code-{version}.zip` |
| Gemini CLI | `install/gemini-cli/` | `xskill-gemini-cli-{version}.zip` |
| GitHub Copilot CLI | `install/github-copilot-cli/` | `xskill-github-copilot-cli-{version}.zip` |

## Copy install

You can install directly from this repository by copying the agent-specific folder into the target project.

For Codex:

```text
copy install/codex/.agents -> your-project/.agents
```

Codex CLI can then discover:

```text
your-project/.agents/skills/xskill/
```

`install/codex/.agents/` is a tracked Xskill install template. A copied `your-project/.agents/skills/` directory is local agent configuration unless that target repository explicitly opts in to committing agent config.

If your agent is not listed, use `xskill-copy-paste-{version}.md`.

## Source of truth

`xskill/` is the source of truth for portable skill content.

The bundled copies inside install packs are generated copies:

```text
install/codex/.agents/skills/xskill/references/xskill/
install/claude-code/.claude/skills/xskill/references/xskill/
install/gemini-cli/xskill/xskill/
install/github-copilot-cli/xskill/
dist/xskill-copy-paste.md
```

Do not hand-edit those generated copies. Update `xskill/` or `xskill-copy-paste.md`, then run:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\sync-install-packs.ps1
```

To verify without changing files:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\sync-install-packs.ps1 -Check
```
