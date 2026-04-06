# codex-skills

Custom Codex skills maintained in a single backup repository.

## Skills

- `self-improving-agent`: Codex-adapted v0 based on an OpenClaw-oriented upstream repo
- `context-compressor`: Codex custom v0 for reducing context usage on noisy tasks
- `repo-orient`: Codex custom v0 for quick repository orientation
- `debug-triage`: Codex custom v0 for structured debugging before code changes
- `change-safety`: Codex custom v0 for lowering regression risk during edits
- `handoff-brief`: Codex custom v0 for compact cross-thread continuation notes
- `doc`: official OpenAI skill for `.docx` reading and editing workflows
- `security-best-practices`: official OpenAI skill for security-focused reviews and secure-by-default guidance

## Sources

- Official OpenAI downloads: `doc`, `security-best-practices`
- Referenced upstream and adapted: `self-improving-agent`
- Local custom Codex skills: `context-compressor`, `repo-orient`, `debug-triage`, `change-safety`, `handoff-brief`

## Notes

- These skills are stored locally under `~/.codex/skills/`
- Some skills may need a Codex restart before new threads reliably discover them
