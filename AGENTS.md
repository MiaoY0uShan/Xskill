# AGENTS.md

This repository uses Xskill.

Xskill is a portable skill bundle for context-budgeted AI coding.

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
10. Do not claim completion without an evidence ledger.
11. If blocked, split the task into a smaller follow-up task instead of retrying blindly.

Available Xskill steps:

- `question-requirements`: use Five Whys and inversion to question the request, reveal the real goal, define success criteria, and decide continue/reduce/ask/stop.
- `delete-scope`: after requirements are clarified, use first principles and Occam's Razor to define the MVP nucleus, delete/defer non-essential entities, and prepare module candidates.
- `semantic-architecture`: after scope is deleted, sketch the MVP module map, coupling risks, dependency direction, and decoupling rules for larger tasks.
- `optimize-path`: choose the smallest stable implementation path using small-batch quick response, agile working increments, lean waste removal, and a minimal safety buffer.
- `shorten-iteration`: split large or failed selected paths into TDD micro-loops with RED/GREEN/REFACTOR/EVIDENCE and evidence handoff.
- `automate-after-stable`: automate only stable repeated work.
- `semantic-memory`: keep project context lightweight through relevant context slices.
- `learn-after-run`: convert post-run evidence into reusable learning without blindly modifying skills.

Default rule:

> Less context. Smaller changes. Verified progress.

When work is complete, record:

- files touched
- checks run
- verified claims
- unverified claims
- scope violations

After any non-trivial task, create a short learning note if the run produced reusable information.
Do not modify skills immediately unless the same issue has repeated or the improvement clearly reduces context, scope, or verification risk.
