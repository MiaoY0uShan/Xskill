# Xskill adapters

Adapters explain how different coding agents should discover and use Xskill.

Default behavior:

```text
Use Xskill proactively for non-trivial coding work. Do not wait for the user to say "Xskill".
```

Manual override:

```text
Xskill: <task or idea>
```

The protocol is the same everywhere:

```text
idea or task
-> router
-> idea cards, if vague
-> compiled execution brief
-> bounded execution
-> evidence
-> metrics
-> improvement
```

Install packs are under `install/`.

No adapter adds a runtime.
