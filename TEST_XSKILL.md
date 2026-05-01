# Test Xskill

After installing Xskill, ask your agent a small safe task:

```text
Rename one README section title without changing anything else.
```

Expected behavior:

```text
Xskill small brief: task, read/touch, verify, result.
```

The agent should not produce a full Execution Brief for this small change unless risk appears.

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
This idea is broad. I will use Xskill Idea Cards first.
```
