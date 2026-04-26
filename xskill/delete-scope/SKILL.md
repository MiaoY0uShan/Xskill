---
name: xskill-delete-scope
description: Use before implementation planning to remove unnecessary work, define the minimum viable slice, defer non-essential scope, and list files or modules to avoid.
---

# Xskill: Delete Scope

Delete before optimizing.

This skill removes unnecessary work before the agent creates or edits anything.

## Use when

- The task has multiple possible interpretations.
- The request includes nice-to-have work.
- The implementation may sprawl across modules.
- The agent may refactor unrelated code.
- The user wants a minimum viable slice.

## Goal

Produce a smaller scope boundary that keeps only what is required for verified progress.

## Procedure

1. Restate the clarified task.
2. Identify the minimum useful outcome.
3. Separate must-have from nice-to-have work.
4. Delete or defer anything not needed for this iteration.
5. Identify likely files to touch.
6. Identify files, modules, or concerns to avoid.
7. Define the smallest slice that can be verified.

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

## Files Likely To Touch
- ...

## Files To Avoid
- ...

## Minimum Verifiable Slice
...
```

## Rules

- If it does not serve the current success criteria, delete or defer it.
- Do not add future-proofing unless required by the current task.
- Do not refactor unrelated modules.
- Prefer one small verified slice over one large uncertain plan.

## Failure mode

If the scope cannot be cut safely, output:

```md
# Scope Blocked

Reason: ...
Risk: ...
Smallest safe next action: ...
```
