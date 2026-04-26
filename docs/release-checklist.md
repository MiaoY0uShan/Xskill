# Release Checklist

## v0.1.7 — Compiled Execution Brief

Before release:

- [ ] README states that Xskill is a portable task compiler.
- [ ] README states that the primary output is a compiled Execution Brief.
- [ ] `AGENTS.md` routes agents toward producing a brief before editing code.
- [ ] `xskill/optimize-path/SKILL.md` compiles upstream reports into the final brief.
- [ ] `xskill/templates/compiled-execution-brief.md` exists.
- [ ] `xskill/templates/execution-brief.md` includes real goal, MVP scope, module boundaries, context budget, files to read/touch/avoid, checks, evidence, and stop condition.
- [ ] `xskill/examples/password-reset.compiled-execution-brief.json` exists.
- [ ] Release bundle contains `README.md`, `AGENTS.md`, `LICENSE`, and `xskill/`.
- [ ] No CLI, npm, npx, pip, runtime, database, or graph engine is introduced.

Suggested release title:

```text
v0.1.7 — Compiled Execution Brief
```

Suggested release note:

```text
- Clarified Xskill as a portable task compiler, not a prompt pack
- Made the compiled Execution Brief the primary output
- Upgraded optimize-path to compile upstream Xskill outputs into the final brief
- Added compiled-execution-brief template
- Added password-reset compiled execution brief JSON example
- Updated README, AGENTS.md, xskill README, design docs, examples, and validation
- Kept Xskill portable: no CLI, runtime, npm, npx, pip, database, graph engine, or automatic executor
```


## v0.1.8 metrics checks

- [ ] `xskill/metrics/SKILL.md` exists.
- [ ] `xskill/templates/metrics-report.md` exists.
- [ ] `xskill/examples/password-reset.metrics-report.md` exists.
- [ ] `docs/metrics.md` exists.
- [ ] README explains TVP and proxy TVP.
- [ ] AGENTS.md says metrics must come from evidence.
