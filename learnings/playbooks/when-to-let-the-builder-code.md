---
slug: when-to-let-the-builder-code
title: Know when to let the Base44 builder write the code
dek: Eight builder turns across two apps cost about 36 credits. Features we could describe in one paragraph worked first time. The open-ended polish cost the most and needed the most fixing.
making: website
tools: [base44]
techniques: [builder-prompts]
models:
  - name: Base44 builder
    tested: 2026-11-22
status: proven
cost_usable: About 6 credits a feature we kept
back_office: published
date: 2026-11-22
updated: 2026-11-23
---

# Know when to let the Base44 builder write the code

Eight builder turns across two apps cost about 36 credits. Features we could describe in one paragraph worked first time. The open-ended polish cost the most and needed the most fixing.

## What happened

Over the weekend of 22 November we built two Base44 apps, the public guest-book site and a private social planner. The first pass of each was typed by hand. After that the builder got one feature per turn, and we read the credit counter before and after each one.

The planner's five features each fitted in a paragraph, and all five worked first time. The restyle landed because the exact token values were pasted into the prompt. The guest book's open-ended polish turn cost 9.4 credits, the most of any, and acted on every idea we had mentioned, including the ones we had only floated. It added "Entry no. 01", which breaks the brand's rule against numbering, so we took it out by hand.

| Turn | Credits |
| --- | --- |
| Open-ended polish (needed the most fixing) | 9.4 |
| Restyle to the design system | 5.94 |
| Link-in-bio page | 4.3 |
| Month calendar | 3.63 |
| Villa Ceresa guest book | 3.6 |
| Three caption suggestions | 3.47 |
| Import from JSON or CSV | 3.14 |
| Instagram grid preview | 2.81 |
| Cloud testing agent | 2.3 |
| First builds, by hand | 0 |

## What to do

Give the builder one feature per turn, written as a single paragraph, with the brand's tokens and voice rules pasted in. Type anything you can describe to the word by hand, which costs nothing. Make a checkpoint after each commit, and add the app's domain to the Adobe Fonts kit before you judge the type.

Review every builder diff against the design system. It hard-coded an 18px font size that isn't a token, and its copy and pictures can disagree (a boat "not in the water since 1969" shown on the lake).

## Prompt (generic)

```
Add a month calendar to the Posts page. Show each post as a chip on its scheduled date, coloured by platform. Dragging a chip to another day changes its scheduled date. Use only these colours: [paste your tokens]. Leave the rest of the app as it is.
```

One feature, one paragraph, the tokens pasted in, and a last line that fences off the rest of the app.

## For Off Duty Hotel Club

Paste the relevant values from `brands/off-duty-hotel-club/tokens.json` and the copy rules from `decisions.md` (no contrast lines, no italic second half in headlines, no numbering) into every builder prompt. Full notes from the guest-book turns: `/mnt/project-files/odhc-guest-book/base44-builder-learnings.md`.

## Settings

| Setting | Value |
| --- | --- |
| Builder turns | 8, plus one testing-agent run |
| Kept as they came | 6 of 8 |
| Hand-built first passes | 2, at no cost |

## Cost

About 6 credits a feature we kept: 36.3 credits over eight turns, and six of the eight stayed as they came.

## Lessons

| Lesson | Status |
| --- | --- |
| `builder-turn-cost`: A builder turn costs about 3 to 4 credits for one clear feature and about 6 for a whole-app restyle. | proven |
| `hand-code-exact-changes`: Changes you can describe exactly cost nothing by hand and land word for word, which leaves the builder for whole new features. | proven |
| `adobe-fonts-need-the-domain`: Adobe Fonts stay blank on a base44.app address until that domain is added to the web kit, and the page falls back to Georgia and Helvetica meanwhile. | proven |
| `open-ended-turns-cost-most`: An open-ended polish turn cost 9.4 credits, more than twice a specific feature, because the builder explores before it acts. | tested |
| `builder-takes-every-idea`: The builder builds any idea you mention in passing, so a prompt lists only the ideas you would accept. | tested |
| `paste-tokens-into-restyles`: Pasting the exact token values into a restyle turn got them applied across every screen in one go. | tested |
| `builder-needs-the-brand`: The builder's own caption prompt called every hotel alpine, so anything it writes gets a brand check before it ships. | tested |
| `testing-agent-is-shallow`: The Base44 testing agent works on its own sample records, so a pass says little about real data. | tested |
| `checkpoint-after-commit`: A checkpoint taken straight after an edit can capture the commit before it, so check the git log before a deploy. | tested |

## Next to try

Hand the testing agent a written checklist and see whether it goes deeper than the first screen.

## History

- 2026-11-22: Guest-book and planner turns measured.
- 2026-11-23: Written up as a playbook.
