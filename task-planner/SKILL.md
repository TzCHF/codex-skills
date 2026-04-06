---
name: task-planner
description: "Creates a compact execution plan before non-trivial work. Use when a task spans multiple files, has unclear sequencing, mixes investigation with implementation, or benefits from explicit milestones, assumptions, and validation steps."
metadata:
---

# Task Planner

Use this skill to turn a broad request into a short executable plan.

## Goals

- separate discovery, implementation, and validation
- make the critical path explicit
- prevent premature coding when scope is still unclear
- keep the plan short enough to remain useful

## Default Workflow

1. Restate the objective in one or two lines.
2. Identify blockers, assumptions, and unknowns.
3. Break the task into a few ordered steps.
4. Mark which step is on the critical path.
5. Define the narrowest useful validation.

## Plan Shape

Use a compact plan like:

```text
Objective:
Assumptions:
Steps:
Validation:
```

## Rules

- Prefer 3-5 steps, not long checklists.
- Keep only one step actively in progress at a time.
- If discovery may invalidate implementation, put discovery first.
- If the user asks for code, do not stop at planning; use the plan to execute.
- Update the plan when evidence changes the sequence.

## When Not To Use

- the task is tiny and the next step is obvious
- the user explicitly wants direct execution without planning overhead
