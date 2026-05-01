# Xskill for Gemini CLI

Install:

```bash
unzip xskill-gemini-cli-v0.2.4.zip
gemini extensions install ./xskill
```

Restart your agent.

Use your agent normally:

```text
Fix the password reset bug.
```

Expected:

- small change -> Xskill activates automatically and produces a 3-5 line brief plus validation result
- medium task -> Xskill produces a compact Execution Brief and Evidence Ledger
- large, vague, architectural, or risky task -> Xskill uses the full chain

Manual override:

```text
Xskill: Fix the password reset bug.
```
