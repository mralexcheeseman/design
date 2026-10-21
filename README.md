# Design

The design systems for Alex's brands: tokens, components, rules and assets that every page, product and print file is built from. Storefronts live in [`storefront-kit`](https://github.com/mralexcheeseman/storefront-kit); this repo says what they should look and sound like.

## What's here

```
CLAUDE.md, AGENTS.md      how agents must use this repo (read first)
checklists/               reviews every piece of work passes before it is called done
brands/
  off-duty-hotel-club/    README (voice, colour, type, layout, photography), tokens.json,
                          tokens.css and index.html (generated), components/, merch.md,
                          decisions.md, assets/ (crests, photography), artwork/ (crest
                          sources, supplier print files)
scripts/build-tokens.mjs  tokens.json -> tokens.css
scripts/build-preview.mjs tokens + component previews -> index.html (CI checks both are current)
CHANGELOG.md              what changed, when, and why
```

Shared storefront rules (photography, 12px minimum, one accent, patterns to avoid) are in `storefront-kit/playbook/principles.md`. A brand system here adds to them and is stricter where it says so; it never relaxes them.

## Brands

| Brand | System | Browsable version |
| --- | --- | --- |
| Off Duty Hotel Club | [`brands/off-duty-hotel-club`](brands/off-duty-hotel-club/README.md), one-page view in `index.html` | [Design System artifact](https://claude.ai/artifact/L4Y5Q8SnMWM58dgqMyyrVt) |
| Edgework | [`brands/edgework`](brands/edgework/README.md), one-page view in `index.html` | Canvas: [Edgework identity](https://claude.ai/artifact/81MWsBJSGEbyhuRdoBxWrT) |
| Small Hours | not yet captured; tokens live in `storefront-kit/brands/small-hours/theme.css` | |
| Long Haul Club | not yet captured; tokens live in `storefront-kit/brands/long-haul-club/theme.css` | |

This repo is the source of truth. When the artifact and this repo disagree, this repo wins, and the artifact is updated to match.

## Changing a token

1. Edit `brands/<brand>/tokens.json` (value and usage note).
2. `node scripts/build-tokens.mjs <brand>` and `node scripts/build-preview.mjs <brand>` to regenerate `tokens.css` and `index.html`.
3. Bring the brand's `theme.css` in `storefront-kit` into line in the same piece of work.
4. Add a line to `CHANGELOG.md`, and to `decisions.md` if it settles a choice.
