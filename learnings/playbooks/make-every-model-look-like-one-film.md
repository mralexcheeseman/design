---
slug: make-every-model-look-like-one-film
title: Make pictures from different AI models look like one film
dek: Normalise every picture's levels and colour cast first, then lay one gentle look over the lot at less than full strength. Pick the look from a contact sheet of real pictures, once.
making: photo
tools: [flow, recraft]
techniques: [grading]
models:
  - name: Nano Banana Pro (Flow)
    tested: 2026-11-25
  - name: Nano Banana Pro (Recraft)
    tested: 2026-11-25
status: tested
cost_usable: Free; a script on any computer, about a second a picture
back_office: unpublished
date: 2026-11-25
updated: 2026-11-25
---

# Make pictures from different AI models look like one film

Normalise every picture's levels and colour cast first, then lay one gentle look over the lot at less than full strength. Pick the look from a contact sheet of real pictures, once.

## What happened

Our feed mixes Flow, Recraft and older Kling stills. Each model has its own black point, contrast and colour cast, so side by side they read as different photographers. A look applied straight on top kept those differences and sometimes made them worse.

The first version of the normalise step blew out snow and sky: a frame with little true white was stretched until its pale greys clipped. Capping the stretch (the white point never set lower than 0.85, mapped to 96%) and adding a soft highlight shoulder fixed it.

## What to do

1. Crop to the post ratio first (4:5, 1080 wide), so the grade sees only what will be posted.
2. Normalise: black point at the 0.5 percentile (capped at 6%), white point at the 99.8 percentile (never below 0.85) mapped to 96%, mid-tone cast removed at 60%.
3. Apply one look, then a highlight shoulder from 0.78, and blend with the original at the chosen strength.
4. Choose the look on a contact sheet: four looks across six real pictures from different models, then the winner at 50%, 75% and 100%. Lock it and write it down.
5. Add no grain and no vignette in the grade.

## Prompt (generic)

```
No prompt: this is a script step after generation. Keep your usual prompt and stop asking the model for a film stock look as well, or it fights the grade.
```

## Prompt we used (Off Duty Hotel Club)

```
None. Grade: look C "Faded slide" at 0.75. Soft focus 0.4, a quarter smoothed, lifted blacks (0.06 + 0.9x), saturation 0.9, warm (R 1.06, B 0.88), a little blue in the shadows, gentle halation.
```

The script is storefront-kit `tools/post-pipeline/grade.py`; `grade_sheet.py` and `strength_sheet.py` make the contact sheets.

## Settings

| Setting | Value |
| --- | --- |
| Ratio | 4:5, 1080 x 1350 |
| Look | C Faded slide |
| Strength | 0.75 |
| JPEG quality | 90 |

## References

- Contact sheets shown to Alex on 25 Nov: looks A to D, and C at three strengths (project files `post-pipeline/`).

## Cost

Free. The script runs in the cloud container in about a second a picture.

## Lessons

| Lesson | Status |
| --- | --- |
| `normalise-first`: level and neutralise each picture before the look, or the look keeps each model's differences. | tested |
| `cap-the-stretch`: never set the white point below 0.85, or pale snow and sky clip. | tested |
| `choose-on-real-pictures`: pick the look on a sheet of your own mixed-model pictures, never on one hero frame. | tested |
| `under-full-strength`: 75% kept the look and let each picture's own light through; 100% flattened faces. | tested |

## Next to try

Run the same grade over a Kling or Higgsfield video's first frame and compare it with the graded still.

## History

- 2026-11-25: First written. Alex locked C Faded slide at 75%.
