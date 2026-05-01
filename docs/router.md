# Xskill proactive router

Xskill is designed to activate automatically for coding tasks, then select the lightest useful path.

The user does not need to say `Xskill`.

Manual override is still supported:

```text
Xskill: <task or idea>
```

## Routing

```text
small clear change
-> 3-5 line brief
-> edit
-> test or validation result
```

```text
medium clear task
-> compact execution brief
-> bounded execution
-> compact evidence ledger
```

```text
vague idea
-> idea cards
-> user chooses
-> compact execution brief or full chain, depending on risk
```

```text
large or multi-module task
-> question-requirements
-> delete-scope
-> semantic-architecture, when needed
-> optimize-path
-> shorten-iteration, when needed
-> execution brief
-> evidence ledger
```

```text
protocol or agent-behavior change
-> restate inferred goal
-> challenge assumptions and scope
-> list proposed files or areas
-> ask for confirmation
-> implement only after approval
```

```text
failed or blocked task
-> evidence ledger or validation note
-> failure-to-smaller-task protocol
-> smaller brief
```

```text
completed task
-> evidence at the same weight as the route
-> metrics only when useful
-> adaptive-improvement only from evidence
-> schema-memory only for reusable patterns
```

## Repository boundary

`.agents/skills/` is local agent configuration, not project source. Do not commit it unless the repository explicitly opts in. Commit portable skills under `xskill/`.

## Rule

Use Xskill when scope, context, verification, or evidence matters. Keep the output focused on what to read, what to change, and how to verify. When the requested change affects Xskill or agent behavior itself, confirm the change before editing.
