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

For coding tasks, Xskill should activate automatically before code is edited and choose the lightest useful path.

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

## Repository boundary

Install packs may intentionally contain agent config templates. For example, `install/codex/.agents/` is tracked so users can copy it into a target project root.

After copying, `your-project/.agents/skills/` is local agent configuration unless that target repository explicitly opts in.

Changes to agent behavior, trigger rules, or install boundaries should be confirmed before editing because they affect future agent behavior.

## Test

Ask:

```text
Rename one README section title without changing anything else.
```

Expected:

- small clear change -> 3-5 line brief plus validation result
- vague idea -> Idea Cards

If the agent does not activate automatically, use the manual override:

```text
Xskill: Rename one README section title without changing anything else.
```
