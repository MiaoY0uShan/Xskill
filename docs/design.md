# Xskill Design

Xskill is a portable task compiler for AI coding agents.

It is not a CLI, runtime, database, graph engine, or autonomous agent. It is a folder of `SKILL.md` files and templates that help an agent compile a vague request into a bounded, verifiable Execution Brief.

## Design goal

```text
vague task
  ↓
reasoning gates
  ↓
one short execution contract
```

The Execution Brief is the primary output.

## Workflow

```text
question-requirements
→ delete-scope
→ semantic-architecture, when needed
→ optimize-path
→ shorten-iteration, when needed
→ compiled execution brief
→ agent execution
→ evidence-ledger
→ adaptive-improvement
→ schema-memory
```

## Skill boundaries

### question-requirements

Find the real goal before planning. Uses Five Whys and inversion. Produces real goal, assumptions, risks, failure paths, success criteria, and non-goals.

### delete-scope

Use first-principles reasoning and Occam's Razor to reduce the real goal into the smallest necessary MVP. Produces MVP nucleus, entity inventory, scope boundary, minimum evidence, and module candidates.

### semantic-architecture

Used only when the MVP spans multiple modules. Produces module boundaries, relationships, coupling risks, decoupling rules, and MVP-first build order.

### optimize-path

Select the smallest stable route using small-batch quick response, agile increments, lean waste removal, and minimal safety buffers. Then compile upstream outputs into the final Execution Brief.

### shorten-iteration

If the route is too large or has failed, split it into TDD micro-loops: RED → GREEN → REFACTOR → EVIDENCE.

### evidence-ledger

After execution, record proof. No evidence means the task is not complete.

### adaptive-improvement

Promote learning only when evidence shows a reusable pattern. Do not self-improve from confidence.

### schema-memory

Store reusable work schemas: triggers, failure modes, context budget patterns, verification patterns, stop conditions. Do not store raw conversation memory.

## Core artifacts

### Compiled Execution Brief

The execution contract.

It contains:

```text
task
real goal
MVP scope
must-not-do list
module boundaries
files to read
files to touch
files to avoid
context budget
selected path
TDD micro-loops
checks
evidence required
stop condition
```

### Context Budget

Prevents context bloat and unrelated changes.

### Evidence Ledger

Makes completion auditable.

### Schema Memory

Turns repeated evidence into reusable patterns.

## Non-goals

Xskill should not become:

```text
CLI
npm package
Python package
runtime
database
automatic graph system
auto-coding loop
auto self-modifying system
```

## Core principle

Xskill deletes process until only the executable contract remains.


## Metrics layer

Xskill should not only ask agents to be smaller and more verifiable. It should record whether they were.

Primary metric:

```text
TVP = total_context_tokens / verified_tasks_completed
```

If exact token counts are unavailable, Xskill uses a proxy:

```text
Context Load Proxy = files_read + skills_loaded + reports_generated
Proxy TVP = context_load_proxy / verified_tasks_completed
```

Supporting metrics:

- Scope Creep Rate
- Verification Rate
- Rework Rate
- Context Load Size
- Iteration Half-life

Metrics are optional for tiny tasks but recommended for demos, comparisons, releases, and non-trivial runs.

Metrics must come after evidence-ledger because Xskill measures from evidence, not guesses.
