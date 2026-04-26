# AGENTS.md

This repository uses Xskill.

Xskill is a portable skill bundle for context-budgeted AI coding.

Before non-trivial coding tasks:

1. Run `question-requirements` when the request is vague, large, or risky. Use Five Whys and inversion to identify the real goal and likely failure paths.
2. Run `delete-scope` after requirements are clarified. Use first-principles reasoning and Occam's Razor to cut the request down to the smallest verifiable MVP.
3. For project, system, feature, refactor, workflow, or multi-module tasks, run `semantic-architecture` after `delete-scope` to define module boundaries and decoupling rules from the MVP.
4. Create or load an Xskill execution brief.
5. Respect the context budget.
6. Do not read or modify files outside the declared scope unless necessary.
7. Run the required checks.
8. Do not claim completion without an evidence ledger.
9. If blocked, split the task into a smaller follow-up task instead of retrying blindly.

Available Xskill steps:

- `question-requirements`: use Five Whys and inversion to question the request, reveal the real goal, define success criteria, and decide continue/reduce/ask/stop.
- `delete-scope`: after requirements are clarified, use first principles and Occam's Razor to define the MVP nucleus, delete/defer non-essential entities, and prepare module candidates.
- `semantic-architecture`: after scope is deleted, sketch the MVP module map, coupling risks, dependency direction, and decoupling rules for larger tasks.
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
