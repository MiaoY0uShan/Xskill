# Migration

## v0.1.5 -> v0.1.6

Xskill's post-run layer changed:

- `semantic-memory` is replaced by `schema-memory`.
- `automate-after-stable` and `learn-after-run` are merged into `adaptive-improvement`.
- `evidence-ledger` is now an explicit skill.

If you installed a previous Xskill bundle, remove these old directories:

```text
xskill/automate-after-stable
xskill/learn-after-run
xskill/semantic-memory
```

Then copy the new `xskill/` folder from the release zip.

The new post-run loop is:

```text
evidence-ledger
→ adaptive-improvement
→ schema-memory
```

Xskill still has no CLI, npm, npx, pip, runtime, or database.
