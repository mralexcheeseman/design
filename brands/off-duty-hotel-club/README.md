Staff-issue T-shirts from four fictional hotels: a small crest on the front, a proper job title on the back. The store should feel like the private stationery of a very good hotel. Use warm paper, black ink and engraved crests, and keep it quiet enough for the shirts and their wit to carry it.

## Content fundamentals

- **Voice: dry, deadpan, a little conspiratorial.** Speak as the club, using "we" and "you". Real lines to match: "Wish you worked here." "Excellent hotels. Questionable employees." "Find your hotel. Choose your role. Take the rest of the day off."
- **Say less.** Use one strong line per section. Cut captions on photos, decorative strips and repeated footnotes.
- **The hotels are fictional, so say so plainly.** Never imply the shirts were taken from real hotels ("acquired", "lifted", "never meant to leave the property"). Good: "Four hotels that don't exist. A small crest on the front, a proper job title on the back."
- **Hotel and job names keep their exact spelling and accents:** Hôtel Solvane, The Oriole Palace, Casa Thalene, Grand Valbrune. The roles are Lifeguard, Security, Pool Boy and Ski Patrol.
- **Sentence case** for headings and buttons. Capitals only come from the `label` style and the wordmark.
- **Prices in whole pounds:** £48, never £48.00.
- **One place for disclaimers.** Put the preview notice in the announcement bar's "About this preview" panel. Elsewhere, add one short line only at the add-to-bag button and in the bag.
- No emoji, no exclamation marks.

## Visual foundations

**Colour.** Use one light ground (`paper`), one ink (`ink`) and one accent (`accent`). `staff-green` frames the page (announcement bar and footer) and appears nowhere in between. Set body copy in `ink`, secondary copy in `ink-2`, and tertiary notes in `ink-3`, which reads on paper only. Each hotel has its own ink (`hotel-solvane`, `hotel-oriole`, `hotel-thalene`, `hotel-valbrune`). Use it only for that hotel's crest, its number and its name, never as a fill or a background block, and never with two hotels' colours side by side in large areas. The garment tokens exist only for the 16px colour dot.

**Typography.** Use three families, each with one job:
- `serif` (Instrument Serif) for headings: `display` for the hero, `headline` for sections, pages and product names, `title` for modals.
- `sans` (DM Sans) for everything read: `body`, `body-sm` and `label`.
- `crest` (Cinzel 600) for the wordmark only. It is the same inscription face as the crests, so the logo and the crests read as one family.

Nothing is set below 12px. The "Line. *Italic line.*" headline appears once, in the hero. Every other heading is a single roman line with no full stop.

**Layout.** Section padding is `space-8` vertically on desktop and `space-7` on phones. The side gutter is `gutter`, never under `space-4`. Product grids have three columns on desktop and two on phones, with a `space-5` gap. Separate sections with `line` hairlines, not boxes. The header is a three-column grid: navigation left, wordmark centred, search and bag right.

**Photography.** Every product shot is a 4:5 portrait on exactly `stone`, with the shirt centred and filling about 78% of the width. The back of the shirt is the main image and the front is the second. The hero is one photograph of one shirt being worn. On phones it is cropped so the back print reads in full; never cut "LIFEGUARD" mid-word. Put no captions or text over photos except the hero headline.

**Borders, radii, shadows.** Corners are square (`radius-0`). `radius-full` is reserved for the colour dot and the bag count. Rules are 1px `line`. Controls that must be seen get `line-strong`. Only the bag drawer (`shadow-drawer`) and modals (`shadow-modal`) cast shadows.

**States.** Hover is slow and soft: photos scale to 1.025 over 700ms with `cubic-bezier(.2,.7,.2,1)`, and on a product card the front image fades in over the back. Buttons darken, never lift. The selected state is an `ink` fill with `paper` text. The focus ring is a 2px solid `accent` outline, offset by 4px, and it passes 3:1 on every ground. Errors are one line of `body-sm` in `accent`. Respect `prefers-reduced-motion` by turning off every transition.

**Calls to action.** There is one solid button style (Button), used for the primary action of a view. Everything else is a TextLink: a `label` in capitals with a 1px underline and no arrow. Arrows are not decoration. The one arrow allowed is inside the primary button.

## Iconography

- **The crests are the brand's pictures** (asset group Crests). There are four engraved single-ink badges, one per hotel, each already in its hotel ink: `hotel-solvane.svg` in `hotel-solvane`, `oriole-palace.svg` in `hotel-oriole`, `casa-thalene.svg` in `hotel-thalene` and `grand-valbrune.svg` in `hotel-valbrune`. Use them on hotel cards, the hotels page, product pages ("The hotel") and print. Never redraw, recolour per page, outline or put them on a coloured block. The minimum size is 56px tall on screen.
- **Interface icons** are Lucide, at a 1.5px stroke and 20px, in `ink`. Use only menu, search, bag, close, plus and minus. No decorative icons, no emoji, and no ✳ or bullet ornaments between words.
- There is no drawn logo. The wordmark is type: "OFF DUTY" in `wordmark`, with "HOTEL CLUB" beneath it in `wordmark-sub`, both in `ink` (or `on-dark` in the footer).

## Hotels

| No. | Hotel | Place | Department | Ink |
| --- | --- | --- | --- | --- |
| 01 | Hôtel Solvane | Saint-Tropez, French Riviera | Lifeguard | `hotel-solvane` |
| 02 | The Oriole Palace | Los Angeles, California | Security | `hotel-oriole` |
| 03 | Casa Thalene | Mykonos, Greek Islands | Pool Boy | `hotel-thalene` |
| 04 | Grand Valbrune | St. Moritz, Swiss Alps | Ski Patrol | `hotel-valbrune` |

The numbers 01–04 are real: they are each hotel's department number and its order in the collection. Set the number as a `label` in the hotel's ink, before the place: "01 · Saint-Tropez".

## Patterns to avoid

Scrolling ticker or destination strips, badges, a back/front toggle on every card, quick-add on hover, an arrow on every link, captions on top of photos, the italic second line repeated down the page, and any label under 12px.

## Known drift

The live store in storefront-kit does not match this system yet in these places. Fix them in storefront-kit (as brand options in `src/` where the code is shared), then delete each line here.

- `ink-3` is #7c7d72 in `theme.css`; this system uses #6b6c61.
- `staff-green`, `line-strong`, `on-dark-2`, `scrim`, the hotel inks and garment colours are missing from `theme.css`.
- The wordmark is Instrument Serif; Cinzel is not loaded.
- The focus ring is 1px `ink`; this system uses 2px `accent` with a 4px offset.
- Buttons are 54px, 13px, uppercase; this system uses 52px, 14px, sentence case.
- Product cards show a heart and scale to 1.03 over 1.4s; this system has no heart and scales to 1.025 over 700ms.
- The announcement bar and the footer's bottom line drop to 11px on phones.
- The header background is a fixed rgba of Small Hours' paper rather than `paper`.

## Files in this system

- `tokens.json`: every value, with a usage note. `tokens.css` is generated from it.
- `components/`: one folder per component, a README with its rules and, where it exists, a `preview.html`. `bundle.css` styles the previews.
- `merch.md`: the shirts, crests, back prints, blanks and labels.
- `decisions.md`: settled choices and what was rejected.
- `assets/crests/`: the four heritage crests in their hotel inks (screen use). Print masters are in storefront-kit `supply/print-files/`.
- `assets/photography/`: product shots (back and front) and the hero. Design visualisations until the samples are photographed.
- Review checklists for all brands: `../../checklists/`.
