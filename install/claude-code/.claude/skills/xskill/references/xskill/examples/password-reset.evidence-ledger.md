# Evidence Ledger

## Task

Fix password reset bug.

## Files Touched

- src/auth/reset.ts
- tests/auth/test_reset.ts

## Commands Run

- `pytest tests/auth/test_reset.py` — pass

## Verified Claims

- Expired reset tokens are rejected.
- Valid reset tokens still pass validation.
- No OAuth or billing files were modified.

## Unverified Claims

- Full end-to-end password reset email flow was not tested.

## Scope Violations

- None.

## Remaining Risk

- Integration behavior with the mail adapter should be verified separately.

## Next Action

- Review focused diff.
