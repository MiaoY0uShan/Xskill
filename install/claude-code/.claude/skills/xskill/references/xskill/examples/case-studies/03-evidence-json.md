# Case Study 3: Add JSON Evidence Ledger audit example

## Task
Add a JSON audit example showing that every agent claim needs evidence.

## Xskill files loaded
- `xskill/AGENTS.md`
- `question-requirements/SKILL.md`
- `delete-scope/SKILL.md`
- `optimize-path/SKILL.md`
- `evidence-ledger/SKILL.md`
- `evidence-ledger.md`
- `context-budget-contract.json`

## Metrics
- Baseline context: 19,562 estimated tokens
- Xskill context: 6,808 estimated tokens
- Reduction: 65.2%

## Scope boundary
Add evidence representation only. Do not add a database, tracker, or runtime.

## Evidence required
- Verified claims and unverified claims are separate.
- Commands run are recorded.
- Scope violations are explicit.
