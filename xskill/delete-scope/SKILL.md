---
name: xskill-delete-scope
description: Use after requirements are understood and before implementation planning. Deletes unnecessary work, defines the minimum viable slice, files to touch, and files to avoid.
---

# Xskill: Delete Scope

Delete unnecessary work before optimizing or coding.

This skill turns a broad task into the smallest safe slice that can be verified.

## Use when

- The task contains multiple features, actors, files, or phases.
- The agent is likely to overbuild.
- The implementation path touches unrelated areas.
- A project has too much context available.
- The user wants a minimum useful result.

## Goal

Produce a scope boundary that prevents context bloat and unrelated changes.

## Procedure

1. Identify the user-visible outcome.
2. Separate must-have from nice-to-have.
3. Delete anything not required for the current success criteria.
4. Defer useful but unnecessary work to later.
5. Define the minimum viable slice.
6. Define files or directories likely to be relevant.
7. Define files or directories that should be avoided.
8. Define the stop condition.

## Output contract

Return this structure:

```md
# Scope Cut

## Must Have
- ...

## Nice To Have
- ...

## Delete Now
- ...

## Defer To Later
- ...

## Minimum Slice
...

## Files To Touch
- ...

## Files To Avoid
- ...

## Stop Condition
...
```

## Rules

- If it does not serve the current success criteria, delete or defer it.
- If a file is not required for the minimum slice, do not read or modify it.
- Do not create abstractions for hypothetical future needs.
- Smaller is better if it can still be verified.

## Failure mode

If the scope cannot be cut safely, output:

```md
# Scope Blocked

Reason: ...
Smallest safe slice: ...
Question for user: ...
```
