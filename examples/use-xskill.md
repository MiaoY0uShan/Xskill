# Use Xskill

Use Xskill with any coding agent that can read Markdown files, skills, extensions, or custom agent profiles.

## Prompt

```text
Use Xskill to compile this task into a bounded Execution Brief before editing code:
<task>
```

## Expected result

The agent should produce:

- Compiled Execution Brief
- Context Budget Contract
- Context Diet Map
- Evidence requirements
- Stop condition

After execution, the agent should produce:

- Evidence Ledger
- Metrics Report, when measurement matters
- Adaptive Improvement Report, when reusable learning appears
- Schema Memory Card, only after repeated evidence
```

## Install packs

Use one of:

```text
install/codex/
install/claude-code/
install/gemini-cli/
install/github-copilot-cli/
```
