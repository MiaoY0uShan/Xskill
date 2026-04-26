# Optimize Path Report

## Input
- Real goal: Fix reset token expiry validation without refactoring the auth provider.
- MVP nucleus: Validate reset token expiry and return the correct failure behavior.
- Scope boundary: Do not implement UI, email delivery, OAuth changes, or full password reset flow.
- Semantic architecture used: yes

## Candidate Paths

### Path A
- Summary: Add a focused token-expiry validation test, then patch the validation function.
- Scope: one validation behavior.
- Modules/files likely involved:
  - `src/auth/reset-token.*`
  - `tests/auth/test_reset_token.*`
- Verification: failing test before fix, passing test after fix.
- Risk: low.
- Reversibility: high.
- Waste risk: low.

### Path B
- Summary: Build the full password reset endpoint, mail integration, and token validation together.
- Scope: API, mail, token, and integration behavior.
- Modules/files likely involved:
  - auth endpoint
  - mail adapter
  - token validator
  - integration tests
- Verification: broad integration test.
- Risk: high.
- Reversibility: medium.
- Waste risk: high.

### Path C
- Summary: Refactor the auth provider before fixing token expiry.
- Scope: auth provider internals and reset validation.
- Modules/files likely involved:
  - auth provider internals
  - token validator
- Verification: unclear.
- Risk: high.
- Reversibility: low.
- Waste risk: high.

## Path Evaluation

| Path | Batch size | Stability | Verification clarity | Waste removed | Reversibility | Coupling risk | Decision |
|---|---|---|---|---|---|---|---|
| A | small | high | high | high | high | low | keep |
| B | large | medium | medium | low | medium | high | reject |
| C | large | low | low | low | low | high | reject |

## Selected Path

Path A: add a focused failing test for expired reset tokens, then make the smallest validation change that passes it.

## Small-Batch Slice

Only validate expired reset tokens. Do not add UI, email delivery, endpoint routing, or OAuth changes.

## Working Increment

A reset token that is expired is rejected by the validator and covered by a test.

## Lean Waste Removed

- Full password reset endpoint.
- Mail adapter integration.
- UI flow.
- Auth provider refactor.
- Broad E2E test before the core behavior is pinned down.

## Minimal Safety Buffer

- Stop if the fix requires changing auth provider internals.
- Keep the change local to token validation.
- Add one regression test before implementation.

## Verification Strategy

TDD required.

## Context Budget
- Max files to read: 4
- Max files to touch: 2
- Files to avoid:
  - `src/oauth/**`
  - `src/billing/**`
  - mail adapter internals
- Forbidden context:
  - unrelated auth provider refactors
  - reset UI work

## Implementation Path
1. Add or identify a failing test for expired reset tokens.
2. Patch the reset-token validation logic only.
3. Run the targeted auth reset-token test.

## Refactor Boundary
local

## Evidence Required
- Failing test before the fix.
- Passing test after the fix.
- List of files touched.

## Stop Condition

Stop if the task requires rewriting auth provider internals or adding the full reset endpoint.

## Decision
continue

## Recommended Next Skill
shorten-iteration
