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
- multi-agent orchestration

## Core artifacts

- Execution Brief
- Context Budget
- Evidence Ledger

These artifacts are more important than the five-step naming.
