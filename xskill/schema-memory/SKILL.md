---
name: xskill-schema-memory
description: Use after evidence has accumulated to store reusable task patterns, failure modes, context budget patterns, verification patterns, and stop conditions. This is pattern memory, not raw context memory.
---

# Xskill: Schema Memory

Remember patterns, not everything.

Schema memory replaces semantic memory. It does not store large context, repository summaries, or raw conversation history. It stores reusable work patterns discovered from evidence.

Use schema memory to answer:

- What kind of task is this?
- How does this kind of task usually fail?
- What context is usually useful?
- What context is usually waste?
- What verification pattern works?
- What stop condition prevents drift?

## Use when

- An evidence ledger and adaptive improvement report reveal a reusable pattern.
- The same class of work has appeared more than once.
- A task type has predictable failure modes.
- A context budget pattern can reduce future context use.
- A verification pattern can prevent repeated mistakes.
- A workflow is becoming stable enough to standardize.

## Do not use when

- There is no evidence ledger.
- The insight is a one-off preference.
- The pattern is speculative.
- The pattern would increase context without reducing risk.
- The agent wants to store raw memory instead of a reusable schema.

## Goal

Produce or update a schema memory card.

A schema memory card captures a reusable pattern for a class of work:

- trigger
- problem pattern
- common failure modes
- recommended execution pattern
- context budget pattern
- verification pattern
- files or modules usually involved
- files or modules usually avoided
- evidence required
- promotion history

## Procedure

1. Read the evidence ledger and adaptive improvement report if available.
2. Identify the class of work.
3. Extract the repeatable pattern, not the incidental details.
4. Identify common failure modes.
5. Identify the smallest useful context pattern.
6. Identify the verification pattern that proved the work.
7. Identify stop conditions that would prevent drift.
8. Decide whether to create, update, or reject the schema.
9. Keep the schema short enough to be reused in a future execution brief.

## Schema promotion rules

Do not create or update schema memory unless at least one is true:

- The same pattern appeared in at least two runs.
- The schema would clearly reduce future context.
- The schema would prevent repeated scope creep.
- The schema would improve verification.
- The schema would prevent a repeated failure mode.

Do not create a schema just because the task succeeded.

## Output contract

Return this structure:

```md
# Schema Memory Card

## Schema Name

## Trigger

## Problem Pattern

## Common Failure Modes

## Recommended Execution Pattern

## Context Budget Pattern

## TDD / Verification Pattern

## Files Or Modules Usually Involved

## Files Or Modules Usually Avoided

## Evidence Required

## Stop Conditions

## Promotion History

## Last Updated Because
```

## Rules

- Store patterns, not raw context.
- Prefer short reusable rules over long explanations.
- Do not summarize the whole repository.
- Do not add context just because it might be useful later.
- Do not turn one run into a permanent rule.
- Schema memory should make future runs smaller, not bigger.

## Failure mode

If the pattern is not reusable, return:

```md
# Schema Memory Decision

Decision: reject

Reason:
This appears to be a one-off lesson and should remain in the evidence ledger or adaptive improvement report.
```
