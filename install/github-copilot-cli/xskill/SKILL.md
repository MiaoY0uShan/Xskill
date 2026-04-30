---
name: xskill
description: "Use proactively before non-trivial coding tasks to create a bounded, evidence-backed Execution Brief. Do not wait for the user to say \"Xskill\". Manual override: \"Xskill: <task or idea>\"."
---

# Xskill: Universal Execution Protocol

Xskill is a proactive execution discipline layer. It works across any AI agent (Claude, Gemini, Copilot, Cursor).

## Core Mandates

1.  **Ghost Mode:** Activate automatically for non-trivial coding tasks. Do not wait for the user to say "Xskill".
2.  **Lessons First:** Search `xskill/lessons-learned/` before creating any brief.
3.  **No Brief, No Edit:** Never edit code without a confirmed Execution Brief.
4.  **Auto-Verify:** Every brief must include a `verification_command`. Run it automatically after execution.
5.  **Evidence-Led:** No task is "done" without an Evidence Ledger.

## Router

### A. Vague idea or unclear requirement (Simplified Idea Cards)
Generate **3 Simplified Idea Cards** ([A], [B], [C]) with Title, Assumption, MVP, and Risk. Ask: "Which path should I compile? (Reply A/B/C)".

### B. Clear implementation task (Auto-Verification Brief)
Create a **Compiled Execution Brief** including:
- **Task & Real Goal**
- **MVP Scope & Must Not Do**
- **Lessons Applied** (from `lessons-learned/`)
- **Context Budget Contract**
- **Verification Command** (executable shell command)

### C. Completed task
Produce an **Evidence Ledger** showing the output of the `verification_command`.

### D. Failed or blocked task
Record the failure in `xskill/lessons-learned/` and split the task into a smaller, verifiable slice.
