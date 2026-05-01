# Release checklist

## v0.2.4 - One-download release kit and keynote README

Build these assets:

```text
Xskill-v0.2.4-release-kit.zip
Xskill-v0.2.4-repo.zip
xskill-v0.2.4.zip
xskill-codex-v0.2.4.zip
xskill-claude-code-v0.2.4.zip
xskill-gemini-cli-v0.2.4.zip
xskill-github-copilot-cli-v0.2.4.zip
xskill-copy-paste-v0.2.4.md
RELEASE_NOTES-v0.2.4.md
git-commands-v0.2.4.txt
```

GitHub Actions can build and upload the per-agent release assets from a `v*` tag or a manual workflow dispatch:

```text
.github/workflows/release.yml
```

Verify:

- `xskill/SKILL.md` exists.
- `xskill/` is treated as the source of truth for bundled install-pack references.
- Run `powershell -ExecutionPolicy Bypass -File .\scripts\sync-install-packs.ps1` before packaging.
- Run `powershell -ExecutionPolicy Bypass -File .\scripts\sync-install-packs.ps1 -Check` before release.
- Confirm `release.yml` packages Codex as `.agents/`, Claude Code as `.claude/`, Gemini CLI as `xskill/`, and GitHub Copilot CLI as `.github/` plus `xskill/`.
- Idea Cards template exists.
- Context Budget Contract includes estimated budget fields.
- All install packs describe proactive activation as the default behavior.
- All install packs preserve `Xskill: <task or idea>` as the manual override.
- Each agent package includes `TEST_XSKILL.md`.
- Each agent package includes its agent-specific entrypoint.
- Packaged `xskill/` reference folders match the source `xskill/` folder.
- `dist/README.md`, install READMEs, and Gemini extension metadata all use `v0.2.4`.
- No CLI, npm, npx, pip, database, or runtime was introduced.
