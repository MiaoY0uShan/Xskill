# Xskill adapter: claude-code

Xskill is agent-agnostic.

## Default behavior (Ghost Mode)

**Proactively activate Xskill for non-trivial work.** Do not wait for the user to say "Xskill".

- **Vague idea →** Generate **3 Simplified Idea Cards** (A/B/C choice).
- **Clear task →** Create a **Compiled Execution Brief** with an **Auto-Verification Command**.
- **Execution →** Run verification commands automatically.
- **Evidence →** Produce an **Evidence Ledger** before claiming done.

## Rules
- Check `xskill/lessons-learned/` before planning.
- No brief, no edit.
- No evidence, no done.
