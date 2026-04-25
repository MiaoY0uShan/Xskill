# Skill: shorten-iteration

Musk step: Accelerate cycle time.

## Trigger

Use when the implementation path has more than one meaningful step, touches multiple files, or risks context bloat.

## Goal

Split work into atomic iterations that can run in fresh contexts with clear verification and rollback.

## Inputs

- Optimized implementation path
- Relevant semantic nodes and files
- Current task queue
- Verification commands

## Procedure

1. Convert the plan into atomic tasks. Each task should fit one focused context window.
2. Give every atomic task one goal, one file set, and one verification method.
3. Group independent tasks into parallel groups only when they do not touch the same files or hidden shared state.
4. Define stop conditions for failure, uncertainty, and scope expansion.
5. Define rollback or revert strategy.
6. Recommend state updates after each iteration.

## Atomic Task Standard

A task is too large if it requires:

- more than one conceptual outcome
- unrelated files
- unverifiable intermediate state
- broad refactor plus feature work
- remembering unstated context from prior iterations

## Output Contract

Return JSON only:

```json
{
  "atomic_tasks": [
    {
      "id": "T001",
      "goal": "",
      "context_nodes": [],
      "files": [],
      "checks": [],
      "max_scope": ""
    }
  ],
  "parallel_groups": [],
  "stop_conditions": [],
  "rollback_plan": [],
  "state_updates": [],
  "next_step": "automate-after-stable|execute"
}
```

## Failure Mode

If the task cannot be split safely, mark it high-risk and require stronger verification before execution.
