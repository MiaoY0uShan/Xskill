# GitHub Copilot CLI Adapter

## Recommended project install

Copy the ready-made project pack into your repository root:

```text
install/github-copilot-cli/.github
install/github-copilot-cli/xskill
```

Your repository should then contain:

```text
.github/agents/xskill.agent.md
xskill/...
```

## Alternative user-level install

Copy only the custom agent file to:

```text
~/.copilot/agents/xskill.agent.md
```

If you use the user-level agent, keep the `xskill/` bundle available in the project or paste the relevant Xskill files when needed.

## Use

In Copilot CLI, select or invoke the `xskill` custom agent, then ask:

```text
Compile this task into a bounded Execution Brief before editing code:
<task>
```
