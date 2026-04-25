# Skill: question-requirements

Musk step: Question every requirement.

## Trigger

Use when a task is new, ambiguous, strategically important, high-risk, or likely to trigger unnecessary implementation.

## Goal

Convert a request into a validated goal with explicit assumptions, risks, success criteria, and stop/reduce/continue decision.

## Inputs

- User request or task goal
- Project constraints from `.musk/state/project.json`
- Relevant semantic nodes from `.musk/state/semantic_tree.json`
- Existing decisions and progress, if available

## Procedure

1. Restate the goal in one sentence.
2. List assumptions. Mark each as `safe`, `risky`, or `unknown`.
3. Identify contradictions, missing information, and hidden scope.
4. Define measurable success criteria.
5. Identify the cheapest validation path.
6. Push back on requirements that are not necessary for the success criteria.
7. Choose one decision: `continue`, `reduce_scope`, or `stop`.

## Output Contract

Return JSON only:

```json
{
  "goal": "",
  "assumptions": [
    {"text": "", "status": "safe|risky|unknown", "action": ""}
  ],
  "unknowns": [],
  "risks": [],
  "success_criteria": [],
  "cheap_validation": "",
  "should_not_do": [],
  "decision": "continue|reduce_scope|stop",
  "next_step": "delete-scope|blocker"
}
```

## Failure Mode

If the requirement cannot be validated, do not implement. Emit:

```json
{
  "decision": "stop",
  "blocker": "",
  "smallest_next_action": ""
}
```
