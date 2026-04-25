# State Schema

## `.musk/state/project.json`

Project-level constraints and default risk policy.

```json
{
  "schema_version": "0.1",
  "name": "",
  "goal": "",
  "constraints": [],
  "non_goals": [],
  "default_checks": [],
  "risk_policy": {
    "high": [],
    "medium": [],
    "low": []
  }
}
```

## `.musk/state/tasks.json`

Task queue.

```json
{
  "tasks": [
    {
      "id": "T001",
      "goal": "",
      "priority": 3,
      "risk": "medium",
      "status": "open",
      "checks": [],
      "created_at": "",
      "updated_at": ""
    }
  ]
}
```

## `.musk/state/semantic_tree.json`

Lightweight project map.

```json
{
  "schema_version": "0.1",
  "generated_at": "",
  "root": "",
  "nodes": [],
  "edges": []
}
```

## `.musk/state/progress.jsonl`

Append-only execution log. One JSON object per line.

## `.musk/state/decisions.jsonl`

Append-only decision log. Reserved for irreversible or strategic choices.
