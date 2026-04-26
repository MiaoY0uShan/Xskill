# Install Xskill

Xskill has no CLI, npm, npx, pip, database, or runtime.

Download the package for your agent, unzip it, restart the agent, and use your agent normally.

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

Expected behavior:

```text
I’ll use Xskill to create a bounded Execution Brief before editing code.
```

Manual override:

```text
Xskill: Rename one README section title without changing anything else.
```
