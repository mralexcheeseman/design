---
slug: lock-cast-and-look
title: Keep the same people and the same colour across every AI picture
dek: Save each recurring person and product once as a reusable subject, and save the colour and light once as a style built from pictures with no people in them. Recraft styles carry content as well as colour, so build them from crops that match the scenes you will make.
making: photo
tools: [recraft, kling]
techniques: [reference-images]
models:
  - name: Recraft V4.1 raster with a custom style
    tested: 2026-11-25
  - name: Kling Elements (subjects) on Kling Image O1
    tested: 2026-11-27
  - name: Kling Elements (subjects) on Kling Image 3.0 Omni
    tested: 2026-11-27
status: try
cost_usable: About 2 Recraft credits a picture with a style; about 2 Kling credits a picture that keeps a saved person
back_office: unpublished
date: 2026-11-25
updated: 2026-11-27
---

# Keep the same people and the same colour across every AI picture

Save each recurring person and product once as a reusable subject, and save the colour and light once as a style built from pictures with no people in them. Recraft styles carry content as well as colour, so build them from crops that match the scenes you will make.

## What happened

Every new picture started from scratch: we pasted the same portrait and the same shirt into each prompt and hoped the face held. In the Oriole pool test (T3, 25 November) Kling rebuilt the reference photograph guest for guest when we gave it the whole picture as a style guide. So the look and the people need separate references, and the look reference must have nobody in it.

We built a Recraft custom style from three crops of the Oriole pool post with every person cut out: the palm shadow on the water, the empty striped loungers and a strip of open water. On a new Oriole pool scene it held the high camera, the diagonal pool and the palm shadow, with the colour paler and flatter than the post. On a St. Moritz terrace the same style painted the snow and the terrace turquoise. The style had learnt the pool as well as the film colour.

A second style mixed two pool crops with people-free crops of the Solvane and Valbrune hotel pictures and a style prompt that says to keep each scene's own colours. The St. Moritz terrace came out right: white snow, blue sky, warm faded colour. The Oriole pool now had snowy mountains behind Los Angeles. Each crop's subject leaks into every picture the style makes.

Kling subjects (Elements) are the other half: a cover picture plus one to three extra angles per person or shirt, called by id in any prompt. Kling only takes subject pictures sent through its own upload link, and that host is blocked from Claude's cloud container, so the subjects go up from a computer on a normal network. Google Drive links are refused for subjects even when shared publicly.

On 27 November a Claude session on Alex's iMac (Remote Control) uploaded the portraits, face crops and shirt pictures and saved all 18 subjects: 12 people and 6 shirts. The cloud thread then made the pictures with those ids.

Six test pictures showed when a saved face holds. On Kling Image O1, with a people-free look picture as image 1, the look held in all four (hard sun, deep blue sky, saturated colour). Gian came out as a different man in each picture, and his subject was weak from the start: his only face crop is a profile behind dark glasses. Bastien, saved from a clear front face, still came out as an older stranger in a hat and sunglasses whenever he was a small figure in a wide scene. On Kling Image 3.0 Omni, framed waist-up and three-quarter, with the prompt naming his tousled fair hair and ruling out hats and sunglasses, both pictures showed a young fair-haired man of the same type. Alex judged them two different men.

That is enough for the club. Each person belongs to one hotel, so a face only has to hold within that hotel's pictures. A person never appears at a second hotel.

## What to do

