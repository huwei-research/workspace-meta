# Upgrade Guide

## From v0.1 or v0.2

Back up the old skill and install this integrated v1.0 release:

```bash
cd /path/to/your-paper-project
mkdir -p .agents/skills
if [ -d .agents/skills/math-paper-writer ]; then
  mv .agents/skills/math-paper-writer .agents/skills/math-paper-writer.backup
fi
unzip math-paper-writer-skill-v1.0-integrated.zip -d .agents/skills
test -f .agents/skills/math-paper-writer/SKILL.md
```

Version 1.0 no longer organizes the skill as a page-by-page coverage matrix. The content has been internalized into `SKILL.md`, task playbooks, reference protocols, templates, scripts, and eval cases.

## After upgrading

Run one proof audit and one introduction review before using the skill for full-manuscript editing. This confirms that Codex loads the new integrated protocols.
