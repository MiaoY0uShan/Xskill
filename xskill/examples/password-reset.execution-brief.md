# Execution Brief

## Task

Fix password reset bug.

## Goal

Fix reset token expiry validation without touching OAuth or billing behavior.

## Context Budget

- Max files to read: 4
- Max files to touch: 2
- Max skill/context notes: 500 words

## Files To Read First

- src/auth/reset.ts
- tests/auth/test_reset.ts

## Files To Avoid

- src/oauth/**
- src/billing/**
- src/auth/provider/**

## Implementation Path

1. Reproduce the bug with a focused failing test for expired reset tokens.
2. Implement the smallest validation fix in the reset token path.
3. Run the targeted auth reset tests.
4. Record evidence before claiming completion.

## Test Strategy

TDD required

## Checks

- pytest tests/auth/test_reset.py

## Evidence Required

- Failing test before fix
- Passing test after fix
- No unrelated files modified

## Review Lenses

- Logic
- Security
- Backward compatibility

## Stop Condition

Stop if the fix requires refactoring the auth provider internals.
