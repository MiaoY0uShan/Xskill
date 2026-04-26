---
name: xskill-evidence-ledger
description: Use after execution to record what changed, what checks ran, which claims are verified, which claims remain unverified, and whether scope was violated.
---

# Xskill: Evidence Ledger

If there is no evidence, the task is not done.

This skill records the result of an agent run. It is the source material for adaptive improvement and schema memory.

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
10. Recommend whether to finish, split smaller, or run adaptive improvement.

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

## Remaining Risk

## Decision
complete | split_smaller | run_more_checks | adaptive_improvement

## Recommended Next Skill
```

## Rules

- Do not claim completion without evidence.
- Do not treat implementation as verification.
- If no checks were run, say so.
- If claims are not verified, list them explicitly.
- If scope was exceeded, record it.
- The evidence ledger should be short, factual, and auditable.
