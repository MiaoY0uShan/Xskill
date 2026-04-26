---
name: xskill-semantic-memory
description: Use to keep project context lightweight by selecting relevant context slices, files to read, and files to avoid. This skill is for context reduction, not memory hoarding.
---

# Xskill: Semantic Memory

Use memory to remove context, not add more of it.

This skill helps the agent identify the smallest relevant project context for a task.

## Use when

- The repository is large.
- The task may touch multiple modules.
- The agent is tempted to read too many files.
- Prior decisions, risks, or project conventions matter.
- A context budget is needed.

## Goal

Produce a relevant context slice and an explicit avoid list.

## Procedure

1. Restate the task.
2. Identify likely modules, files, or concepts involved.
3. Select only the context needed for the current task.
4. Mark irrelevant or risky context to avoid.
5. Identify prior decisions or evidence that matter.
6. Keep the context slice small enough for one agent run.

## Output contract

Return this structure:

```md
# Semantic Context Slice

## Task
...

## Relevant Context
- id: ...
  type: ...
  path: ...
  reason: ...

## Files To Read
- ...

## Files To Avoid
- ...

## Prior Decisions To Respect
- ...

## Risks
- ...

## Context Budget Recommendation
- Max files to read: ...
- Max files to touch: ...
```

## Rules

- Do not summarize the entire repository.
- Do not add context just because it exists.
- Prefer context that changes the implementation decision.
- If a file is only tangentially related, put it in files to avoid.
- This is not a graph database or long-term memory system.

## Failure mode

If relevant context cannot be identified, output:

```md
# Context Blocked

Reason: ...
Smallest safe next action: ...
```
