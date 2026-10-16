# <Brand>

<One paragraph: what the brand sells, how the store should feel, what carries it.>

Copy this folder to `brands/<folder>/` (the same folder name as in storefront-kit), then start `tokens.json` from the nearest existing brand's and change the values. The build scripts skip this template because it has no `tokens.json`. See `storefront-kit/.claude/skills/launch-brand/SKILL.md` for the whole launch.

## Content fundamentals

- **Voice:** <three adjectives>. Real lines to match: "<line>" "<line>" "<line>"
- **Say less.** One strong line per section.
- **Names** keep their exact spelling and accents: <list>.
- **Sentence case** for headings and buttons; capitals only from `label` and the wordmark.
- **Prices in whole pounds.**
- **One place for disclaimers:** the "About this preview" panel, plus one line at add-to-bag and in the bag.
- No emoji, no exclamation marks.

## Visual foundations

**Colour.** One ground (`paper`), one ink (`ink`), one accent (`accent`). Collection inks only on their own mark, number and colour dot.

**Typography.** `serif` (with a real italic) for headings, `sans` for everything read, and at most one display face for the wordmark and marks only. Nothing below 12px. The italic second line appears once, in the hero.

**Layout.** Shared storefront tokens (see the nearest brand).

**Photography.** 4:5 on exactly `stone`; how the product is laid out; what the close-up shows; what the hero shows.

## The brand's mark

<What plays the role of a crest or postmark, how it is drawn, which files exist and where the master lives.>

## Patterns to avoid

<Brand-specific ones, plus: tickers, badges, quick-add on hover, arrows on every link, labels under 12px.>

## Known drift

None known.

## Files in this system

- `tokens.json`, `tokens.css` (generated), `components/README.md`, `merch.md`, `decisions.md`, `index.html` (generated), `assets/`, `artwork/`.
