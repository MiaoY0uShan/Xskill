# Example Feature Request

Goal: Add password reset flow.

Constraints:

- Must not weaken auth security.
- Must be testable without sending real email.
- Must not require a new background job system in v1.

Suggested commands:

```bash
musk init
musk index
musk task add "Add password reset flow" --priority 5 --risk high --check "pytest"
musk next --step question-requirements
musk brief delete-scope --task "Add password reset flow"
musk brief optimize-path --task "Add password reset flow"
musk brief shorten-iteration --task "Add password reset flow"
```
