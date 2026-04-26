# Xskill

**Context diet for AI coding agents.**

Xskill is a portable skill bundle that helps coding agents read less context, touch fewer files, and prove what changed.

Most agent workflows add more context.

Xskill removes context until the task becomes safe to execute.

Before planning, Xskill can run a lightweight Five Whys and inversion pass: what is the real goal, and how could this fail?

After the real goal is clear, Xskill uses first-principles reasoning and Occam's Razor to cut the request down to the smallest necessary MVP. Larger tasks then get a lightweight semantic architecture sketch for module boundaries, coupling risks, and decoupling rules. Implementation planning uses a small-batch path: smallest useful slice, working increment, lean waste removal, minimal safety buffer, then TDD micro-loops when the route is still too large.

```text
Use Xskill to create an execution brief before editing code:
Fix password reset bug.
```

Expected output:

```md
# Execution Brief

## Task
Fix password reset bug.

## Goal
Fix reset token expiry validation without refactoring the auth provider.

## Context Budget
- Max files to read: 4
- Max files to touch: 2
- Files to avoid:
  - src/oauth/**
  - src/billing/**

## Checks
- pytest tests/auth/test_reset.py

## Evidence Required
- Failing test before the fix
- Passing test after the fix

## Stop Condition
Stop if the fix requires rewriting auth provider internals.
```

**Less context. Smaller changes. Verified progress.**

---

## What Xskill is

Xskill is **not** a CLI, npm package, Python package, autonomous agent, or full runtime.

Xskill is a **portable skill bundle**:

```text
Download zip.
Unzip.
Copy the xskill/ folder into your agent skills directory.
Use it with your coding agent.
```

It works best with agents that can read `SKILL.md` files or repository instructions such as `AGENTS.md`. If your agent does not support skills directly, open the relevant `SKILL.md` file and paste it into the agent before a task.

---

## Why this exists

AI coding agents are powerful, but they often fail in predictable ways:

| Without Xskill | With Xskill |
|---|---|
| Reads too much context | Reads only the relevant slice |
| Touches unrelated files | Gets a context budget |
| Says “done” without proof | Produces an evidence ledger |
| Retries failed tasks blindly | Splits failure into smaller work |
| Accumulates huge rule files | Loads one skill at a time |

Xskill focuses on one job:

> Turn vague agent work into bounded, verifiable execution.

---

## Install

Xskill does not require npm, npx, pip, Python, or a command-line tool.

1. Download the latest `xskill-v*.zip` from GitHub Releases.
2. Unzip it.
3. Copy the `xskill/` folder into your agent skills directory.

Recommended global location:

```text
~/.agents/skills/xskill
```

Recommended project-local location:

```text
your-project/.agents/skills/xskill
```

Optional: copy `AGENTS.md` into your project root.

Final structure:

```text
.agents/skills/xskill/
  question-requirements/SKILL.md
  delete-scope/SKILL.md
  semantic-architecture/SKILL.md
  optimize-path/SKILL.md
  shorten-iteration/SKILL.md
  automate-after-stable/SKILL.md
  semantic-memory/SKILL.md
  learn-after-run/SKILL.md
  templates/
  examples/
```

Restart your coding agent after copying the files.

---

## Quick use

For most non-trivial coding tasks, ask:

```text
Use Xskill to create an execution brief before editing code:
<your task>
```

For unclear or risky tasks:

```text
Use Xskill question-requirements for:
<your task>
```

The agent should first run Five Whys and inversion before proposing an implementation.

After requirements are clear, cut scope first:

```text
Use Xskill delete-scope after question-requirements for:
<your task>
```

For broad or multi-module MVPs, sketch architecture after scope deletion:

```text
Use Xskill semantic-architecture after delete-scope for:
<your task>
```

For implementation:

```text
Use Xskill optimize-path after semantic-architecture or delete-scope for:
<your task>
```

After completion:

```text
Use Xskill to produce an evidence ledger for what changed.
```

After a non-trivial run:

```text
Use Xskill learn-after-run to extract reusable learning from the evidence.
```

If the task fails:

