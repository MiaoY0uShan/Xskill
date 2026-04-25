# Skill: automate-after-stable

Musk step: Automate only after the manual process is stable.

## Trigger

Use after a workflow has been performed manually several times, or when the same verification, task selection, indexing, or state update repeats.

## Goal

Identify safe automation candidates and convert only stable repetition into commands, hooks, or scripts.

## Inputs

- Progress log
- Repeated manual steps
- Verification history
- Failure notes
- Current CLI/runtime capabilities

## Procedure

1. List repeated manual steps.
2. Exclude steps that still require judgment, unclear inputs, or unstable success criteria.
3. Choose the smallest automation candidate.
4. Define guardrails, dry-run behavior, and failure recovery.
5. Define exactly what state the automation may read and write.
6. Add automation only after the manual process is clear enough to test.

## Automation Gate

Do not automate when:

- the requirement is still disputed
- success criteria are not measurable
- failures are not recoverable
- the command would hide important judgment
- the automation would require large always-on context

## Output Contract

Return JSON only:

```json
{
  "manual_steps_observed": [],
  "stable_repetition": false,
  "automation_candidate": "",
  "command_to_create": "",
  "state_reads": [],
  "state_writes": [],
  "guardrails": [],
  "failure_recovery": [],
  "do_not_automate": [],
  "next_step": "execute|learn|stop"
}
```

## Failure Mode

If repetition is not stable, do not automate. Record the unstable parts and return to manual execution.
