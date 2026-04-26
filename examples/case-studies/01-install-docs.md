# Case Study 1: Rewrite install docs

## Task
Rewrite installation guidance so users do not need to copy a root `AGENTS.md` manually.

## Xskill files loaded
- `xskill/AGENTS.md`
- `question-requirements/SKILL.md`
- `delete-scope/SKILL.md`
- `optimize-path/SKILL.md`
- `compiled-execution-brief.md`
- `context-budget-contract.md`
- `evidence-ledger.md`

## Metrics
- Baseline context: 19,562 estimated tokens
- Xskill context: 7,120 estimated tokens
- Reduction: 63.6%

## Scope boundary
Do not add CLI, npm, npx, pip, or runtime installation.

## Evidence required
- README explains release zip usage.
- Adapter install packs remain the main user path.
- No additional configuration step is required beyond copying the relevant install pack.
