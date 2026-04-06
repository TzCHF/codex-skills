---
name: repo-orient
description: "Quickly orients within an unfamiliar repository before implementation or debugging. Use when starting work in a new codebase, when the user asks where something lives, when a bug could be in multiple modules, or when you need a minimal map of entrypoints, config, tests, and likely change locations."
metadata:
---

# Repo Orient

Use this skill to build a minimal working map of a repository before going deeper.

## Goals

- identify the active app or package quickly
- find likely entrypoints, configs, and test locations
- avoid reading large amounts of code before the failing path is known
- produce a short repo brief that can be reused in later steps

## Default Workflow

1. Identify the repo root and top-level structure.
2. Detect the primary language, framework, and package manager.
3. Find likely entrypoints, configs, and task runners.
4. Find relevant tests, scripts, and docs.
5. Summarize the repo in 3-5 lines before making changes.

## What To Look For

- root manifests such as `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`
- framework configs
- app entrypoints
- test directories and test commands
- build, lint, and typecheck commands
- environment or deployment files

## Output Brief

Use a compact brief like this:

```text
Stack:
Entrypoint(s):
Relevant modules:
Validation path:
Notes:
```

## Rules

- Prefer top-level manifests and config files before implementation files.
- Prefer filename search and symbol search over broad recursive reading.
- Only read module internals after identifying a plausible change path.
- If there are multiple apps or packages, name the active one explicitly.
- If the repo is monorepo-shaped, identify the owning package before debugging.

## When Not To Use

- the repo is already familiar and the target file is known
- the user only wants a tiny localized edit with a precise file path
