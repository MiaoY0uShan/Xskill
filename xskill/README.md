# Xskill Bundle

This folder is the canonical portable Xskill bundle.

It contains everything an agent needs to follow the Xskill protocol:

```text
AGENTS.md
question-requirements/
delete-scope/
semantic-architecture/
optimize-path/
shorten-iteration/
evidence-ledger/
metrics/
adaptive-improvement/
schema-memory/
templates/
examples/
```

No separate root `AGENTS.md` is required.

For native agent installs, use the ready-made packs in the repository-level `install/` directory:

```text
install/codex/.agents/skills/xskill/
install/claude-code/.claude/skills/xskill/
install/gemini-cli/xskill/
install/github-copilot-cli/.github/agents/xskill.agent.md
```

## Protocol

```text
user task
→ question-requirements
→ delete-scope
→ semantic-architecture, when needed
→ optimize-path
→ shorten-iteration, when needed
→ compiled execution brief
→ bounded execution
→ evidence-ledger
→ metrics, when measurement matters
→ adaptive-improvement
→ schema-memory
```

## Rule

Do not use Xskill to create long planning documents.

Use it to create the shortest safe execution contract.
