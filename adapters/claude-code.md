# Xskill adapter: claude-code

Xskill is agent-agnostic.

Default behavior:

```text
Use Xskill proactively for non-trivial coding work. Do not wait for the user to say "Xskill".
```

Manual override:

```text
Xskill: <task or idea>
```

Expected behavior:

- vague idea -> 3 Idea Cards
- clear task -> Compiled Execution Brief
- completed task -> Evidence Ledger
- failed task -> Failure-to-Smaller-Task Protocol

This adapter does not add a runtime, CLI, npm package, npx installer, pip package, or database.
