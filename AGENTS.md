# AGENTS.md

This repository uses Xskill.

Xskill is a portable skill bundle for context-budgeted AI coding.

Default rule:

> Less context. Smaller changes. Verified progress.

Before non-trivial coding tasks:

1. Run `question-requirements` when the request is vague, large, or risky. Use Five Whys and inversion to identify the real goal and likely failure paths.
2. Run `delete-scope` after requirements are clarified. Use first-principles reasoning and Occam's Razor to cut the request down to the smallest verifiable MVP.
3. For project, system, feature, refactor, workflow, or multi-module tasks, run `semantic-architecture` after `delete-scope` to define module boundaries and decoupling rules from the MVP.
4. Run `optimize-path` to select the smallest stable route using small-batch, agile, lean waste-removal, and minimal safety-buffer filters.
5. If the selected path is too large or has failed, run `shorten-iteration` to split it into TDD micro-loops.
6. Create or load an Xskill execution brief.
7. Respect the context budget.
8. Do not read or modify files outside the declared scope unless necessary.
9. Run the required checks.
10. Record an `evidence-ledger` before claiming completion.
11. If blocked, split the task into a smaller follow-up task instead of retrying blindly.
12. After a non-trivial run, use `adaptive-improvement` only if there is evidence.
13. Use `schema-memory` to store reusable patterns, not raw context.

Available Xskill steps:

- `question-requirements`: use Five Whys and inversion to question the request, reveal the real goal, define success criteria, and decide continue/reduce/ask/stop.
- `delete-scope`: after requirements are clarified, use first principles and Occam's Razor to define the MVP nucleus, delete/defer non-essential entities, and prepare module candidates.
- `semantic-architecture`: after scope is deleted, sketch the MVP module map, coupling risks, dependency direction, and decoupling rules for larger tasks.
- `optimize-path`: choose the smallest stable implementation path using small-batch quick response, agile working increments, lean waste removal, and a minimal safety buffer.
- `shorten-iteration`: split large or failed selected paths into TDD micro-loops with RED/GREEN/REFACTOR/EVIDENCE and evidence handoff.
- `evidence-ledger`: record files touched, checks run, verified claims, unverified claims, remaining risk, and scope violations.
- `adaptive-improvement`: turn evidence into feedback, schema updates, checklist improvements, or automation candidates. Do not auto-modify skills.
- `schema-memory`: store reusable task patterns, failure modes, context budget patterns, verification patterns, and stop conditions.

Adaptive improvement rules:

- Xskill learns from evidence, not confidence.
- Do not promote a lesson after one run unless it clearly reduces context, narrows scope, improves verification, or prevents a repeated failure.
- Do not automate confusion.
- Automation is only a candidate after repeated, stable manual behavior.
- Prefer schema memory over raw memory.
- Prefer small checklist changes over new skills.

When work is complete, record:

- files touched
- checks run
- verified claims
- unverified claims
- scope violations
- remaining risk
