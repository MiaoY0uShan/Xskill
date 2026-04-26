# Xskill

**Context diet for AI coding agents.**

AI coding agents do not need more context.

They need a smaller task, a harder boundary, and proof that the work is done.

Xskill is an **agent-agnostic execution discipline layer**.

It turns vague coding requests into **bounded, verifiable Execution Briefs** for Codex, Claude Code, Gemini CLI, GitHub Copilot CLI, Cursor, OpenCode, or any agent that can read Markdown instructions.

**Less context. Smaller changes. Verified progress.**

---

## Demo

Tell your coding agent:

```text
Use Xskill to compile this task into an Execution Brief before editing code:
Add password reset flow.
```

Expected output:

```json
{
  "task": "Add password reset flow",
  "real_goal": "Allow users to reset passwords safely without refactoring auth provider internals",
  "mvp_scope": "Reset token generation and validation only",
  "must_not_do": [
    "Do not rewrite the auth provider",
    "Do not touch OAuth login",
    "Do not build admin reset",
    "Do not add a full email abstraction yet"
  ],
  "context_budget_contract": {
    "max_files_to_read": 5,
    "max_files_to_touch": 3,
    "max_skill_tokens": 900,
    "max_execution_notes": 500,
    "required_semantic_nodes": ["auth.reset-token", "tests.auth.reset"],
    "required_schema_cards": ["validation-bug"],
    "forbidden_context": ["src/oauth/**", "src/billing/**", "src/auth/provider/**"],
    "scope_boundary": "Do not modify auth provider internals",
    "violation_handling": "Stop and split smaller before exceeding the contract"
  },
  "context_diet_map": {
    "relevant_nodes": ["auth.reset-token", "tests.auth.reset"],
    "irrelevant_nodes": ["oauth.provider", "billing", "admin.reset"],
    "files_to_read": ["src/auth/reset.ts", "src/auth/token.ts", "tests/auth/test_reset.ts"],
    "files_to_avoid": ["src/oauth/**", "src/billing/**", "src/auth/provider/**"],
    "reason": "Task only touches reset-token validation, not OAuth provider internals"
  },
  "tdd_micro_loops": [
    {
      "loop": 1,
      "red": "Expired reset token is rejected",
      "green": "Implement minimal expiry validation",
      "evidence": "Focused test passes"
    }
  ],
  "checks": ["pytest tests/auth/test_reset.py"],
  "evidence_required": [
    "failing test before fix",
    "passing focused test after fix",
    "no unrelated files touched"
  ],
  "stop_condition": "Stop if implementation requires auth provider refactor"
}
```

That JSON is the product moment.

Xskill is not a longer prompt. It is a portable task compiler.

---

## Problem

AI coding agents are powerful, but they often fail in predictable ways.

| Without Xskill | With Xskill |
|---|---|
| Reads too much context | Reads only the relevant slice |
| Touches unrelated files | Gets a context contract |
| Accepts the first request literally | Questions the real goal first |
| Builds the full idea too early | Deletes scope down to MVP |
| Creates a big plan | Compiles a small execution brief |
| Says “done” without proof | Produces an evidence ledger |
| Retries failed work blindly | Splits failure into smaller verified work |
| Stores vague memory | Stores reusable task schemas |

The failure mode is not that agents are lazy.

The failure mode is that they are unconstrained.

---

## Solution

Xskill gives each non-trivial task four hard artifacts.

### 1. Context Budget Contract

A task starts with a budget.

```json
{
  "max_files_to_read": 5,
  "max_files_to_touch": 3,
  "max_skill_tokens": 900,
  "max_execution_notes": 500,
  "required_semantic_nodes": [],
  "required_schema_cards": [],
  "forbidden_context": [],
  "scope_boundary": "Do not modify auth provider internals",
  "violation_handling": "Stop and split smaller before exceeding the contract"
}
```

If the agent needs to exceed the contract, it must stop.

It should not silently expand the task.

### 2. Context Diet Map

Most memory systems add context.

Xskill removes context.

```json
{
  "relevant_nodes": [],
  "irrelevant_nodes": [],
  "files_to_read": [],
  "files_to_avoid": [],
  "reason": "Task only touches reset-token validation, not OAuth provider internals"
}
```

The goal is not to remember everything.

The goal is to decide what does not belong in this run.

