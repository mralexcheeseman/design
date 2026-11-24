---
slug: frame-ai-pictures-with-a-layout-reference
title: Stop AI pictures cutting off heads and crowding the frame
dek: Add a rough layout sketch as its own reference image, and give every reference one job in the first lines of the prompt. Under test on Nano Banana Pro.
making: photo
tools: [nano-banana-pro, higgsfield, recraft]
techniques: [reference-images, scoring]
models:
  - name: Nano Banana Pro on Higgsfield Unlimited
    tested: 2026-11-24
status: try
cost_usable: Free on Higgsfield Unlimited
back_office: unpublished
date: 2026-11-24
updated: 2026-11-24
---

# Stop AI pictures cutting off heads and crowding the frame

Add a rough layout sketch as its own reference image, and give every reference one job in the first lines of the prompt. Under test on Nano Banana Pro.

## What happened

We scored 27 Higgsfield takes of 1960s resort pictures with our shirts in them. They averaged 11.1 of 15, and the points went at the edges of the frame: heads cut off at the bottom, guests crowding out the place, the wearer too small to read the print. Our prompts described the framing in a long paragraph and sent two images, the shirt and a hotel picture "for the colour and light".

The same prompt also swung hard between takes. Twelve rows had both takes scored, and the two differed by 3 points on average. One scored 11 and then 3.

Google's advice for Nano Banana Pro is to "clearly define the role of each" uploaded image, for example one for pose, one for style and one for background. OpenAI says the same for GPT Image: identify each input by number and purpose. So we added a third image that carries only the layout.

## What to do

1. Draw the layout as a plain grey blocking sketch at the picture's ratio: horizon, the main shapes, each person as a silhouette where they stand and facing the way they face. Leave a strip of empty ground under the lowest feet. Put no words on it.
2. Attach the references in order of what must survive: the product first, then the look, then the layout.
3. Open the prompt with one line per image saying its job, and say what to ignore in the sketch.
4. Make four takes and score all four. Two takes can't tell a better prompt from a lucky one.

A sketch, one of your own past keepers, or a photograph you own all work as layout references. Photographs by a named photographer belong to whoever holds their archive, so keep them out of the reference slots.

## Prompt (generic)

```
Three images are attached, each with one job. Image 1 is the [product]: copy its colour and print exactly. Image 2 sets the colour and light only. Image 3 is a rough layout sketch: take only where the camera stands, the height of the horizon, and where each person stands and which way they face. Image 3 has no colours, clothes or buildings to copy.

[The rest of your picture prompt.]
```

## Prompt we used (Off Duty Hotel Club)

Shot sheet row T1b: the H1e prompt for Hôtel Solvane (Bastien furling the parasol at six, see [product print playbook](product-print-on-ai-model.md) for its full text) with the paragraph above in front of it. Row T1a runs H1e unchanged as the control, and T1c adds positive wording in place of the list of bans.

## Settings

| Setting | Value |
| --- | --- |
| Model | Nano Banana Pro (check the Higgsfield picker says Pro) |
| Ratio | 4:5 |
| Size | 2K |
| Takes | 4 per arm |
| Scored on | Real, Shirt and Slim Aarons, 1 to 5 each (see [scoring note](../notes/score-ai-pictures.md)) |

## References

- Image 1: the shirt's back product shot.
- Image 2: the hotel's hero picture, for colour and light.
- Image 3: `composition-h1e-blocking.png`, a grey blocking sketch in the Drive "ODHC shot references" folder.

## Cost

Free on Higgsfield Unlimited. The same 12 takes on Recraft's Nano Banana Pro would cost about 240 credits.

## Lessons

| Lesson | Status |
| --- | --- |
| `one-job-per-reference`: Name each reference image's job in the first lines of the prompt, as Google and OpenAI both advise. | try |
| `layout-sketch-as-reference`: A wordless blocking sketch as its own image should hold framing better than a paragraph of words. | try |
| `four-takes-per-test`: The same prompt swung by 3 points on average between two takes, so judge a prompt change on four takes a side. | tested |
| `say-what-the-frame-holds`: Google advises describing what you want ("empty street") over what you don't ("no cars"); our prompts carried more than a dozen bans. | try |
| `check-the-model-picker`: Higgsfield's history labels our recent takes as Nano Banana 2 while the shot sheet says Pro, so log the model with every take. | try |

## Next to try

Run rows T1a, T1b and T1c, and keep the sketch if T1b beats T1a by 1.5 points or more without copying the sketch's flat grey look.

## History

- 2026-11-24: First written from the process audit (Claude Doc "ODHC picture process audit"). Test set up in the shot sheet, not yet run.
