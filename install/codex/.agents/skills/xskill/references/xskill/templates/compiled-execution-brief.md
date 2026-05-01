# Execution Brief

This is the medium-task output of Xskill.

Use it for focused changes that need more than a tiny brief. For small changes, use the tiny brief. For large, vague, architectural, or risky work, run the full chain first and compile the result into this shape.

## Markdown form

```md
# Execution Brief

## Selected Idea Card
Only include this if Idea Cards were used.

## Task

## Real Goal

## MVP Scope

## Must Not Do

## Files To Read

## Files To Touch

## Files To Avoid

## Verification Command

## Evidence To Capture

## Stop Condition
```

## Confirm-first form

Use this before protocol, trigger, install-boundary, memory-policy, or default-workflow changes:

```md
Inferred goal:
Assumptions to challenge:
Proposed files/areas:
Confirmation needed:
```

After confirmation, use the tiny or medium brief that fits the approved change.

## Tiny brief form

Use this for small clear changes:

```md
Task:
Read/touch:
Verify:
Result:
```

Add a fifth line only when a stop condition matters.

## JSON form

```json
{
  "selected_idea_card": null,
  "task": "",
  "real_goal": "",
  "mvp_scope": "",
  "must_not_do": [],
  "files_to_read": [],
  "files_to_touch": [],
  "files_to_avoid": [],
  "verification_command": "",
  "evidence_to_capture": [],
  "stop_condition": ""
}
```
