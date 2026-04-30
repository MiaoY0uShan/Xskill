# Xskill for Gemini CLI (Ghost Mode Enabled)

Use Xskill **proactively** before non-trivial coding work.

Do not wait for the user to say `Xskill`. Act as an autonomous execution discipline layer.

Manual override:

```text
Xskill: <task or idea>
```

## Automatic behavior (The Ghost Mode)

- **Detection:** If a task involves more than 1 file change, architectural decisions, or complex logic, automatically respond with: "I’ll use Xskill to create a bounded Execution Brief before editing code."
- **Lessons Learned:** Before creating a brief, always check `xskill/lessons-learned/` for relevant anti-patterns or project-specific traps.
- **Vague idea →** Generate **3 Simplified Idea Cards** (A/B/C choice).
- **Clear task →** Create a **Compiled Execution Brief** with an **Auto-Verification Command**.
- **Execution →** Run the verification command automatically after implementation.
- **Evidence →** Produce an **Evidence Ledger** before claiming done.

## Hard rules

- **No Brief, No Edit:** Do not edit code before the brief is accepted (or presented).
- **Check Lessons:** Always search `xskill/lessons-learned/` at the start of a task.
- **Verification First:** Every Brief must include a `verification_command` that can be run in the shell.
- **Stop on Violation:** If you exceed the Context Budget or touch unplanned files, stop and report immediately.
- **Learn from Evidence:** After a task (especially if it failed), record a new Lesson in `xskill/lessons-learned/` if a reusable anti-pattern is found.
