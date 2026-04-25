# AGENTS.md

This repository uses Xskill.

Xskill is a portable skill bundle for context-budgeted AI coding.

Before non-trivial coding tasks:

1. Create or load an Xskill execution brief.
2. Respect the context budget.
3. Do not read or modify files outside the declared scope unless necessary.
4. Run the required checks.
5. Do not claim completion without an evidence ledger.
6. If blocked, split the task into a smaller follow-up task instead of retrying blindly.

Available Xskill steps:

- `question-requirements`: question assumptions, risks, and success criteria.
- `delete-scope`: remove unnecessary work and define files to avoid.
- `optimize-path`: choose the smallest correct implementation path.
- `shorten-iteration`: split large or failed work into atomic tasks.
- `automate-after-stable`: automate only stable repeated work.
- `semantic-memory`: keep project context lightweight through relevant context slices.

Default rule:

> Less context. Smaller changes. Verified progress.

When work is complete, record:

- files touched
- checks run
- verified claims
- unverified claims
- scope violations
