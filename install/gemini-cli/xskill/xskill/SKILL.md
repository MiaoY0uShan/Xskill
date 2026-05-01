---
name: xskill
description: "Use proactively before coding tasks to choose the lightest evidence-backed path: tiny brief, Execution Brief, or full chain. Manual override: \"Xskill: <task or idea>\"."
---

# Xskill: Universal Execution Protocol

Xskill is a proactive execution discipline layer. It works across any AI agent (Claude, Gemini, Copilot, Cursor).

## Core Mandates

1. **Ghost Mode:** Activate automatically for coding tasks, then choose the lightest path that can still be verified.
2. **Lessons First:** Search `xskill/lessons-learned/` before creating any brief.
3. **No Proof, No Edit:** Before editing, state what will be read, what will be touched, and how it will be verified.
4. **Auto-Verify:** Every path must include a verification command or explicit validation method. Run it after execution.
5. **Evidence-Led:** No task is "done" without test or validation results.
6. **Challenge Before Changing the System:** If the request changes Xskill itself, agent behavior, trigger rules, install boundaries, memory policy, or default workflow, do not edit immediately. First state the inferred goal, challenge weak assumptions, list the proposed change set, and ask for confirmation unless the user has already explicitly approved implementation.

## Default Paths

Use the smallest path that fits the task:

- **Small change:** Use a 3-5 line brief. Include task, files to read/touch, verification, and result. Do not generate a full Execution Brief or Evidence Ledger unless risk appears.
- **Medium change:** Use an Execution Brief plus Evidence Ledger. Keep both compact and focused on read/touch/verify.
- **Large, vague, architectural, or risky task:** Use the full chain: Idea Cards or question-requirements, delete-scope, semantic-architecture when needed, optimize-path, shorten-iteration when needed, Execution Brief, Evidence Ledger, and optional metrics/improvement.
- **Protocol or agent-behavior change:** Treat as high-impact even if the edit is small. Confirm the intent and boundaries before editing unless the user has explicitly said to implement the agreed feedback.

## Repository Boundary

`.agents/skills/` is local agent configuration, not project source. Do not commit it unless a repository explicitly documents otherwise. Prefer committing portable skill content under `xskill/` and install packages under `install/`.

## Router

### A. Small clear change (Tiny Brief)

Produce 3-5 lines:
- Task:
- Read/touch:
- Verify:
- Result after execution:

### B. Medium clear implementation task (Compact Execution Brief)

Create a compact **Execution Brief** including:
- **Task / Real Goal**
- **MVP Scope / Must Not Do**
- **Files to Read / Touch / Avoid**
- **Verification Command**
- **Stop Condition**

After execution, create a compact **Evidence Ledger** with commands run, result, files touched, and remaining risk.

### C. Vague idea or unclear requirement (Simplified Idea Cards)

Generate **3 Simplified Idea Cards** ([A], [B], [C]) with Title, Assumption, MVP, and Risk. Ask: "Which path should I compile? (Reply A/B/C)".

### D. Large, architectural, or risky task (Full Chain)

Use the full internal flow only when the work is broad, multi-module, ambiguous, high-risk, or requires architecture decisions.

### E. Protocol or agent-behavior change (Confirm First)

Before editing:
- Restate the requested behavior change.
- Challenge whether the change belongs in core rules, docs, install packs, or local config.
- List files likely to change.
- Ask for confirmation, unless the user explicitly says to implement already-discussed feedback.

### F. Completed task

Produce evidence at the same weight as the path used: validation line for small changes, Evidence Ledger for medium and large changes.

### G. Failed or blocked task

Record the failure in `xskill/lessons-learned/` and split the task into a smaller, verifiable slice.
