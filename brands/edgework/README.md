# Edgework

Alex Cheeseman's public writing identity, after Hunter S. Thompson: the manuscript filed at 4am, red ink, no apologies. Two places use it. The private newsroom **Owl Farm** (Base44) is where ideas get collected and drafted. The public **Edgework site** (Base44) is where the Positions, the Last Animal essays and published Dispatches live. Every social card and reel exported from Owl Farm uses this system too.

The look is photographic, not illustrated. Every stain, highlight, tape strip and pen mark is a real scan from `assets/marks/`. That realism is the brand, so a flat or stock version of any mark is off-brand.

## Content fundamentals

- **Voice: first person, plain, a little dangerous.** Short declaratives. Say the thing, then stop. "Brands were built on human irrationality. The agent is more rational than you."
- **One argument per piece,** with a clear enemy, a reason it matters now, and one line people would repeat. That line is the `pull`, and its key phrase is the one highlighted phrase.
- **UK English.** No em dashes in body copy. Never the "Not X, but Y" construction.
- **Labels speak like a filing system:** "FILE 014", "FILED 04:12", "No. 07". They are the only place capitals come from, apart from Anton headlines.
- **Scrawls are asides,** lower case, five words at most: "read that twice.", "argue with me."
- **Never invent:** dates, read times, venues, clients or results. Essay titles and excerpts are quoted exactly from The Last Animal.
- No emoji, no exclamation marks.

## Visual foundations

**Colour.** Two grounds: `paper` (always with the paper scan) and `night` (the 4am black). Text is `ink` on paper and `on-night` on night. Red pen is the only accent: `red` on paper, `red-night` on night. `coffee` exists only inside the stain scans. A page frames itself in night (masthead and footer) and may have one more night band (HeyRube).

**Typography.** Four families, each with one job:
- `shout` (Anton) for headlines: uppercase. At `shout` and `shout-xl` sizes it always carries the letterpress mask (`.ew-lp`), so it reads as inked type rather than a font. `shout-sm` goes without it, because the mask breaks small letters up.
- `type` (TT2020 Style G, self-hosted) for anything read as writing: Positions, decks, dispatch bodies. Words jitter (TypedText).
- `label` (Courier Prime 700) for navigation, file numbers, dates and buttons, uppercase and tracked.
- `scrawl` (Rock Salt) for one red-pen aside per card or section.

"HEY RUBE." is never typeset: it is the letterpress scan (or the rubber stamp on paper). Nothing is set below 12px.

**Layout.** A desk, not a grid of boxes. Sheets and cards sit on the paper with `shadow-sheet`, tilted a little (±2.5°, ±1° on phones), and overlap only at their edges. Long reading is a single sheet at `measure`. Sections are separated by space (`space-8`, `space-7` on phones), not rules.

**Marks.** 1–2 stains per card, 3–4 per hero, chosen by seed so a card always looks the same. Stains bleed off edges and never cover a headline or the highlighted phrase. Tape sits on corners and the top edge. See [Marks](components/Marks/README.md).

**Motion.** Paper physics: cards lift on hover, manuscripts slide out of folders, headlines type themselves on once. Landings may overshoot (`ease-drop`); nothing else bounces. Stains never move. `prefers-reduced-motion` turns all of it off.

**Corners and shadows.** Square corners everywhere. Only paper casts shadows.

## Iconography

There are no icons. Arrows, circles and underlines are red-pen scans (`pen-*.webp`). The only glyph allowed is "↗" after a link that leaves the site.

## Patterns to avoid

Stock grunge textures, CSS-drawn stains, a flat yellow highlight, rounded cards, glassmorphism, gradients, emoji, more than one highlighted phrase per card, conviction scores as stars or numbers, and "HEY RUBE" in a font.

## Known drift

- **Owl Farm** (private newsroom) uses the same values under `--ew-*` names in `src/edgework.css` rather than `tokens.css`. That is acceptable while it is private; port it to these token names when it is next touched.
- **Owl Farm** sets the masthead with "OWL FARM", not "EDGEWORK", because it is the newsroom, not the publication. This is deliberate (see decisions).

## Files in this system

- `tokens.json` (source) and `tokens.css` (generated): colours, type, spacing, motion, layout.
- `components/`: component specs and `bundle.css`.
- `assets/marks/`: the mark library (master copy). `assets/fonts/`: TT2020 (SIL OFL, see `assets/fonts/OFL.txt`).
- `decisions.md`, `merch.md`, `index.html` (generated one-page view).
