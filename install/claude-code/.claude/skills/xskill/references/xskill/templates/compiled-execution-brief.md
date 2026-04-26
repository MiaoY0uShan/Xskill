# Compiled Execution Brief

This is the primary output of Xskill.

It should be short enough for an agent to execute without rereading every upstream report.

If the user's input was vague, produce Idea Cards first. After the user chooses a card, compile the selected path into this brief.

## Markdown form

```md
# Compiled Execution Brief

## Selected Idea Card
Only include this if Idea Cards were used.

## Task

## Real Goal

## MVP Scope

## Must Not Do

## Module Boundaries

## Estimated Context Budget Contract
- Budget type: estimated
- Confidence:
- Max files to read:
- Max files to touch:
- Max skill tokens:
- Max execution notes:
- Required context:
- Required semantic / schema nodes:
- Forbidden context:
- Scope boundary:
- Budget assumptions:
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
- Files read:
- Files touched:
- Checks run:
- Verified claims:
- Unverified claims:
- Scope violations:
- Context Load Proxy:

## Handoff
After execution:
1. Create an Evidence Ledger.
2. Create a Metrics Report if measurement matters.
3. Use Adaptive Improvement only from evidence.
4. Update Schema Memory only for repeated, reusable patterns.
```

## JSON form

```json
{
  "selected_idea_card": null,
  "task": "",
  "real_goal": "",
  "mvp_scope": "",
  "must_not_do": [],
  "module_boundaries": [],
  "context_budget_contract": {
    "budget_type": "estimated",
    "confidence": "low | medium | high",
    "max_files_to_read": 0,
    "max_files_to_touch": 0,
    "max_skill_tokens": 0,
    "max_execution_notes": 0,
    "required_context": [],
    "required_schema_cards": [],
    "forbidden_context": [],
    "scope_boundary": "",
    "budget_assumptions": [],
    "violation_handling": "Stop before exceeding the budget."
  },
  "context_diet_map": {
    "relevant_context": [],
    "irrelevant_context": [],
    "files_to_read": [],
    "files_to_avoid": [],
    "reason": ""
  },
  "files_to_read": [],
  "files_to_touch": [],
  "files_to_avoid": [],
  "selected_path": "",
  "tdd_micro_loops": [],
  "checks": [],
  "evidence_required": [],
  "failure_to_smaller_task": {
    "failure_split_rule": "",
    "smaller_fallback_task": "",
    "new_verification": ""
  },
  "max_scope": "",
  "stop_condition": "",
  "metrics_to_record": [],
  "handoff": [
    "evidence-ledger",
    "metrics, if useful",
    "adaptive-improvement, if evidence-backed",
    "schema-memory, if reusable"
  ]
}
```
