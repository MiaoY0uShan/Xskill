# Architecture

## Core idea

Musk Agent Skills separates three concerns:

1. **Policy** — `.musk/kernel/SKILL.md` is the small always-on kernel.
2. **Skills** — `.musk/skills/*/SKILL.md` are loaded only when their trigger matches the current step.
3. **State** — `.musk/state/*` persists tasks, project constraints, semantic memory, progress, and decisions.

The CLI does not attempt to be a full AI agent. It prepares the state and prompt briefs that a coding agent can execute.

## Runtime flow

```text
request
  → question-requirements
  → delete-scope
  → optimize-path
  → shorten-iteration
  → execute with verification
  → automate-after-stable only after repetition
  → record learning
```

## Why state files instead of long prompts

Long prompts are expensive and fragile. State files let each agent session begin with a small brief and retrieve only the relevant project memory.

## Semantic tree

`musk index` builds `.musk/state/semantic_tree.json` by scanning text/code files and extracting lightweight nodes:

```json
{
  "id": "src:auth:login.py",
  "type": "code",
  "path": "src/auth/login.py",
  "summary": "Handles login validation",
  "tags": ["auth", "api"],
  "risk": "high"
}
```

This MVP uses deterministic indexing. Later versions can add AST-level extraction, graph clustering, and confidence-tagged inferred edges.

## Risk policy

The default policy lives in `.musk/state/project.json`:

- high risk: question, delete, optimize, shorten
- medium risk: delete, optimize, shorten
- low risk: delete, optimize

Automation is intentionally excluded from the default path. It requires evidence of stable repetition.