### 3. Evidence Ledger

Every agent claim needs evidence.

```json
{
  "task_id": "T001",
  "files_read": [],
  "files_touched": [],
  "commands_run": [
    {
      "command": "pytest tests/auth/test_reset.py",
      "result": "pass"
    }
  ],
  "claims": [
    {
      "claim": "Expired reset tokens are rejected",
      "evidence": "Focused test passed"
    }
  ],
  "unverified_claims": [],
  "scope_violations": [],
  "next_action": "Merge or run integration test"
}
```

No evidence means the task is not done.

### 4. Failure-to-Smaller-Task Protocol

Failed runs should shrink the work.

```json
{
  "failed_task": "Add password reset flow",
  "failure_type": "coupling discovered",
  "root_cause": "mail adapter is not mockable",
  "smaller_tasks": [
    "Extract mail sender seam",
    "Add unit test for reset token generation",
    "Add endpoint after seam exists"
  ]
}
```

Xskill turns failed agent runs into smaller verified work.

---

## Quickstart

Xskill does not require an Xskill CLI, npm package, npx command, pip package, database, or runtime.

Download the release zip, unzip it, then choose the ready-made install pack for your agent.

```text
install/
  codex/.agents/skills/xskill/
  claude-code/.claude/skills/xskill/
  gemini-cli/xskill/
  github-copilot-cli/.github/agents/xskill.agent.md

xskill/
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

You no longer need to copy a separate root `AGENTS.md` into your project.

The agent contract is bundled inside:

```text
xskill/AGENTS.md
```

---

## Install by agent

### Codex

Copy the ready-made folder into your repository root:

```text
install/codex/.agents
```

Your repository should contain:

```text
.agents/skills/xskill/SKILL.md
.agents/skills/xskill/references/xskill/...
```

Then ask:

```text
Use Xskill to compile this task into a bounded Execution Brief before editing code:
<task>
```

### Claude Code

Copy the ready-made folder into your repository root:

```text
install/claude-code/.claude
```

Your repository should contain:

```text
.claude/skills/xskill/SKILL.md
.claude/skills/xskill/references/xskill/...
```

Then ask:

```text
/xskill Compile this task into a bounded Execution Brief before editing code: <task>
```

Or:

```text
Use Xskill before editing code: <task>
```

### Gemini CLI

Copy the ready-made extension folder to:

```text
~/.gemini/extensions/xskill
```

Use this source folder:

```text
install/gemini-cli/xskill
```

It already contains:

```text
gemini-extension.json
GEMINI.md
xskill/...
```

Restart Gemini CLI.

Then ask:

```text
Use Xskill to compile this task into a bounded Execution Brief before editing code:
<task>
```

Optional Gemini CLI install command:

```bash
gemini extensions install install/gemini-cli/xskill
```

### GitHub Copilot CLI

Copy the ready-made project pack into your repository root:

```text
install/github-copilot-cli/.github
install/github-copilot-cli/xskill
```

Your repository should contain:

```text
.github/agents/xskill.agent.md
xskill/...
```

Then use the `xskill` custom agent and ask:

```text
Compile this task into a bounded Execution Brief before editing code:
<task>
```

---

## Workflow

Use the full chain only for non-trivial tasks.

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

For small edits, use only the relevant step.

Xskill is not process theater.

It is a boundary system.

---

## Examples

The bundle includes examples under:

```text
xskill/examples/
```

Examples include:

```text
password-reset.question-requirements.md
password-reset.delete-scope.md
password-reset.optimize-path.md
password-reset.shorten-iteration.md
password-reset.compiled-execution-brief.json
password-reset.context-budget-contract.json
password-reset.context-diet-map.md
password-reset.evidence-ledger.json
password-reset.metrics-report.md
password-reset.failure-to-smaller-task.md
validation-bug.schema-memory-card.md
```

The main before/after is simple.

Before Xskill:

```text
Add password reset flow.
```

After Xskill:

```text
Add only the reset-token validation slice.
Read at most 5 files.
Touch at most 3 files.
Avoid OAuth and billing.
Run focused reset-token tests.
Stop if auth provider refactor is required.
Produce evidence before claiming completion.
```

---

## Preliminary self-use evidence

These are **self-use case studies** from building Xskill itself. They are not yet an external benchmark across unrelated repositories.

The goal is to test whether Xskill can reduce prompt/context volume, reduce scope drift, and turn failures into smaller verified work.

Token numbers below are approximate. They are estimated with a simple `characters / 4` rule, rounded to the nearest token. The baseline is a monolithic-agent setup that loads the README, `xskill/AGENTS.md`, all `SKILL.md` files, and all templates. In this repository, that baseline is about **19,562 tokens**.

| Case | Real task | Baseline context | Xskill loaded context | Reduction | Drift control | Verification / failure result |
|---|---|---:|---:|---:|---|---|
| 1 | Rewrite install docs so users no longer copy a root `AGENTS.md` | 19,562 | 7,120 | 63.6% | Limited to README/install wording | Required evidence: docs updated, no runtime added |
| 2 | Add Codex adapter guidance without binding Xskill to Codex | 19,562 | 8,112 | 58.5% | Adapter-only boundary | Required evidence: Codex path documented, generic protocol unchanged |
| 3 | Add JSON Evidence Ledger audit example | 19,562 | 6,808 | 65.2% | Evidence files only | Required evidence: verified/unverified claims represented explicitly |
| 4 | Split a failed password-reset flow into smaller TDD work | 19,562 | 7,520 | 61.6% | No full auth rewrite | Failure converted into smaller tasks and focused checks |
| 5 | Add metrics report for TVP, scope creep, verification, and rework | 19,562 | 8,365 | 57.2% | Metrics-only addition | Required evidence: TVP proxy and supporting metrics recorded |

Average context reduction across these five self-use cases: **61.2%**.

What this proves so far:

- Xskill can keep task-specific loaded context under the 50% reduction target for these repository-maintenance tasks.
- Xskill can express scope boundaries before execution.
- Xskill can require checks and evidence instead of accepting "done" as a claim.
- Xskill can turn at least one failure scenario into smaller TDD micro-loops.

What this does **not** prove yet:

- It does not prove performance across 10 unrelated external repositories.
- It does not prove exact model token savings from hosted agent APIs.
- It does not prove lower bug rate without a controlled before/after benchmark.

Next benchmark target:

- Run 10 external tasks with and without Xskill.
- Record irrelevant file edits, skipped verification, scope expansion, misunderstood requirements, and rework.
- Publish the raw Evidence Ledgers and Metrics Reports.


## Metrics

Xskill is designed to reduce context load, scope creep, and unverifiable work.

Primary metric:

```text
TVP = total_context_tokens / verified_tasks_completed
```

When exact token counts are unavailable, use a portable proxy:

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

Metrics live in:

```text
xskill/metrics/
xskill/templates/metrics-report.md
docs/metrics.md
```

---

## Architecture

Xskill has three layers.

```text
1. Agent adapters
   install/codex/
   install/claude-code/
   install/gemini-cli/
   install/github-copilot-cli/
   adapters/

