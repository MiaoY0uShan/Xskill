# Example: Using Xskill in a coding task

User prompt:

```text
Use Xskill to create an execution brief before editing code:
Fix password reset bug.
```

Agent should produce:

1. Question Requirements Report if the task is unclear, risky, or broad. This should include Five Whys and inversion.
2. Delete Scope Report after the real goal is clear. This should cut the task down to the smallest verifiable MVP using first principles and Occam's Razor.
3. Semantic Architecture Report if the scoped MVP crosses modules or has coupling risk.
4. Execution brief before editing.
5. Evidence ledger after completion.

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

Minimum scope deletion before architecture:

```md
# Delete Scope Report

## First-Principles Core
Required user outcome: expired reset tokens are rejected.
Irreducible capability: reset-token validation checks expiry.
Required evidence: failing test before fix, passing test after fix.

## Occam Filter
Keep:
- reset-token validation fix
- focused unit test

Delete now:
- OAuth provider refactor
- mailer redesign
- new token abstraction

## MVP Nucleus
One user outcome: expired reset tokens are rejected.
One primary workflow: validate an expired reset token and receive rejection.
Minimum verification: focused regression test passes.

## Recommended Next Skill
optimize-path
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

## Multi-module or architecture-sensitive task

After `question-requirements` clarifies the real goal, cut scope first:

```text
Use Xskill delete-scope after question-requirements for:
<task>
```

If the scoped MVP still crosses modules, ask:

```text
Use Xskill semantic-architecture after delete-scope for:
<task>
```

The agent should produce:

- MVP module map,
- module relationships,
- coupling risks,
- decoupling rules,
- MVP-first build order,
- deferred modules.

Then continue with:

```text
Use Xskill optimize-path for:
<task>
```

## Post-run learning

After the task is complete, ask:

```text
Use Xskill learn-after-run to extract reusable learning from the evidence ledger.
```

Keep the learning as a note unless the same issue repeats or the improvement clearly reduces context, scope, or verification risk.

## Small-batch implementation route

After `delete-scope` and `semantic-architecture`, choose the route before editing:

```text
Use Xskill optimize-path after semantic-architecture for:
Fix password reset bug.
```

The agent should select one small-batch route, remove lean waste, define a minimal safety buffer, and specify verification evidence.

If the route is still too large:

```text
Use Xskill shorten-iteration to split the selected path into TDD micro-loops:
Fix password reset bug.
```

Each loop should follow:

```text
RED -> GREEN -> REFACTOR -> EVIDENCE
```
