# Postmark

Woven phone straps, one pattern per destination: Amalfi, Marrakech, Kyoto and Mexico City. Each destination has a crossbody strap and a wrist strap. The store should feel like a well-travelled letter, with envelope paper, navy ink and a postmark for every place. Keep it quiet enough for the patterns to carry it.

Working name, version 1, 16 Oct 2026. The store is `storefront-kit/brands/postmark` (preview on Vercel project `postmark`). Built from a one-line brief as the factory's first brand made end to end by the kit.

## Content fundamentals

- **Voice: warm, well-travelled and lightly witty.** We sound like a friend who has been, not a guidebook. Real lines to match: "Wear where you're going." "Your phone goes everywhere you do. It might as well dress for it." "Hands free. Phone on. Never left on a café table again."
- **Say less.** Use one strong line per section and no captions on photos.
- **The patterns are ours, inspired by the places.** Never imply they are official, traditional or made in the destination unless that's true for a given batch. Good: "Eight-point stars from a riad courtyard." Never: "Authentic Moroccan zellige."
- **Destination names keep their spelling and accents:** Amalfi, Marrakech, Kyoto, Mexico City (Ciudad de México on the postmark). Products are "<Destination> Crossbody" and "<Destination> Wrist Strap".
- **Sentence case** for headings and buttons. Capitals only come from the `label` style, the wordmark and the postmarks.
- **Prices in whole pounds:** £68, £38.
- **One place for disclaimers.** The preview notice lives in "About this preview". Elsewhere, one short line at add-to-bag and in the bag.
- No emoji, no exclamation marks.

## Visual foundations

**Colour.** Use one light ground (`paper`), one ink (`ink`) and one accent, airmail red (`accent`), for focus and errors only. `frame` (the same navy as ink) is the announcement bar and footer. Each destination has its own ink (`dest-amalfi`, `dest-marrakech`, `dest-kyoto`, `dest-mexico-city`). Use it only for that destination's postmark, number and colour dot, never as a fill. The patterns bring all the colour the page needs.

**Typography.** Use three families, each with one job:
- `serif` (Newsreader, with a real italic) for headings: `display`, `headline` and `title`.
- `sans` (Manrope) for everything read: `body`, `body-sm` and `label`.
- `postmark` (Barlow Condensed 600) for the wordmark and the postmarks only.

Nothing is set below 12px. The italic second line appears once, in the hero.

**Layout.** Postmark uses the shared storefront, so layout, spacing, motion, radius and z-index follow the same tokens as Off Duty Hotel Club. The featured row and the destination row are four across on desktop and two on phones.

**Photography.** Every product shot is a 4:5 portrait on exactly `stone`, shot from directly above. A crossbody strap is laid as a tall U with the loop at the top, clasps at the bottom and the slider on the right. A wrist strap is one teardrop loop with the clasp at the bottom. The strap fills up to 80% of the frame height (`height: 0.8` in `product-boxes.json`). The close-up is the top of the loop, so the weave reads. The hero is one strap being worn, from behind, with the place soft in the background. Until samples exist, images are generated renders and labelled as previews.

**Calls to action.** Use one solid Button for the primary action of a view. Everything else is a TextLink.

## The postmarks

The postmarks are the brand's pictures, and they work like Off Duty's crests: one family, drawn in code by `artwork/postmarks/make_postmarks.py` (the master is in storefront-kit `brands/postmark/supply/postmarks/`). Each has a double ring, the city on the top arc, the country on the bottom arc, the destination number with "PAR AVION", and five wavy cancellation lines.

- `assets/postmarks/<id>.svg` is the full postmark, for product pages, packaging and social posts.
- `assets/postmarks/<id>-ring.svg` has no waves, for destination cards and anything under 160px wide.
- `artwork/postmarks/<id>.svg` holds the black print masters. Text is outlined in every file.

Never redraw one by hand, recolour it per page, or put it on a coloured block. To add a destination, add a row to `STAMPS` in the script and re-run it.

| No. | Destination | Postmark text | Pattern | Ink |
| --- | --- | --- | --- | --- |
| 01 | Amalfi | AMALFI / ITALIA | Lemons on cobalt majolica | `dest-amalfi` |
| 02 | Marrakech | MARRAKECH / MAROC | Zellige stars, terracotta and saffron | `dest-marrakech` |
| 03 | Kyoto | KYOTO / NIPPON | Asanoha in two indigos, vermilion edge | `dest-kyoto` |
| 04 | Mexico City | CIUDAD DE MÉXICO / MÉXICO | Barragán blocks, pink and marigold | `dest-mexico-city` |

## Patterns to avoid

Airmail-stripe borders on everything, stamp-perforation edges on photos, tickers of destination names, badges, quick-add on hover, an arrow on every link, and any label under 12px.

## Known drift

None known. The store was built from this system on the day it was written.

## Files in this system

- `tokens.json`: every value, with a usage note. `tokens.css` is generated from it.
- `components/`: Postmark uses the shared storefront components. See `components/README.md`.
- `merch.md`: the straps, hardware, packaging and samples.
- `decisions.md`: settled choices and what was rejected.
- `index.html`: the system on one page (generated).
- `assets/postmarks/`: the postmarks for screens. `assets/photography/`: where sample photography goes.
- `artwork/postmarks/`: the black print masters and the script that draws them.
