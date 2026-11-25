---
slug: name-results-from-the-prompt
title: Name generated files from the shot ID in the prompt list
dek: A local vision model guessed which shot each picture showed and got most of them wrong. Carry the shot ID from the prompt list into the file name instead, and the naming needs no guessing at all.
making: photo
tools: [google-flow]
techniques: [workflow]
models:
  - name: Qwen2.5-VL 7B (Ollama, local)
    tested: 2026-11-25
status: tested
cost_usable: Free
back_office: private
date: 2026-11-25
updated: 2026-11-25
---

# Name generated files from the shot ID in the prompt list

A local vision model guessed which shot each picture showed and got most of them wrong. Carry the shot ID from the prompt list into the file name instead, and the naming needs no guessing at all.

## What happened

File Result, the Dock app on Alex's Mac (design PR #25), asks Qwen2.5-VL 7B through Ollama which shot a dropped picture shows, against `ODHC shot list.txt`. On its one-picture test it said SE1 at 90 per cent because it read "Pool Boy" on the shirt; the picture was H2b at Casa Thalene. The confidence figure meant nothing.

Then Alex dropped 40 Flow downloads on it. The guesses were weak enough that the thread set every shot itself, from Flow's own download names (which carried the prompt's words: towel, confetti, gate, lemonade) and a look at the less obvious ones. One picture filed as MA1 was the surf lesson, MA2. The app also guessed the tool from each shot's usual tool, so it called Flow stills `higgsfieldnbpro` until the tool was set by hand.

Ten pictures fitted no shot exactly (a beach bonfire, lunch on a blanket, Señora Valdés reading in a hammock). The model had nothing to say about those either.

## What to do

- The prompt list is the manifest. Every prompt a thread writes starts with its shot ID, and the run keeps the order, so a download's position or name maps back to the ID.
- Name `<ID>-v<N>-<tool>-take<N>.<ext>`, with the tool taken from where the run happened (a Flow download is `flow`).
- Crop Flow's 3:4 stills to 4:5 at 864 by 1080 while filing.
- Logging runs on its own and no longer uses Zapier, which would have needed about 400 tasks a month against a free plan of 100. See [log-results-from-drive](log-results-from-drive.md) for how it works now.
- Keep the vision model for one job only: flagging a picture that looks unlike its prompt, for a person to check.

## Lessons

| Lesson | Status |
| --- | --- |
| `local-vision-guesses-badly`: Qwen2.5-VL 7B on the Mac picked the wrong shot with 90 per cent confidence, and its guesses across 40 Flow stills were too weak to use. | tested |
| `manifest-names-files`: Name generated files from the shot ID in the prompt list; it is free, instant and right every time. | tested |
| `tool-from-the-source`: Set the tool from where the run happened (Flow, Recraft, Higgsfield). | tested |

## History

- 2026-11-25: Written after the 40-picture Flow batch through File Result.
