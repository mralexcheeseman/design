# Learnings

What we've learned making things with AI tools: the prompts, settings, costs, what went wrong and the fix. This folder is the master copy. [The Back Office](https://app.base44.com/apps/6b044d6aaa73f82d3c126031/editor/preview) (Base44 app `6b044d6aaa73f82d3c126031`) publishes the playbooks marked `published` from here, so the two always say the same thing.

**Before you run any AI tool for a brand, read the playbooks for what you're making and the tools you'll use.** Start from their prompts and settings rather than from a blank page, and check the `tested` date on each model before you trust a price or a quirk.

## Playbooks

Each one answers one reader's problem. Public on The Back Office unless marked private.

| Playbook | Making | Tools | Status | Cost per usable result | Tested |
| --- | --- | --- | --- | --- | --- |
| [Make your best picture the reference for the next ones](playbooks/reuse-a-picture-that-works.md) | photo | nano-banana-pro, higgsfield, adobe-express | try | Free on Higgsfield Unlimited | 2026-11-25 |
| [Stop AI pictures cutting off heads and crowding the frame](playbooks/frame-ai-pictures-with-a-layout-reference.md) | photo | nano-banana-pro, higgsfield, recraft | try | Free on Higgsfield Unlimited | 2026-11-24 |
| [Stop buildings drifting when you stitch stills into video](playbooks/stop-buildings-drifting.md) | video | kling, recraft | tested | 142 credits a clip | 2026-11-23 |
| [Keep a scroll-scrubbed video sharp on the web](playbooks/keep-scroll-video-sharp.md) | website | kling, base44 | tested | Free | 2026-11-23 |
| [Get your product's print right on an AI model](playbooks/product-print-on-ai-model.md) | photo | nano-banana-pro, higgsfield | proven | About 25 cents a picture | 2026-11-23 |
| [Get editable text into Adobe Express from HTML](playbooks/live-text-in-adobe-express.md) | social | adobe-express | proven | Free | 2026-11-21 |
| [Know when to let the Base44 builder write the code](playbooks/when-to-let-the-builder-code.md) | website | base44 | proven | About 6 credits a feature | 2026-11-22 |

## Working notes (private)

Kept out of The Back Office: credit planning, account reach and house methods.

| Note | What it covers |
| --- | --- |
| [Score AI pictures the same way every time](notes/score-ai-pictures.md) | The Real, Shirt and Period look score out of 15 |
| [Pick where to run a model by what each credit costs](notes/spend-credits-before-renewal.md) | Unit prices per app, the use-every-credit rule |
| [Know which tools a Claude thread can run and which need Alex](notes/what-a-thread-can-drive.md) | Connector reach, blocked hosts, small fixes |
| [Log every generated picture in the shot sheet without typing](notes/log-results-from-drive.md) | Drive folder to Sheets via a scheduled Claude task, file-name parsing formulas |
| [Run paid Higgsfield video through ChatGPT and keep Unlimited stills on the website](notes/run-higgsfield-through-chatgpt.md) | The ChatGPT standing brief, one-cell job blocks, which jobs go where |
| [Run Google Flow from a thread through Alex's Chrome](notes/drive-flow-through-chrome.md) | Free Nano Banana Pro stills, queueing Veo clips back to back, limits |
| [Name generated files from the prompt list](notes/name-results-from-the-prompt.md) | Why the local vision model lost to the shot ID in the prompt |

Balances, renewal dates, account ids and anything secret stay in project memory and never go in this repo.

## Tags

Every file carries the same three public tags as The Back Office.

- **making**: `photo`, `video`, `website`, `social`
- **tools**: `kling`, `recraft`, `higgsfield`, `nano-banana-pro`, `google-flow`, `firefly`, `adobe-express`, `base44`, `elevenlabs`, `picsart`
- **techniques**: `waypoint-stills` (Waypoint stills), `edit-chain` (Edit chains), `first-last-frame` (First and last frames), `web-encoding` (Web video encoding), `reference-images` (Reference images), `refine` (Refining a take), `film-look` (Film look), `scoring` (Scoring results), `html-import` (HTML import), `builder-prompts` (Builder prompts). Private notes also use `credit-planning` and `workflow`.

The labels match `TECHNIQUES` in The Back Office's `src/lib/logbook.js`. A new technique gets added in both places.

## Status

Each playbook and each lesson carries one of three:

- **proven**: worked every time across several runs or projects.
- **tested**: worked in the runs we made, at least once.
- **try**: an idea or a single result worth testing next.

A playbook takes the status most of its main lessons share. Move a lesson up only with a new run behind it.

## Adding to it

Every thread that runs an AI tool adds what it learned the same day, here first and then in The Back Office.

1. **New problem?** Copy [`_template.md`](_template.md) to `playbooks/<slug>.md`. Name it after the reader's problem, as a task ("Stop buildings drifting when you stitch stills into video"). The slug never changes once published.
2. **Existing problem?** Edit that playbook: add the lesson to its Lessons table with a short slug, update the prompt or fix if they changed, bump `updated`, re-date the model under `models`, and add a line to History. Edit a lesson in place rather than adding a near-duplicate.
3. **Always write** the reader's problem as the title, tool and model with the date tested, the references, a generic prompt and the one we used, settings, cost per usable result, what went wrong, the fix and a status.
4. **Mirror it** to The Back Office: one Playbook record per file (same slug, fields named as in the frontmatter and sections) and one Learning record per Lessons row with `playbook_slug` set. Leave `published` off until Alex says go. The thread that owns The Back Office does this if you can't.
5. **Add a line** to the root `CHANGELOG.md`.

### Writing rules

Write for a creative or brand marketer who wants tested answers. Lead with the failure and the picture. Plain British English, specific numbers, no AI phrasing. No contrast lines ("not X, it's Y" or "X. Y." pairs) and no headline with an italic second half (see `brands/off-duty-hotel-club/decisions.md`, 2026-11-23). Run `checklists/copy.md` on anything that will be published.

Brand values in an example prompt (hex codes, hotel names, shirt names) come from that brand's `tokens.json` and README, never from memory.
