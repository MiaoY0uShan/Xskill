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
