# Xskill

**Context diet for AI coding agents.**

Xskill is a portable task compiler for AI coding agents.

It does not give agents a longer prompt. It helps them compile a vague coding task into a short, bounded, verifiable **Execution Brief**.

```text
user task
  ↓
question requirements
  ↓
delete scope
  ↓
semantic architecture
  ↓
optimize path
  ↓
shorten iteration
  ↓
compiled execution brief
  ↓
agent execution
  ↓
evidence ledger
  ↓
metrics report
  ↓
adaptive improvement
  ↓
schema memory
```

Most agent workflows add more context.

Xskill removes context until the task becomes safe to execute.

**Less context. Smaller changes. Verified progress.**

---

## 10-second demo

Ask your coding agent:

```text
Use Xskill to compile this task into an Execution Brief before editing code:
Add password reset flow.
```

Expected compiled output:

```json
{
  "task": "Add password reset flow",
  "real_goal": "Allow users to reset passwords safely without refactoring auth provider internals",
  "mvp_scope": "Reset token generation and validation only",
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
  "checks": ["pytest tests/auth/test_reset.py"],
  "evidence_required": ["failing test before fix", "passing focused test after fix", "no unrelated files touched"],
  "failure_to_smaller_task_protocol": {
    "failure_split_rule": "If implementation requires auth provider refactor, stop and split into a smaller seam task"
  }
}
```

That JSON is the product moment.

Xskill is not just a prompt pack. The primary output is a compiled Execution Brief that a coding agent can execute.

---

## What Xskill is

Xskill is **not** a CLI, npm package, Python package, autonomous agent, database, or full runtime.

Xskill is a **portable skill bundle**:

```text
Download zip.
Unzip.
Copy the xskill/ folder into your agent skills directory.
Use it with your coding agent.
```

It works best with agents that can read `SKILL.md` files or repository instructions such as `AGENTS.md`. If your agent does not support skills directly, open the relevant `SKILL.md` file and paste it into the agent before a task.

---

## The four differentiators

### 1. Context Budget Contract

Every non-trivial task should produce a hard context contract:

```json
{
  "max_files_to_read": 5,
  "max_files_to_touch": 3,
  "max_skill_tokens": 900,
  "max_execution_notes": 500,
  "required_semantic_nodes": [],
  "required_schema_cards": [],
  "forbidden_context": [],
  "scope_boundary": "Do not modify auth provider internals"
}
```

If the agent needs to exceed the contract, it must stop and ask for a revised contract or split the task smaller.

### 2. Evidence Ledger

Every agent claim needs evidence.

A completed task records files read, files touched, commands run, verified claims, unverified claims, scope violations, and next action.

No evidence means the task is not done.

### 3. Failure-to-Smaller-Task Protocol

Failed runs should shrink the work.

Do not blindly retry the same task.

A failed or blocked run should produce:

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

### 4. Context Diet Map

Xskill is not generic memory.

It uses context only to decide what does and does not belong in the current task.

A Context Diet Map says:

```json
{
  "relevant_nodes": [],
  "irrelevant_nodes": [],
  "files_to_read": [],
  "files_to_avoid": [],
  "reason": "Task only touches reset-token validation, not OAuth provider internals"
}
```

Other memory systems add context. Xskill removes context.

---

## Why this exists

AI coding agents are powerful, but they often fail in predictable ways:

| Without Xskill | With Xskill |
|---|---|
| Reads too much context | Gets a Context Budget Contract |
| Touches unrelated files | Gets files to read, touch, and avoid |
| Starts from a vague request | Compiles the request into an Execution Brief |
| Builds too much | Deletes scope down to MVP |
| Says “done” without proof | Produces an Evidence Ledger |
| Retries failed tasks blindly | Uses a Failure-to-Smaller-Task Protocol |
| Uses memory to add context | Uses Context Diet Maps to remove context |
| Learns from vibes | Learns from evidence-backed schemas |

Xskill focuses on one job:

> Turn vague agent work into bounded, verifiable execution.

---

## Install

Xskill does not require npm, npx, pip, Python, or a command-line tool.

1. Download the latest `xskill-v*.zip` from GitHub Releases.
2. Unzip it.
3. Copy the `xskill/` folder into your agent skills directory.

Recommended global location:

```text
~/.agents/skills/xskill
```

Recommended project-local location:

```text
your-project/.agents/skills/xskill
```

Optionally copy `AGENTS.md` into your project root.

---

## Skills

```text
question-requirements     Five Whys, inversion, real goal, failure paths
delete-scope              first principles, Occam filter, MVP nucleus
semantic-architecture     MVP module boundaries and decoupling rules
optimize-path             small-batch route and compiled Execution Brief
shorten-iteration         TDD micro-loops and failure split protocol
evidence-ledger           evidence-first audit record
metrics                   TVP, scope creep, verification, rework, context load
adaptive-improvement      evidence-backed improvement decisions
schema-memory             reusable task schemas, not raw context
```

---

## Primary artifacts

```text
Compiled Execution Brief
Context Budget Contract
Context Diet Map
Failure-to-Smaller-Task Protocol
Evidence Ledger
Metrics Report
Adaptive Improvement Report
Schema Memory Card
```

---

## Metrics

Xskill is designed to reduce context load, scope creep, and unverifiable work.

Primary metric:

```text
TVP = total_context_tokens / verified_tasks_completed
```

When exact token counts are unavailable:

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

---

## When not to use Xskill

Do not use the full workflow for:

- tiny typo fixes;
- trivial formatting;
- one-line copy edits;
- tasks whose scope and verification are already obvious.

Use Xskill when scope, context, verification, or failure risk matters.

---

## Philosophy

```text
Question first.
Delete aggressively.
Design only the MVP.
Choose the smallest stable path.
Split failure into smaller verified work.
Demand evidence.
Measure the result.
Learn only from evidence.
```

Xskill learns from evidence, not confidence.

---

## License

MIT
