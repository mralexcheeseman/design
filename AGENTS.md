# AGENTS.md

The rules for Codex and other agents are the same as `CLAUDE.md`. In short:

1. Before creating anything for a brand, read `brands/<brand>/README.md`, use only tokens from `brands/<brand>/tokens.json`, reuse components from `brands/<brand>/components/`, and read `merch.md` and `decisions.md`.
2. Before running any AI tool, read `learnings/README.md` and the matching playbooks; afterwards, add what you learned there the same day.
3. Before finishing, run the applicable checklists in `checklists/` and report which ones you ran.
4. Token or component changes: run `node scripts/build-tokens.mjs` and `node scripts/build-preview.mjs`, commit the generated files. Artwork masters are in `brands/<brand>/artwork/`. Log every change in `CHANGELOG.md`.
