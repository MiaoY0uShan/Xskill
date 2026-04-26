---
name: xskill-automate-after-stable
description: Use only after a workflow has been repeated manually and is stable. Identifies safe automation candidates, guardrails, commands, and failure recovery rules.
---

# Xskill: Automate After Stable

Automate last.

This skill prevents the agent from automating a workflow that is still unclear.

## Use when

- A manual workflow has succeeded repeatedly.
- The steps are stable and predictable.
- The failure modes are understood.
- The automation can be guarded and reversed.

## Do not use when

- The workflow has not been run manually.
- Requirements are still changing.
- Failures are not understood.
- The automation would hide important judgment.

## Goal

Identify whether automation is justified and define its guardrails.

## Procedure

1. List the manual steps observed.
2. Confirm the workflow is stable.
3. Identify repetitive steps that can be automated safely.
4. Define guardrails and failure recovery.
5. Define what evidence must be recorded after automation runs.
6. Reject automation if the process is still unstable.

## Output contract

Return this structure:

```md
# Automation Review

## Manual Steps Observed
- ...

## Stable Repetition
Yes | No

## Automation Candidate
...

## Guardrails
- ...

## Failure Recovery
- ...

## Evidence To Record
- ...

## Decision
Automate | Keep manual | Revisit later
```

## Rules

- Do not automate confusion.
- Automation should reduce repeated work, not remove judgment.
- Every automation must have a stop condition.
- If the automation cannot be verified, do not automate it.
