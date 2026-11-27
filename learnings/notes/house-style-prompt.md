---
slug: house-style-prompt
title: Start every ODHC picture prompt with the house style paragraph
dek: One fixed paragraph, pasted word for word at the top of every Off Duty Hotel Club picture prompt, so every model aims at the same look.
making: photo
tools: [nano-banana-pro, higgsfield, kling, recraft, firefly, google-flow]
techniques: [film-look]
models: []
status: try
cost_usable: Free
back_office: private
date: 2026-11-26
updated: 2026-11-26
---

# Start every ODHC picture prompt with the house style paragraph

One fixed paragraph, pasted word for word at the top of every Off Duty Hotel Club picture prompt, so every model aims at the same look.

## What happened

On 24 November we took Slim Aarons' name out of every prompt and described the look instead ("a 1960s colour photograph for a travel magazine"). Over the next two days the pictures drifted: each model filled the vague wording with its own default look. On 26 November Alex said "we need to add back in slim aarons refereence". His name now goes back into the prompts we send to image models. It stays out of everything public (see `brands/off-duty-hotel-club/decisions.md`, 2026-11-26).

## The paragraph

Paste this first, filling the two brackets, then describe the scene. Never paraphrase it.

```
A Slim Aarons photograph of [place], [month year], shot on Kodachrome for a travel magazine. The place is the star: seen from a high vantage or wide across the scene, hard sun, a deep blue sky and saturated colour (pink and cream stucco, turquoise water, white loungers with striped cushions, tanned skin). A few wealthy, relaxed guests at leisure in 1960s clothes, hair and sunglasses, none of them looking at the camera. Fine film grain, warm highlights close to burning out, soft edges. Every person, object and building belongs in the 1960s.
```

For snow scenes, swap the colour list for: white snow, deep blue sky, red and navy ski wear, dark pine, warm wood chalets.

## The look book

On 26 November Alex picked 19 of our early pictures as the look every new picture is checked against: the Oriole, Solvane and Valbrune hero shots, the Oriole pool picture, and the guest-book portraits of Fairweather, Malone, Whitlock, Augustin, the Commodore, the honeymooners, Bastien, Odile, Teddy, the Doctor, the Bevacqua sisters, the Baroness, Gian, Harcourt-Vane and Seraina. Files: `/mnt/project-files/odhc-look-book/keep/`. One sheet of all 19 is in Drive, "ODHC shot references / Locked cast and look", file `ODHC look book (Alex picks, 26 Nov).jpg` (id `1NWpYx_5kT9Xe6DPdwX5RSiL2R7YbaMrx`).

He ruled two kinds of picture out:

- **Too real.** Nikos (plain T-shirt, flat light, a documentary portrait) "feels a little too real vs our aesthetic". The house look is polished and sunlit, with glamour, saturated colour and a postcard-blue sky, never gritty documentary realism.
- **Soft and muted.** The three Villa Ceresa pictures (Ottavio, the Contessa, Emilio) are "completely off": misty light, a pale sky and muted, faded colour. Every keeper has hard sun and strong colour.

Before a picture goes to review, put it beside the look book. If it would stand out in that sheet, it fails, whatever its score.

## Rules

- The name goes only into prompts sent to image and video models, the shot sheet and this note. It never goes into captions, alt text, ads, product copy, posts, file names others see, Express doc names, The Back Office or any playbook marked `published`.
- Public playbooks keep their generic wording. A thread running an ODHC prompt from a playbook puts this paragraph in front of it.
- Never attach one of his photographs as a reference. Attach one of our own keepers (for example the Oriole pool picture) for colour and light.
- Never reuse an old prompt. On 27 Nov a Flow run came back looking like current photos because it reused the 25 Nov T3 prompts, which didn't open with this paragraph and still asked for "real, slightly imperfect colour" and "skin with pores". Realism lines pull every model modern. Rebuild each prompt from this paragraph and the scene.
- Finish every still with the warm film grade and 0.08 grain, then put it beside the look book. Only pictures that pass go public (`decisions.md`, publish gate, 2026-11-27).
- Score the look on the "Slim Aarons" line of the [scoring note](score-ai-pictures.md).

## History

- 2026-11-26: Written when the name went back into prompts. Same day: Alex picked the 19-picture look book and ruled out the too-real and soft, muted looks.
