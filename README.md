# Xskill

**Context diet for AI coding agents.**

Xskill is a portable skill bundle that helps coding agents read less context, touch fewer files, and prove what changed.

Most agent workflows add more context.

Xskill removes context until the task becomes safe to execute.

Before planning, Xskill can run a lightweight Five Whys and inversion pass: what is the real goal, and how could this fail?

After the real goal is clear, Xskill uses first-principles reasoning and Occam's Razor to cut the request down to the smallest necessary MVP. Larger tasks then get a lightweight semantic architecture sketch for module boundaries, coupling risks, and decoupling rules. Implementation planning uses a small-batch path: smallest useful slice, working increment, lean waste removal, minimal safety buffer, then TDD micro-loops when the route is still too large.

After execution, Xskill records evidence and can improve from evidence-backed patterns through adaptive improvement and schema memory.

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

Xskill is **not** a CLI, npm package, Python package, autonomous agent, database, or full runtime.

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
| Learns from vibes | Learns from evidence-backed schemas |
| Automates confusion | Only marks stable repetition as automation candidate |

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
  evidence-ledger/SKILL.md
  adaptive-improvement/SKILL.md
  schema-memory/SKILL.md
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
Use Xskill optimize-path after scope and architecture are clear for:
<your task>
```

If the selected route is too large or a previous attempt failed:

```text
Use Xskill shorten-iteration to split this selected path into TDD micro-loops.
```

After execution:

```text
Use Xskill evidence-ledger to record what changed, what was verified, and what remains unverified.
```

After a non-trivial run with evidence:

```text
Use Xskill adaptive-improvement to extract reusable improvement from the evidence ledger.
```

If a repeated task pattern emerges:

```text
Use Xskill schema-memory to create or update a schema memory card.
```

---

## Workflow

```text
question-requirements
→ delete-scope
→ semantic-architecture
→ optimize-path
→ shorten-iteration
→ evidence-ledger
→ adaptive-improvement
→ schema-memory
```

Small tasks can skip most of this. Load only the relevant skill.

---

## Core artifacts

Xskill is built around lightweight artifacts.

### 1. Question Requirements Report

A pre-planning challenge that uses Five Whys and inversion to identify the real goal, likely failure paths, assumptions, success criteria, non-goals, and a continue/reduce/ask/stop decision.

See: [`xskill/templates/question-requirements-report.md`](xskill/templates/question-requirements-report.md)

### 2. Delete Scope Report

A first-principles and Occam's Razor pass that cuts the real goal down to the smallest verifiable MVP nucleus before architecture.

See: [`xskill/templates/delete-scope-report.md`](xskill/templates/delete-scope-report.md)

### 3. Semantic Architecture Report

A lightweight module map used after scope deletion and before implementation planning.

It captures MVP slice, modules, module relationships, coupling risks, decoupling rules, MVP-first build order, and deferred modules.

See: [`xskill/templates/semantic-architecture-report.md`](xskill/templates/semantic-architecture-report.md)

This is not a graph database or runtime. It is a short planning artifact for larger tasks.

### 4. Optimize Path Report

A small-batch implementation route that selects the smallest stable path that can produce verified progress.

See: [`xskill/templates/optimize-path-report.md`](xskill/templates/optimize-path-report.md)

### 5. Shorten Iteration Report

A TDD micro-loop plan used when the selected path is too large or a previous attempt failed.

It uses:

```text
RED -> GREEN -> REFACTOR -> EVIDENCE
```

See: [`xskill/templates/shorten-iteration-report.md`](xskill/templates/shorten-iteration-report.md)

### 6. Execution Brief

A compact task plan that tells the agent what to do, what not to do, and how success will be verified.

See: [`xskill/templates/execution-brief.md`](xskill/templates/execution-brief.md)

### 7. Context Budget

A boundary contract for the agent: max files to read, max files to touch, files to avoid, allowed context, forbidden context, and stop condition.

See: [`xskill/templates/context-budget.md`](xskill/templates/context-budget.md)

### 8. Evidence Ledger

A record of what actually happened: files touched, checks run, verified claims, unverified claims, scope violations, and remaining risk.

See: [`xskill/templates/evidence-ledger.md`](xskill/templates/evidence-ledger.md)

If there is no evidence, the task is not done.

### 9. Adaptive Improvement Report

A post-run feedback report that decides whether evidence should become a local note, schema memory update, template improvement, checklist improvement, automation candidate, or no action.

See: [`xskill/templates/adaptive-improvement-report.md`](xskill/templates/adaptive-improvement-report.md)

### 10. Schema Memory Card

A reusable task-pattern card. It stores how a class of work should be handled: trigger, failure modes, context budget pattern, verification pattern, and stop conditions.

See: [`xskill/templates/schema-memory-card.md`](xskill/templates/schema-memory-card.md)

Xskill stores patterns, not raw memory.

---

## Adaptive improvement

Xskill does not auto-improve blindly.

It uses this chain:

```text
evidence ledger
→ adaptive improvement report
→ schema memory card
→ future execution brief
```

Rules:

- Xskill learns from evidence, not confidence.
- One run is usually not enough to promote a rule.
- Schema memory stores reusable task patterns, not raw context.
- Automation is only a candidate after repeated stable manual behavior.
- Do not add process unless it reduces context, narrows scope, improves verification, or prevents repeated failure.

---

## The Xskill skills

| Skill | Purpose |
|---|---|
| `question-requirements` | Run Five Whys and inversion to reveal the real goal, failure paths, assumptions, and decision |
| `delete-scope` | Use first principles and Occam's Razor to remove unnecessary entities and define the MVP nucleus |
| `semantic-architecture` | Sketch the MVP slice, module map, coupling risks, and decoupling rules for larger tasks |
| `optimize-path` | Select the smallest stable route using small-batch, agile, lean, and minimal safety-buffer filters |
| `shorten-iteration` | Split large or failed routes into TDD micro-loops with evidence handoff |
| `evidence-ledger` | Record what changed, what was verified, what remains unverified, and whether scope was violated |
| `adaptive-improvement` | Convert evidence into schema updates, checklist improvements, or automation candidates |
| `schema-memory` | Store reusable work patterns, failure modes, context budget patterns, and verification patterns |

These are not always-on rules. Load only the skill that matches the current task.

---

## Design rules

Xskill should stay small.

1. Do not load long context by default.
2. Question vague or risky requests with Five Whys and inversion before planning.
3. Delete scope with first principles and Occam's Razor before architecture.
4. For multi-module work, sketch semantic architecture after deleting scope.
5. Select the smallest stable implementation path before editing.
6. Prefer small-batch working increments over broad plans.
7. Respect the context budget.
8. Touch the smallest possible set of files.
9. Split large or failed work into TDD micro-loops.
10. Verify with evidence.
11. Learn only from evidence.
12. Store schemas, not raw memory.
13. Do not claim completion without an evidence ledger.

---

## Project structure

```text
Xskill/
  README.md
  AGENTS.md
  xskill/
    question-requirements/SKILL.md
    delete-scope/SKILL.md
    semantic-architecture/SKILL.md
    optimize-path/SKILL.md
    shorten-iteration/SKILL.md
    evidence-ledger/SKILL.md
    adaptive-improvement/SKILL.md
    schema-memory/SKILL.md
    templates/
      question-requirements-report.md
      delete-scope-report.md
      semantic-architecture-report.md
      optimize-path-report.md
      shorten-iteration-report.md
      execution-brief.md
      context-budget.md
      evidence-ledger.md
      adaptive-improvement-report.md
      schema-memory-card.md
      automation-candidate.md
    examples/
      password-reset.question-requirements.md
      password-reset.delete-scope.md
      xskill.semantic-architecture.md
      password-reset.optimize-path.md
      password-reset.shorten-iteration.md
      password-reset.evidence-ledger.md
      password-reset.adaptive-improvement.md
      validation-bug.schema-memory-card.md
  docs/
    portable-install.md
    design.md
    release-checklist.md
