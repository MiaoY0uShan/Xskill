# Compiled Execution Brief

This is the primary output of Xskill.

It should be short enough for an agent to execute without rereading every upstream report.

The brief must include a Context Budget Contract, a Context Diet Map, and an Evidence Ledger handoff.

## Markdown form

```md
# Compiled Execution Brief

## Task

## Real Goal

## MVP Scope

## Must Not Do

## Module Boundaries

## Context Budget Contract
- Max files to read:
- Max files to touch:
- Max skill tokens:
- Max execution notes:
- Required semantic / schema nodes:
- Forbidden context:
- Scope boundary:
- Violation handling:

## Context Diet Map
- Relevant context:
- Irrelevant context:
- Files to read:
- Files to avoid:
- Reason:

## Files To Read

## Files To Touch

## Files To Avoid

## Selected Path

## TDD Micro-Loops

## Checks

## Evidence Required

## Failure-to-Smaller-Task Protocol
- Failure split rule:
- Smaller fallback task:
- New verification:

## Max Scope

## Stop Condition

## Metrics To Record
- Files read
- Files planned to touch
- Files actually touched
- Unplanned files touched
- Context budget violations
- Checks required
- Checks run
- Checks passed
- Verified tasks completed
- Failed or reopened tasks
- Exact token counts, if available

## Handoff
Execute this brief. After execution, produce an Evidence Ledger. If the contract is exceeded, stop and produce a Failure-to-Smaller-Task Protocol instead of continuing.
```

## JSON form

```json
{
  "task": "",
  "real_goal": "",
  "mvp_scope": "",
  "must_not_do": [],
  "module_boundaries": [
    {
      "module": "",
      "responsibility": "",
      "must_not_own": ""
    }
  ],
  "context_budget_contract": {
    "max_files_to_read": 0,
    "max_files_to_touch": 0,
    "max_skill_tokens": 900,
    "max_execution_notes": 500,
    "required_semantic_nodes": [],
    "required_schema_cards": [],
    "forbidden_context": [],
    "scope_boundary": "",
    "violation_handling": "Stop and request a revised contract before exceeding the budget."
  },
  "context_diet_map": {
    "relevant_nodes": [],
    "irrelevant_nodes": [],
    "files_to_read": [],
    "files_to_avoid": [],
    "reason": ""
  },
  "files_to_read": [],
  "files_to_touch": [],
  "files_to_avoid": [],
  "selected_path": [],
  "tdd_micro_loops": [
    {
      "loop": 1,
      "red": "",
      "green": "",
      "refactor_boundary": "",
      "evidence": "",
      "stop_condition": ""
    }
  ],
  "checks": [],
  "evidence_required": [],
  "failure_to_smaller_task_protocol": {
    "failure_split_rule": "",
    "smaller_fallback_task": "",
    "new_verification": []
  },
  "max_scope": "",
  "stop_condition": "",
  "handoff": "Execute this brief. After execution, produce an Evidence Ledger."
}
```
