---
slug: score-ai-pictures
title: Score AI pictures the same way every time
dek: Three scores of 1 to 5 (real, shirt, Slim Aarons). 12 of 15 or more is a keeper.
making: photo
tools: [nano-banana-pro, higgsfield, kling, recraft, firefly, google-flow]
techniques: [scoring]
models: []
status: tested
cost_usable: Free
back_office: private
date: 2026-11-23
updated: 2026-11-23
---

# Score AI pictures the same way every time

Three scores of 1 to 5 (real, shirt, Slim Aarons). 12 of 15 or more is a keeper.

## What happened

Photo Studio run 01 scored on five lines out of 25 (real, period, place, shirt, frame). Scoring that many lines by hand was the slowest step, and Alex cut it to three on 2026-11-23: "we only need a score for real, tshirt and how close it is to slim aarons". The shot sheet (Google Sheet "ODHC shot ideas", see project memory) uses the three-line score for every v1 and v2.

## What to do

Score each variant 1 to 5 on three lines (definitions from the shot sheet's Read me tab):

- **Real**: would it pass as a real 1960s film photograph at full size? 5 is grain, skin, hands, fabric and light that hold up when you zoom in. 3 looks real at phone size and too clean up close. 1 is plainly AI: waxy skin, melted hands, plastic light.
- **Shirt**: is it our shirt? 5 is the exact colour and the back print reading in full, letter for letter like the product shot, small lines included. 3 is the right colour and main word with the small lines smudged, invented or partly hidden. 1 is the wrong colour or made-up lettering. Leave it blank if the shot has no shirt.
- **Slim Aarons**: 5 could sit in one of his books: the place is the star, a few relaxed people, sunlit Kodachrome colour, 1960s through and through. 3 has the right idea and feels staged, crowded or a bit modern. 1 is a generic stock or AI look.

Total out of 15. 12 or more is a keeper. 9 to 11, change one plain thing in the prompt and run it again. Under 9, rewrite the prompt. Older Photo Studio scores are out of 25, so keep the scale beside any number you quote.

## Lessons

| Lesson | Status |
| --- | --- |
| `three-line-score`: Three scores of 1 to 5 are enough to pick keepers, and quick enough to give every take. | tested |
| `auto-grade-next`: A vision model scoring the same three lines could send anything under 12 straight to refine, with Alex's score as the final say. | try |

## History

- 2026-11-23: Cut from five lines to three on Alex's word.
