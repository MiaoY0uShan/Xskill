# Xskill for Gemini CLI

Use Xskill proactively before coding work.

Do not wait for the user to say `Xskill`. Act as an autonomous execution discipline layer.

Manual override:

```text
Xskill: <task or idea>
```

## Automatic behavior

- **Small change:** Produce a 3-5 line brief that states task, read/touch, verification, and result.
- **Medium task:** Produce a compact Execution Brief, run verification, and produce an Evidence Ledger.
- **Large, vague, architectural, or risky task:** Use Idea Cards or the full chain before execution.
- **Protocol or agent-behavior change:** Confirm intent and boundaries before editing.
- **Lessons Learned:** Check `xskill/lessons-learned/` for relevant anti-patterns or project-specific traps.

## Hard rules

- **No Proof, No Edit:** State scope and verification before editing.
- **Confirm System Changes:** Do not change protocol, trigger rules, install boundaries, memory policy, or default workflow without confirmation unless already approved.
- **Check Lessons:** Search `xskill/lessons-learned/` at the start of a task.
- **Verification First:** Every path must include a command or explicit validation method.
- **Stop on Violation:** If you exceed the chosen route or touch unplanned files, stop and report.
- **Learn from Evidence:** Record a new lesson only when a reusable anti-pattern is supported by evidence.
