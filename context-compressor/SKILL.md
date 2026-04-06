---
name: context-compressor
description: "Reduces token usage for coding and research tasks by compressing context before deeper work. Use when the task includes long logs, large files, broad codebases, repeated background, or multi-step debugging where only a small subset of context is actually relevant. Also use when the user explicitly asks to save tokens, summarize first, minimize context, audit what is consuming context, or create a short brief before deeper analysis."
metadata:
---

# Context Compressor

Use this skill to keep context small without losing important information.

## Goals

- avoid reading more files than necessary
- avoid pasting large logs or repeated summaries into the working context
- turn long inputs into short working notes before deeper analysis
- preserve only facts that affect the next decision
- create a short reusable brief when the task may span multiple steps

## Default Workflow

1. Restate the task in one or two lines.
2. Identify the minimum information needed to make the next decision.
3. Read only the smallest relevant slice of files, logs, or docs.
4. Convert findings into a short working summary.
5. Expand context only if the current summary is insufficient.

## Priority Levers

Apply these in order:

1. Lazy load context instead of front-loading it.
2. Produce a brief before broad analysis.
3. Replace repeated explanation with stable shorthand.
4. Prefer deterministic commands and targeted searches over open-ended exploration.
5. Reuse prior summaries until they are proven incomplete.

## Rules

- Prefer targeted search over broad file reads.
- Prefer line ranges over whole-file reads.
- Prefer summaries over verbatim output.
- Prefer one relevant trace over multiple similar traces.
- Do not re-read the same background unless something changed.
- If a command output is long, keep only errors, warnings, counts, paths, and decisive lines.
- If a file is large, extract the relevant function, type, config block, or interface first.
- If the user already gave stable constraints, do not repeat them back in full.
- If a task is repetitive and narrow, use a fixed workflow instead of re-deriving the process each time.

## Context Audit

When a task feels expensive, quickly classify what is consuming context:

- user requirements that truly constrain the work
- active files that directly affect the change
- noise: repeated history, stale hypotheses, duplicate logs, broad docs
- optional background that can wait

If useful, report the audit in one line:

```text
Need now: X | Can defer: Y | Ignore: Z
```

## File Strategy

- Start with filename search, symbol search, or error-string search.
- Read the entrypoint, failing path, or narrowest matching file first.
- Only open adjacent files when the first file is insufficient.
- For config-heavy repos, inspect the active config before reading implementation details.
- For unfamiliar repos, create a 3-5 line repo brief before opening more files.

## Log Strategy

When logs are long, reduce them to:

- failing command
- error message
- first relevant stack frame
- affected file or module
- one likely cause
- one next action

If multiple log blocks say the same thing, keep only the first representative block.

## Response Strategy

- Give short intermediate updates.
- Keep summaries incremental rather than restating the entire situation.
- In final answers, report outcome, files changed, and remaining risk without replaying the whole investigation.
- When the task is likely to continue across turns, keep a compact running brief and update it instead of regenerating a full recap.

## Escalation Rule

Only expand the context window when one of these is true:

- the current evidence is contradictory
- the first hypothesis failed
- multiple modules could plausibly own the bug
- the user explicitly asks for a thorough walkthrough

## Compression Template

Use this internal template when the task is noisy:

```text
Task:
Relevant scope:
Current evidence:
Known constraints:
Next check:
```

## Brief Template

Use this when the task may branch or continue for a while:

```text
Objective:
Relevant files/modules:
Confirmed facts:
Open question:
Next action:
```

## Anti-Patterns

- reading whole repositories up front
- quoting long command outputs unnecessarily
- repeating the same plan after each tool call
- carrying obsolete hypotheses forward after disproof
- mixing useful evidence with background narration
- opening multiple near-duplicate files before proving the first one is insufficient
- expanding into architecture discussion before confirming the failing path

## When Not To Use

Do not force compression when:

- the task is already tiny
- the user explicitly wants a deep walkthrough
- exact wording from a source is required
- the problem depends on broad architectural context that is genuinely necessary
