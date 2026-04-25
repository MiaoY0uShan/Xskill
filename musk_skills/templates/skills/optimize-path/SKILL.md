# Skill: optimize-path

Musk step: Simplify and optimize after deletion.

## Trigger

Use when the minimum slice is known and you need an implementation path, test strategy, or review strategy.

## Goal

Select the shortest safe path from current state to verified success.

## Inputs

- Minimum slice from `delete-scope`
- Relevant files and semantic nodes
- Task risk level
- Available verification commands

## Procedure

1. Choose a test strategy: `none`, `smoke`, `unit`, `integration`, or `e2e`.
2. For high-risk logic, public APIs, bug fixes, auth, payment, data loss, or concurrency: require test-first or repro-first work.
3. For low-risk docs/config/copy changes: use direct edit plus acceptance check.
4. Propose the fewest implementation steps.
5. Attach a verification command or manual acceptance check to every step.
6. Select review lenses only if relevant: logic, security, data, performance, UX, release.
7. Disallow broad refactors unless they are necessary for the minimum slice.

## Output Contract

Return JSON only:

```json
{
  "test_strategy": "none|smoke|unit|integration|e2e",
  "implementation_path": [
    {"step": "", "verification": ""}
  ],
  "verification_commands": [],
  "review_lenses": [],
  "refactor_allowed": false,
  "risk_notes": [],
  "next_step": "shorten-iteration"
}
```

## Failure Mode

If no reliable verification exists, create the smallest verification first or emit a blocker.
