# Changelog

## v0.2.3 — Proactive Xskill activation

- Made proactive activation the default behavior for non-trivial coding tasks.
- Downgraded `Xskill: <task>` to a manual override instead of the primary user interface.
- Updated `xskill/SKILL.md` and `xskill/AGENTS.md` with automatic trigger rules.
- Updated README, START_HERE, INSTALL, TEST_XSKILL, install packs, copy-paste fallback, and adapter-facing instructions.
- Kept Xskill portable: no CLI, npm, npx, pip, database, runtime, or automatic executor.

## v0.2.2 — Xskill router and Idea Cards

- Added top-level `xskill/SKILL.md` router.
- Changed the default user trigger to `Xskill: <task or idea>`.
- Added Idea Cards for vague user intent.
- Added `xskill/templates/idea-cards.md`.
- Added `xskill/examples/dumb-simple-install.idea-cards.md`.
- Added `docs/router.md`.
- Upgraded Context Budget Contract to support agent-estimated budgets with confidence and assumptions.
- Updated README, START_HERE, INSTALL, install packs, test instructions, adapter docs, and release checklist.
- Kept Xskill portable: no CLI, npm, npx, pip, database, runtime, or automatic executor.


## v0.2.1 — One zip per agent

- Added one-zip-per-agent release assets for Codex, Claude Code, Gemini CLI, and GitHub Copilot CLI.
- Added copy-paste fallback for unsupported agents.
- Added `TEST_XSKILL.md` for install verification.
- Added `dist/README.md` and `dist/xskill-copy-paste.md`.
- Simplified README around: pick agent → download one zip → unzip → say one sentence.
- Updated `START_HERE.md`, `INSTALL.md`, `install/README.md`, `docs/portable-install.md`, and `docs/release-checklist.md`.
- Kept Xskill portable: no CLI, npm, npx, pip, database, runtime, or automatic executor.

## v0.2.0 — Dumb-simple install

- Added `START_HERE.md` for the shortest possible install path.
- Added `INSTALL.md` with copy-only instructions for Codex, Claude Code, Gemini CLI, and GitHub Copilot CLI.
- Added `install/README.md` so release users can pick one folder and start.
- Simplified README around a 30-second start path.
- Moved complex protocol details lower in the README.
- Clarified the single usage sentence: `Use Xskill to compile this task before editing code: <task>`.
- Kept Xskill portable: no CLI, npm, npx, pip, database, runtime, or automatic executor.

## v0.1.11 — Self-use evidence case studies

- Added preliminary self-use evidence to README.
- Added five repository-maintenance case studies.
- Added docs/case-studies.md with token reduction method and results.
- Added case-study examples under examples/case-studies and xskill/examples/case-studies.
- Clarified that these are preliminary self-use cases, not an external 10-task benchmark.


## v0.1.11 — Agent-agnostic adapters

- Added ready-made install packs for Codex, Claude Code, Gemini CLI, and GitHub Copilot CLI.
- Moved the agent contract into `xskill/AGENTS.md` so users do not need to copy a separate root `AGENTS.md`.
- Added `adapters/` documentation.
- Added `docs/execution-protocol.md`.
- Added single-folder `xskill` skill packs for Codex and Claude Code.
- Added Gemini CLI extension pack.
- Added GitHub Copilot CLI custom agent pack.
- Kept Xskill portable: no Xskill CLI, npm, npx, pip, database, runtime, token tracker, graph engine, or automatic executor.


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
