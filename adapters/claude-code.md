# Claude Code Adapter

## Recommended install

Copy this ready-made folder into your repository root:

```text
install/claude-code/.claude
```

Your project should then contain:

```text
.claude/skills/xskill/SKILL.md
.claude/skills/xskill/references/xskill/...
```

For global use across projects, copy the `xskill` skill folder to:

```text
~/.claude/skills/xskill
```

## Use

Invoke directly:

```text
/xskill Compile this task into a bounded Execution Brief before editing code: <task>
```

Or ask naturally:

```text
Use Xskill before editing code: <task>
```
