# Xskill

**Context diet for AI coding agents.**

Install it. Then use your agent normally.

For non-trivial coding tasks, Xskill should activate automatically before code is edited.

```text
Fix the password reset bug.
```

Expected first response:

```text
I’ll use Xskill to create a bounded Execution Brief before editing code.
```

Manual override, if your agent does not activate it:

```text
Xskill: Fix the password reset bug.
```

No Xskill CLI. No npm. No npx. No pip. No database. No runtime.

---

## 30-second start

### 1. Pick your agent

| Agent | Download | Install |
|---|---|---|
| Codex | `xskill-codex-v0.2.3.zip` | Unzip into your project root |
| Claude Code | `xskill-claude-code-v0.2.3.zip` | Unzip into your project root |
| Gemini CLI | `xskill-gemini-cli-v0.2.3.zip` | Unzip, then install the bundled `xskill/` extension |
| GitHub Copilot CLI | `xskill-github-copilot-cli-v0.2.3.zip` | Unzip into your project root |
| Any agent | `xskill-copy-paste-v0.2.3.md` | Paste into your agent |

### 2. Restart your agent

Reload the project so the agent can discover Xskill.

### 3. Use your agent normally

Ask for a non-trivial coding task:

```text
Fix the password reset bug.
```

Xskill should activate automatically and create a **Compiled Execution Brief** before editing code.

For a vague idea, say it naturally:

```text
I want this project to be easier for people to use.
```

Xskill should generate **3 Idea Cards** first.

### 4. Manual override

If the agent does not activate Xskill, force it:

```text
Xskill: <your task or idea>
```

---

## What Xskill gives you

A normal prompt says:

```text
Please be careful.
```

Xskill gives the agent a task contract:

```json
{
  "task": "Add password reset flow",
  "real_goal": "Allow users to reset passwords safely without refactoring auth provider internals",
  "mvp_scope": "Reset token generation and validation only",
  "context_budget_contract": {
    "budget_type": "estimated",
    "confidence": "medium",
    "max_files_to_read": 5,
    "max_files_to_touch": 3,
    "max_skill_tokens": 900,
    "max_execution_notes": 500,
    "forbidden_context": ["src/oauth/**", "src/billing/**"],
    "scope_boundary": "Do not modify auth provider internals"
  },
  "files_to_read": ["src/auth/reset.ts", "tests/auth/test_reset.py"],
  "files_to_touch": ["src/auth/reset.ts", "tests/auth/test_reset.py"],
  "files_to_avoid": ["src/oauth/**", "src/billing/**"],
  "checks": ["pytest tests/auth/test_reset.py"],
  "evidence_required": ["failing test before fix", "passing test after fix", "no unrelated files touched"],
  "stop_condition": "Stop if implementation requires auth provider refactor"
}
```

**Less context. Smaller changes. Verified progress.**

---

## The Xskill protocol

The default experience is normal agent use. The manual override is:

```text
Xskill: <task or idea>
```

Internal protocol:

```text
task or idea
→ proactive router
→ idea cards, if needed
→ brief
→ bounded execution
→ evidence
→ metrics
→ improvement
```

Full internal flow:

```text
user task
→ Xskill proactive router
→ idea cards, if vague
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

You do not need to trigger each step manually.

---

## Install from this repository

If you cloned the repository directly:

| Agent | Copy this | Destination |
|---|---|---|
| Codex | `install/codex/.agents` | project root |
| Claude Code | `install/claude-code/.claude` | project root |
| Gemini CLI | `install/gemini-cli/xskill` | `~/.gemini/extensions/xskill` or install as local extension |
| GitHub Copilot CLI | `install/github-copilot-cli/.github` and `install/github-copilot-cli/xskill` | project root |

---

## Roadmap

### Now

- Proactive Xskill activation
- Idea Cards for vague intent
- Agent-specific install zips
- Real case studies
- Adapter verification

### Not planned

- Xskill CLI
- npm package
- npx installer
- pip package
- database
- runtime
- automatic executor
- automatic self-modifying engine

## License

MIT
