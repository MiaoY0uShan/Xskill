# AGENTS.md

This repository uses Xskill.

Xskill is a portable skill bundle for context-budgeted AI coding.

Before non-trivial coding tasks:

1. Run `question-requirements` when the request is vague, large, or risky. Use Five Whys and inversion to identify the real goal and likely failure paths.
2. For project, system, feature, refactor, workflow, or multi-module tasks, run `semantic-architecture` after requirements are clarified and before deleting scope.
3. Create or load an Xskill execution brief.
4. Respect the context budget.
5. Do not read or modify files outside the declared scope unless necessary.
6. Run the required checks.
7. Do not claim completion without an evidence ledger.
8. If blocked, split the task into a smaller follow-up task instead of retrying blindly.

Available Xskill steps:

- `question-requirements`: use Five Whys and inversion to question the request, reveal the real goal, define success criteria, and decide continue/reduce/ask/stop.
- `semantic-architecture`: after requirements are clarified, sketch the MVP slice, module map, coupling risks, and decoupling rules for larger tasks.
- `delete-scope`: remove unnecessary work and define files to avoid.
- `optimize-path`: choose the smallest correct implementation path.
- `shorten-iteration`: split large or failed work into atomic tasks.
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
