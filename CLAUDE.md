# design

Also see AGENTS.md (same rules, for Codex and other agents).

This repo holds the design system for each brand. Anything you create for a brand (a page, a component, copy, a product image, a crest, a print file, a social post, an email) must follow that brand's system here.

## Before you create anything

1. Read `brands/<brand>/README.md` in full: voice, colour, type, layout, photography, iconography, patterns to avoid.
2. Use only values from `brands/<brand>/tokens.json`. If you need a value that isn't a token, stop and add the token (with a usage note) rather than hard-coding it.
3. Use an existing component from `brands/<brand>/components/` when one fits, and follow its README. If none fits, write the component's README (what the consumer provides, rules, what never to do) before building it.
4. For physical products read `brands/<brand>/merch.md`. Check `brands/<brand>/decisions.md` so you don't reopen a settled choice.

## Before you call it done

Run the checklists in `checklists/` that apply (page, copy, photography, crest and print) and say in your summary which ones you ran. A failed item is fixed, or written in `decisions.md` as a deliberate exception with the reason.

## Changing the system

- Token or component changes: edit `tokens.json` or `components/`, run `node scripts/build-tokens.mjs` and `node scripts/build-preview.mjs`, commit the generated files too. CI fails if `tokens.css` or `index.html` is stale.
- Artwork (crests, print files) lives in `brands/<brand>/artwork/` and is the master copy. Change it here first.
- Every change gets a dated line in `CHANGELOG.md`. Settled choices go in `decisions.md`.
- Keep the Design System artifact (link in README.md) in step: when you change this repo, update it, or say in your summary that it needs updating.
- Brand-specific copy and assets stay in that brand's folder.