```text
Use Xskill shorten-iteration to split this selected path or failed task into TDD micro-loops.
```

---

## First-principles scope deletion

After the real goal is clear, Xskill does not design the full system immediately.

It first asks:

```text
What is the irreducible user outcome?
What capability is truly required?
What evidence proves the MVP works?
Which entities can be deleted or deferred?
```

The rule is simple:

> Do not add entities without necessity.

`delete-scope` produces an MVP nucleus before architecture:

- one user outcome
- one primary workflow
- minimum artifacts
- minimum verification
- explicit non-goals

Then `semantic-architecture` can use that MVP nucleus to define module boundaries and decoupling rules.

## Small-batch optimize path

After MVP scope and module boundaries are clear, Xskill does not jump into a large implementation plan.

`optimize-path` selects one route using four filters:

- **Small-batch quick response**: start with the smallest slice that can produce feedback.
- **Agile working increment**: prefer something observable and reviewable over a broad plan.
- **Lean waste removal**: delete steps that do not produce verified learning.
- **Minimal safety buffer**: keep rollback, stop conditions, and fallback checks without building just-in-case systems.

If the selected route is still too large, `shorten-iteration` breaks it into TDD micro-loops:

```text
RED -> GREEN -> REFACTOR -> EVIDENCE
```

Each loop should have one goal, one verification point, one small implementation boundary, and one evidence handoff.

## Core artifacts


Xskill is built around eight lightweight artifacts.

### 1. Question Requirements Report

A pre-planning challenge that uses Five Whys and inversion to identify the real goal, likely failure paths, assumptions, success criteria, non-goals, and a continue/reduce/ask/stop decision.

See: [`xskill/templates/question-requirements-report.md`](xskill/templates/question-requirements-report.md)

### 2. Semantic Architecture Report

A lightweight module map used after requirements are clarified and before implementation planning.

It captures:

- MVP slice
- modules
- module relationships
- coupling risks
- decoupling rules
- MVP-first build order
- deferred modules

See: [`xskill/templates/semantic-architecture-report.md`](xskill/templates/semantic-architecture-report.md)

This is not a graph database or runtime. It is a short planning artifact for larger tasks.

### 3. Optimize Path Report

A small-batch implementation route that selects the smallest stable path that can produce verified progress.

It captures:

- candidate paths
- small-batch slice
- working increment
- lean waste removed
- minimal safety buffer
- verification strategy
- context budget

See: [`xskill/templates/optimize-path-report.md`](xskill/templates/optimize-path-report.md)

### 4. Shorten Iteration Report

A TDD micro-loop plan used when the selected path is too large or a previous attempt failed.

It captures:

- iteration budget
- RED/GREEN/REFACTOR/EVIDENCE loops
- files per loop
- stop conditions
- failure split rules
- evidence ledger handoff

See: [`xskill/templates/shorten-iteration-report.md`](xskill/templates/shorten-iteration-report.md)

### 5. Execution Brief

A compact task plan that tells the agent what to do, what not to do, and how success will be verified.

See: [`xskill/templates/execution-brief.md`](xskill/templates/execution-brief.md)

### 6. Context Budget

A boundary contract for the agent.

It defines:

- max files to read
- max files to touch
- files to avoid
- allowed context
- forbidden context
- stop condition

See: [`xskill/templates/context-budget.md`](xskill/templates/context-budget.md)

### 7. Evidence Ledger

A record of what actually happened.

It captures:

- files touched
- checks run
- verified claims
- unverified claims
- scope violations
- remaining risk

See: [`xskill/templates/evidence-ledger.md`](xskill/templates/evidence-ledger.md)

If there is no evidence, the task is not done.

### 8. Iteration Learning Note

A short post-run note that turns evidence into reusable learning.

It captures:

- what worked
- what failed or drifted
- which context was wasted
- a reusable rule candidate
- whether the rule should be promoted

See: [`xskill/templates/iteration-learning-note.md`](xskill/templates/iteration-learning-note.md)

Xskill does not auto-improve blindly. It learns only from evidence.

---

## The Xskill steps

