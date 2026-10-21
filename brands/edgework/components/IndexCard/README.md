# IndexCard

One Position, typed on a ruled index card and taped to the desk.

**Consumer provides:** `number`, `statement`, `arena` (marketing-machine, ai-work or judgement), `conviction` (1–5), `source_essay` and its URL, and a `seed` (the Position number) so its marks and tilt are always the same.

**Rules**
- `ratio-card` on desktop, `sheet` with ruled `line` hairlines and the red top rule (from `bundle.css`).
- Top row: `label` "No. 07" left, the arena right, in `ink-3`.
- The statement in `type-lg`, through TypedText. If the statement has a `*phrase*`, that phrase gets the highlighter; otherwise nothing is highlighted.
- Conviction is shown as red-pen underlines under the label: one stroke per point, from the pen marks, never as stars or a bar.
- One strip of tape on one corner (picked by seed). At most one stain, and it never covers the statement.
- Tilt between -2.5° and 2.5° from the seed; flat on phones under 640px (max ±1°).
- Hover lifts the card flat (`shadow-lifted`, `duration-lift`). Click or Enter opens the dossier: the card at 2× on the night backdrop with the source essay's excerpt and link.

**Never:** show conviction as a number out of 5, highlight more than one phrase, or let tape cross the statement.
