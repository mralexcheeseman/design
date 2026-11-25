---
slug: run-higgsfield-through-chatgpt
title: Run paid Higgsfield video through ChatGPT and keep Unlimited stills on the website
dek: ChatGPT's Higgsfield app can generate, with Unlimited switched off for connected apps. Paid video goes through ChatGPT with a standing brief. Free stills stay on the website.
making: video
tools: [higgsfield]
techniques: [workflow, credit-planning]
models:
  - name: Seedance 2.0
    tested: 2026-11-24
  - name: Nano Banana Pro
    tested: 2026-11-24
status: try
cost_usable: Same credits as the website for paid models
back_office: private
date: 2026-11-24
updated: 2026-11-24
---

# Run paid Higgsfield video through ChatGPT and keep Unlimited stills on the website

ChatGPT's Higgsfield app can generate, with Unlimited switched off for connected apps. Paid video goes through ChatGPT with a standing brief. Free stills stay on the website.

## What happened

Our own Higgsfield connector reads balance, models and past generations, and can't generate. Alex's ChatGPT (Plus, no API) has a Higgsfield app that can. Asked to check the account on 2026-11-24, ChatGPT reported: Plus plan, 1,132.5 credits (our connector read the same), **Unlimited generation unavailable through connected apps**, 4 free generations left (motion control and object replacement only, 480p to 720p, up to 30 s), and Seedance 2.0 and 2.5 as the Unlimited-capable video models. Higgsfield's own model list also flags Nano Banana Pro, Nano Banana 2 and 2.1, Soul 2 and GPT Image 2 as Unlimited-capable, so the website's Unlimited still applies there. Through the app, the same stills would cost credits.

## What to do

1. Make a ChatGPT Project with the Higgsfield app on and paste the standing brief into its instructions. The brief is in project files at `higgsfield-chatgpt/chatgpt-brief.md`. It makes ChatGPT check for free or Unlimited first, quote the cost and wait for `go`, pass the prompt word for word, never buy or top up, and end with one LOG line.
2. Each shot-sheet row on this route has a one-cell job block in **Paste this**: `JOB <ID>`, model, settings, start-image link, takes, save-as names, expected cost and the prompt. Start images use the public store links (`https://offdutyhotel.club/assets/stories/<hotel>/<name>.webp`), so nothing needs attaching.
3. Results come back by download: ChatGPT gives links (or saves to Drive itself, if its Drive connection can write). Drop each take in the Drive folder "ODHC shot results" under the save-as name. The results log and sheet formulas pick it up from the leading ID and `v1`/`v2` (see [log-results-from-drive](log-results-from-drive.md)).
4. A thread can check afterwards with the read-only connector: `show_generations` lists each take with its model, and `balance` shows the credits actually spent.

## Route by job

| Job | Route |
| --- | --- |
| Nano Banana Pro stills | Higgsfield website, Unlimited on (free) |
| Seedance 2.0 video | ChatGPT, after a quoted cost and Alex's `go`. If the website shows Unlimited for Seedance 2.0 on the Plus plan, run it there for free. |
| Motion control, object replacement | ChatGPT, using the free generations first |

## Lessons

| Slug | Lesson | Status |
| --- | --- | --- |
| `unlimited-is-website-only` | Higgsfield's Unlimited mode is off for connected apps, so a model that is free on the website costs credits through ChatGPT. Route Unlimited jobs to the website. | tested |
| `brief-once-paste-a-job` | Put the rules in the ChatGPT Project instructions once, so each run is a single pasted job block with the cost check built in. | try |
| `public-links-as-start-images` | Give the app public image links from the live store, so a job needs no attaching. Ask for the file only if the app refuses a link. | try |

## History

- 2026-11-24: Route set up. Brief written, S1 to S3 marked for ChatGPT. No credits spent yet.
