# Xskill

**Context diet for AI coding agents.**

AI coding agents do not need more context.

They need a smaller task, a harder boundary, and proof that the work is done.

Xskill turns vague coding requests into **bounded, verifiable Execution Briefs**.

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

Xskill is not a longer prompt. It is a task compiler.

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

Xskill does not require npm, npx, pip, a CLI, a database, or a runtime.

### 1. Download

Download the latest release zip from GitHub Releases.

### 2. Unzip

You should see:

```text
xskill/
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

### 3. Copy

Copy the `xskill/` folder into your agent skills directory.

Common locations:

```text
~/.agents/skills/xskill
```

or inside a project:

```text
your-project/.agents/skills/xskill
```

### 4. Add AGENTS.md

Copy the included `AGENTS.md` into the root of your project if your agent supports repository instructions.

### 5. Use

Ask your agent:

```text
Use Xskill to compile this task into an Execution Brief before editing code:
<your task>
```

If your agent does not support skills directly, open the relevant `SKILL.md` file and paste it into the agent before starting the task.

---

## Workflow

Xskill is a portable task compiler.

```text
user task
  ↓
question-requirements
  ↓
delete-scope
  ↓
semantic-architecture
  ↓
optimize-path
  ↓
shorten-iteration
  ↓
compiled execution brief
  ↓
agent execution
  ↓
evidence-ledger
  ↓
metrics
  ↓
adaptive-improvement
  ↓
schema-memory
```

### 1. Question requirements

Use Five Whys and inversion to find the real goal.

The agent asks:

```text
What is the stated goal?
What is the likely real goal?
Why does this need to exist?
How would this fail?
Should we continue, reduce scope, ask the user, or stop?
```

### 2. Delete scope

Use first principles and Occam’s Razor.

Keep only what is necessary for the smallest useful MVP.

```text
凡无必要，勿增实体。
```

### 3. Sketch semantic architecture

Only for multi-module tasks.

Generate a lightweight module map, coupling risks, decoupling rules, and MVP-first build order.

No graph database. No architecture engine.

### 4. Optimize path

Choose the smallest stable route.

Xskill uses:

- small-batch quick response
- agile working increments
- lean waste removal
- minimal just-in-case safety buffers

The result is a selected path that can be verified.

### 5. Shorten iteration

Large or failed tasks become TDD micro-loops.

```text
RED → GREEN → REFACTOR → EVIDENCE
```

### 6. Compile Execution Brief

The upstream outputs are compressed into one short artifact.

The brief tells the agent:

- what to do
- why it matters
- what not to do
- what files to read
- what files to avoid
- how to verify
- when to stop

### 7. Record evidence

After execution, the agent must produce an Evidence Ledger.

### 8. Measure

The Metrics Report records context load, verification, rework, and scope creep.

### 9. Improve only from evidence

Adaptive improvement can update schema memory, templates, checklists, or automation candidates.

It does not auto-modify skills blindly.

Xskill learns from evidence, not confidence.

---

## Examples

### Before Xskill

```text
Task: Add password reset flow.

Agent reads auth, OAuth, billing, user profile, email, admin tools.
Agent rewrites the auth provider.
Agent adds three abstractions.
Agent says “done”.
No focused test proves token expiry.
```

### After Xskill

```text
Task: Add password reset flow.

Real goal:
Reset token generation and validation only.

MVP scope:
No OAuth refactor. No admin reset. No full email abstraction.

Context budget:
Read at most 5 files. Touch at most 3 files.

