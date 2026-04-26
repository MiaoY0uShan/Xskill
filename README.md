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
  "must_not_do": [
    "Do not rewrite the auth provider",
    "Do not touch OAuth login",
    "Do not build admin reset flows",
    "Do not add a full email delivery abstraction"
  ],
  "module_boundaries": [
    {
      "module": "reset-token",
      "responsibility": "Generate, validate, expire, and consume reset tokens",
      "must_not_own": "OAuth provider behavior"
    }
  ],
  "files_to_read": [
    "src/auth/reset.ts",
    "src/auth/token.ts",
    "tests/auth/test_reset.ts"
  ],
  "files_to_touch": [
    "src/auth/reset.ts",
    "tests/auth/test_reset.ts"
  ],
  "files_to_avoid": [
    "src/oauth/**",
    "src/billing/**",
    "src/auth/provider/**"
  ],
  "context_budget": {
    "max_files_to_read": 4,
    "max_files_to_touch": 2,
    "max_notes": "500 words"
  },
  "checks": [
    "pytest tests/auth/test_reset.py"
  ],
  "tdd_micro_loops": [
    {
      "loop": 1,
      "red": "Expired reset token is rejected",
      "green": "Implement minimal expiry validation",
      "evidence": "Focused test passes"
    },
    {
      "loop": 2,
      "red": "Used reset token cannot be reused",
      "green": "Mark token as consumed",
      "evidence": "Regression test passes"
    }
  ],
  "max_scope": "one validation module and one focused test file",
  "stop_condition": "Stop if implementation requires auth provider refactor",
  "evidence_required": [
    "failing test before fix",
    "passing test after fix",
    "no unrelated files touched"
  ]
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

## Why this exists

AI coding agents are powerful, but they often fail in predictable ways:

| Without Xskill | With Xskill |
|---|---|
| Reads too much context | Gets a context budget |
| Touches unrelated files | Gets files to read, touch, and avoid |
| Starts from a vague request | Compiles the request into an Execution Brief |
| Builds too much | Deletes scope down to MVP |
| Says “done” without proof | Produces an evidence ledger |
| Retries failed tasks blindly | Splits failure into TDD micro-loops |
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

Optional: copy `AGENTS.md` into your project root.

Final structure:

```text
.agents/skills/xskill/
  question-requirements/SKILL.md
  delete-scope/SKILL.md
  semantic-architecture/SKILL.md
  optimize-path/SKILL.md
  shorten-iteration/SKILL.md
  evidence-ledger/SKILL.md
  metrics/SKILL.md
  adaptive-improvement/SKILL.md
  schema-memory/SKILL.md
  templates/
  examples/
```

Restart your coding agent after copying the folder.

---

## How it works

### 1. Question requirements

Before non-trivial work, the agent challenges the request.

It uses lightweight Five Whys and inversion:

```text
What is the real goal?
Why does this matter?
If this failed, why would it fail?
If the agent made it worse, what would it do?
```

Output: real goal, assumptions, failure paths, success criteria, non-goals, and decision.

---

### 2. Delete scope

After the real goal is clear, Xskill uses first-principles reasoning and Occam's Razor:

```text
What is irreducibly required?
What entity has no necessary purpose?
What can be deleted, deferred, or avoided?
```

Output: MVP nucleus, scope boundary, minimum evidence, and module candidates.

---

### 3. Sketch semantic architecture

For multi-module work, Xskill creates a lightweight architecture sketch.

It does not create a graph database or architecture engine. It only clarifies:

```text
modules
relationships
coupling risks
decoupling rules
MVP-first build order
```

Output: module boundaries and dependency direction.

---

### 4. Optimize path

Xskill chooses the smallest stable implementation route.

It uses:

```text
small-batch quick response
agile working increment
lean waste removal
minimal just-in-case buffer
```

Then it compiles upstream outputs into the final Execution Brief.

Output: selected path, context budget, files to read/touch/avoid, checks, evidence requirements, stop condition, and optional TDD loops.

---

### 5. Shorten iteration

If the route is too large or fails, Xskill splits it into TDD micro-loops:

```text
RED → GREEN → REFACTOR → EVIDENCE
```

Output: a smaller set of verified loops that can be inserted into the Execution Brief.

---

### 6. Execute with the brief

