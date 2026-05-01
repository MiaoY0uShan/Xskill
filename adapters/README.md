# Xskill adapters

Xskill is agent-agnostic. Adapters describe how each agent should discover and apply the same routing rules.

Default behavior:

```text
Use Xskill proactively for coding work, then choose the lightest evidence-backed path.
```

Manual override:

```text
Xskill: <task or idea>
```

Expected behavior:

- small change -> 3-5 line brief plus validation result
- medium task -> compact Execution Brief plus Evidence Ledger
- large, vague, architectural, or risky task -> full chain
- failed task -> Failure-to-Smaller-Task Protocol and a smaller brief
- protocol or agent-behavior change -> confirm intent and boundaries before editing

Agent-local skill directories such as `.agents/skills/` are local configuration unless a repository explicitly opts in.
