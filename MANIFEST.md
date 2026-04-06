# Repository Manifest

This repository is for general-purpose Codex skills only.

## Allowed

- skills useful in ordinary coding, debugging, planning, documentation, review, and cross-thread workflow
- official public skills that are not security-only
- local custom skills intended for broad reuse

## Not Allowed

- security-only skills
- offensive security workflows
- vulnerability triage or exploit-lab specific skills
- skills whose primary value depends on sensitive client or environment context

## Current Scope

- `self-improving-agent`
- `context-compressor`
- `repo-orient`
- `debug-triage`
- `change-safety`
- `handoff-brief`
- `task-planner`
- `pr-reviewer`
- `doc`
- `pdf`

## Validation Rule

Before pushing changes, run:

```bash
python tests/validate_skills.py
```

Only push if validation passes.
