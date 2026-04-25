# Xskill

**Musk 5-Step Xskill** is a lightweight skill pack and local runtime for AI-assisted software development.

It turns heavyweight agent workflows into five compact, executable skills based on the five-step engineering method:

1. **Question requirements**
2. **Delete unnecessary scope**
3. **Optimize the path**
4. **Shorten iteration cycles**
5. **Automate only after the process is stable**

The goal is simple:

> Use less context, less ceremony, and fewer tokens — while keeping stronger execution discipline.

---

## Why this exists

Modern AI coding workflows are powerful, but many of them become too heavy:

- too many prompts
- too many agents
- too many roles
- too much always-on context
- too much process before the task is even understood

This project takes a different approach.

Instead of building another large agent framework, **Musk 5-Step Xskill** extracts useful mechanisms from proven AI workflow projects and recompiles them into a small set of skills that can be loaded only when needed.

The result is a lean workflow for planning, building, verifying, and iterating with AI coding agents.

---

## Core idea

This project is not a replacement for coding agents.

It is a **thinking and execution layer** on top of them.

```text
User goal
  ↓
Question requirements
  ↓
Delete unnecessary scope
  ↓
Optimize the implementation path
  ↓
Shorten the iteration loop
  ↓
Automate stable repeated work
  ↓
Record learning into state
```

Each step is implemented as a compact skill.

Each skill has:

- a trigger
- a goal
- an execution procedure
- an output contract
- a failure mode

This makes the workflow easier to reuse across tools like Claude Code, Codex, Cursor, OpenCode, or any agent runtime that can read Markdown instructions.

------

## What is Xskill?

**Xskill** means **executable skill**.

A normal prompt tells an agent what to do.

An Xskill defines:

- when to activate
- what input it needs
- what output it must produce
- how to verify the result
- when to stop

The emphasis is on small, composable, auditable behavior.

------

## The five skills

### 1. `question-requirements`

Question assumptions before execution.

Use this when the task is vague, large, risky, or product-facing.

It produces:

- goal
- assumptions
- unknowns
- risks
- success criteria
- things not to do
- decision: continue, reduce scope, or stop

------

### 2. `delete-scope`

Remove unnecessary work before planning implementation.

Use this before creating tasks or touching code.

It produces:

- must-have scope
- nice-to-have scope
- deleted scope
- deferred scope
- files to touch
- files to avoid
- minimum viable slice

------

### 3. `optimize-path`

Choose the simplest correct implementation path.

Use this before editing code.

It produces:

- implementation path
- test strategy
- verification commands
- review lenses
- refactor permission

The default rule is:

> Do the smallest correct thing that can be verified.

------

### 4. `shorten-iteration`

Break work into small, verifiable iterations.

Use this when a task is too large for one clean context window.

It produces:

- atomic tasks
- context slices
- parallel groups
- stop conditions
- rollback plan

The default unit is:

```
one task
one context slice
one verification
one state update
```

------

### 5. `automate-after-stable`

Automate only after the manual process has repeated successfully.

Use this after a workflow has been executed several times by hand.

It produces:

- automation candidates
- guardrails
- commands to create
- failure recovery rules
- state update rules

The principle is:

> Do not automate confusion.

------

## Semantic memory

The project also includes a supporting skill:

```
semantic-memory
```

This is used to keep long-term project context lightweight.

Instead of injecting an entire repository into the model context, the project maintains a small semantic tree:

```
{
  "nodes": [
    {
      "id": "auth.login",
      "type": "code.module",
      "path": "src/auth/login.ts",
      "summary": "Handles login validation and session creation",
      "tags": ["auth", "session", "security"],
      "risk": "high"
    }
  ],
  "edges": [
    {
      "from": "auth.login",
      "to": "db.users",
      "relation": "depends_on",
      "evidence": "EXTRACTED",
      "confidence": 0.92
    }
  ]
}
```

