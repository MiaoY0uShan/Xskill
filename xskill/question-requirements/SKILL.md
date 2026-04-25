---
name: xskill-question-requirements
description: Use before coding when a task is vague, risky, large, product-facing, or likely to contain hidden assumptions. Produces clarified goals, assumptions, risks, success criteria, and a continue/reduce/stop decision.
---

# Xskill: Question Requirements

Question requirements before execution.

This skill is the first gate in the Xskill loop. Its job is to stop the agent from confidently building the wrong thing.

## Use when

- The task is vague or broad.
- The task may affect product behavior, data, security, APIs, or architecture.
- Success criteria are missing.
- The user asks for a large feature.
- The agent is tempted to start coding immediately.

## Goal

Produce a concise requirement challenge that separates facts from assumptions and defines what success means.

## Procedure

1. Restate the task in one sentence.
2. Identify assumptions the agent would otherwise make silently.
3. Identify unknowns that could change the implementation.
4. Identify risks, especially scope creep, security, data loss, compatibility, and testability.
5. Define success criteria that can be verified.
6. Define explicit non-goals.
7. Decide whether to continue, reduce scope, or stop.

## Output contract

Return this structure:

```md
# Requirement Challenge

## Goal
...

## Assumptions
- ...

## Unknowns
- ...

## Risks
- ...

## Success Criteria
- ...

## Non-goals
- ...

## Decision
Continue | Reduce scope | Stop

## Smallest Useful Next Step
...
```

## Rules

- Do not propose an implementation yet.
- Do not expand the task.
- Prefer fewer, sharper requirements.
- If the requirement is not worth building, say so.
- If success cannot be verified, stop and ask for a measurable criterion.

## Failure mode

If the task cannot be clarified, output:

```md
# Blocked

Reason: ...
Missing information: ...
Smallest next action: ...
```
