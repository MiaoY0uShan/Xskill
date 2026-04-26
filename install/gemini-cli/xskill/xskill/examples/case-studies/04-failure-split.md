# Case Study 4: Split failed password reset flow

## Task
A password-reset task becomes blocked because the mail adapter cannot be mocked cleanly.

## Xskill files loaded
- `xskill/AGENTS.md`
- `question-requirements/SKILL.md`
- `delete-scope/SKILL.md`
- `optimize-path/SKILL.md`
- `shorten-iteration/SKILL.md`
- `failure-to-smaller-task-protocol.md`
- `shorten-iteration-report.md`

## Metrics
- Baseline context: 19,562 estimated tokens
- Xskill context: 7,520 estimated tokens
- Reduction: 61.6%

## Failure split
```json
{
  "failed_task": "Add password reset flow",
  "failure_type": "coupling discovered",
  "root_cause": "mail adapter is not mockable",
  "smaller_tasks": [
    "Extract mail sender seam",
    "Add unit test for reset token generation",
    "Add endpoint after seam exists"
  ]
}
```

## Evidence required
- Failure reason is recorded.
- Smaller tasks each have focused checks.
- The original large task is not retried blindly.
