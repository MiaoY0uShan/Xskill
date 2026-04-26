# Case Study 2: Add Codex adapter guidance

## Task
Add Codex-specific usage guidance without making Xskill Codex-specific.

## Xskill files loaded
- `xskill/AGENTS.md`
- `question-requirements/SKILL.md`
- `delete-scope/SKILL.md`
- `semantic-architecture/SKILL.md`
- `optimize-path/SKILL.md`
- `adapters/codex.md`
- `context-budget-contract.md`
- `evidence-ledger.md`

## Metrics
- Baseline context: 19,562 estimated tokens
- Xskill context: 8,112 estimated tokens
- Reduction: 58.5%

## Scope boundary
Only document Codex adapter behavior. Do not change the unified Xskill protocol.

## Evidence required
- Codex path is documented.
- Generic protocol remains unchanged.
- Xskill remains agent-agnostic.
