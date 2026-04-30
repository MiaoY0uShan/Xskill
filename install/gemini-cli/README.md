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

- non-trivial task → Xskill activates automatically and produces a Compiled Execution Brief
- vague idea → Xskill produces 3 Idea Cards first

Manual override:

```text
Xskill: Fix the password reset bug.
```