| Step | Skill | Purpose |
|---|---|---|
| Question | `question-requirements` | Run Five Whys and inversion to reveal the real goal, failure paths, assumptions, and decision |
| Architecture | `semantic-architecture` | Sketch the MVP slice, module map, coupling risks, and decoupling rules for larger tasks |
| Delete | `delete-scope` | Remove unnecessary work and define scope boundaries |
| Optimize | `optimize-path` | Select the smallest stable route using small-batch, agile, lean, and minimal safety-buffer filters |
| Shorten | `shorten-iteration` | Split large or failed routes into TDD micro-loops with evidence handoff |
| Automate | `automate-after-stable` | Automate only stable repeated work |
| Support | `semantic-memory` | Select only the context needed for this task |
| Learning | `learn-after-run` | Extract reusable learning after a run without blindly modifying skills |

These are not always-on rules. Load only the skill that matches the current task.

---

## When to use Xskill

Use Xskill when:

- the task is vague
- the task may touch many files
- the agent may over-read context
- the change affects logic, APIs, data, security, or architecture
- verification matters
- a previous agent run failed or drifted

Do not use the full workflow for:

- typo fixes
- simple copy edits
- tiny config changes
- obvious one-line fixes

For small changes, use only the relevant skill or skip Xskill entirely.

---

## Design rules

Xskill should stay small.

1. Do not load long context by default.
2. Question vague or risky requests with Five Whys and inversion before planning.
3. For multi-module work, sketch semantic architecture after deleting scope.
4. Select the smallest stable implementation path before editing.
5. Prefer small-batch working increments over broad plans.
6. Respect the context budget.
7. Touch the smallest possible set of files.
8. Split large or failed work into TDD micro-loops.
9. Verify with evidence.
10. If blocked, split the task smaller.
11. Do not claim completion without an evidence ledger.

---

## Project structure

```text
Xskill/
  README.md
  AGENTS.md
  xskill/
    question-requirements/SKILL.md
    semantic-architecture/SKILL.md
    delete-scope/SKILL.md
    optimize-path/SKILL.md
    shorten-iteration/SKILL.md
    automate-after-stable/SKILL.md
    semantic-memory/SKILL.md
    learn-after-run/SKILL.md
    templates/
      question-requirements-report.md
      semantic-architecture-report.md
      execution-brief.md
      context-budget.md
      evidence-ledger.md
      iteration-learning-note.md
    examples/
      password-reset.question-requirements.md
      xskill.semantic-architecture.md
      password-reset.execution-brief.md
      password-reset.evidence-ledger.md
      password-reset.iteration-learning-note.md
  docs/
    portable-install.md
    design.md
    release-checklist.md
```

---

## Example

See [`xskill/examples/password-reset.question-requirements.md`](xskill/examples/password-reset.question-requirements.md), [`xskill/examples/xskill.semantic-architecture.md`](xskill/examples/xskill.semantic-architecture.md), [`xskill/examples/password-reset.execution-brief.md`](xskill/examples/password-reset.execution-brief.md), and [`xskill/examples/password-reset.evidence-ledger.md`](xskill/examples/password-reset.evidence-ledger.md).

---

## Non-goals

Xskill is intentionally not:

- a CLI-first tool
- a package manager installation flow
- a multi-agent framework
- a semantic graph database
- an autonomous coding loop
- an automatic self-improvement engine
- a replacement for your coding agent

Future automation or deeper self-iteration may exist, but only after the manual skill workflow is proven stable.

---

## Influences

Xskill is influenced by ideas from AI coding workflow projects such as Superpowers, GSD, Ralph, gstack, Karpathy-style coding principles, Graphify, Hermes Agent, and agent harness projects.

It does not copy their prompts or workflows. It extracts general execution mechanisms and compresses them into a smaller portable skill system.

---

## Description

Recommended GitHub description:

```text
Context diet for AI coding agents. Less context, smaller changes, verified progress.
```

Recommended topics:

```text
ai-agents, coding-agents, agent-skills, agents-md, context-engineering, claude-code, codex, cursor, developer-tools
```

---

## License

MIT
