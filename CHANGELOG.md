# Changelog

Newest first. `## YYYY-MM-DD · brand · what changed`, then why.

## 2026-10-16 · postmark · First version
New brand: phone straps from four destinations. Tokens (envelope paper, navy ink, airmail red, four destination inks, Newsreader, Manrope and Barlow Condensed), the postmark family (full and ring versions, outlined, black print masters and the script that draws them), merch, decisions and component notes. Built alongside the store in one session.

## 2026-10-16 · all · Template for new brands
`brands/_template/` holds the README, decisions, merch and components skeleton. `build-preview.mjs` now shows a brand's postmarks as well as crests.

## 2026-10-15 · off-duty-hotel-club · Artwork and a one-page view
Added the crest source sheet, explorations, traced masters and scripts (`artwork/crests/`), every supplier print file (`artwork/print-files/`) and the original product renders (`assets/photography/source/`), copied from storefront-kit `supply/`. This repo is now the master copy of the artwork. Added `index.html`, a generated one-page view of colours, type, crests and components, checked in CI.

## 2026-10-15 · off-duty-hotel-club · Known drift cleared
storefront-kit#3 brings the live store in line with this system, so the drift list in the brand README is now empty.

## 2026-10-15 · off-duty-hotel-club · First version in GitHub
Brought in from the Design System artifact (version 1, captured from the Base44 storefront with the agreed improvements). Added in version 2 of `tokens.json`: motion, focus, breakpoint, layout, ratio, z-index and print tokens, plus phone sizes for display, headline, title and wordmark. Added `tokens.css` and its build script, specs for the storefront components the system didn't cover yet, `merch.md`, `decisions.md` and shared review checklists. Crest assets are the traced heritage vectors from storefront-kit, recoloured to each hotel's ink.
