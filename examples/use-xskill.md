# Example: Using Xskill

## Goal

Use Xskill to compile a vague coding task into one bounded Execution Brief.

## User prompt

```text
Use Xskill to compile this task into an Execution Brief before editing code:
Fix password reset bug.
```

## Expected agent behavior

The agent should not edit code immediately.

It should run the Xskill gates:

```text
question-requirements
→ delete-scope
→ semantic-architecture if needed
→ optimize-path
→ shorten-iteration if needed
→ compiled execution brief
```

## Final output

The final output should be a short brief, not a long planning essay.

It should include:

```text
Task
Real Goal
MVP Scope
Must Not Do
Files To Read
Files To Touch
Files To Avoid
Context Budget
Selected Path
TDD Micro-Loops
Checks
Evidence Required
Stop Condition
```

## Execution

After producing the brief, the agent may execute only within the brief.

If the agent needs to exceed the brief, it must stop and create a new narrower brief.

## After execution

The agent should create an Evidence Ledger:

```text
files touched
commands run
verified claims
unverified claims
scope violations
remaining risk
```

If the run produced reusable evidence, the agent may create an Adaptive Improvement Report or Schema Memory Card.

Do not update skills from one run.