1. **Look:** crop three to five pieces of your best pictures with no people in them. Pick crops that show light, colour and texture, and avoid landmarks you don't want repeated (mountains, a particular pool).
2. Make one style per family of scenes: one for the pool hotels and one for the snow hotel.
3. Add a short style prompt describing the film, the light and the grain, and say "keep the scene's own colours".
4. In every prompt name the place, season and time of day, so the scene text outweighs the style.
5. **Cast:** for each recurring person save a subject with the full portrait as cover and a head-and-shoulders crop as the extra angle. Both must show the face front-on or three-quarter, without dark glasses. For each product save the back as cover, the front if you have it, and a close crop of the print.
6. Call a subject by id in the prompt and in the elements list. Give the look picture one job in the first line: light, colour and grain only, none of its layout.
7. When the person must be recognisable, use Kling Image 3.0 Omni, frame them waist-up or closer, name their hair and face in the prompt ("same face and tousled fair hair as the subject"), and rule out hats and sunglasses. Keep wide scenes for pictures where the staff member can be anyone.
8. Keep each person to their own hotel. Check consistency with two scenes at that hotel and ask someone who hasn't seen the prompts whether it is the same man.

## Prompt (generic)

Recraft, with the style selected:

```
A [decade] colour photograph for a travel magazine, [place], [month year], at [time]. [Camera position and the main shapes]. [Who is there and what they do]; nobody looks at the camera. [The one staff member or product, where they stand, what they hold].
```

Kling, with a subject saved:

```
Image 1 sets light, colour and grain only; use none of its layout. <<<subject id>>> is [role] at [place], [year], [time]: [action, pose, clothes]. Same face and [hair] as the subject, no hat and no sunglasses. [Who else is there]. Waist-up, three-quarter view, face clearly visible.
```

## Prompt we used (Off Duty Hotel Club)

Shot sheet rows LK1 to LK4 (Recraft) and LK5 to LK10 (Kling). Every ODHC Kling prompt opens with the private house-style paragraph from project notes, then the line for image 1, then the scene. LK9, the one that held Bastien:

```
Image 1 sets light, colour and grain only; use none of its layout. <<<Bastien>>> is the beach boy at a Riviera hotel, July 1964, at noon: carrying a stack of striped towels past the pool in a yellow T-shirt and white shorts. Same face and tousled fair hair as the subject. Guests on white loungers behind him. Waist-up, three-quarter view, his face clearly visible.
```

The Recraft Valbrune text:

```
A 1960s colour photograph for a travel magazine, St. Moritz, February 1965, at noon. A grand hotel's sun terrace above a frozen lake and snowy mountains, guests in fur hats and sunglasses at a long white-clothed lunch table with fondue pots, wooden skis standing upright in the snow behind them. Nobody looks at the camera. At the end of the table, a young ski instructor in a red T-shirt over a cream turtleneck pours white wine.
```

Style prompt for the all-hotels style:

```
1960s colour transparency film photograph for a travel magazine, any season or place: strong noon sun, warm faded colour with a slight magenta cast, true-to-life sky, snow and water colours, highlights close to burning out, deep cool shadows, fine film grain, slightly soft edges. Keep the scene's own colours; never tint snow or stone turquoise.
```

## Settings

| Setting | Value |
| --- | --- |
| Recraft model | V4.1 raster (the style picks it) |
| Ratio | 4:5 |
| Takes | 1 a call (2 a call timed out twice and still charged) |
| Styles saved | "ODHC house look (Oriole pool)" and "ODHC house look (all hotels)", private, in Recraft under My styles |
| Kling model for a recognisable person | `kling-image-v3_0_omni`, 2k, 3:4, one take |
| Kling model for scenes where staff can be anyone | `kling-image-o1` (about 1 credit) |
| Kling subjects saved (27 Nov) | People, tagged Characters: Nikos, Gian, Bastien, Whitlock, Augustin, Fairweather, Malone, the Commodore, the Doctor, the Baroness, Harcourt-Vane, Seraina. Shirts, tagged Costumes: Head Gardener, Lifeguard, Pool Boy (Thalene), Pool Boy (Selune), Security, Ski Patrol. Ids in the table below. |

