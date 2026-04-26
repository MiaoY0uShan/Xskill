---
name: xskill-adaptive-improvement
description: Use after a non-trivial run to turn evidence into feedback, schema memory updates, checklist improvements, or automation candidates. Learns from evidence, not confidence.
---

# Xskill: Adaptive Improvement

Learn from evidence, not confidence.

This skill merges the old automate-after-stable and learn-after-run steps into one evidence-backed improvement loop.

It does not create an autonomous self-improving agent. It does not rewrite skills automatically. It only decides whether a run produced a reusable improvement.

## Use when

- A non-trivial task has completed.
- A task failed, drifted, or got blocked.
- The agent read too much context.
- The agent touched too many files.
- A verification check failed or revealed a useful lesson.
- A repeated manual step may deserve automation later.
- A pattern may deserve schema memory.
- A previous schema did not prevent failure.

## Do not use when

- The task was a tiny typo, copy edit, or formatting change.
- There is no evidence ledger.
- The proposed lesson is speculative.
- The agent is trying to justify work it cannot verify.
- The change would increase ceremony without reducing context, scope, or verification risk.

## Goal

Produce an adaptive improvement report.

The report decides whether the evidence should become:

- a local note
- a schema memory update
- a template improvement
- a checklist improvement
- an automation candidate
- no action

## Inputs

Prefer these inputs, in order:

1. Evidence Ledger
2. Metrics Report
3. Execution Brief
4. Shorten Iteration Report
5. Existing Schema Memory Card
6. Previous Adaptive Improvement Reports

If there is no evidence ledger, do not proceed.

## Procedure

1. Identify the source evidence.
2. Determine whether the run passed, failed, was blocked, or partially completed.
3. Extract what worked.
4. Extract what failed, drifted, or wasted context.
5. Determine whether the pattern is repeated or one-off.
6. Use the metrics report, if available, to decide whether the improvement would reduce context, reduce scope creep, improve verification, reduce rework, or stabilize a repeated workflow.
7. Choose one improvement type.
8. Run a safety check: what could this improvement make worse?
9. Decide reject, observe more, promote to schema, or mark as automation candidate.

## Promotion rules

Do not promote a lesson unless at least one is true:

- It appeared in more than one run.
- It clearly reduces context load or proxy TVP.
- It narrows future scope.
- It improves verification rate.
- It prevents a repeated failure or reduces rework rate.
- It stabilizes a repeated workflow.

Never automate confusion.

Automation is allowed only when:

- the manual step is repeated,
- the outcome is stable,
- the risks are understood,
- guardrails are clear,
- rollback is possible.

## Output contract

Return this structure:

```md
# Adaptive Improvement Report

## Source Evidence

## Run Result
Pass | Fail | Blocked | Partial

## Repeated Pattern Detected

## What Worked

## What Failed Or Drifted

## Context Or Scope Waste

## What Should Change?

## Improvement Type
- [ ] Keep as local note
- [ ] Update schema memory
- [ ] Update template
- [ ] Add checklist
- [ ] Suggest automation candidate
- [ ] Do nothing

## Why This Improves Xskill
- [ ] Reduces context
- [ ] Reduces scope
- [ ] Improves verification
- [ ] Prevents repeated failure
- [ ] Stabilizes repeated workflow

## Promotion Decision
reject | observe_more | promote_to_schema | automation_candidate

## Safety Check
What could this improvement make worse?

## Recommended Next Step
```

## Automation candidate output

If automation is suggested, also return:

```md
# Automation Candidate

## Repeated Manual Step

## Evidence Of Repetition

## Stability Level
low | medium | high

## Risk If Automated Too Early

## Guardrails Required

## Rollback Plan

## Decision
not_now | observe_more | automate_later
```

## Rules

- Evidence before learning.
- Repetition before promotion.
- Stability before automation.
- Prefer schema memory over skill mutation.
- Prefer small checklist changes over new skills.
- Do not modify skills automatically.
- Do not add process unless it makes future work smaller, safer, or more verifiable.

## Failure mode

If there is no evidence, return:

```md
# Adaptive Improvement Blocked

Decision: reject

Reason:
No evidence ledger was provided. Xskill learns from evidence, not confidence.
```
