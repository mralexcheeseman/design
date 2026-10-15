# AGENTS.md

The rules for Codex and other agents are the same as `CLAUDE.md`. In short:

1. Before creating anything for a brand, read `brands/<brand>/README.md`, use only tokens from `brands/<brand>/tokens.json`, reuse components from `brands/<brand>/components/`, and read `merch.md` and `decisions.md`.
2. Before finishing, run the applicable checklists in `checklists/` and report which ones you ran.
3. Token changes: edit `tokens.json`, run `node scripts/build-tokens.mjs`, commit both. Log every change in `CHANGELOG.md`.
