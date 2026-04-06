---
name: change-safety
description: "Reduces regression risk when editing code. Use before non-trivial changes, when touching shared modules, when tests are sparse, when interfaces may affect multiple callers, or when the user wants safe, reviewable edits with minimal blast radius."
metadata:
---

# Change Safety

Use this skill to keep changes narrow, verifiable, and low-risk.

## Goals

- minimize blast radius
- identify likely dependents before editing
- preserve existing behavior unless change is intentional
- validate the narrowest useful slice after editing

## Default Workflow

1. Define the exact intended behavior change.
2. Identify callers, configs, and tests likely affected.
3. Prefer the smallest change that satisfies the requirement.
4. Add or update validation where the risk is highest.
5. Verify the narrowest relevant path after the edit.

## Risk Checks

- shared utility or leaf module?
- public interface or internal helper?
- config default or explicit opt-in?
- data shape or rendering only?
- single caller or many callers?

## Rules

- Avoid opportunistic refactors during bug fixes.
- Keep unrelated cleanup out of the patch unless it is required.
- If a function has many callers, prefer compatibility-preserving changes.
- If behavior changes intentionally, state that clearly in the final summary.
- Validate the changed path even if full test coverage is unavailable.

## Safety Note

Use a short note like:

```text
Target behavior:
Likely dependents:
Blast radius:
Validation plan:
```

## When Not To Use

- the task is purely exploratory
- no code or config changes are being made
