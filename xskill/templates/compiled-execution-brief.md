# Compiled Execution Brief

This is the primary output of Xskill.

It should be short enough for an agent to execute without rereading every upstream report.

## Markdown form

```md
# Compiled Execution Brief

## Task

## Real Goal

## MVP Scope

## Must Not Do

## Module Boundaries

## Files To Read

## Files To Touch

## Files To Avoid

## Context Budget
- Max files to read:
- Max files to touch:
- Max notes:
- Forbidden context:

## Selected Path

## TDD Micro-Loops

## Checks

## Evidence Required

## Max Scope

## Stop Condition

## Handoff
Execute this brief. After execution, produce an Evidence Ledger.
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
  "files_to_read": [],
  "files_to_touch": [],
  "files_to_avoid": [],
  "context_budget": {
    "max_files_to_read": 0,
    "max_files_to_touch": 0,
    "max_notes": "",
    "forbidden_context": []
  },
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
  "max_scope": "",
  "stop_condition": "",
  "handoff": "Execute this brief. After execution, produce an Evidence Ledger."
}
```
