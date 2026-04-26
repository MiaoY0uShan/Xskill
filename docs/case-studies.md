# Xskill self-use case studies

These case studies were created while building Xskill itself.

They are preliminary evidence, not a formal benchmark. The purpose is to show how the Xskill protocol can be used to constrain real repository-maintenance tasks before a broader external evaluation.

## Measurement method

Baseline context is defined as a monolithic rules setup that loads:

- `README.md`
- `xskill/AGENTS.md`
- every `xskill/*/SKILL.md`
- every `xskill/templates/*`

Estimated baseline: **19,562 tokens**.

Token estimates use:

```text
estimated_tokens = characters / 4
```

Xskill loaded context is the subset of skill files, adapter docs, and templates required for that task.

## Case summary

| Case | Task | Baseline | Xskill | Reduction |
|---|---|---:|---:|---:|
| 1 | Rewrite install docs | 19,562 | 7,120 | 63.6% |
| 2 | Add Codex adapter guidance | 19,562 | 8,112 | 58.5% |
| 3 | Add JSON Evidence Ledger example | 19,562 | 6,808 | 65.2% |
| 4 | Split failed password reset flow | 19,562 | 7,520 | 61.6% |
| 5 | Add metrics report | 19,562 | 8,365 | 57.2% |

Average reduction: **61.2%**.

## Test 1: prompt/context volume

Target: reduce always-on context by more than 50%.

Result: passed for all five self-use cases.

## Test 2: drift control

For these five self-use cases, Xskill required explicit boundaries such as:

- files or sections to touch
- files or areas to avoid
- maximum scope
- stop conditions
- evidence required

This is not yet the same as a controlled 10-task external run. The next benchmark should record:

- unrelated files changed
- skipped checks
- expanded scope
- misunderstood requirements

## Test 3: failure-to-smaller-task

The failure-split case demonstrates the protocol:

```text
failed task
→ root cause
→ smaller task list
→ focused checks
```

This satisfies the shape of the test, but more external failure cases are needed.
