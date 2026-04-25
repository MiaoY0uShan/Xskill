---
name: xskill-automate-after-stable
description: Use only after a workflow has been repeated manually and is stable. Identifies safe automation candidates, guardrails, commands, and failure recovery rules.
---

# Xskill: Automate After Stable

Automate last.

This skill prevents premature automation of unclear or unstable work.

## Use when

- A manual workflow has repeated successfully.
- The user wants to convert repeated steps into a script, command, hook, checklist, or template.
- The workflow has clear inputs, outputs, and failure modes.
- Verification is already known.

## Goal

Determine whether a repeated workflow is safe to automate and define the automation boundary.

## Procedure

1. List the manual steps observed.
2. Identify which steps repeated without variation.
3. Identify which steps still require judgment.
4. Confirm that success and failure are detectable.
5. Define the automation candidate.
6. Define guardrails and stop conditions.
7. Define recovery steps.
8. Decide automate, keep manual, or delay.

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

## Keep Manual
- ...

## Guardrails
- ...

## Failure Detection
- ...

## Recovery Plan
- ...

## Decision
Automate | Keep manual | Delay

## Proposed Artifact
Script | Command | Hook | Template | Checklist | None
```

## Rules

- Do not automate confusion.
- Do not automate a workflow that has not succeeded manually.
- Keep judgment-heavy steps manual.
- Automation must have a safe failure mode.

## Failure mode

If automation is premature, output:

```md
# Automation Delayed

Reason: ...
Manual repetitions still needed: ...
Next observation to record: ...
```
