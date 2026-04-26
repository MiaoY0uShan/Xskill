# OpenCode Adapter

OpenCode support is intentionally lightweight in this release.

Recommended use:

1. Keep `xskill/` in your repository or user prompt library.
2. Ask OpenCode to read `xskill/AGENTS.md`.
3. Ask it to use only the relevant Xskill module files before editing.

Prompt:

```text
Use the Xskill protocol from xskill/AGENTS.md. Compile this task into a bounded Execution Brief before editing code:
<task>
```

A future release may add a dedicated OpenCode adapter pack.
