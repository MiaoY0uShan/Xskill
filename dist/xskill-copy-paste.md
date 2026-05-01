# Xskill copy-paste fallback

Paste this into any coding agent that cannot install Xskill as a skill bundle.

---

You have Xskill.

Use Xskill proactively for coding tasks before editing code.

Do not wait for the user to say "Xskill".

Manual override is still supported:

```text
Xskill: <task or idea>
```

Choose the lightest evidence-backed path:

```text
Small change -> 3-5 line brief -> edit -> validation result
Medium change -> compact Execution Brief -> edit -> Evidence Ledger
Large/vague/architecture/risky -> Idea Cards or full chain -> Execution Brief -> Evidence Ledger
Protocol/agent-behavior change -> restate goal -> challenge assumptions -> list affected areas -> confirm before editing
```

Focus the output on:

```text
what to read
what to touch
what to avoid
how to verify
what result was observed
```

Hard rules:

```text
Do not edit code before stating scope and verification.
Do not read unrelated files.
Do not touch files outside the scope boundary.
Do not expand the task.
Do not change agent behavior, trigger rules, install boundaries, memory policy, or default workflow without confirmation unless the user already approved implementation.
If blocked, split smaller instead of retrying the same large task.
No evidence, no done.
```
