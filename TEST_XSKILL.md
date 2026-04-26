# Test Xskill

After installing Xskill, ask your agent a non-trivial but safe task:

```text
Rename one README section title without changing anything else.
```

Expected behavior:

```text
I’ll use Xskill to create a bounded Execution Brief before editing code.
```

The agent should produce a brief before editing.

Manual override, if the agent does not activate Xskill automatically:

```text
Xskill: Rename one README section title without changing anything else.
```

For vague ideas, test:

```text
I want this project to be easier for people to use.
```

Expected behavior:

```text
This idea is broad. I’ll use Xskill Idea Cards first.
```
