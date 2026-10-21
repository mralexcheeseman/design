# Marks

The photographic mark library in `assets/marks/`: coffee ×5, splat (red ink) ×4, smudge ×3, burn ×2, tape ×3, highlight ×3, red pen ×6, the paper scans, the letterpress mask and the two "HEY RUBE." letterings. They are real scans with the paper removed, so they keep their own translucency on any ground.

**Consumer provides:** a numeric `seed` and a list of slots (where a mark may go, which kinds are allowed, base rotation, jitter, opacity). The same seed always gives the same marks (`pickMarks` in Owl Farm's `src/lib/marks.js` is the reference implementation).

**Rules**
- Stains blend with `multiply`; tape never blends.
- 1–2 stains per card and 3–4 per hero, never more.
- Tape only on corners or the top edge.
- A mark never covers a headline or the highlighted phrase. Keep stains to the edges, bleeding off the sheet.
- On the night ground use only splat (red ink) and tape.

**Never:** use stock or generated stains that aren't in this folder, tint a mark, or animate a stain.
