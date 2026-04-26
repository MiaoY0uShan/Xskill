# Contracts Layer

Xskill's core differentiator is not a longer prompt. It is a set of execution contracts.

## 1. Context Budget Contract

Defines what the agent may read, touch, and assume.

Key fields:

```text
max_files_to_read
max_files_to_touch
max_skill_tokens
max_execution_notes
required_semantic_nodes
required_schema_cards
forbidden_context
scope_boundary
violation_handling
```

If the contract is exceeded, the agent must stop and split or request a revised contract.

## 2. Evidence Ledger

Every agent claim needs evidence.

The ledger records:

```text
files_read
files_touched
commands_run
verified_claims
unverified_claims
scope_violations
context_budget_violations
next_action
```

## 3. Failure-to-Smaller-Task Protocol

Failure is not a reason to retry the same task.

A failed run should produce smaller verified tasks with their own budgets and checks.

## 4. Context Diet Map

This is not generic memory.

It decides what context to exclude.

```text
relevant_nodes
irrelevant_nodes
files_to_read
files_to_avoid
reason
```

Other systems use memory to add context. Xskill uses memory to remove context.
