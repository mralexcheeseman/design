# Merch: the shirts themselves

The website is the shop window; the T-shirt is the product. These rules cover everything that gets printed, stitched or packed. Artwork is in `artwork/` in this folder (`crests/`, `print-files/`); supplier orders and research stay in storefront-kit `brands/off-duty-hotel-club/supply/` (`SAMPLE-ORDER.md`, `LAUNCH-PACK.md`). Physical values are also in the `print` group of `tokens.json`.

## The range

| Shirt | Hotel | Garment colour | Ink | Crest size |
| --- | --- | --- | --- | --- |
| Lifeguard | Hôtel Solvane, Saint-Tropez | rescue yellow (`garment-rescue-yellow`) | red | max 85 mm |
| Security | The Oriole Palace, Los Angeles | washed black (`garment-washed-black`) | off-white `#f5f2ea` | 70 × 85 mm |
| Pool Boy | Casa Thalene, Mykonos | pool blue (`garment-pool-blue`) | navy | max 85 mm |
| Ski Patrol | Grand Valbrune, St. Moritz | alpine red (`garment-alpine-red`) | cream `#f1e6d2` | 83 × 85 mm |

Pantone references (TCX for fabric, C for ink) are to be confirmed against a swatch book and the supplier's strike-off. Fill in `pantoneTCX` and `pantone` in `tokens.json` when they are.

## Front: the crest
- The illustrated heritage crests (chosen 11 Oct 2026). Source and rules: the `hotel-crest` skill in storefront-kit.
- Printed DTG, not embroidered: the engraved linework would fill in as stitches.
- Left chest, centred about 18 cm below the shoulder seam on the wearer's left. 85 mm maximum.
- One ink, the shirt's ink above. On screen the crests appear in each hotel's ink (`hotel-*` tokens); on the shirt they take the garment's ink.
- The current vectors are traces of a 1024 px sheet. A designer clean-up is due before bulk production.

## Back: the job title
- Job title in Anton, capitals, 280 mm wide (`back-print-width`), centred 80 mm below the collar.
- Hotel name below in Oswald 500, 14 mm, tracked 0.18em; city below that in Oswald 500, 8.5 mm, tracked 0.35em.
- Use the worn-ink version on dark shirts: about 9% of the lettering knocked out in a speckle, so less ink sits on the fabric and it stays soft.
- Generator: `artwork/print-files/make_art.py`. Outlined SVG and 300 dpi PNG for every back.

## Blanks
- Softness beats weight. Prefer garment-dyed or combed ring-spun heavyweight cotton.
- Current samples: Comfort Colors 1717 (Security, Printful) and Stanley/Stella Creator Vintage or Blaster 2.0 (Ski Patrol, Prodigi). The winner on softness after three washes takes the first order.

## Not designed yet
These need designing before the first bulk order and should follow this system (Cinzel for names, one ink, square corners, dry voice):
- Neck label or printed inner tag (size, care, "Off Duty Hotel Club").
- Swing tag: crest on one side, the shirt's "staff card" on the other (role, department number, hotel).
- Mailer and any insert card.
- An outlined wordmark SVG for print use.

Run `checklists/crest-and-print.md` before anything goes to a supplier.

## Caps: Hat Check (proposed, 26 Oct 2026)

A trucker-cap line, one per hotel, each the department the T-shirt store lists as "on the drawing board". Not approved yet; preview only.

| Cap | Hotel | Front / mesh / peak | Ink |
| --- | --- | --- | --- |
| Tennis Club | Hôtel Solvane, Saint-Tropez | white / white / clay red | red |
| Valet | The Oriole Palace, Los Angeles | washed black throughout | off-white `#f5f2ea` |
| Beach Club | Casa Thalene, Mykonos | pool blue / white / navy | navy |
| Night Porter | Grand Valbrune, St. Moritz | burgundy / cream / burgundy | cream `#f1e6d2` |
| Boatman | Villa Ceresa, Lake Lugano | cypress green / cream / cypress green | cream `#f1e6d2` |

- Front: the job title in Anton across the foam panel, hotel name and town beneath in Oswald 500, tracked like the shirt backs. Draft art in `artwork/caps/` (raster drafts, not print files yet).
- Boatman moved from orange-on-lawn-green to cream on cypress green: orange and lawn green are the same lightness and merge for colour-blind viewers.
- Photography in `assets/photography/caps/`: `-front` and `-side` on `stone`, `-scene` on location, and `hero-hat-check.webp`. Design visualisations (nano-banana-pro edit from the draft art) until samples exist.
