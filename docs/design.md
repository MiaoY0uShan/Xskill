# Design

Xskill is a portable skill bundle for context-budgeted AI coding.

## Layers

```text
AGENTS.md
  Always-on router. Short. Project-level guidance.

xskill/*/SKILL.md
  On-demand skills. Loaded only when relevant.

templates/*
  Reusable output formats.

examples/*
  Concrete examples for users and agents.
```

## Product thesis

Most agent workflows add context.

Xskill removes context until the task becomes safe to execute.

## Current scope

Xskill currently provides skills and templates only.

It does not provide:

- CLI runtime
- npm or pip install
- state database
- automatic semantic graph
- autonomous loop runner
- automatic self-improvement engine
- multi-agent orchestration

## Core artifacts

- Question Requirements Report
- Delete Scope Report
- Semantic Architecture Report
- Execution Brief
- Context Budget
- Evidence Ledger
- Iteration Learning Note

These artifacts are more important than the five-step naming.

## Self-iteration boundary

Xskill supports post-run learning, not autonomous mutation.

The `learn-after-run` skill turns evidence into a learning note and may propose a rule or skill patch. It must not modify skills blindly.

A lesson should be promoted only when it:

- repeats across runs,
- reduces context,
- narrows scope,
- improves verification, or
- prevents a known class of failure.

The default action is to keep learning as a local note.


## Requirement challenge boundary

`question-requirements` uses a lightweight Five Whys and inversion pass.

It should reveal the real goal and likely failure paths before planning. It must not become a long interview or an implementation plan. The agent should answer from available context first and ask the user only when a blocking unknown remains.

Outputs from this skill should feed later skills:

- real goal -> `delete-scope`, `semantic-architecture`, and `optimize-path`
- failure paths -> context budget and stop condition
- things to avoid -> files to avoid and non-goals
- success criteria -> evidence ledger

## Scope deletion boundary

`delete-scope` runs after `question-requirements` and before `semantic-architecture`.

It uses first-principles reasoning and Occam's Razor to reduce the real goal into the smallest verifiable MVP.

It should produce:

- first-principles core,
- entity inventory,
- Occam filter,
- MVP nucleus,
- scope boundary,
- minimum evidence,
- MVP module candidates,
- decoupling notes.

It must not become:

- an implementation plan,
- a full architecture design,
- a justification for future-proofing,
- a reason to add automation,
- a runtime dependency.

The output should feed later skills:

- MVP nucleus -> `semantic-architecture` or `optimize-path`
- delete/defer lists -> non-goals and files to avoid
- module candidates -> decoupling analysis
- minimum evidence -> evidence ledger
- stop condition -> context budget

## Semantic architecture boundary

`semantic-architecture` is an optional planning skill used after `delete-scope` for project, system, feature, refactor, workflow, or multi-module MVPs.

It should produce:

- MVP slice,
- module map,
- module relationships,
- coupling risks,
- decoupling rules,
- MVP-first build order,
- deferred modules.

It must not become:

- a graph database,
- a repository-wide indexer,
- an automatic diagram tool,
- a runtime dependency,
- a required step for small tasks.

The output should feed later skills:

- MVP module map -> `optimize-path`
- coupling risks -> context budget and stop condition
- decoupling rules -> `optimize-path`
- deferred modules -> non-goals

## Small-batch path optimization

`optimize-path` is the boundary between planning and implementation. It should not write code and should not expand the MVP.

It selects one path using four filters:

1. Small-batch quick response: choose the smallest slice that can create feedback.
2. Agile working increment: produce something observable and reviewable.
3. Lean waste removal: remove steps that do not create verified learning.
4. Minimal safety buffer: keep rollback and stop conditions without building just-in-case systems.

The output is an `Optimize Path Report` that can become an execution brief.

## TDD micro-loops

`shorten-iteration` receives the selected path when it is too large or when a run failed.

It breaks work into loops:

```text
RED -> GREEN -> REFACTOR -> EVIDENCE
```

Each loop should have one behavior, one verification point, a small file budget, a refactor boundary, and an evidence handoff. If a loop fails, split that loop again instead of retrying blindly.
