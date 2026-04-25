# Xskill

**Context diet for AI coding agents.**

Xskill is a portable skill bundle that turns vague coding tasks into small, bounded, verifiable execution briefs.

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
Fix reset token expiry validation.

## Context Budget
- Max files to read: 4
- Max files to touch: 2
- Files to avoid:
  - src/oauth/**
  - src/billing/**

## Checks
- pytest tests/auth/test_reset.py

## Evidence Required
- Failing test before fix
- Passing test after fix

## Stop Condition
Do not refactor auth provider internals.
```

**Less context. Smaller changes. Verified progress.**

---

## What this is

Xskill is not a CLI, npm package, Python package, or full agent framework.

It is a **portable skill bundle**:

```text
Download zip.
Unzip.
Copy the xskill/ folder into your agent skills directory.
Use it with your coding agent.
```

Xskill is designed for AI coding agents that can read `SKILL.md` files or project-level agent instructions.

---

## Why it exists

AI coding agents often fail in predictable ways:

| Without Xskill | With Xskill |
|---|---|
| Reads too much context | Reads only the relevant slice |
| Touches unrelated files | Gets a context budget |
| Says "done" without proof | Produces an evidence ledger |
| Retries failed tasks blindly | Splits failure into smaller work |
| Accumulates huge rule files | Loads one skill at a time |

Xskill focuses on one job:

> Turn open-ended agent work into bounded, evidence-backed execution.

---

## Installation

Xskill does not require npm, pip, or a command-line installer.

### Option A: Project-local installation

Use this when you want Xskill available only inside one repository.

1. Download the latest `xskill-v0.1.0.zip` from GitHub Releases.
2. Unzip it.
3. Copy the `xskill/` folder into your project.

Recommended structure:

```text
your-project/
  AGENTS.md
  .agents/
    skills/
      xskill/
        question-requirements/SKILL.md
        delete-scope/SKILL.md
        optimize-path/SKILL.md
        shorten-iteration/SKILL.md
        automate-after-stable/SKILL.md
        semantic-memory/SKILL.md
```

If your agent does not use `.agents/skills/`, place the `xskill/` folder wherever your agent expects skill folders.

### Option B: Global installation

Use this when you want Xskill available across projects.

```text
~/.agents/skills/xskill/
  question-requirements/SKILL.md
  delete-scope/SKILL.md
  optimize-path/SKILL.md
  shorten-iteration/SKILL.md
  automate-after-stable/SKILL.md
  semantic-memory/SKILL.md
```

Restart your coding agent after copying the folder.

---

## AGENTS.md

Xskill includes a root `AGENTS.md` template.

Copy it to your project root if your coding agent supports `AGENTS.md`.

`AGENTS.md` is the always-on router. It should stay short.

The detailed procedures live in the skill files and should be loaded only when needed.

---

## How to use

Ask your coding agent:

```text
Use Xskill to create an execution brief before editing code:
<your task>
```

For larger tasks:

```text
Use Xskill question-requirements, then delete-scope, then optimize-path for:
<your task>
```

For failed tasks:

```text
Use Xskill shorten-iteration to split this failure into smaller verifiable tasks.
```

For completed work:

```text
Use Xskill to produce an evidence ledger for the completed change.
```

---

## The five-step system

Xskill adapts the five-step engineering loop into agent skills.

| Step | Skill | Output |
|---|---|---|
| Question | `question-requirements` | assumptions, risks, success criteria |
| Delete | `delete-scope` | minimum slice, files to avoid |
| Optimize | `optimize-path` | smallest implementation path |
| Iterate | `shorten-iteration` | atomic tasks and stop conditions |
| Automate | `automate-after-stable` | repeatable commands and guardrails |

A supporting skill, `semantic-memory`, keeps long-term project context lightweight.

---

## Core artifacts

### Execution Brief

A short plan the agent must follow before editing code.

```md
# Execution Brief

## Task
...

## Goal
...

## Context Budget
- Max files to read: ...
- Max files to touch: ...
- Files to avoid: ...

## Checks
...

## Evidence Required
...

## Stop Condition
...
```

### Context Budget

A hard boundary for agent behavior.

```md
# Context Budget

- Max files to read: 5
- Max files to touch: 3
- Forbidden context:
  - unrelated migrations
  - auth provider internals
- Scope boundary:
  - implement reset-token validation only
```

### Evidence Ledger

A record of what changed and what proves it.

```md
# Evidence Ledger

## Files touched
- src/auth/reset.ts
- tests/auth/test_reset.ts

## Commands run
- pytest tests/auth/test_reset.py — pass

## Verified claims
- Expired reset tokens are rejected.

## Unverified claims
- None.

## Scope violations
- None.
```

---

## Folder structure

```text
xskill/
  question-requirements/
    SKILL.md
  delete-scope/
    SKILL.md
  optimize-path/
    SKILL.md
  shorten-iteration/
    SKILL.md
  automate-after-stable/
    SKILL.md
  semantic-memory/
    SKILL.md
  templates/
    execution-brief.md
    context-budget.md
    evidence-ledger.md
  examples/
    password-reset.execution-brief.md
    password-reset.evidence-ledger.md
```

---

## Design principles

### Keep the always-on layer small

Do not paste the full system into every agent instruction file.

`AGENTS.md` should route behavior.

Skills should contain the actual workflow.

### Prefer boundaries over advice

Weak instruction:

```text
Be careful not to change too much.
```

Xskill instruction:

```text
Max files to touch: 2.
Files to avoid: src/oauth/**.
Stop if auth provider refactor is required.
```

### Evidence over claims

The agent should not claim completion without evidence.

Tests, typechecks, lint results, screenshots, manual verification notes, or explicit acceptance checks count as evidence.

### Failure should shrink scope

A failed task should produce a smaller follow-up task instead of an unbounded retry.

---

## Influences

Xskill is influenced by ideas from AI coding workflow projects such as GSD, Superpowers, Ralph, gstack, Karpathy-style coding principles, Graphify, and agent harness projects.

It does not copy their prompts or workflows.

It extracts general execution mechanisms and compresses them into a smaller skill bundle.

---

## Disclaimer

Xskill is inspired by the five-step engineering method popularized by Elon Musk.

It is not affiliated with Elon Musk, Tesla, SpaceX, X, xAI, or any referenced open-source project.

All skill text and implementation in this repository are original unless otherwise stated.

---

## License

MIT