2. Portable skill bundle
   xskill/AGENTS.md
   xskill/*/SKILL.md
   xskill/templates/
   xskill/examples/

3. Execution artifacts
   Compiled Execution Brief
   Context Budget Contract
   Context Diet Map
   Evidence Ledger
   Metrics Report
   Adaptive Improvement Report
   Schema Memory Card
```

The protocol is always the same:

```text
task → brief → bounded execution → evidence → metrics → improvement
```

See:

```text
docs/execution-protocol.md
adapters/README.md
```

---

## Roadmap

### Current

- Portable Xskill bundle
- Agent-agnostic adapters
- Compiled Execution Brief
- Context Budget Contract
- Context Diet Map
- Evidence Ledger
- Failure-to-Smaller-Task Protocol
- Metrics Layer
- Adaptive Improvement
- Schema Memory

### Next

- More real examples
- Better adapter documentation
- Optional Cursor rules pack
- Optional OpenCode pack
- More schema memory cards
- More before/after runs with metrics

### Not planned for now

- Xskill CLI
- npm package
- npx installer
- pip package
- database memory
- graph engine
- automatic executor
- automatic self-modifying agent

---

## Philosophy

Most agent workflows add more context.

Xskill removes context.

Most agents say done.

Xskill asks for evidence.

Most loops retry failure.

Xskill splits failure into smaller work.

**Think less context. Build with proof.**

---

## License

MIT
