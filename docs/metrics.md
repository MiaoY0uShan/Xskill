# Xskill Metrics

Xskill is designed to make AI coding agents produce smaller, safer, more verifiable work.

Metrics are how Xskill proves whether that actually happened.

## Primary metric: TVP

```text
TVP = total_context_tokens / verified_tasks_completed
```

TVP means **Tokens to Verified Progress**.

Lower TVP is better only when verified progress is preserved.

If no task was verified, TVP is undefined.

## When token counts are unavailable

Xskill is a portable skill bundle. It does not own the agent runtime and usually cannot access exact token counts.

When exact token counts are unavailable, use a proxy:

```text
Context Load Proxy = files_read + skills_loaded + reports_generated
Proxy TVP = context_load_proxy / verified_tasks_completed
```

This proxy is not perfect. It is meant for early evaluation and manual comparisons.

## Supporting metrics

### Scope Creep Rate

```text
Scope Creep Rate = touched_unplanned_files / touched_files
```

Measures whether the agent touched files outside the brief.

### Verification Rate

```text
Verification Rate = tasks_with_checks / completed_tasks
```

Measures whether completed tasks had checks.

### Rework Rate

```text
Rework Rate = failed_or_reopened_tasks / completed_tasks
```

Measures repeated failure or reopening.

### Context Load Size

```text
Context Load Size = files_loaded_per_task
```

Measures how much repository context was loaded per task.

### Iteration Half-life

```text
Iteration Half-life = time_to_first_verified_slice
```

If time is unavailable, use TDD micro-loops to first verified slice as a proxy.

## Evidence required

Metrics should come from:

- Compiled Execution Brief
- Evidence Ledger
- Shorten Iteration Report
- Metrics Report

Do not fabricate metrics.

Use `unknown` when the value is unavailable.

## What Xskill can and cannot claim

Xskill can claim:

- the brief constrained files to read, touch, and avoid;
- required checks were or were not run;
- scope creep was or was not recorded;
- proxy context load improved or worsened across comparable runs.

Xskill cannot claim:

- fewer tokens were used without token logs or a comparable baseline;
- verification improved without evidence;
- a workflow is better from one anecdotal run.

## Recommended comparison

Run the same task twice when possible:

1. Baseline: agent without Xskill.
2. Xskill: agent using the compiled Execution Brief.

Compare:

- files read;
- files touched;
- unplanned files touched;
- checks run;
- failed attempts;
- time or loops to first verified slice;
- exact tokens, if available.
