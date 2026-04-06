---
name: pr-reviewer
description: "Reviews code changes with a bug-and-risk-first mindset. Use when reviewing a pull request, diff, patch, or recent code change and the goal is to identify defects, regressions, missing tests, or risky assumptions rather than provide general praise."
metadata:
---

# PR Reviewer

Use this skill to review changes for correctness and risk.

## Goals

- find real bugs and regressions
- prioritize findings by severity
- distinguish proven issues from assumptions
- keep summaries short after findings

## Default Workflow

1. Determine the intended behavior change.
2. Inspect the changed files and affected boundaries.
3. Look for correctness issues, regressions, and missing validation.
4. Record findings in severity order.
5. Note open questions and residual risk briefly.

## Review Lens

Check for:

- broken control flow
- incorrect assumptions about data shape or state
- missing edge case handling
- caller compatibility issues
- config or default behavior regressions
- test gaps for newly risky paths

## Output Shape

Prefer:

```text
Findings:
- ...

Open questions:
- ...

Residual risk:
- ...
```

## Rules

- Findings come before summary.
- Prefer concrete file-and-line backed issues over vague concerns.
- Do not invent problems when evidence is weak; mark them as questions instead.
- If no findings are found, say so explicitly and mention any remaining test gap.

## When Not To Use

- the task is implementation, not review
- there is no meaningful code change to inspect
