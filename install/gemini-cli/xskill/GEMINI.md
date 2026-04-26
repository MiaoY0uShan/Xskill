# Xskill for Gemini CLI

Use Xskill as an execution discipline layer before non-trivial coding work.

Primary protocol:

```text
user task
→ question-requirements
→ delete-scope
→ semantic-architecture, when needed
→ optimize-path
→ shorten-iteration, when needed
→ compiled execution brief
→ bounded execution
→ evidence-ledger
→ metrics, when measurement matters
→ adaptive-improvement
→ schema-memory
```

Detailed modules and templates are bundled in `xskill/` inside this extension.

When the user says "Use Xskill", read only the relevant files under `xskill/` and produce a Compiled Execution Brief before editing code.

Hard rules:

- Respect the Context Budget Contract.
- Use the Context Diet Map to decide what not to read.
- Do not claim completion without an Evidence Ledger.
- If the task fails or exceeds budget, produce a Failure-to-Smaller-Task Protocol.
- Xskill learns from evidence, not confidence.
