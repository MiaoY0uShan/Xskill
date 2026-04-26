# Context Budget Contract

This is a hard execution boundary for one task.

A Context Budget Contract is stronger than a casual context budget. It tells the agent what it may read, what it may touch, what it must avoid, and when it must stop.

## Task

## Scope Boundary

## Context Limits
- Max files to read:
- Max files to touch:
- Max skill tokens:
- Max execution notes:

## Required Context
- Required semantic / schema nodes:
- Required files:
- Required prior reports:

## Forbidden Context
- Forbidden files / directories:
- Forbidden modules:
- Forbidden assumptions:
- Forbidden future work:

## Modification Limits
- Files allowed to touch:
- Files explicitly forbidden to touch:
- Max scope:

## Verification Boundary
- Required checks:
- Evidence required:

## Violation Handling
If the agent needs to exceed this contract:

1. Stop.
2. State which limit would be exceeded.
3. Explain why the current contract is insufficient.
4. Ask for a smaller follow-up task or a revised contract.
5. Do not continue silently.

## JSON form

```json
{
  "task": "",
  "max_files_to_read": 5,
  "max_files_to_touch": 3,
  "max_skill_tokens": 900,
  "max_execution_notes": 500,
  "required_semantic_nodes": [],
  "required_schema_cards": [],
  "required_files": [],
  "forbidden_context": [],
  "files_allowed_to_touch": [],
  "files_forbidden_to_touch": [],
  "scope_boundary": "",
  "checks": [],
  "evidence_required": [],
  "violation_handling": "Stop and request a revised contract before exceeding the budget."
}
```
