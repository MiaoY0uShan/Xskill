# Xskill

**Context diet for AI coding agents.**

Install it once. Then use your coding agent normally.

For non-trivial coding work, Xskill should activate before code is edited and produce a bounded, evidence-backed **Execution Brief**.

Manual override:

```text
Xskill: Fix the password reset bug.
```

No CLI. No npm. No npx. No pip. No database. No runtime.

---

## 1. Hero

AI coding agents do not need more context.

They need a smaller task, a harder boundary, and proof that the work is done.

**Less context. Smaller changes. Verified progress.**

---

## 2. Enemy

Agents usually fail in predictable ways:

| Failure | What goes wrong |
|---|---|
| Vague request | Agent guesses the real goal |
| Too much context | Agent reads unrelated files |
| Scope creep | Agent touches files outside the task |
| False completion | Agent says “done” without proof |
| Failed run | Agent retries the same large task |
| Memory bloat | Agent remembers raw context instead of useful patterns |

Xskill makes these failures harder by forcing a bounded execution contract before non-trivial work starts.

---

## 3. Demo

User asks normally:

```text
Fix the password reset bug.
```

Expected first response:

```text
I’ll use Xskill to create a bounded Execution Brief before editing code.
```

Expected output:

```json
{
  "task": "Fix the password reset bug",
  "real_goal": "Fix reset token validation without refactoring auth provider internals",
  "mvp_scope": "Validate expired and reused reset tokens only",
  "must_not_do": ["Do not rewrite auth", "Do not touch OAuth", "Do not build admin reset"],
  "context_budget_contract": {
    "budget_type": "estimated",
    "confidence": "medium",
    "max_files_to_read": 4,
    "max_files_to_touch": 2,
    "max_skill_tokens": 900,
    "forbidden_context": ["src/oauth/**", "src/billing/**"],
    "scope_boundary": "Only touch reset-token validation and focused tests"
  },
  "files_to_read": ["src/auth/reset.ts", "tests/auth/test_reset.py"],
  "files_to_avoid": ["src/oauth/**", "src/billing/**"],
  "checks": ["pytest tests/auth/test_reset.py"],
  "evidence_required": ["failing test", "passing test", "no unrelated files touched"],
  "stop_condition": "Stop if this requires auth provider refactor"
}
```

---

## 4. Magic

Xskill hides the workflow behind one behavior:

> Create a bounded Execution Brief before non-trivial code edits.

Internally, it routes the task:

| Situation | Xskill response |
|---|---|
| Vague idea | Generate 3 Idea Cards |
| Unclear goal | Run Five Whys and inversion |
| Scope too large | Delete down to MVP |
| Multi-module work | Sketch module boundaries |
| Clear implementation | Choose the smallest verifiable path |
| Large implementation | Split into TDD micro-loops |
| Failed task | Split into a smaller task |
| Completed task | Require evidence, metrics, and learning when useful |

Users do not need to choose skills manually.

---

## 5. Proof

Primary metric:

```text
TVP = total_context_tokens / verified_tasks_completed
```

Portable proxy:

```text
Context Load Proxy = files_read + skills_loaded + reports_generated
Proxy TVP = context_load_proxy / verified_tasks_completed
```

Supporting metrics:

```text
Scope Creep Rate     = touched_unplanned_files / touched_files
Verification Rate    = tasks_with_checks / completed_tasks
Rework Rate          = failed_or_reopened_tasks / completed_tasks
Context Load Size    = files_loaded_per_task
Iteration Half-life  = time_to_first_verified_slice
```

Preliminary self-use cases from building Xskill showed **61.2% average context reduction** against a monolithic full-bundle baseline.

These are self-use cases, not a formal external benchmark.

See `docs/metrics.md` and `docs/case-studies.md`.

---

## 6. Workflow

Simple protocol:

```text
task → brief → bounded execution → evidence → metrics → improvement
```

Full internal flow:

```text
user task or vague idea
→ Xskill router
→ Idea Cards, if needed
→ question-requirements
→ delete-scope
→ semantic-architecture, when needed
→ optimize-path
→ shorten-iteration, when needed
→ compiled execution brief
→ bounded execution
→ evidence-ledger
→ metrics, when useful
→ adaptive-improvement
→ schema-memory
```

The five operating principles:

```text
Question.
Delete.
Optimize.
Shorten iteration.
Improve from evidence.
```

---

## 7. Install

Download the latest release kit.

Pick the package for your agent:

| Agent | Asset | Action |
|---|---|---|
| Codex | `xskill-codex-{version}.zip` | Unzip into project root |
| Claude Code | `xskill-claude-code-{version}.zip` | Unzip into project root |
| Gemini CLI | `xskill-gemini-cli-{version}.zip` | Install bundled `xskill/` extension |
| GitHub Copilot CLI | `xskill-github-copilot-cli-{version}.zip` | Unzip into project root |
| Any agent | `xskill-copy-paste-{version}.md` | Paste into the agent |

Restart your agent. Then use it normally.

Manual override:

```text
Xskill: <task or idea>
```

See `START_HERE.md`, `INSTALL.md`, and `install/README.md`.

---

## 8. Examples

Before Xskill:

```text
User: Fix the password reset bug.
Agent: Reads auth provider, OAuth login, billing hooks, and unrelated tests.
Agent: Edits multiple files.
Agent: Says done.
No focused evidence.
```

After Xskill:

```text
User: Fix the password reset bug.
Agent: Creates an Execution Brief.
Agent: Limits files to reset-token validation and focused tests.
Agent: Runs focused checks.
Agent: Records Evidence Ledger.
```

For vague ideas, Xskill produces 3 Idea Cards:

```text
Card A — Dumb-simple install
Card B — Demo-first README
Card C — Copy-paste fallback
```

See `examples/case-studies/` and `xskill/examples/`.

---

## 9. Philosophy

Less is the feature.

Most agent workflows add more prompts, more memory, more roles, and more automation.

Xskill removes until the work is small enough to verify.

Core rules:

```text
Do not edit before the brief.
Do not read everything.
Do not touch unrelated files.
Do not expand the task.
Do not claim done without evidence.
Do not retry large failures.
Do not learn from confidence; learn from evidence.
```

Xskill is not a full agent runtime.

It is a small execution discipline layer.

---

## 10. Credits / disclaimer

Xskill is inspired by ideas from Musk-style five-step engineering, Toyota Five Whys, first-principles reasoning, Occam’s Razor, small-batch quick response, agile and lean development, TDD micro-loops, evidence-led execution, schema-based learning, and agent skill systems such as Superpowers.

Xskill is not affiliated with Elon Musk, Tesla, SpaceX, X, xAI, Toyota, SHEIN, Superpowers, OpenAI, Anthropic, Google, GitHub, or any referenced project.

All Xskill text and templates are original unless otherwise noted.

License: MIT
