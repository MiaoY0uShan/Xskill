# Xskill Agent Contract

This project includes Xskill.

Use Xskill proactively for non-trivial coding tasks. Do not wait for the user to say `Xskill`.

Manual trigger is still supported:

```text
Xskill: <task or idea>
```

## When to activate automatically

Use Xskill before editing code when the user asks for:

- code modification
- bug fix
- new feature
- refactor
- repository structure change
- installation flow change
- agent instruction change
- tests
- multi-file work
- architecture decision
- work that needs verification

## When not to run the full flow

Skip the full flow for typos, obvious one-line edits, pure explanations, casual discussion, and tasks where the user explicitly says not to use Xskill.

For tiny edits, use a lightweight brief.

## Required behavior

1. Produce a Compiled Execution Brief before non-trivial edits.
2. Estimate the Context Budget Contract yourself.
3. If the request is vague, generate 3 Idea Cards first.
4. Respect files to read, files to touch, and files to avoid.
5. If blocked or over budget, split into a smaller task.
6. Do not claim completion without an Evidence Ledger.
7. Use metrics when measurement matters.
8. Promote learning only from evidence.
