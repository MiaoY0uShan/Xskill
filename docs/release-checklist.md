# Release Checklist

## v0.1.6 — Schema memory and adaptive improvement

Before release:

- [ ] Confirm no CLI, npm, npx, pip, Python package, runtime, database, or automatic self-modifying engine is introduced.
- [ ] Confirm `adaptive-improvement/SKILL.md` exists.
- [ ] Confirm `schema-memory/SKILL.md` exists.
- [ ] Confirm `evidence-ledger/SKILL.md` exists.
- [ ] Confirm old `automate-after-stable`, `learn-after-run`, and `semantic-memory` directories are removed.
- [ ] Confirm templates exist:
  - `adaptive-improvement-report.md`
  - `schema-memory-card.md`
  - `automation-candidate.md`
  - `evidence-ledger.md`
- [ ] Confirm examples exist:
  - `password-reset.adaptive-improvement.md`
  - `validation-bug.schema-memory-card.md`
  - `validation-bug.automation-candidate.md`
- [ ] Confirm README and AGENTS.md describe the adaptive improvement loop.

Release title:

```text
v0.1.6 — Schema memory and adaptive improvement
```

Release note:

```text
- Replaced semantic-memory with schema-memory
- Merged automate-after-stable and learn-after-run into adaptive-improvement
- Added evidence-ledger skill
- Added schema memory cards
- Added adaptive improvement reports
- Added automation candidate template
- Added evidence-based promotion rules
- Clarified that Xskill learns from evidence, not confidence
- Kept Xskill portable: no CLI, runtime, database, npm, npx, pip, or automatic self-modifying engine
```
