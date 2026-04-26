# Xskill Execution Protocol

Xskill is agent-agnostic.

It is not a Claude Code skill pack, a Codex-only workflow, or a GitHub Copilot-only agent.

It is one execution discipline layer for any coding agent that can read files, instructions, skills, extensions, custom agents, or copied Markdown.

## Protocol

```text
task
→ compiled execution brief
→ context budget contract
→ context diet map
→ bounded execution
→ evidence ledger
→ metrics report, when measurement matters
→ adaptive improvement
→ schema memory
```

## Contract

Every meaningful task should produce a Compiled Execution Brief before execution.

That brief must include:

- real goal
- MVP scope
- must-not-do list
- Context Budget Contract
- Context Diet Map
- files to read
- files to touch
- files to avoid
- checks
- evidence required
- stop condition

## Handoff

After execution, the agent must produce an Evidence Ledger.

When measurement matters, it also produces a Metrics Report.

When learning matters, it produces Adaptive Improvement and Schema Memory updates only from evidence.

## Rule

Xskill does not make an agent more autonomous.

It makes the agent more bounded, auditable, and measurable.
