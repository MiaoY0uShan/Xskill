---
name: xskill-optimize-path
description: Use after MVP scope is defined to choose the smallest stable implementation path, small-batch slice, verification strategy, and minimal safety buffer before coding.
---

# Xskill: Optimize Path

Choose the smallest stable path that can produce verified progress.

This skill converts the MVP nucleus and semantic architecture into an execution path. It does not write code. It does not expand the MVP. It selects the route that should be implemented next.

## Use when

- `question-requirements` has identified the real goal.
- `delete-scope` has defined the MVP nucleus and scope boundary.
- `semantic-architecture` has defined module boundaries for larger tasks, if needed.
- The agent is ready to choose a coding path, checks, and evidence requirements.
- The task needs a bounded route before implementation.

Do not use this skill to redesign the product goal or expand the MVP.

---

## Core principle

> Choose the smallest stable path that can produce verified progress.

The best path is not the biggest plan. It is the path with the smallest useful batch, clear verification, low waste, acceptable risk, and a safe stop condition.

---

## Path filters

Use these four filters before choosing an implementation path.

### 1. Small-batch quick response

Do not bet on a large batch before feedback exists.

For Xskill, this means:

- Start with the smallest verifiable slice.
- Prefer one behavior, one module boundary, or one bug reproduction at a time.
- Expand only after evidence exists.
- Do not implement the full future workflow in the first pass.

Ask:

```text
What is the smallest slice that can produce useful feedback?
What is the smallest change that can prove the path works?
What can be postponed until after this slice passes?
```

### 2. Agile working increment

Prefer a working increment over a comprehensive plan.

For Xskill, this means:

- The selected path should produce something observable.
- Progress should be measured by working behavior or verified artifact, not by explanation length.
- The path should allow early feedback.

Ask:

```text
What is the first working increment?
Can it be reviewed or tested independently?
What evidence will show that this increment is real?
```

### 3. Lean waste removal

Remove work that does not contribute to the selected verification target.

Waste includes:

- premature abstractions
- broad refactors
- speculative adapters
- unnecessary documentation changes
- extra tests not tied to the current risk
- reading files outside the context budget
- supporting future modes before the MVP needs them

Ask:

```text
Which steps do not create verified learning?
Which files or modules can be avoided?
Which abstractions are premature?
What can be deleted from this route?
```

### 4. Minimal just-in-case buffer

Use a small safety buffer, not a second hidden project.

Valid buffers:

- rollback plan
- stop condition
- fallback check
- manual verification note
- small compatibility guard

Invalid buffers:

- building an unused plugin system
- implementing a backup architecture
- adding future provider support
- creating a runtime because it might be needed later

Ask:

```text
What is the minimum safety buffer needed for this task?
What would be excessive just-in-case scope?
How can we make this reversible without overbuilding?
```

---

## Procedure

### 1. Read the upstream reports

Use the latest available outputs from:

- Question Requirements Report
- Delete Scope Report
- Semantic Architecture Report, if the task is multi-module

If the MVP nucleus is missing, stop and ask to run `delete-scope` first.

### 2. Define candidate paths

Generate 2-4 candidate paths.

Each path should have:

- scope
- touched modules
- expected evidence
- risk
- reversibility
- waste risk

Do not generate paths that violate explicit non-goals.

### 3. Evaluate candidate paths

Compare paths using:

- batch size
- stability
- verification clarity
- waste removed
- reversibility
- coupling risk
- context cost

Prefer paths that are smaller, more reversible, and easier to verify.

### 4. Select one path

Choose exactly one selected path.

If no path is safe, return `Decision: ask_user` or recommend `shorten-iteration`.

### 5. Define the small-batch slice

State the first slice to build.

It should include:

- one primary behavior or artifact
- files/modules likely involved
- what is explicitly excluded
- how feedback will be collected

### 6. Define the working increment

Describe what will exist after the slice is complete.

It must be observable through:

- a test
- a check
- a generated artifact
- a manual review
- a reproducible command

### 7. Remove lean waste

List what was removed from the path because it does not help the current verification target.

### 8. Define the minimal safety buffer

Define only the required safety measures.

Examples:

- rollback note
- stop condition
- compatibility check
- one fallback verification

### 9. Define verification strategy

Choose one:

- None
- Smoke
- Unit
- Integration
- E2E
- TDD required
- Manual review with evidence

Use TDD when the task involves:

- bug fixes
- core logic
- public APIs
- security-sensitive behavior
- data migration or validation

Do not force TDD for:

- documentation
- copy changes
- tiny config edits
- exploratory spikes
- simple UI text changes

### 10. Define refactor boundary

Specify whether refactoring is allowed.

Use:

- `none`: no refactor allowed
- `local`: only inside touched module
- `supporting`: allowed only to make the selected path testable
- `defer`: refactor should become a separate task

### 11. Recommend next skill

Use:

- `shorten-iteration` if the selected path is still too large or needs multiple TDD loops
- `evidence-ledger` after execution
- `learn-after-run` after evidence is collected

---

## Output contract

Return this structure:

```md
# Optimize Path Report

## Input
- Real goal:
- MVP nucleus:
- Scope boundary:
- Semantic architecture used: yes / no

## Candidate Paths

### Path A
- Summary:
- Scope:
- Modules/files likely involved:
- Verification:
- Risk:
- Reversibility:
- Waste risk:

### Path B
- Summary:
- Scope:
- Modules/files likely involved:
- Verification:
- Risk:
- Reversibility:
- Waste risk:

## Path Evaluation

| Path | Batch size | Stability | Verification clarity | Waste removed | Reversibility | Coupling risk | Decision |
|---|---|---|---|---|---|---|---|
| A | small/medium/large | low/medium/high | low/medium/high | low/medium/high | low/medium/high | low/medium/high | keep/reject |
| B | small/medium/large | low/medium/high | low/medium/high | low/medium/high | low/medium/high | low/medium/high | keep/reject |

## Selected Path

## Small-Batch Slice

## Working Increment

## Lean Waste Removed

## Minimal Safety Buffer

## Verification Strategy

## Context Budget
- Max files to read:
- Max files to touch:
- Files to avoid:
- Forbidden context:

## Implementation Path
1.
2.
3.

## Refactor Boundary
none / local / supporting / defer

## Evidence Required
-

## Stop Condition

## Decision
continue | reduce_scope | ask_user | stop

## Recommended Next Skill
shorten-iteration | evidence-ledger | learn-after-run
```

---

## Rules

- Do not write code.
- Do not expand the MVP.
- Do not choose a path that lacks verification.
- Do not choose the fastest path if it is not reversible or testable.
- Do not add just-in-case systems. Add only minimal safety buffers.
- Prefer small-batch, working, low-waste increments.
- If the path is still too large, send it to `shorten-iteration`.
