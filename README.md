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

Xskill is **not** a CLI, npm package, Python package, or full agent framework.

It is a **portable skill bundle**:

```text
Download zip.
Unzip.
Copy the xskill/ folder into your agent skills directory.
Use it with your coding agent.
```

Xskill works best with AI coding agents that can read `SKILL.md` files, project-level instructions, or an `AGENTS.md` file.

If your agent does not support skills directly, you can still open the relevant `SKILL.md` file and paste it into the agent before a task.

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

> Turn open-ended agent work into bounded, evidence-backed execution.

---

## Installation

Xskill does not require npm, pip, npx, or a command-line installer.

### Option A: Project-local installation

Use this when you want Xskill available only inside one repository.

1. Download the latest `xskill-v0.1.0.zip` from GitHub Releases.
2. Unzip it.
3. Copy the `xskill/` folder into your project’s agent skills directory.
4. Optionally copy the root `AGENTS.md` template into your project root.
5. Restart your coding agent.

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

If your agent uses a different skills directory, place the `xskill/` folder there instead.

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

Then restart your coding agent.

---

## First use

After installation, ask your agent:

```text
Use Xskill to create an execution brief before editing code:
<your task>
```

For example:

```text
Use Xskill to create an execution brief before editing code:
Fix password reset bug.
```

For a larger task:

```text
Use Xskill question-requirements, then delete-scope, then optimize-path for:
Add password reset flow.
```

For a failed attempt:

```text
Use Xskill shorten-iteration to split this failure into smaller verifiable tasks.
```

For completed work:

```text
Use Xskill to produce an evidence ledger for the completed change.
```

---

## The five-step system

Xskill adapts a five-step engineering loop into agent skills.

| Step | Skill | Use it for | Output |
|---|---|---|---|
| Question | `question-requirements` | vague or risky tasks | assumptions, risks, success criteria |
| Delete | `delete-scope` | broad scope | minimum slice, files to avoid |
| Optimize | `optimize-path` | pre-coding plan | execution brief, checks, evidence |
| Iterate | `shorten-iteration` | failed or oversized tasks | atomic tasks, stop conditions |
| Automate | `automate-after-stable` | repeated stable work | repeatable commands and guardrails |

A supporting skill, `semantic-memory`, keeps long-term project context lightweight.

---

## Core artifacts

Xskill is built around three artifacts.

### 1. Execution Brief

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

### 2. Context Budget

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

Most agent workflows add context.

Xskill defines what the agent should not read, not touch, and not claim.

### 3. Evidence Ledger

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

If there is no evidence, the task is not done.

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

## AGENTS.md

Xskill includes a root `AGENTS.md` template.

Use it as the always-on router for a project.

It should stay short:

```md
# AGENTS.md

This project uses Xskill.

Before non-trivial coding tasks:
1. Create or load an Xskill execution brief.
2. Respect the context budget.
3. Do not read or modify files outside the declared scope unless necessary.
4. Run the required checks.
5. Do not claim completion without evidence.
6. If blocked, split the task into a smaller task instead of retrying blindly.
```

The detailed procedures live in the skill files and should be loaded only when needed.

---

## Design principles

### Keep the always-on layer small

Do not paste the full system into every agent instruction file.

`AGENTS.md` should route behavior. Skills should contain the workflow.

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

## Example workflow

```text
User task
  ↓
question-requirements
  ↓
delete-scope
  ↓
optimize-path
  ↓
Execution Brief
  ↓
Agent edits code within the Context Budget
  ↓
Checks run
  ↓
Evidence Ledger
  ↓
Done, blocked, or split into a smaller task
```

---

## When not to use Xskill

Do not use Xskill when the task is already trivial.

Examples:

- Fixing a typo
- Renaming a heading
- Formatting a small snippet
- Answering a question without editing code

Use Xskill when scope, risk, context size, or verification matters.

---

## Roadmap

- [x] Portable skill bundle
- [x] Five core skills
- [x] Semantic memory support skill
- [x] Execution brief template
- [x] Context budget template
- [x] Evidence ledger template
- [x] AGENTS.md template
- [ ] Better install examples for specific agents
- [ ] More real-world execution brief examples
- [ ] More evidence ledger examples
- [ ] Optional adapters for common agent folders

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
