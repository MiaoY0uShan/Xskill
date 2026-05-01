# Install Xskill

Xskill has no CLI, npm, npx, pip, database, or runtime.

Download the package for your agent, unzip it, restart the agent, and use your agent normally.

Agent-local directories such as `.agents/skills/` are not project source. Do not commit them unless your repository explicitly says it owns that directory. Keep portable Xskill content in `xskill/`.

## Codex

```bash
unzip xskill-codex-{version}.zip -d your-project/
```

## Claude Code

```bash
unzip xskill-claude-code-{version}.zip -d your-project/
```

## Gemini CLI

```bash
unzip xskill-gemini-cli-{version}.zip
gemini extensions install ./xskill
```

## GitHub Copilot CLI

```bash
unzip xskill-github-copilot-cli-{version}.zip -d your-project/
```

## Any agent

Open and paste:

```text
xskill-copy-paste-{version}.md
```

## Test

After installing, ask:

```text
Rename one README section title without changing anything else.
```

Expected behavior for this small change:

```text
Xskill small brief: task, read/touch, verify, result.
```

Manual override:

```text
Xskill: Rename one README section title without changing anything else.
```
