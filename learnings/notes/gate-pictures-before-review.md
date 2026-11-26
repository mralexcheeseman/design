---
slug: gate-pictures-before-review
title: Score and check every generated picture before a person reviews it
dek: A scheduled Claude run scores each new picture on the house rubric and fails any with a wrong shirt, bad hands, stray text or a tool watermark. The sheet then ranks the tools by usable pictures and credits per usable picture.
making: photo
tools: [higgsfield, kling, recraft, google-flow, firefly, picsart]
techniques: [scoring, workflow]
models: []
status: try
cost_usable: One scheduled run every two hours, up to 20 pictures a run
back_office: private
date: 2026-11-26
updated: 2026-11-26
---

# Score and check every generated picture before a person reviews it

A scheduled Claude run scores each new picture on the house rubric and fails any with a wrong shirt, bad hands, stray text or a tool watermark. The sheet then ranks the tools by usable pictures and credits per usable picture.

## What happened

By 25 Nov the Results tab held 112 pictures and clips from seven tools, and only the Higgsfield rows had Alex's scores. Picking a winner per job ("two tools per job") needs every take scored the same way, and Alex's time is the scarce part. On 25 Nov he approved a scoring agent and a quality gate.

The logger (see `log-results-from-drive.md`) already ran every two hours, so the scoring and the gate went into the same scheduled task. One writer owns the Results tab, which keeps two tasks from fighting over the same rows.

## What to do

1. Add agent columns after the logger's: Made with, Real, Shirt, Look, Gate, Gate notes, Credits, Checked. Put the formula columns last (Claude /15, Final /15, Usable), so the agent writes one block of eight cells per row and never types into a formula column.
2. Final score is the person's score where they gave one, otherwise Claude's. Usable is a final score of 12 or more, and for Claude-only scores a gate pass too.
3. Score blind. Small back-print lines fail the gate but do not lower the Shirt score; Alex judges the picture as a whole and a garbled hotel name is caught by the gate anyway. The task never reads the person's score columns, so the two can be compared honestly.
4. Fetch each still with the Google Drive connector's `download_file_content`. The picture shows to the model and is also saved to a local file, so the run can crop the shirt, hands and any lettering with PIL and look again at full size. `read_file_content` returns nothing for images.
5. Give the agent the back print of every shirt as text, letter for letter, and a Drive folder of the flat product shots to compare against. Every run can reach Drive.
6. Gate codes, one per failure, so failures can be counted: `shirt-colour`, `shirt-print`, `hands`, `faces`, `stray-text`, `cut-off`, `modern`, `frame`, `ai-mark`, `name`, `off-look`. A shirt partly hidden by the pose only lowers the shirt score.
7. Record the tool from the file name before the sheet row. T3 was planned on Higgsfield and run on Kling, so the row's tool and cost were wrong for those files.
8. Credits per file, in each tool's own credits. When the price is unknown, leave it blank and say so in the notes. The ranking counts unpriced rows separately.
9. A ranking tab built from one `QUERY` over Results: results, scored, usable, gate fails, credits spent, unpriced, usable rate, credits per usable. Compare credits within one pool.
10. Score the Look line beside the look book (see `house-style-prompt.md`). The agent downloads the one-sheet look book once per run and fails any picture with Look under 4, or one that would stand out in the sheet: too real, or soft and muted.
11. Cap each run (20 pictures here) and work newest first after the new files, so a backlog clears over a few runs without one run timing out.

## Lessons

| Slug | Lesson | Status |
| --- | --- | --- |
| `drive-download-shows-the-picture` | The Drive connector's `download_file_content` hands the model the image and a local copy to crop, so a scheduled run can judge pictures with no other service. | tested |
| `one-writer-per-tab` | Fold new jobs on a tab into the task that already writes it, so one task owns every row. | try |
| `tool-from-file-name` | The file name says which tool made a picture more reliably than the planned row does. | tested |
| `small-lines-fail-first` | First run, 25 Nov, 20 stills (T3 on Kling and Recraft, A1 expands): 17 failed the gate. The commonest failures were the small hotel line on the back ("THE ORIDLE PALACE", "LOS ANIELES") and garbled newspapers and magazines on the loungers. Both read fine at phone size and only show in a full-size crop. | tested |
| `judge-the-look-beside-the-keepers` | A written description of the look let pictures drift for two days. A sheet of the pictures Alex kept, opened beside each new one, gives the agent something concrete to compare against. | try |
| `gate-stricter-than-a-glance` | The blind scores ran 2 to 3 points under the scores another thread gave the same T3 takes by eye (Kling with Nano Banana Pro: 9 to 11 here, 12 to 13 by eye). Compare with Alex's own scores before trusting either. | tested |
| `same-average-different-picks` | On the 32 Higgsfield stills Alex had scored, the blind scores averaged the same as his (0.2 lower) but picked different pictures: they agreed on keeper or not for 17 of 32, and the two sets of scores did not rise and fall together. His five 15s (the Villa Ceresa gardener set) scored 10 here, because the small sage lines on the back were garbled at full size. The blind score squeezes everything into 9 to 12 while he uses 5 to 15. An average alone hides this, so compare the picks. | tested |

## History

- 2026-11-25: First run checked 20 stills in about 20 minutes: 3 passed, 17 failed. One usable (an Adobe expand of the Valbrune house look, 13).

- 2026-11-26: Scoring and the gate added to the two-hourly results task; Tool ranking tab added.

- 2026-11-26: Calibration against Alex's 32 scored Higgsfield stills: mean gap 0.2, keeper agreement 17 of 32. Alex chose to count the small back-print lines in the gate only. The Shirt score now judges colour, ink, the main word and where the print sits, and the task rescores the stills marked down for small lines.

- 2026-11-26: Alex picked a 19-picture look book. The Look line is now scored beside it, a new `off-look` gate code fails anything under 4 or too real or soft and muted, and every checked still is rescored.
