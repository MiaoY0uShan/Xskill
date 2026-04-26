# Portable install

The simplest install path is one zip per agent.

## User flow

```text
Pick your agent
→ download one zip
→ unzip
→ restart agent
→ say: Xskill: <task>
```

## Release assets

```text
xskill-codex-v0.2.2.zip
xskill-claude-code-v0.2.2.zip
xskill-gemini-cli-v0.2.2.zip
xskill-github-copilot-cli-v0.2.2.zip
xskill-copy-paste-v0.2.2.md
```

## Test

Ask:

```text
Xskill: Rename one README section title without changing anything else.
```

Expected:

- clear task → Compiled Execution Brief
- vague idea → Idea Cards
