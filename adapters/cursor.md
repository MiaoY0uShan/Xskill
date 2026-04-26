# Cursor Adapter

Cursor support is intentionally lightweight in this release.

Recommended use:

1. Keep `xskill/` in your repository.
2. Ask Cursor's agent to read `xskill/AGENTS.md`.
3. Ask it to use only the relevant Xskill module files before editing.

Prompt:

```text
Use the Xskill protocol from xskill/AGENTS.md. Compile this task into a bounded Execution Brief before editing code:
<task>
```

A future release may add a dedicated Cursor rules pack.
