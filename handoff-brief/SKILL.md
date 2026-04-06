---
name: handoff-brief
description: "Creates a compact continuation brief for later turns, later threads, or another agent. Use when a task will continue later, when the user may resume work in another thread, when investigation is partially complete, or when a concise state handoff is more useful than a long recap."
metadata:
---

# Handoff Brief

Use this skill to preserve only the information needed to continue work later.

## Goals

- make continuation easy across turns or threads
- avoid replaying long histories
- preserve confirmed facts, open questions, and next actions
- keep the brief short enough to reuse directly

## Default Workflow

1. Capture the current objective.
2. List the files, modules, or systems that matter now.
3. Separate confirmed facts from unverified hypotheses.
4. State the next best action.
5. Drop stale investigation history that no longer affects the task.

## Brief Template

```text
Objective:
Relevant files:
Confirmed facts:
Open questions:
Next action:
```

## Rules

- Prefer facts over narrative.
- Keep only the active path, not every path explored.
- Name files and modules explicitly when they matter.
- If a hypothesis was disproven, omit it unless it prevents repeating work.
- If there is a blocker, state the blocker and the unblock path in one line.

## When To Emit

- before ending a thread
- after a long investigation
- before asking the user to continue later
- before switching to another major subtask

## When Not To Use

- the task is already complete
- the conversation is short and the state is obvious
