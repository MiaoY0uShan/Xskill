# Example: Using Xskill in a coding task

User prompt:

```text
Use Xskill to create an execution brief before editing code:
Fix password reset bug.
```

Agent should produce:

1. Question Requirements Report if the task is unclear, risky, or broad. This should include Five Whys and inversion.
2. Scope cut if the task is broad.
3. Execution brief before editing.
4. Evidence ledger after completion.

Minimum requirement challenge before code:

```md
# Question Requirements Report

## Likely Real Goal
Fix reset token validation without refactoring the auth provider.

## Five Whys
Root objective: verify and fix reset token validation with the smallest safe change.

## Inversion
Failure path: the agent rewrites auth provider internals or skips a failing test.

## Decision
reduce_scope
```

Minimum execution brief before code:

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

## Post-run learning

After the task is complete, ask:

```text
Use Xskill learn-after-run to extract reusable learning from the evidence ledger.
```

Keep the learning as a note unless the same issue repeats or the improvement clearly reduces context, scope, or verification risk.

## Multi-module or architecture-sensitive task

After `question-requirements` clarifies the real goal, ask:

```text
Use Xskill semantic-architecture after question-requirements for:
<task>
```

The agent should produce:

- MVP slice,
- module map,
- module relationships,
- coupling risks,
- decoupling rules,
- MVP-first build order,
- deferred modules.

Then continue with:

```text
Use Xskill delete-scope for:
<task>
```
