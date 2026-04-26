# Generic Adapter

Use this when your agent does not have native `SKILL.md`, extension, or custom-agent support.

Open `xskill/AGENTS.md`, then tell the agent:

```text
Use the Xskill protocol in xskill/AGENTS.md. Read only the relevant Xskill module files. Compile this task into a bounded Execution Brief before editing code:
<task>
```

This keeps Xskill portable even on agents without a formal skill system.
