# Xskill

**Context diet for AI coding agents.**

Xskill is a portable skill bundle that helps coding agents read less context, touch fewer files, and prove what changed.

Most agent workflows add more context.

Xskill removes context until the task becomes safe to execute.

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
  optimize-path/SKILL.md
  shorten-iteration/SKILL.md
  automate-after-stable/SKILL.md
  semantic-memory/SKILL.md
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

For unclear tasks:

```text
Use Xskill question-requirements for:
<your task>
```

For broad tasks:

```text
Use Xskill delete-scope for:
<your task>
```

For implementation:

```text
Use Xskill optimize-path for:
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
Use Xskill shorten-iteration to split this failed task into smaller verified work.
```

---

## Core artifacts

Xskill is built around three artifacts.

### 1. Execution Brief

A compact task plan that tells the agent what to do, what not to do, and how success will be verified.

See: [`xskill/templates/execution-brief.md`](xskill/templates/execution-brief.md)

### 2. Context Budget

A boundary contract for the agent.

It defines:

- max files to read
- max files to touch
- files to avoid
- allowed context
- forbidden context
- stop condition

See: [`xskill/templates/context-budget.md`](xskill/templates/context-budget.md)

### 3. Evidence Ledger

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

### 4. Iteration Learning Note

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
| Question | `question-requirements` | Challenge assumptions, risks, and success criteria |
| Delete | `delete-scope` | Remove unnecessary work and define scope boundaries |
| Optimize | `optimize-path` | Create the smallest correct execution path |
| Shorten | `shorten-iteration` | Split large or failed work into smaller verified tasks |
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
2. Create an execution brief before non-trivial edits.
3. Respect the context budget.
4. Touch the smallest possible set of files.
5. Verify with evidence.
6. If blocked, split the task smaller.
7. Do not claim completion without an evidence ledger.

---

## Project structure

```text
Xskill/
  README.md
  AGENTS.md
  xskill/
    question-requirements/SKILL.md
    delete-scope/SKILL.md
    optimize-path/SKILL.md
    shorten-iteration/SKILL.md
    automate-after-stable/SKILL.md
    semantic-memory/SKILL.md
    learn-after-run/SKILL.md
    templates/
      execution-brief.md
      context-budget.md
      evidence-ledger.md
      iteration-learning-note.md
    examples/
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

See [`xskill/examples/password-reset.execution-brief.md`](xskill/examples/password-reset.execution-brief.md) and [`xskill/examples/password-reset.evidence-ledger.md`](xskill/examples/password-reset.evidence-ledger.md).

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
