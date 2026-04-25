# Skill: semantic-memory

Support skill: use a semantic tree as a map, not as always-on context.

## Trigger

Use before searching a large repository, after meaningful changes, or when a task needs architectural orientation.

## Goal

Retrieve the smallest relevant semantic subtree and keep long-term project memory outside the prompt.

## Inputs

- `.musk/state/semantic_tree.json`
- Task text
- Recently changed files
- Progress and decision logs

## Procedure

1. Query semantic nodes by task terms, tags, paths, and risk.
2. Prefer extracted relationships over inferred relationships.
3. Treat inferred relationships as hypotheses, not facts.
4. Read only files linked to relevant nodes unless evidence says more context is needed.
5. After changes, update or rebuild the semantic tree.
6. Record learnings that should affect future retrieval or execution.

## Output Contract

Return JSON only:

```json
{
  "relevant_nodes": [],
  "relationships_used": [],
  "files_to_read": [],
  "files_to_ignore": [],
  "confidence": "low|medium|high",
  "memory_update_needed": false,
  "next_step": "question-requirements|delete-scope|execute"
}
```

## Failure Mode

If the semantic tree is stale or empty, run `musk index` before using repository-wide context.