| Subject | Kling id |
| --- | --- |
| Nikos | 327776304667988 |
| Gian | 327776374305417 |
| Bastien | 327776375312647 |
| Whitlock | 327776376313919 |
| Augustin | 327776378316321 |
| Fairweather | 327776379652595 |
| Malone | 327776380666784 |
| The Commodore | 327776381318965 |
| The Doctor | 327776383651432 |
| The Baroness | 327776384306661 |
| Harcourt-Vane | 327776385313985 |
| Seraina | 327776387662367 |
| Head Gardener shirt | 327776388664667 |
| Lifeguard shirt | 327776390315030 |
| Pool Boy (Thalene) shirt | 327776391667417 |
| Pool Boy (Selune) shirt | 327776392653717 |
| Security shirt | 327776394317049 |
| Ski Patrol shirt | 327776395318426 |

Call one in `image_to_image` with `<<<id>>>` in the prompt and `elements: [{"id": "<id>", "bindName": "<name>"}]`. Image 1 must be a Kling upload link; the people-free look crops already uploaded are in project files `locked-cast/kling-look-urls.md`.

Recraft styles only work with Recraft's own models. Nano Banana Pro and GPT Image on Recraft can't take them, so for those keep attaching a people-free crop as image 2.

## References

- Drive "ODHC shot references / Locked cast and look": the five people-free look crops (`look-*.jpg`).
- `/mnt/project-files/locked-cast/kling-elements/` in the project: each portrait, its face crop, each shirt back, front and print crop, as uploaded.
- `/mnt/project-files/locked-cast/kling-look-urls.md`: Kling upload links for the look crops (pool shadow, Solvane, Valbrune). The loungers and open-water crops are too wide for Kling's image tools.
- Results LK5 to LK10: Drive "ODHC shot results" and `/mnt/project-files/locked-cast/results/`.

## Cost

About 2 Recraft credits a picture with a style; 16 credits for the six test pictures including four lost to a timeout. Making a style and saving a subject are free. Kling: about 10 credits for LK5 to LK10 (O1 about 1 a picture, 3.0 Omni about 2). The two usable ones cost about 2 each.

## Lessons

| Lesson | Status |
| --- | --- |
| `look-refs-have-no-people`: Cut every person out of a picture you use for look only, or the model copies them. | tested |
| `style-carries-content`: A Recraft style learns what is in its pictures as well as their colour: a pool-only style turned snow turquoise, and Alpine crops put mountains behind Los Angeles. | tested |
| `one-style-per-scene-family`: Build a style per family of scenes (pool hotels, snow hotel) from crops of that family. | try |
| `recraft-style-one-take`: Ask for one picture a call with a style; two a call timed out at 60 seconds twice and still charged. | tested |
| `kling-subjects-need-kling-upload`: Kling subjects only take pictures sent through Kling's own upload, which Claude's cloud can't reach; Drive links are refused. A Claude session on a Mac does the upload. | tested |
| `subjects-need-a-clear-face`: Save each person from a front or three-quarter face with no dark glasses. A profile in sunglasses gave a different man in every picture. | tested |
| `wide-scenes-lose-the-face`: On Kling O1 a saved person who is a small figure in a wide scene turns into a stranger, even from a good face. | tested |
| `omni-waist-up-gets-closer`: Kling Image 3.0 Omni, waist-up, with the hair named and hats and sunglasses ruled out, gave the same type of man in two places. Alex still saw two different men. | tested |
| `continuity-within-one-hotel`: A recurring person only needs to hold within their own hotel (Alex, 27 Nov), so test and use each subject in that hotel's scenes alone. | settled |

## Next to try

Test one person in two scenes at their own hotel on 3.0 Omni. Rebuild Gian's subject from a front-facing picture. Test one person in a wide scene on 3.0 Omni to see whether the model or the framing lost the face. Test a shirt subject on its own. Make a snow-only and a Riviera-only Recraft style to test against the all-hotels one.

## History

- 2026-11-25: First written. Two Recraft styles saved and tested on two scenes; Kling subjects prepared but not uploaded.
- 2026-11-27: 18 Kling subjects saved from Alex's Mac. Consistency check LK5 to LK10: the look held; the person changed between hotels, which Alex is happy with because each person belongs to one hotel.
