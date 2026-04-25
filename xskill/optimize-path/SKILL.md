---
name: xskill-optimize-path
description: Use before editing code to choose the smallest correct implementation path, context budget, checks, evidence required, and review lenses.
---

# Xskill: Optimize Path

Choose the smallest correct implementation path.

This skill produces the execution brief the agent should follow while coding.

## Use when

- Requirements and scope have been clarified.
- The agent is ready to edit code.
- The task needs tests, checks, or review.
- The user wants a bounded implementation plan.

## Goal

Produce an execution brief with context budget, implementation path, verification commands, and evidence requirements.

## Procedure

1. Restate the task and goal.
2. Define the context budget.
3. List likely files to read.
4. List files to avoid.
5. Choose the smallest implementation path.
6. Choose the test strategy.
7. Define verification commands.
8. Define evidence required before completion.
9. Define stop conditions.

## Output contract

Return this structure:

```md
# Execution Brief

## Task
...

## Goal
...

## Context Budget
- Max files to read: ...
- Max files to touch: ...
- Max skill/context notes: ...

## Files To Read First
- ...

## Files To Avoid
- ...

## Implementation Path
1. ...
2. ...
3. ...

## Test Strategy
None | Smoke | Unit | Integration | E2E | TDD required

## Checks
- ...

## Evidence Required
- ...

## Review Lenses
- Logic
- Security
- Performance
- UX
- Backward compatibility

## Stop Condition
...
```

## Rules

- Prefer the smallest correct change.
- High-risk logic, bug fixes, and public APIs should use test-first or reproduction-first workflow.
- Do not refactor unrelated code.
- Do not claim completion without evidence.
- If checks are unavailable, state the manual verification plan.

## Failure mode

If no safe path exists, output:

```md
# Path Blocked

Reason: ...
Risk: ...
Smallest investigation task: ...
```
