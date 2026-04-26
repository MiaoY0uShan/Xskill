# AGENTS.md

This repository uses Xskill.

Xskill is a portable task compiler for AI coding agents. Its primary output is a compiled Execution Brief, not a long prompt.

Before non-trivial coding tasks:

1. Use `question-requirements` to identify the real goal, Five Whys, failure paths, assumptions, success criteria, and non-goals.
2. Use `delete-scope` to reduce the request to the smallest necessary MVP using first-principles reasoning and Occam's Razor.
3. Use `semantic-architecture` only when the task spans multiple modules or needs MVP-based module boundaries.
4. Use `optimize-path` to select the smallest stable implementation route and compile the final Execution Brief.
5. Use `shorten-iteration` if the selected route is too large or needs multiple TDD micro-loops.
6. Execute only the compiled Execution Brief.
7. Use `evidence-ledger` after execution.
8. Use `metrics` when the run should prove context load, scope control, verification, rework, or TVP.
9. Use `adaptive-improvement` and `schema-memory` only when evidence shows a reusable pattern.

Core rule:

> Xskill compiles vague tasks into bounded, verifiable Execution Briefs.

The Execution Brief is the contract. Respect:

- real goal
- MVP scope
- must-not-do list
- files to read
- files to touch
- files to avoid
- context budget
- checks
- TDD micro-loops
- stop condition
- evidence required

Do not:

- expand the MVP
- read broad context by default
- touch unrelated files
- refactor outside the declared boundary
- claim completion without evidence
- turn one run into a permanent rule
- automate before the process is stable

If blocked:

1. Stop.
2. Record the blocker.
3. Split the task smaller.
4. Produce a narrower Execution Brief.

If there is no evidence, the task is not done.

If there is no verified progress, TVP is undefined.

Xskill measures from evidence, not guesses.
Xskill learns from evidence, not confidence.
