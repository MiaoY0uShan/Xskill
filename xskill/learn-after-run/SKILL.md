---
name: xskill-learn-after-run
description: Use after a non-trivial agent run to convert evidence into reusable learning. Produces an iteration learning note, rule candidate, and promotion decision without automatically changing skills.
---

# Xskill: Learn After Run

Learn from evidence, not vibes.

This skill is the lightweight self-iteration layer for Xskill. It helps the agent extract reusable learning after a run without turning Xskill into an autonomous runtime.

## Use when

- A non-trivial task has completed.
- A task failed, drifted, or got blocked.
- The agent read too much context.
- The agent touched too many files.
- A check failed or produced a useful lesson.
- The same mistake has appeared before.
- A workflow may deserve future automation or a skill update.

## Do not use when

- The task was a tiny typo or copy edit.
- There is no evidence from the run.
- The agent is trying to justify a change it cannot verify.
- The proposed learning is a one-off preference, not a reusable rule.

## Goal

Produce an iteration learning note that records what worked, what failed, what context was wasted, and whether a rule should be promoted.

This skill does **not** automatically rewrite skills. It proposes learning. Promotion requires evidence.

## Procedure

1. Read the execution brief and evidence ledger if available.
2. Summarize the result: pass, fail, blocked, or partial.
3. Identify what worked.
4. Identify what failed or caused drift.
5. Identify unnecessary context, unnecessary files, or unnecessary skills.
6. Extract one reusable rule candidate.
7. Decide whether to promote the rule.
8. If the task failed, create the smallest next task.
9. If the same issue has repeated, propose a precise patch to an existing skill.

## Promotion rules

Do not promote a lesson into a skill unless at least one is true:

- The same issue happened more than once.
- The lesson would clearly reduce context, scope, or verification risk.
- The lesson prevents a repeated class of failure.
- The lesson adds a better stop condition.

Never create a new skill when a small patch to an existing skill is enough.

## Output contract

Return this structure:

```md
# Iteration Learning Note

## Task
...

## Result
Pass | Fail | Blocked | Partial

## Evidence Used
- ...

## What Worked
- ...

## What Failed Or Drifted
- ...

## Context Waste
- Files read unnecessarily: ...
- Files touched unnecessarily: ...
- Skills loaded unnecessarily: ...
- Assumptions that were wrong: ...

## Smaller Next Task
Required only if failed, blocked, or partial.

## Reusable Rule Candidate
...

## Promotion Decision
Do not promote | Keep as local note | Patch existing skill | Create new skill later

## Skill Patch Candidate
Only include if promotion decision is `Patch existing skill`.

Target skill: ...
Patch: ...
Reason: ...
```

## Rules

- Do not auto-improve blindly.
- Do not promote one-off lessons.
- Prefer deleting or narrowing rules over adding broad rules.
- A learning is only useful if it reduces context, reduces scope, improves verification, or prevents repeated failure.
- If there is no evidence, record that no learning can be trusted.
