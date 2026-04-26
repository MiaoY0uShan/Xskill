# Portable Install

Xskill does not require npm, npx, pip, Python, or a command-line tool.

## Install globally

1. Download the latest `xskill-v*.zip` from GitHub Releases.
2. Unzip it.
3. Copy `xskill/` to:

```text
~/.agents/skills/xskill
```

4. Restart your coding agent.

## Install inside one project

Copy `xskill/` to:

```text
your-project/.agents/skills/xskill
```

Optionally copy `AGENTS.md` into the project root.

## First use

Ask your agent:

```text
Use Xskill to compile this task into an Execution Brief before editing code:
<task>
```

The final output should be a compiled Execution Brief, not a long prompt.


## v0.1.9 contracts layer

Xskill now treats four artifacts as core differentiators:

- Context Budget Contract;
- Evidence Ledger;
- Failure-to-Smaller-Task Protocol;
- Context Diet Map.

These keep the bundle portable while making each run bounded, auditable, failure-shrinking, and context-reducing.
