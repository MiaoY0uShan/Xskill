# Portable install

The simplest install path is one zip per agent.

## User flow

```text
Pick your agent
-> download one zip
-> unzip
-> restart agent
-> use your agent normally
```

For non-trivial coding tasks, Xskill should activate automatically before code is edited.

Manual override:

```text
Xskill: <task or idea>
```

## Release assets

```text
xskill-codex-v0.2.4.zip
xskill-claude-code-v0.2.4.zip
xskill-gemini-cli-v0.2.4.zip
xskill-github-copilot-cli-v0.2.4.zip
xskill-copy-paste-v0.2.4.md
```

## Test

Ask:

```text
Rename one README section title without changing anything else.
```

Expected:

- clear task -> Compiled Execution Brief before editing
- vague idea -> Idea Cards

If the agent does not activate automatically, use the manual override:

```text
Xskill: Rename one README section title without changing anything else.
```
