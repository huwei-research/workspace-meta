---
name: research-orchestrator
description: Master entry point for the complete research lifecycle in 2026Projects. Use automatically for literature reading or search, research-direction work, manuscript checking, review, writing or revision, numerical experiment design or execution, result analysis, peer review, and multi-stage research tasks that must use the governed literature corpus and remain resumable.
---

# Research Orchestrator

Use the tested canonical contract at
`LiteratureLibrary/research-lit-harness/.agents/skills/research-orchestrator/SKILL.md`.

## Startup

1. Read workspace and project-local `AGENTS.md` files.
2. Read the canonical skill above and only the task-route reference it names.
3. Use `LiteratureLibrary/research-lit-harness` as the default governed corpus unless the project
   declares another source.
4. Run the corpus audit before a nontrivial mission.
5. Build and audit one full-corpus mission, then load only the next routed specialist skill.

The workspace entry point is intentionally thin. Authority, commands, coverage rules, additive
integration, stage transitions, failure behavior, and specialist routes live in the canonical
tested skill so the operational and open-source contracts do not drift.
