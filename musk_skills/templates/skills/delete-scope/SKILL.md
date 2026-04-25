# Skill: delete-scope

Musk step: Delete unnecessary parts and processes.

## Trigger

Use after the requirement has success criteria, or whenever a plan is growing in files, roles, prompts, dependencies, abstractions, or workflows.

## Goal

Produce the smallest useful slice and an explicit deletion/defer list.

## Inputs

- Validated goal and success criteria
- Current task or plan
- Relevant semantic nodes
- Project constraints and non-goals

## Procedure

1. Separate `must_have`, `nice_to_have`, `delete_now`, and `defer_to_v2`.
2. Remove anything not directly tied to success criteria.
3. Identify the smallest file set required.
4. Identify files and modules to avoid touching.
5. Reject speculative abstraction, generic framework work, and unrequested configurability.
6. Produce a minimum slice that can be verified independently.

## Deletion Tests

Ask these questions for every proposed item:

- Does it directly affect the current success criteria?
- Would failure to do it block verification?
- Is it needed now, or merely plausible later?
- Can it be replaced by a note, test, TODO, or follow-up task?

## Output Contract

Return JSON only:

```json
{
  "must_have": [],
  "nice_to_have": [],
  "delete_now": [],
  "defer_to_v2": [],
  "minimum_slice": "",
  "files_to_touch": [],
  "files_to_avoid": [],
  "removed_process": [],
  "next_step": "optimize-path"
}
```

## Failure Mode

If the task cannot be made smaller, state why and set `minimum_slice` to the smallest risky slice instead of expanding scope.
