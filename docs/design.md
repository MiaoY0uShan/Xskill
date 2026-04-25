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

## Non-goals

- Xskill is not a CLI-first tool.
- Xskill is not a multi-agent framework.
- Xskill is not a memory database.
- Xskill is not a prompt dump.

## Core artifacts

- Execution Brief
- Context Budget
- Evidence Ledger

These artifacts are more important than the five-step naming.
