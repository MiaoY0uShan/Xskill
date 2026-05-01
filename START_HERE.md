# Start here

Install Xskill once. Then use your agent normally.

For coding tasks, Xskill should activate automatically before code is edited and choose the lightest useful path.

## 1. Pick your agent

| Agent | Download |
|---|---|
| Codex | `xskill-codex-{version}.zip` |
| Claude Code | `xskill-claude-code-{version}.zip` |
| Gemini CLI | `xskill-gemini-cli-{version}.zip` |
| GitHub Copilot CLI | `xskill-github-copilot-cli-{version}.zip` |
| Any agent | `xskill-copy-paste-{version}.md` |

## 2. Install

Unzip the package for your agent.

Most project-level packages are designed to unzip into your project root.

For Codex when installing from this repository, copy `install/codex/.agents` into your target project root.

The `install/codex/.agents/` folder in this repository is a tracked install template. A copied target-project `.agents/skills/` folder is local agent configuration unless that project explicitly opts in.

## 3. Restart your agent

Reload the project so the agent can discover Xskill.

## 4. Use your agent normally

```text
Fix the password reset bug.
```

Expected behavior:

```text
Small change -> 3-5 line brief plus validation result.
Medium change -> Execution Brief plus Evidence Ledger.
Large/vague/architecture/risky task -> full chain.
```

Manual override:

```text
Xskill: Fix the password reset bug.
```
