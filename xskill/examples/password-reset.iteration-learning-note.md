# Iteration Learning Note

## Task
Fix password reset bug.

## Result
Pass

## Evidence Used
- Execution brief limited the task to reset token expiry validation.
- Evidence ledger recorded one targeted test command.
- Files touched: `src/auth/reset.ts`, `tests/auth/test_reset.py`.

## What Worked
- The context budget prevented reading OAuth and billing code.
- The check was narrow enough to run quickly.
- The stop condition prevented auth provider refactoring.

## What Failed Or Drifted
- None recorded.

## Context Waste
- Files read unnecessarily: none recorded.
- Files touched unnecessarily: none recorded.
- Skills loaded unnecessarily: none recorded.
- Assumptions that were wrong: none recorded.

## Smaller Next Task
Not required.

## Reusable Rule Candidate
For auth bug fixes, start with the smallest failing test that reproduces the specific behavior before inspecting adjacent auth providers.

## Promotion Decision
Keep as local note.

## Skill Patch Candidate
Not promoted yet. Revisit if the same auth-provider drift appears again.
