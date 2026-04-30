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

Xskill is now a proactive, automated discipline layer.

### Ghost Mode
It detects non-trivial work and activates automatically. No more manual prompting.

### Lessons Learned
It remembers project-specific traps and anti-patterns in `xskill/lessons-learned/`. It searches this memory before every task.

### Auto-Verification
Every plan includes a mandatory `verification_command`. Xskill runs it automatically after editing code. No more "trust me, it's done."

### Simplified Idea Cards
Broad ideas are met with a simple [A] [B] [C] choice menu. Fast decision, fast execution.

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

### Case Study 06: Auto-Metrics & Self-Refactor
**Task:** Refactor Xskill for Ghost Mode and implement automated metrics.
**Outcome:** Verified implementation with zero scope creep.

| Metric | Result |
|---|---|
| Context Load Proxy | 9 (Low) |
| Files Read | 6 |
| Scope Creep Rate | 0.00% |
| Verification Rate | 100% |
| Proxy TVP | 9.00 |

*Data generated automatically by the new `xskill/metrics/collect.js` tool.*

See `examples/case-studies/` and `xskill/examples/`.

---

## 9. Philosophy

**Tokens are precious.**

Most agent workflows (like Superpowers or get-shit-down) add more prompts, more memory, more roles, and more automation. They treat the context window as infinite, leading to "context corruption"—where the agent hallucinates, loses focus, and forgets the original goal.

Xskill is the **ultra-lean alternative**. It removes until the work is small enough to verify. It is designed to take a baseline model (Pro) and elevate it to Max-level performance through sheer discipline, without the token bloat.

### The Five Pillars of Xskill

1. **Context Diet:** Do not read everything. Do not touch unrelated files. Every token must earn its keep.
2. **Musk-Style 5-Step Engineering:** Question the requirements, delete the scope, optimize the path, accelerate the iteration time, and automate verification.
3. **Semantic Architecture:** Design the smallest decoupling boundary before writing code, preventing monolithic spaghetti.
4. **Schema Memory:** Do not remember raw code. Remember the *shape* of the solution and the *lessons learned* from failure.
5. **Anti-Corruption:** Stop context degradation by forcing a hard reset (Failure-to-Smaller-Task) instead of blindly retrying failed large tasks.

Xskill is not a full agent runtime. It is an **execution discipline layer** that forces the AI to think like a senior engineer.

---

## 10. Credits / disclaimer

Xskill is inspired by ideas from Musk-style five-step engineering, Toyota Five Whys, first-principles reasoning, Occam’s Razor, small-batch quick response, agile and lean development, TDD micro-loops, evidence-led execution, schema-based learning, and agent skill systems such as Superpowers.

Xskill is not affiliated with Elon Musk, Tesla, SpaceX, X, xAI, Toyota, SHEIN, Superpowers, OpenAI, Anthropic, Google, GitHub, or any referenced project.

All Xskill text and templates are original unless otherwise noted.

License: MIT
