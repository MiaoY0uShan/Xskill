# Mechanism Mapping

This project maps external agent-method ideas into Musk 5-Step skills by mechanism, not by repository.

| Musk step | Skill | Mechanisms absorbed |
| --- | --- | --- |
| Question | `question-requirements` | assumption surfacing, CEO/architect review, tradeoff forcing, measurable success criteria |
| Delete | `delete-scope` | v1/v2/out-of-scope separation, surgical file boundaries, semantic subtree filtering |
| Optimize | `optimize-path` | TDD/repro-first work, shortest verified implementation path, selective review lenses |
| Accelerate | `shorten-iteration` | fresh-context atomic tasks, wave planning, stop conditions, rollback planning |
| Automate | `automate-after-stable` | loop runner, hooks, state updates, indexing, verification automation |
| Support | `semantic-memory` | queryable semantic tree, extracted/inferred distinction, context compression |

## Non-goals

- Do not recreate a large multi-role agent organization.
- Do not keep all skills in the prompt at all times.
- Do not automate unstable judgment.
- Do not treat semantic memory as truth when it is inferred.
- Do not copy third-party prompt text.

## MVP success criteria

The MVP is successful if it can:

1. Install a small `.musk` runtime into an existing repo.
2. Add and track tasks.
3. Build a lightweight semantic tree.
4. Generate step-specific briefs.
5. Preserve progress and learnings across fresh contexts.
