---
name: xskill-evidence-ledger
description: Use after execution to record what changed, what checks ran, which claims are verified, which claims remain unverified, and whether scope was violated.
---

# Xskill: Evidence Ledger

Every agent claim needs evidence.

If there is no evidence, the task is not done.

This skill records the result of an agent run. It is the source material for metrics, adaptive improvement, and schema memory.

## Use when

- A task is complete or claimed complete.
- A task failed or was blocked.
- A verification command was run.
- The agent touched files.
- A scope boundary may have been crossed.
- The run will be used for future learning.

## Goal

Produce an evidence ledger that separates verified claims from unverified claims.

## Procedure

1. Restate the task.
2. List files read if known.
3. List files touched.
4. List commands or checks run.
5. Record result for each check.
6. List claims that are verified by evidence.
7. List claims that remain unverified.
8. Identify scope violations or near-violations.
9. Record remaining risk.
10. Recommend whether to finish, split smaller, run metrics, or run adaptive improvement.

## Output contract

Return this structure:

```md
# Evidence Ledger

## Task

## Result
Pass | Fail | Blocked | Partial

## Files Read

## Files Touched

## Checks Run

## Verified Claims

## Unverified Claims

## Scope Violations

## Context Budget Violations

## Remaining Risk

## Decision
complete | split_smaller | run_more_checks | metrics | adaptive_improvement

## Recommended Next Skill
```

## Rules

- Do not claim completion without evidence.
- Do not treat implementation as verification.
- If no checks were run, say so.
- If claims are not verified, list them explicitly.
- If scope was exceeded, record it.
- The evidence ledger should be short, factual, and auditable.


## Metrics handoff

If measurement matters, pass this ledger to `metrics` before adaptive improvement.

The metrics skill needs:

- files read;
- files planned to touch;
- files actually touched;
- unplanned files touched;
- checks required;
- checks run;
- checks passed;
- verified tasks completed;
- failed or reopened tasks;
- exact token counts, if available.


## JSON audit form

When auditability matters, also produce a JSON ledger using `templates/evidence-ledger.md`.

The JSON form should include:

- task_id;
- files_read;
- files_touched;
- commands_run;
- verified claims with evidence;
- unverified_claims;
- scope_violations;
- context_budget_violations;
- next_action.
