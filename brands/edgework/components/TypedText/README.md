# TypedText

Typewriter text where every word sits a fraction off the line, like a real strike.

**Consumer provides:** `text` (with at most one `*phrase*`) and a `salt` so the jitter is stable.

**Rules**
- Each word: translateY within ±1.2px and rotate within ±0.66°, from a hash of salt and word index (`typedWords` in Owl Farm's `src/lib/marks.js`).
- The `*phrase*` gets `.ew-hl` (the scanned highlighter stroke).
- Headlines that type on: one character per `duration-key`, the cursor blinks for 1.2s, then disappears. Reduced motion shows the full text at once.

**Never:** jitter labels or Anton headlines, or highlight with a flat colour.
