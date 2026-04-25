# Example: Using Xskill in a coding task

User prompt:

```text
Use Xskill to create an execution brief before editing code:
Fix password reset bug.
```

Agent should produce:

1. Requirement challenge if the task is unclear.
2. Scope cut if the task is broad.
3. Execution brief before editing.
4. Evidence ledger after completion.

Minimum output before code:

```md
# Execution Brief

## Task
Fix password reset bug.

## Context Budget
- Max files to read: 4
- Max files to touch: 2

## Checks
- pytest tests/auth/test_reset.py

## Evidence Required
- Failing test before fix
- Passing test after fix
```
