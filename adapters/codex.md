# Codex Adapter

## Recommended install

Copy this ready-made folder into your repository root:

```text
install/codex/.agents
```

Your project should then contain:

```text
.agents/skills/xskill/SKILL.md
.agents/skills/xskill/references/xskill/...
```

Codex can also use user-level skills by placing skills under:

```text
~/.agents/skills
```

## Use

Ask Codex:

```text
Use Xskill to compile this task into a bounded Execution Brief before editing code:
<task>
```

Codex may invoke the `xskill` skill explicitly or implicitly when the task matches the skill description.
