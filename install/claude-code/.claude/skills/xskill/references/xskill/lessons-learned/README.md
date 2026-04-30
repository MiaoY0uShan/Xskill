# Xskill: Lessons Learned (Anti-Pattern Memory)

This directory stores project-specific anti-patterns, traps, and hard-won lessons to prevent the AI from repeating mistakes.

## Workflow

1.  **Search:** Before starting any task, the agent must search this directory.
2.  **Apply:** If a relevant lesson is found, it must be listed in the `Execution Brief` under a new `Lessons Applied` section.
3.  **Record:** If a task fails or an error is discovered during verification, create a new "Lesson Card" here.

## Lesson Card Template

File: `xskill/lessons-learned/LXXX-<short-name>.md`

```md
# Lesson: <Descriptive Title>

## Context
When trying to <action> in <environment/module>.

## Anti-Pattern (The Trap)
<What the agent usually does wrong>

## Correction (The Fix)
<What the agent should do instead>

## Evidence
<Link to failed task or error message>
```

## Initial Lessons

- (Add your first lesson here after the next failure!)
