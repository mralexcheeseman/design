---
slug: product-print-on-ai-model
title: Get your product's print right on an AI model
dek: Send the product photo as a reference image and say how it should be worn. The shirt came back the right colour on every take, and one plain sentence fixed the one that was wrong.
making: photo
tools: [nano-banana-pro, higgsfield]
techniques: [reference-images, refine, film-look, scoring]
models:
  - name: Nano Banana Pro on fal
    tested: 2026-11-23
  - name: Nano Banana 2 on Higgsfield Unlimited
    tested: 2026-11-23
status: proven
cost_usable: About 25 cents a usable picture
back_office: published
date: 2026-11-23
updated: 2026-11-23
---

# Get your product's print right on an AI model

Send the product photo as a reference image and say how it should be worn. The shirt came back the right colour on every take, and one plain sentence fixed the one that was wrong.

Before, first take, 19 of 25: the lifeguard faces the camera, so the back print is lost. [run01-solvane-lifeguard-take1.jpg](https://media.base44.com/images/public/6b044d6aaa73f82d3c126031/03d506425a1f7ef9a51a25bc41b37402_run01-solvane-lifeguard-take1.jpg)
After, one refine, 22 of 25: turned away, print readable, the rest of the frame kept. [run01-solvane-lifeguard-refined.jpg](https://media.base44.com/images/public/6b044d6aaa73f82d3c126031/8a89640c005746c58b043b69453b6b3a_run01-solvane-lifeguard-refined.jpg)

## What happened

Photo Studio is a small app we built in Base44. You pick a hotel, a shirt and a moment, and it writes the prompt, sends the shirt's product shot to Nano Banana Pro, adds a Kodachrome grade and files the result. The first run made one 1960s resort picture for each of four hotels at about 15 cents a take.

All four shirts came back the right colour, and three had a readable back print first time. The points we lost were at the edges of the frame: heads cut off along the bottom and a tiny number plate. Nano Banana Pro also draws a rounded film-slide border whatever you ask, so the app crops 6.5% off each edge on save.

Later Alex made the same lifeguard in Higgsfield, where the model is free on the Unlimited plan, and scored it 18 of 25. He liked the scene and marked it down for looking too crisp for 1960s film up close, and the two small lines under LIFEGUARD came out as squiggles. The generic prompt below now asks for both.

| Hotel | Shirt | Score /25 | Note |
| --- | --- | --- | --- |
| The Oriole Palace | Security | 21 | Strong place shot, print reads. A tiny licence plate is the only stray text. |
| Grand Valbrune | Ski Patrol | 21 | Print sharp, colour right. Guests crowd the frame so the lake plays second. |
| Casa Thalene | Pool Boy | 20 | Back print clear. Heads cut off along the bottom edge. |
| Hôtel Solvane | Lifeguard | 19, then 22 after one refine | Turned away on the refine, print readable. |

Finished files are in Cloudinary, folder `off-duty-hotel-club/lifestyle-4k`. Approved house looks (Alex, 2026-11-23): Oriole is the Security shot, Valbrune is the Ski Patrol shot.

## What to do

Attach the product shot as image 1 and write how it is worn and seen: who wears it, which way they face, and that the print is copied exactly with nothing added. Name the small lines of the print too, or they turn to squiggles.

When a take is close, refine it with one sentence about the one thing to change. A fresh take can lose everything you liked about the first.

To pass as old film, ask for it in plain words: visible grain, soft edges, faded colour, skin with pores.

## Prompt (generic)

```
A [decade] [photographer or magazine] colour photograph, [place], [month and year]. [Where the camera stands and what it sees: the setting, three or four people each doing something different]. Shot on [camera] on [film stock] in natural light only: [colour notes], visible grain, soft edges, slightly faded colour, skin with pores. The camera stands well back, so the place is half the picture.

[The wearer] wears the T-shirt in image 1 exactly: the same [colour name and hex] cotton and the same back print, copied letter for letter including the small lines, with nothing added or changed. [He or she] is turned away from the camera so the back print reads in full. That print is the only lettering in the picture. Match the colour and light of image 2.

[Ratio], full bleed. No text, no signs, no logos, no number plates, no border, no rounded corners, no modern objects. Every head and every foot sits inside the frame.
```

## Prompt we used (Off Duty Hotel Club)

This is the Higgsfield version Alex scored 18. The generic prompt above adds the grain and small-print lines it was missing.

```
A 1960s Slim Aarons colour photograph for Holiday magazine, Saint-Tropez on the French Riviera, July 1965. Seen from a terrace above and behind: a hotel swimming pool cut into pale stone above the sea, a tall white wooden lifeguard chair at its far corner with a young lifeguard sitting high in it under a blue-and-white striped parasol, two women on loungers below him reading, one man mid-dive, a waiter crossing with a tray of drinks, the bay and sailing boats beyond. Shot on a Hasselblad on Kodachrome slide film in natural light only, no flash: real, slightly imperfect colour, rich saturated Riviera blues and whites with rescue-yellow and coral accents, bright highlights that almost burn out, deep clean shadows, fine grain. The camera stands well back, so the place is half the picture and the people are small to medium within it, everything in deep focus. Only a few people, each doing something different, unposed and unhurried, in authentic mid-1960s Riviera resort clothes: linen shirts, one-piece swimsuits, straw hats and white sunglasses. The hotel's lifeguard, a tanned young man with short dark hair, sitting in the chair, wears the T-shirt in image 1 exactly: the same rescue-yellow (#efc331) cotton and the same back print, copied from the reference with nothing added or changed. He is turned away from the camera so the back print reads in full. That print is the only lettering anywhere in the picture. Match the colour and light of image 2. Vertical 4:5 composition, full-bleed edge to edge. No text, no signs, no logos, no emblems, no number plates, no border, no caption, no rounded corners, no vignette, no modern objects. Every head and every foot sits inside the frame. Avoid: modern sunglasses.
```

Shirt hex values come from `brands/off-duty-hotel-club/tokens.json`. Never type them from memory.

## Settings

| Setting | Value |
| --- | --- |
| Ratio | 4:5 |
| Size | 2K |
| References | Product shot, plus one picture for the look |
| Finish | Kodachrome grade, 6.5% crop off each edge |
| Scored on | Real, Shirt and Slim Aarons, 1 to 5 each (see [scoring note](../notes/score-ai-pictures.md)) |

## References

- Image 1, the product shot: [ref-lifeguard-shirt.webp](https://media.base44.com/images/public/6b044d6aaa73f82d3c126031/2fef41484993fd3ad509dcec1158390f_ref-lifeguard-shirt.webp)
- Image 2, the hotel's approved house look where there is one.

## Cost

About 25 cents a usable picture. Five takes on fal for about 75 cents gave three keepers. The same model is free on Higgsfield's Unlimited plan.

## Lessons

| Lesson | Status |
| --- | --- |
| `shirt-reference-holds-colour`: Sending the product shot as the reference image kept the shirt colour right on all four first takes, and three had a readable back print. | proven |
| `crop-the-slide-border`: Nano Banana Pro adds a rounded film-slide border whatever the prompt says, and a 6.5% edge crop on save removes it. | proven |
| `refine-before-reroll`: One plain-language refine fixed the Solvane shot and kept everything else in the frame. | tested |
| `say-film-grain-out-loud`: "Kodachrome, fine grain" still gave a crisp digital picture and squiggly small print. Ask for visible grain, soft edges, faded colour and skin with pores, and name the small lines of the print as something to copy letter for letter. | tested |
| `clear-bottom-edge`: Cropped heads at the bottom edge and a stray number plate cost the most points, so the recipe asks for a clear bottom edge and no plates. | try |
| `higgsfield-unlimited-for-shirt-stills`: Higgsfield's Unlimited Nano Banana Pro takes up to 14 reference images, so shirt-reference stills can be made there at no cost while fal sits at zero. | try |

## Next to try

Run the tightened prompt on Nano Banana Pro in Higgsfield and score two takes side by side.

## History

- 2026-11-23: Photo Studio run 01 (four hotels, one refine). Higgsfield lifeguard scored 18. Written up as a playbook.
