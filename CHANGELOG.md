# Changelog

## v0.1.9 — Contracts layer

- Added Context Budget Contract template and JSON contract.
- Added Context Diet Map template and example.
- Added Failure-to-Smaller-Task Protocol template and example.
- Added JSON Evidence Ledger audit example.
- Upgraded the compiled Execution Brief to include contract, diet map, failure protocol, and evidence handoff.
- Updated README, AGENTS.md, xskill README, design docs, metrics docs, and validation.
- Kept Xskill portable: no CLI, runtime, database, npm, npx, pip, token tracker, graph engine, or automatic executor.

## v0.1.8 — Metrics layer

- Added `metrics` skill.
- Added `metrics-report.md` template.
- Added `password-reset.metrics-report.md` example.
- Added `docs/metrics.md`.
- Defined TVP: `total_context_tokens / verified_tasks_completed`.
- Added proxy TVP for portable runs without exact token counts.
- Added supporting metrics: Scope Creep Rate, Verification Rate, Rework Rate, Context Load Size, and Iteration Half-life.
- Updated evidence-ledger and adaptive-improvement to use metrics as an evidence-backed handoff.
- Updated compiled Execution Brief to include metrics to record.
- Kept Xskill portable: no CLI, runtime, database, npm, npx, pip, token tracker, or automatic benchmark runner.

## v0.1.7 — Compiled Execution Brief

- Clarified that Xskill is a portable task compiler, not a prompt pack.
- Made the compiled Execution Brief the primary output of the workflow.
- Upgraded `optimize-path` to compile upstream Xskill outputs into the final brief.
- Added `compiled-execution-brief.md` template.
- Strengthened `execution-brief.md` with real goal, MVP scope, module boundaries, files to read/touch/avoid, TDD micro-loops, checks, and evidence requirements.
- Added `password-reset.compiled-execution-brief.json` example.
- Updated README, AGENTS.md, xskill README, design docs, usage example, release checklist, and validation workflow.
- Kept Xskill portable: no CLI, runtime, npm, npx, pip, database, graph engine, or automatic executor.

## v0.1.6 — Schema memory and adaptive improvement

- Replaced semantic-memory with schema-memory.
- Merged automate-after-stable and learn-after-run into adaptive-improvement.
- Added evidence-ledger skill.
- Added schema memory cards.
- Added adaptive improvement reports.
- Added automation candidate template.
- Added evidence-based promotion rules.
- Clarified that Xskill learns from evidence, not confidence.

## v0.1.5 — Small-batch optimize path

- Upgraded optimize-path with small-batch quick response, agile working increments, lean waste removal, and minimal safety buffers.
- Upgraded shorten-iteration to split large or failed selected paths into TDD micro-loops.

## v0.1.4 — First-principles scope deletion

- Upgraded delete-scope with first-principles reasoning and Occam's Razor.
- Added MVP nucleus output.

## v0.1.3 — Semantic architecture sketch

- Added semantic-architecture skill.

## v0.1.2 — Five Whys requirement challenge

- Upgraded question-requirements with Five Whys and inversion thinking.

## v0.1.1 — Self-iteration layer

- Added learn-after-run skill and iteration learning note template.

## v0.1.0 — Portable skill bundle

- Initial portable release.