Context diet:
Avoid src/oauth/** and src/billing/**.

TDD micro-loop:
Expired token rejected → minimal expiry validation → focused test passes.

Evidence:
Failing test before fix. Passing test after fix. No unrelated files touched.
```

### Included examples

```text
xskill/examples/password-reset.question-requirements.md
xskill/examples/password-reset.delete-scope.md
xskill/examples/xskill.semantic-architecture.md
xskill/examples/password-reset.optimize-path.md
xskill/examples/password-reset.shorten-iteration.md
xskill/examples/password-reset.compiled-execution-brief.json
xskill/examples/password-reset.context-budget-contract.json
xskill/examples/password-reset.context-diet-map.md
xskill/examples/password-reset.evidence-ledger.json
xskill/examples/password-reset.metrics-report.md
xskill/examples/password-reset.failure-to-smaller-task.md
xskill/examples/password-reset.adaptive-improvement.md
```

---

## Metrics

The primary metric is **TVP**.

```text
TVP = total_context_tokens / verified_tasks_completed
```

Lower is better.

When exact token counts are unavailable, use a proxy:

```text
Context Load Proxy = files_read + skills_loaded + reports_generated
Proxy TVP = context_load_proxy / verified_tasks_completed
```

Supporting metrics:

| Metric | Formula | What it catches |
|---|---|---|
| Scope Creep Rate | `touched_unplanned_files / touched_files` | Agent touched files outside the brief |
| Verification Rate | `tasks_with_checks / completed_tasks` | Agent claimed completion without checks |
| Rework Rate | `failed_or_reopened_tasks / completed_tasks` | Work had to be redone |
| Context Load Size | `files_loaded_per_task` | Agent read too much |
| Iteration Half-life | `time_to_first_verified_slice` | Agent took too long to produce verified progress |

Xskill is not just a methodology.

It is designed to be measured.

---

## Architecture

Xskill has no runtime state by default.

It is a portable folder of skills, templates, and examples.

```text
xskill/
  question-requirements/
    SKILL.md
  delete-scope/
    SKILL.md
  semantic-architecture/
    SKILL.md
  optimize-path/
    SKILL.md
  shorten-iteration/
    SKILL.md
  evidence-ledger/
    SKILL.md
  metrics/
    SKILL.md
  adaptive-improvement/
    SKILL.md
  schema-memory/
    SKILL.md
  templates/
    compiled-execution-brief.md
    context-budget-contract.md
    context-budget-contract.json
    context-diet-map.md
    evidence-ledger.md
    failure-to-smaller-task-protocol.md
    metrics-report.md
    schema-memory-card.md
  examples/
    password-reset.compiled-execution-brief.json
    password-reset.context-budget-contract.json
    password-reset.evidence-ledger.json
```

### Optional artifact state

If you want to keep task artifacts inside your project, use a lightweight folder such as:

```text
.xskill/
  runs/
    T001/
      compiled-execution-brief.json
      context-budget-contract.json
      context-diet-map.md
      evidence-ledger.json
      metrics-report.md
      adaptive-improvement.md
```

This folder is optional.

Xskill does not require a database, daemon, CLI, or background process.

---

## When to use Xskill

Use Xskill for:

- unclear requirements
- new features
- refactors
- bug fixes with risk
- auth, billing, data, permissions, or security work
- tasks that may touch multiple modules
- tasks where agent scope creep would be expensive

Do not use the full workflow for:

- typo fixes
- formatting
- trivial copy changes
- obvious one-line edits

For small tasks, use only the relevant skill or just the compiled Execution Brief template.

---

## Roadmap

### Current

- Portable skill bundle
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
- More before/after task comparisons
- Agent-specific installation notes
- Stronger schema memory examples
- Better metrics examples with real token data

### Later

- Optional adapter docs for Claude Code, Codex, Cursor, Copilot, and OpenCode
- Optional report packs for teams
- Optional benchmark dataset

### Not planned for now

- CLI
- npm package
- npx command
- pip package
- database
- daemon
- automatic executor
- graph engine
- self-modifying runtime

---

## Philosophy

Most agent systems try to become smarter by adding more context.

Xskill tries to become safer by removing context.

Most agents say they are done.

Xskill asks for evidence.

Most failed loops retry.

Xskill splits the work smaller.

Most memory systems store more.

Xskill stores reusable schemas.

**Think smaller. Execute tighter. Prove progress.**

---

## Influences

Xskill is influenced by ideas from:

- Five-step engineering methods
- Toyota Five Whys
- Occam’s Razor
- first-principles reasoning
- small-batch quick response
- agile development
- lean software development
- TDD
- context engineering
- evidence-based review
- adaptive learning loops

Xskill does not copy prompts or workflows from other projects.

It compresses general execution mechanisms into a smaller portable skill system.

---

## License

MIT
