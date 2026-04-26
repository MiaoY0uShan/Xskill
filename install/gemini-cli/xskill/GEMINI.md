# Xskill for Gemini CLI

Use Xskill proactively before non-trivial coding work.

Do not wait for the user to say `Xskill`.

Manual override:

```text
Xskill: <task or idea>
```

## Automatic behavior

- Clear coding task → create a Compiled Execution Brief before editing code.
- Vague idea → generate 3 Idea Cards first.
- Failed task → split into smaller verified work.
- Completed task → produce an Evidence Ledger before claiming done.

Bundled references are inside:

```text
xskill/
```

## Hard rules

- Do not edit code before the brief.
- Estimate the Context Budget Contract yourself.
- Respect the Context Diet Map.
- Do not claim completion without an Evidence Ledger.
- If the task fails or exceeds budget, produce a smaller task.
- Xskill learns from evidence, not confidence.
