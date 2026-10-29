# Changelog

Newest first. `## YYYY-MM-DD · brand · what changed`, then why.

## 2026-10-29 · off-duty-hotel-club · Gardener replaces Head Gardener
Alex chose the Gardener shirt for Villa Ceresa: `garment-garden-green` and `ink-geranium` replace `garment-lawn-green`, `ink-orange` and `ink-sage`. The back is GARDENER in Anton, one ink. The swan crest prints in geranium. Print files, renders and lifestyle mocks renamed to `gardener-*`.
Same day: the copy checklist's spelling list now includes Villa Ceresa and Gardener. New Gardener lifestyle shot and poster (storefront-kit `supply/instagram/`) checked against the product print.

## 2026-10-25 · off-duty-hotel-club · Head Gardener: brighter shirt, five-star crest
On Alex's notes: `garment-garden-green` became `garment-lawn-green` (#5a9e47), and two print inks were added, `ink-orange` for the job title and `ink-sage` for the hotel line and chest crest, making Head Gardener the one two-ink back, with its title stacked on two lines (`make_art.py` `stack=True`). The Villa Ceresa crest was redrawn without the spade and rake (swan before a loggia, cypresses, camellia, five stars). New artwork, crest and photography. Ran the crest-and-print, photography, page and copy checklists.

## 2026-10-23 · off-duty-hotel-club · Fifth hotel: Villa Ceresa, Head Gardener
Alex asked for a green Head Gardener shirt from a hotel in a picturesque part of Switzerland. Added Villa Ceresa (Lake Lugano, est. 1911, department 05): `hotel-ceresa` ink, `garment-garden-green`, the heritage crest (generated in the set's style with the four existing crests as reference, then traced by `trace_heritage.py`, which now also takes single-crest images), the back print from `make_art.py`, and `render_print.py`, which makes the 300 dpi and worn-ink PNGs. Copy that counted four hotels now says five. Ran the crest-and-print, photography, page and copy checklists.

## 2026-10-21 · edgework · Manila tokens and button arrows
Added `manila` and `manila-ink` for the essay folders on the new Edgework site, and allowed "→" inside buttons, matching what the site does. Ran the page and copy checklists against the site.

## 2026-10-21 · edgework · First version
New brand folder for Alex's public writing identity, Edgework (after Hunter S. Thompson). Holds the photographic mark library and TT2020 fonts as the master copy, tokens for the paper and night grounds, specs for the masthead, index card, file card, dispatch, Hey Rube band, marks, typed text, scrawl and button, and the settled decisions. Used by the private Owl Farm newsroom and the new public Edgework site. `build-preview.mjs` now reads an optional `meta.preview` block so a brand can name its own display and label styles; Off Duty Hotel Club's view is unchanged.

## 2026-10-15 · off-duty-hotel-club · Artwork and a one-page view
Added the crest source sheet, explorations, traced masters and scripts (`artwork/crests/`), every supplier print file (`artwork/print-files/`) and the original product renders (`assets/photography/source/`), copied from storefront-kit `supply/`. This repo is now the master copy of the artwork. Added `index.html`, a generated one-page view of colours, type, crests and components, checked in CI.

## 2026-10-15 · off-duty-hotel-club · Known drift cleared
storefront-kit#3 brings the live store in line with this system, so the drift list in the brand README is now empty.

## 2026-10-15 · off-duty-hotel-club · First version in GitHub
Brought in from the Design System artifact (version 1, captured from the Base44 storefront with the agreed improvements). Added in version 2 of `tokens.json`: motion, focus, breakpoint, layout, ratio, z-index and print tokens, plus phone sizes for display, headline, title and wordmark. Added `tokens.css` and its build script, specs for the storefront components the system didn't cover yet, `merch.md`, `decisions.md` and shared review checklists. Crest assets are the traced heritage vectors from storefront-kit, recoloured to each hotel's ink.
