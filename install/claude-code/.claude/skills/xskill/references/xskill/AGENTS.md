# Xskill Agent Contract

This project includes Xskill.

Use Xskill proactively for coding tasks, but choose the lightest path that still gives clear scope and verification.

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

## Confirm before changing the system

Some requests are high-impact even when the file edit is small. If the user asks to change Xskill itself, agent behavior, trigger rules, install boundaries, memory policy, default workflow, or repository ownership rules:

1. Restate the inferred goal.
2. Challenge unclear or risky assumptions.
3. List the proposed files or areas to change.
4. Ask for confirmation before editing.

Skip the confirmation only when the user explicitly says to implement feedback that has already been discussed and approved.

## Trigger levels

### Small change

Use a 3-5 line brief only. Include:

- task
- files to read/touch
- verification command or validation method
- result after execution

Examples: one-line fixes, copy edits, small config edits, focused test expectation updates.

### Medium change

Use a compact Execution Brief and Evidence Ledger.

Examples: focused bug fixes, single-feature edits, multi-file changes with clear boundaries, tests that need implementation updates.

### Large, vague, architectural, or risky task

Use the full chain only here: Idea Cards or question-requirements, delete-scope, semantic-architecture when needed, optimize-path, shorten-iteration when needed, Execution Brief, Evidence Ledger, and optional metrics or adaptive improvement.

Examples: unclear product requests, architecture decisions, repository restructuring, broad refactors, cross-module behavior changes.

### Protocol or agent-behavior change

Confirm first, then use the smallest route that safely implements the approved change. Sync install packs and generated fallback docs when the changed rule affects shipped behavior.

## Repository boundary

`.agents/skills/` is local agent configuration, not repository source. Do not commit it unless the repository explicitly says it owns that directory. Keep portable Xskill content in `xskill/` and installation packages in `install/`.

## When not to run the full flow

Skip the full flow for typos, obvious one-line edits, pure explanations, casual discussion, and tasks where the user explicitly says not to use Xskill.

For tiny edits, use the small-change brief.

## Required behavior

1. Pick small, medium, full-chain, or confirm-first routing before editing.
2. For protocol or agent-behavior changes, confirm intent and boundaries before editing unless already approved.
3. State what will be read, what will be touched, and how the work will be verified.
4. If the request is vague, generate 3 Idea Cards first.
5. Respect files to read, files to touch, and files to avoid.
6. If blocked or over budget, split into a smaller task.
7. Do not claim completion without test or validation results.
8. Use metrics only when measurement matters.
9. Promote learning only from evidence.
