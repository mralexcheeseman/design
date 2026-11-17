# In-situ library

Each shirt worn at its own hotel: five shots per shirt, one recurring member of staff per hotel, one setting and light per hotel. `contact-sheet.jpg` shows all 25.

These are AI-generated design visualisations, made before the samples exist. Treat them like the product renders: fine for the store, social and ads (the fiction is played straight, see `decisions.md`), but replace them with real photography of the samples when it exists. Never present them as photographs of real places or people.

## Shots

| File | Shot | Made with |
| --- | --- | --- |
| `<shirt>-01-back.webp` | Hero: from behind, the job title readable | FASHN product-to-model, from the back product shot |
| `<shirt>-02-threequarter.webp` | Three-quarter from behind, looking over the shoulder | FASHN product-to-model, the hero as the model |
| `<shirt>-03-front.webp` | Front, the chest crest visible | FASHN product-to-model from a front shot carrying the heritage crest, the hero as the model; crest then replaced with the print file |
| `<shirt>-04-crest.webp` | Close-up of the chest crest | As 03, cropped shoulder to mid-chest; crest replaced with the print file |
| `<shirt>-05-offduty.webp` | The shirt laid flat at the hotel, a few belongings beside it | FASHN background-change on the back product shot (keeps the real print) |

Hero shots are 1843 × 2304 (4:5). Off-duty shots are 896 × 1120 (4:5), which is all FASHN's background change gives: use them small (grids, stories), not full-bleed.

## Cast and settings

| Shirt | Hotel | Staff member | Setting and light |
| --- | --- | --- | --- |
| Lifeguard | Hôtel Solvane | Tanned man, short dark hair, red swim shorts | Pool deck of a grand Riviera hotel, red and white striped parasols, white loungers, cream stone balustrades; late afternoon gold |
| Security | The Oriole Palace | Broad-shouldered man, shaved head, black trousers | Hillside driveway, tall palms, valet stand, wrought-iron gate; dusk, warm sodium lights |
| Pool Boy | Casa Thalene | Young man, dark curly hair, white linen shorts | Whitewashed steps by a small infinity pool, blue doors, bougainvillea, the Aegean; hard midday sun |
| Ski Patrol | Grand Valbrune | Man with tousled fair hair, navy ski trousers | Wooden terrace above the slopes, ski lockers, snow peaks; clear cold morning |
| Head Gardener | Villa Ceresa | Man in his forties, grey-flecked beard, khaki work trousers | Formal lakeside gardens, clipped box, cypresses, camellias, terracotta pots, a stone loggia, Lake Lugano; soft early morning |

To add a shot for an existing hotel, pass that hotel's `01-back` hero as FASHN's `model_image` so the same person appears. A new hotel gets its own staff member and setting, added to this table.

## How the crests were fixed

FASHN draws the job title on the back correctly, but garbles the small lettering in chest crests. So for every front and close-up:

1. The front product shots in `source/` still showed the old clip-art crests. `source/*-front-heritage.png` are those shots with the heritage crest print file printed in its place (`recrest.py`); these were FASHN's input.
2. After generation, the crest FASHN drew was replaced with the print file from `artwork/print-files/`, fitted to its angle and printed through the fabric's shading (`overcrest3.py`).

The scripts and the request settings are in storefront-kit `tools/in-situ/`.

## Known deviations

- `ski-patrol-04-crest.webp` keeps FASHN's crest: its large solid areas could not be replaced cleanly. Names and shapes are right, but a row of stars stands where "EST. 1898" should be.
- In the three-quarter views an arm or the turn of the body hides part of the job title. That is the pose, not an error.
- The small line under each job title on the back (hotel and place) is FASHN's drawing of the print, not the print file: it reads correctly in every shot, but letterforms are softer than the real print.

Cost: 71 FASHN credits for the 25 shots and the pilot tests (2K product-to-model 3 credits a shot, background change 1).