The coding agent executes the brief. The brief is the contract.

The agent should not exceed:

```text
context budget
files to touch
scope boundary
stop condition
```

---

### 7. Evidence ledger

After execution, the agent records proof:

```text
files touched
commands run
verified claims
unverified claims
scope violations
remaining risk
```

If there is no evidence, the task is not done.

---

### 8. Metrics

Xskill can measure whether a run actually became smaller, safer, and more verifiable.

Primary metric:

```text
TVP = total_context_tokens / verified_tasks_completed
```

When exact token counts are unavailable, Xskill uses a proxy:

```text
Context Load Proxy = files_read + skills_loaded + reports_generated
Proxy TVP = context_load_proxy / verified_tasks_completed
```

Supporting metrics:

```text
Scope Creep Rate
Verification Rate
Rework Rate
Context Load Size
Iteration Half-life
```

Metrics must come from evidence, not guesses.

---

### 9. Adaptive improvement and schema memory

Xskill does not auto-improve blindly.

It can convert repeated evidence into reusable schemas:

```text
what worked
what failed
what context was wasted
what verification was reliable
what should be repeated next time
```

Xskill learns from evidence, not confidence.

---

## Core artifacts

### Compiled Execution Brief

The primary output of Xskill.

A short contract that tells the agent:

```text
what to do
why it matters
what not to do
which files to read
which files to touch
which files to avoid
how to verify
when to stop
what evidence is required
```

Templates:

```text
xskill/templates/execution-brief.md
xskill/templates/compiled-execution-brief.md
```

Example:

```text
xskill/examples/password-reset.compiled-execution-brief.json
```

---

### Context Budget

A boundary that prevents context bloat:

```text
max files to read
max files to touch
forbidden context
scope boundary
stop condition
```

---

### Evidence Ledger

A proof record after execution:

```text
what changed
what checks ran
what was verified
what remains unverified
whether scope was violated
```

---

### Metrics Report

A measurement artifact that records whether Xskill reduced context load, scope creep, rework, or unverifiable work.

Primary metric:

```text
TVP = total_context_tokens / verified_tasks_completed
```

Proxy metric when token counts are unavailable:

```text
Proxy TVP = (files_read + skills_loaded + reports_generated) / verified_tasks_completed
```

Template:

```text
xskill/templates/metrics-report.md
```

Example:

```text
xskill/examples/password-reset.metrics-report.md
```

---

### Schema Memory

A reusable pattern extracted from multiple evidence-backed runs.

It remembers how a class of work should be handled:

```text
trigger
common failure modes
recommended execution pattern
context budget pattern
verification pattern
stop conditions
```

---

## Recommended prompts

### Compile a task

```text
Use Xskill to compile this task into an Execution Brief before editing code:
<task>
```

### Compile a larger feature

```text
Use Xskill end to end:
1. question-requirements
2. delete-scope
3. semantic-architecture
4. optimize-path
5. shorten-iteration if needed
Then produce one compiled Execution Brief.

Task:
<task>
```

### After execution

```text
Use Xskill evidence-ledger to record what changed, what was verified, and what remains unverified.
Then use Xskill metrics to measure context load, scope creep, verification, rework, and TVP.
Then use adaptive-improvement only if there is reusable evidence.
```

---

## When not to use Xskill

Do not run the full workflow for:

```text
typo fixes
small formatting changes
obvious one-line edits
pure copy changes
throwaway experiments
```

Use Xskill when:

```text
scope matters
context matters
verification matters
multiple modules are involved
failure would be expensive
```

---

## Philosophy

Most agent workflows add more process.

Xskill deletes process until only the executable contract remains.

```text
Question first.
Delete aggressively.
Sketch only the needed architecture.
Choose the smallest stable path.
Split into TDD micro-loops when needed.
Compile one brief.
Execute with evidence.
Measure verified progress.
Improve only from evidence.
```

---

## Influences

Xskill is influenced by ideas from five-step engineering, first-principles reasoning, Occam's Razor, Toyota-style Five Whys, inversion thinking, small-batch quick response, agile development, lean development, TDD, evidence-ledger workflows, execution metrics, schema memory, and agent skill systems.

It does not copy prompts or workflows from referenced projects. It compresses general execution mechanisms into a portable skill bundle.

---

## License

MIT
