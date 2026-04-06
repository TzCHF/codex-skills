# codex-skills

Custom Codex skills maintained in a single backup repository.

Security-only skills are maintained separately in `codex-security-skills`.

## Skills

- `self-improving-agent`: Codex-adapted v0 based on an OpenClaw-oriented upstream repo
- `context-compressor`: Codex custom v0 for reducing context usage on noisy tasks
- `repo-orient`: Codex custom v0 for quick repository orientation
- `debug-triage`: Codex custom v0 for structured debugging before code changes
- `change-safety`: Codex custom v0 for lowering regression risk during edits
- `handoff-brief`: Codex custom v0 for compact cross-thread continuation notes
- `doc`: official OpenAI skill for `.docx` reading and editing workflows
- `pdf`: official OpenAI skill for PDF workflows
- `task-planner`: Codex custom v0 for compact execution planning
- `pr-reviewer`: Codex custom v0 for bug-and-risk-first review

## Sources

- Official OpenAI downloads: `doc`, `pdf`
- Referenced upstream and adapted: `self-improving-agent`
- Local custom Codex skills: `context-compressor`, `repo-orient`, `debug-triage`, `change-safety`, `handoff-brief`, `task-planner`, `pr-reviewer`

## Notes

- These skills are stored locally under `~/.codex/skills/`
- Some skills may need a Codex restart before new threads reliably discover them
