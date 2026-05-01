# Xskill distribution

This folder contains generated release-facing files.

Release assets:

```text
xskill-codex-v0.2.4.zip
xskill-claude-code-v0.2.4.zip
xskill-gemini-cli-v0.2.4.zip
xskill-github-copilot-cli-v0.2.4.zip
xskill-copy-paste-v0.2.4.md
```

GitHub Actions builds these assets from `.github/workflows/release.yml` when a `v*` tag is pushed or the release workflow is run manually.

After installing, use your agent normally. Xskill should activate automatically for coding tasks and choose the lightest useful path:

- small change -> 3-5 line brief plus validation result
- medium task -> compact Execution Brief plus Evidence Ledger
- large, vague, architectural, or risky task -> full chain

Agent-local directories such as `.agents/skills/` are not project source unless a repository explicitly opts in.

`xskill/` is the source of truth. Generated install-pack copies are refreshed with:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\sync-install-packs.ps1
```
