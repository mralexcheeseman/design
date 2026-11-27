---
slug: score-ai-pictures
title: Score AI pictures the same way every time
dek: Three scores of 1 to 5 (real, shirt, period look). 12 of 15 or more is a keeper.
making: photo
tools: [nano-banana-pro, higgsfield, kling, recraft, firefly, google-flow]
techniques: [scoring]
models: []
status: tested
cost_usable: Free
back_office: private
date: 2026-11-23
updated: 2026-11-27
---

# Score AI pictures the same way every time

Three scores of 1 to 5 (real, shirt, period look). 12 of 15 or more is a keeper.

## What happened

Photo Studio run 01 scored on five lines out of 25 (real, period, place, shirt, frame). Scoring that many lines by hand was the slowest step, and Alex cut it to three on 2026-11-23: real, shirt, and how close the picture comes to the 1960s resort look we want. The shot sheet (Google Sheet "ODHC shot ideas", see project memory) uses the three-line score for every v1 and v2.

## What to do

Score each variant 1 to 5 on three lines (definitions from the shot sheet's Read me tab):

- **Real**: would it pass as a real 1960s film photograph at full size? 5 is grain, skin, hands, fabric and light that hold up when you zoom in. 3 looks real at phone size and too clean up close. 1 is plainly AI: waxy skin, melted hands, plastic light.
- **Shirt**: is it our shirt? 5 is the exact colour and the back print reading in full, letter for letter like the product shot, small lines included. 3 is the right colour and main word with the small lines smudged, invented or partly hidden. 1 is the wrong colour or made-up lettering. Leave it blank if the shot has no shirt.
- **Period look**: 5 could pass for a 1960s resort photograph in a travel magazine: the place is the star, a few relaxed people, sunlit Kodachrome colour, 1960s through and through. 3 has the right idea and feels staged, crowded or a bit modern. 1 is a generic stock or AI look.

Total out of 15. 12 or more is a keeper. 9 to 11, change one plain thing in the prompt and run it again. Under 9, rewrite the prompt. Older Photo Studio scores are out of 25, so keep the scale beside any number you quote.

## Lessons

| Lesson | Status |
| --- | --- |
| `three-line-score`: Three scores of 1 to 5 are enough to pick keepers, and quick enough to give every take. | tested |
| `fail-checks-first`: Before scoring, tick six pass or fail checks (hands, faces, cut-off heads, stray text, number plates, modern objects). Any fail means refine or drop, whatever the score. | try |
| `score-every-take`: Two takes of one prompt differed by 3 points on average across 12 rows, so a prompt test scores four takes a side. | tested |
| `auto-grade-next`: A vision model scoring the same three lines could send anything under 12 straight to refine, with Alex's score as the final say. | tested, not ready |
| `real-needs-calibrating`: Claude's Real score does not track Alex's yet. Zoom crops and four anchor pictures moved Keeper agreement from 10 to 13 of 22, but Real still had no correlation with his. Keep Alex as the scorer until a model reaches 18 of 22. | tested |

## Can a model score for us? (27 Nov test)

Alex asked how a model could do the scoring. We compared Claude's scores with his on the 22 files he had scored that the Drive connector could download (files over 10 MB can't be fetched).

- **First scorer (the two-hourly results task):** it matched his Keeper or Try again on 10 of 22 files. It gave Real 4 to every picture, so it could not tell his 1s from his 5s. It also marked Shirt down for small lines that he forgives.
- **Second scorer (blind, fresh agent):** we gave it 100% crops of faces, hands and the print, plus four of his scored pictures as anchors (H2e v1 at 15, H1d v1 at 12, T1b v1 at 10, H3e v1 at 7). It matched him on 13 of 22. Shirt now follows his practice. On Real the model still gives his two 15s in the test (H3 v1, H3b v2) Real 3, and his Real-1 T1c pictures Real 4.
- **What this means:** his Real covers something the definition doesn't name yet, because the model's zoom check doesn't find it. The next step is a one-line reason from Alex on four disagreements, written into the definition. After that, rerun the same 22 files and switch over at 18 of 22.
- Training our own picture classifier only makes sense once he has scored about 200 files.

## History

- 2026-11-27: Tested two Claude scorers against Alex's scores (see above).

- 2026-11-24: Added fail checks and the four-takes rule from the process audit.
- 2026-11-23: Cut from five lines to three on Alex's word.
