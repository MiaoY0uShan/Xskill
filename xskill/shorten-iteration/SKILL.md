---
name: xskill-shorten-iteration
description: Use when work is too large, an attempt failed, or the agent needs to split a task into atomic verifiable iterations with context slices and stop conditions.
---

# Xskill: Shorten Iteration

Break work into smaller verified loops.

This skill prevents long, drifting agent runs by creating atomic tasks with clean context boundaries.

## Use when

- A task is too large for one context window.
- A previous attempt failed.
- The agent touched too many files.
- Verification failed.
- Work can be parallelized safely.
- The user asks for a plan that should not sprawl.

## Goal

Produce small tasks where each task has one goal, one context slice, one verification path, and one state update.

## Procedure

1. Identify the original task.
2. Identify the reason it is too large or failed.
3. Split it into atomic tasks.
4. Assign each task a context slice.
5. Define checks for each task.
6. Define stop conditions.
7. Group independent tasks if they can be done in parallel.
8. Define rollback or recovery steps.

## Output contract

Return this structure:

```md
# Iteration Plan

## Original Task
...

## Why It Needs Shorter Iterations
...

## Atomic Tasks

### T001: ...
- Goal: ...
- Context slice: ...
- Files to read: ...
- Files to touch: ...
- Checks: ...
- Stop condition: ...

### T002: ...
- Goal: ...
- Context slice: ...
- Files to read: ...
- Files to touch: ...
- Checks: ...
- Stop condition: ...

## Parallel Groups
- Wave 1: ...
- Wave 2: ...

## Rollback Plan
- ...
```

## Rules

- One task should fit in one clean agent run.
- Each task must have a verification method.
- If a task fails, split it again instead of retrying blindly.
- Do not create parallel tasks that touch the same files.

## Failure mode

If the task cannot be split, output:

```md
# Iteration Blocked

Reason: ...
Smallest investigation task: ...
Evidence needed: ...
```