```

---

## Example

See:

- [`xskill/examples/password-reset.question-requirements.md`](xskill/examples/password-reset.question-requirements.md)
- [`xskill/examples/password-reset.delete-scope.md`](xskill/examples/password-reset.delete-scope.md)
- [`xskill/examples/xskill.semantic-architecture.md`](xskill/examples/xskill.semantic-architecture.md)
- [`xskill/examples/password-reset.optimize-path.md`](xskill/examples/password-reset.optimize-path.md)
- [`xskill/examples/password-reset.shorten-iteration.md`](xskill/examples/password-reset.shorten-iteration.md)
- [`xskill/examples/password-reset.evidence-ledger.md`](xskill/examples/password-reset.evidence-ledger.md)
- [`xskill/examples/password-reset.adaptive-improvement.md`](xskill/examples/password-reset.adaptive-improvement.md)
- [`xskill/examples/validation-bug.schema-memory-card.md`](xskill/examples/validation-bug.schema-memory-card.md)

---

## Non-goals

Xskill is intentionally not:

- a CLI-first tool
- a package manager installation flow
- a multi-agent framework
- a semantic graph database
- an autonomous coding loop
- an automatic self-modifying engine
- a replacement for your coding agent

Future automation may exist, but only after the manual skill workflow is proven stable.

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
