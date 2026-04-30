---
name: xskill-metrics
description: "Use after evidence-ledger to measure context load, scope creep, verification, rework, iteration speed, and TVP for a run or small batch of runs."
---

# Xskill: Metrics

Use this skill when you want to prove whether Xskill made an agent run smaller, safer, or more verifiable.

Xskill is designed to reduce context load, scope creep, and unverifiable work. This skill turns evidence into metrics.

## Primary metric

```text
TVP = total_context_tokens / verified_tasks_completed
```

TVP means **Tokens to Verified Progress**.

Lower TVP is better only when the task still produces verified progress.

Do not optimize for low token use if verification gets weaker.

## Proxy metric

Exact token counts are often unavailable.

When exact token counts are unavailable, use:

```text
Context Load Proxy = files_read + skills_loaded + reports_generated
Proxy TVP = context_load_proxy / verified_tasks_completed
```

The proxy is not a replacement for token accounting. It is an early-stage measurement method for portable skill bundle usage.

## Use when

- A task has an evidence ledger.
- A run should be compared against a baseline.
- The user asks whether Xskill reduced context, drift, or rework.
- A release needs before/after examples.
- Adaptive improvement needs quantitative support.

## Do not use when

- There is no evidence ledger.
- The task was too trivial to measure.
- The agent cannot distinguish planned vs unplanned file touches.
- The run has no verified outcome.

If the run has no verified outcome, TVP is undefined.

## Inputs

Prefer these inputs:

1. Compiled Execution Brief
2. Evidence Ledger
3. Shorten Iteration Report
4. Adaptive Improvement Report
5. Baseline run, if available

## Metrics

### Context Budget Contract compliance

Record whether the run stayed within:

- max files to read;
- max files to touch;
- max skill tokens, if known;
- max execution notes;
- forbidden context;
- scope boundary.

Any violation should be counted as scope or context drift.


### TVP

```text
TVP = total_context_tokens / verified_tasks_completed
```

If `verified_tasks_completed = 0`, return:

```text
TVP: undefined
Reason: no verified progress
```

### Proxy TVP

```text
Context Load Proxy = files_read + skills_loaded + reports_generated
Proxy TVP = context_load_proxy / verified_tasks_completed
```

### Scope Creep Rate

```text
Scope Creep Rate = touched_unplanned_files / touched_files
```

If `touched_files = 0`, return `0` only if no files were expected to be touched. Otherwise return `undefined`.

### Verification Rate

```text
Verification Rate = tasks_with_checks / completed_tasks
```

For a single task, use:

```text
Verification Rate = 1 if required checks were run and passed, else 0
```

### Rework Rate

```text
Rework Rate = failed_or_reopened_tasks / completed_tasks
```

For a single task, report failed attempts and whether the task was reopened.

### Context Load Size

```text
Context Load Size = files_loaded_per_task
```

Also record skills loaded and reports used.

### Iteration Half-life

```text
Iteration Half-life = time_to_first_verified_slice
```

If time is unavailable, use the number of TDD micro-loops needed to reach the first verified slice.

## Procedure

1. Confirm there is an evidence ledger.
2. Identify the task and whether it produced verified progress.
3. Count files read, files touched, and unplanned files touched.
4. Count checks required, checks run, and checks passed.
5. Count failed attempts or reopened tasks.
6. Estimate exact token use if available.
7. If exact tokens are unavailable, calculate the context-load proxy.
8. Calculate the supporting metrics.
9. Decide whether Xskill reduced context, reduced scope creep, improved verification, or exposed missing evidence.
10. Recommend whether the result should feed adaptive improvement or schema memory.

## Output contract

Return this structure:

```md
# Xskill Metrics Report

## Task

## Run Type
- [ ] With Xskill
- [ ] Without Xskill baseline

## Verified Progress
- Verified tasks completed:
- Evidence source:

## Context Load
- Exact total context tokens, if available:
- Skills loaded:
- Reports generated or used:
- Files read:
- Context Load Size:
- Context Load Proxy:

## Scope Control
- Files planned to touch:
- Files actually touched:
- Unplanned files touched:
- Scope Creep Rate:

## Verification
- Checks required:
- Checks run:
- Checks passed:
- Tasks with checks:
- Completed tasks:
- Verification Rate:

## Rework
- Failed attempts:
- Reopened tasks:
- Rework Rate:

## Iteration
- Time to first verified slice:
- TDD micro-loops to first verified slice:
- Iteration Half-life:

## TVP
- Exact TVP:
- Proxy TVP:

## Interpretation

## Decision
metrics_complete | missing_evidence | no_verified_progress | compare_against_baseline

## Recommended Next Skill
```

## Rules

- Metrics must come from evidence, not guesses.
- If a value is unknown, write `unknown`, not a fabricated number.
- If exact token counts are unavailable, use proxy metrics and label them as proxy.
- Do not claim Xskill reduced token use unless there is a baseline or repeated measurement.
- Do not count a task as verified unless evidence exists.
- Lower TVP is only good if verification quality remains intact.
```
