# Test Xskill

Ask your agent normally:

```text
Rename one README section title without changing anything else.
```

Expected result:

The agent should activate Xskill and produce a **Compiled Execution Brief** before editing code.

Then test vague intent:

```text
I want this project to be easier for people to use.
```

Expected result:

The agent should produce **3 Idea Cards** and ask you to choose A, B, C, merge cards, or generate new cards.

Manual override:

```text
Xskill: Rename one README section title without changing anything else.
```
