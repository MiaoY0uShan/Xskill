# Portable install

Xskill is installed by copying a ready-made folder for your agent.

For the shortest version, see:

- `START_HERE.md`
- `INSTALL.md`
- `install/README.md`

## Default usage sentence

```text
Use Xskill to compile this task before editing code:
<task>
```

## Agent folders

```text
install/codex/.agents
install/claude-code/.claude
install/gemini-cli/xskill
install/github-copilot-cli/.github
install/github-copilot-cli/xskill
```

## No separate root AGENTS.md

Earlier versions asked users to copy an `AGENTS.md` into the project root.

Current versions do not require that.

The agent contract is bundled in:

```text
xskill/AGENTS.md
```

And in the ready-made install packs.

## What happens after install

The agent should use Xskill to produce:

1. Compiled Execution Brief
2. Context Budget Contract
3. Context Diet Map
4. Evidence Ledger
5. Failure-to-Smaller-Task Protocol, when blocked or failed
6. Metrics Report, when measurement matters
