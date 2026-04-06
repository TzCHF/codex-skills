---
name: debug-triage
description: "Structures debugging before code changes. Use when a command fails, a test breaks, an error message is unclear, a bug could have multiple causes, or the user wants root-cause analysis instead of guess-and-check edits."
metadata:
---

# Debug Triage

Use this skill to narrow bugs before editing code.

## Goals

- classify the failure quickly
- separate symptoms from likely causes
- identify the next decisive check
- avoid speculative changes before evidence exists

## Default Workflow

1. Capture the exact failing command, test, or user-visible symptom.
2. Extract the shortest useful error evidence.
3. Classify the failure type.
4. Identify the module or boundary most likely to own the bug.
5. Run the next check that can disprove the leading hypothesis.

## Failure Types

- environment or dependency issue
- config mismatch
- interface or type mismatch
- logic bug
- state or data bug
- integration boundary failure
- flaky or timing-sensitive failure

## Triage Note

Keep an internal note like:

```text
Symptom:
Best evidence:
Leading hypothesis:
Competing hypothesis:
Next decisive check:
```

## Rules

- Do not patch first and investigate later.
- Preserve the exact error message if it determines the next step.
- Prefer one decisive reproduction over multiple partial reproductions.
- If a hypothesis fails, replace it; do not carry it forward by inertia.
- Stop broad exploration once one module clearly owns the failure.

## When Not To Use

- the bug and fix are already obvious
- the user only wants a mechanical refactor