The agent should retrieve only the relevant semantic slice for the current task.

------

## Project structure

```
.musk/
  kernel.md
  skills/
    question-requirements/SKILL.md
    delete-scope/SKILL.md
    optimize-path/SKILL.md
    shorten-iteration/SKILL.md
    automate-after-stable/SKILL.md
    semantic-memory/SKILL.md
  state/
    project.json
    tasks.json
    progress.jsonl
    decisions.jsonl
    semantic_tree.json
```

------

## Installation

Clone the repository:

```
git clone https://github.com/YOUR_NAME/5step-xskill.git
cd 5step-xskill
```

Install locally:

```
pip install -e .
```

------

## Quick start

Initialize Xskill state in your project:

```
musk init
```

Add a task:

```
musk task add "Add password reset flow" \
  --priority 5 \
  --risk high \
  --check "pytest"
```

Get the next task:

```
musk next
```

Generate a step brief:

```
musk brief question-requirements --task "Add password reset flow"
```

Index project context:

```
musk index
```

Mark a task as done:

```
musk task done T001 --note "pytest passed"
```

------

## Example workflow

```
1. Run question-requirements
   Clarify the goal, assumptions, risks, and success criteria.

2. Run delete-scope
   Remove anything not required for the minimum viable slice.

3. Run optimize-path
   Decide the smallest implementation path and verification strategy.

4. Run shorten-iteration
   Split the work into atomic tasks with clean context boundaries.

5. Run automate-after-stable
   Only automate steps that have become stable through repetition.
```

------

## Design principles

### 1. Keep the kernel small

The always-on instruction layer should be short.

Long methodology documents should not live permanently in context.

------

### 2. Load skills only when needed

Each skill should be activated by task type, risk level, or workflow stage.

No skill should be active by default unless the task requires it.

------

### 3. Prefer state over memory

The agent should not rely on conversation memory.

Important information should be written to:

- `tasks.json`
- `progress.jsonl`
- `decisions.jsonl`
- `semantic_tree.json`

------

### 4. Optimize for verifiable progress

A task is not complete because the agent says it is complete.

It is complete only when there is evidence:

- tests passed
- typecheck passed
- lint passed
- review completed
- acceptance criteria satisfied

------

### 5. Failure should create smaller work

When an iteration fails, do not blindly retry the same task.

Instead:

```
failure
  ↓
record cause
  ↓
create smaller follow-up task
  ↓
retry with narrower context
```

------

## Influences

This project is inspired by mechanisms from several AI coding and agent workflow projects:

- Karpathy-inspired coding skills
- Superpowers
- Get Shit Done
- Ralph
- gstack
- Graphify
- oh-my-openagent

This project does not copy those projects.

It extracts general workflow mechanisms and recompiles them into a smaller five-step skill system.

------

## Roadmap

### MVP

-  Five core skills
-  Semantic memory skill
-  Local state structure
-  CLI initialization
-  Task queue
-  Step brief generation
-  Lightweight semantic index

### Next

-  Better semantic tree generation
-  Git-aware progress tracking
-  Agent-specific adapters
-  Skill self-improvement loop
-  Verification command auto-selection
-  Parallel task grouping
-  HTML report output

### Later

-  Claude Code adapter
-  Cursor adapter
-  Codex adapter
-  OpenCode adapter
-  Multi-agent execution mode
-  Graph visualization

------

## Philosophy

Most agent systems try to become smarter by adding more process.

This project tries to become smarter by deleting process.

The default behavior is:

```
question first
delete aggressively
implement minimally
verify honestly
iterate quickly
automate last
```

------

## Disclaimer

This project is inspired by the five-step engineering method popularized by Elon Musk.

It is not affiliated with Elon Musk, Tesla, SpaceX, X, xAI, or any of the referenced open-source projects.

All skill text and implementation in this repository are original unless otherwise stated.

------

## License

MIT
