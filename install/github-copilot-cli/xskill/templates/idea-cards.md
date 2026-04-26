# Idea Cards

Use this template when the user says `Xskill` with a vague idea, broad goal, or unclear requirement.

The goal is to help the user choose a direction without forcing them to write a full specification.

Do not produce more than 3 cards unless the user asks.

## User Input

```text
Xskill:
...
```

## Why cards are needed

```text
The request is broad / ambiguous / exploratory because:
...
```

## Card A — <short path name>

### Interpretation
What this path assumes the user probably means.

### MVP
The smallest useful version of this path.

### Best for
What this path optimizes for.

### Tradeoff / Risk
What this path does not solve, or what it could make worse.

### Estimated Context Budget Contract
```json
{
  "budget_type": "estimated",
  "confidence": "high | medium | low",
  "max_files_to_read": 0,
  "max_files_to_touch": 0,
  "max_skill_tokens": 0,
  "max_execution_notes": 0,
  "required_context": [],
  "forbidden_context": [],
  "scope_boundary": "",
  "budget_assumptions": [],
  "budget_violation_rule": "Stop and ask before exceeding the budget."
}
```

### Recommended Workflow
```text
question-requirements → delete-scope → optimize-path → compiled execution brief
```

---

## Card B — <short path name>

Same fields as Card A.

---

## Card C — <short path name>

Same fields as Card A.

---

## Choose

Reply with:

```text
A
B
C
merge A+B
none, generate 3 new cards
```

After the user chooses, continue the normal Xskill workflow.
