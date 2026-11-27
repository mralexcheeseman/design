# Changelog

Newest first. `## YYYY-MM-DD · brand · what changed`, then why.

## 2026-11-27 · off-duty-hotel-club · Day notes in Alex's diary voice
Alex asked for the Day notes to read as his own diary: storytelling, the reader brought in, clear actions with examples, and quotes from him that build on each point. He approved the second drafts ("perfect"). The notes for 23 to 26 Nov were rewritten live in The Back Office, and the voice is now a "Day notes" section in `learnings/README.md`. Ran `checklists/copy.md` on all four.

## 2026-11-27 · off-duty-hotel-club · Day wrap 26 Nov: two public playbooks
Nothing from 26 Nov had reached The Back Office. Two new playbooks written for readers from the day's private notes: `stop-pictures-drifting-off-your-look` (light words in the scene beat the style paragraph; the Villa Ceresa and Hotel Marisol remakes) and `check-ai-pictures-at-full-size` (the results gate, the small back-print rule, the man's head and hubcap badge caught at full size). Four pictures in `learnings/images/`. Mirrored to The Back Office with Day note `day-2026-11-26`, all unpublished. Fixed the broken heading at the top of this file. Ran `checklists/copy.md` on both playbooks and the Day note; the photography checklist covers product shots, so it does not apply.

## 2026-11-27 · off-duty-hotel-club · Layout sketch loses on Recraft
Ran T1 on Recraft's Nano Banana Pro. The control (no sketch) averaged 14 of 15 over 2 takes, and the sketch arm averaged 12.3 over 4. The sketch kept everyone in frame and garbled the shirt's small lines on 2 of 4 takes, and one take added a border and a drawn circle. `frame-ai-pictures-with-a-layout-reference` stays at try, as a fix for cut-off heads only. Three new lessons: `sketch-costs-the-small-print`, `sketch-can-leak-marks`, `score-full-size`. Ran `checklists/photography.md` and `checklists/copy.md`.

## 2026-11-26 · all · A log of credits lost
Alex asked us to track every credit a tool charges for nothing, so he can claim it back. New private note `learnings/notes/lost-credits.md`: the 24 Nov Recraft timeouts (60, refunded 26 Nov), the 25 Nov Recraft timeouts (188 over 13 images, claim drafted), and the 840 Firefly credits lost to duplicate takes on 26 Nov (our fault). Also flags an unexplained gap of about 255 Recraft credits. Ran `checklists/copy.md`.

## 2026-11-25 · off-duty-hotel-club · A reel line from one approved picture
Alex said "Do it all" to a reel line. Proved it on the Oriole pool picture (row OR1): Kling 3.0 Turbo clip, words set in FreightBig Pro and Neue Haas Unica through Express, ElevenLabs pool sound and lounge music, one ffmpeg finish, then a draft reel in the Social Planner. New playbook `learnings/playbooks/turn-one-picture-into-a-reel.md`; the thread-reach note gains the Base44 sandbox render and Kling file hosting routes. Finishing script in storefront-kit `tools/reel-line/`. Ran the copy checklist (the photography checklist covers product photos, so it doesn't apply).

## 2026-11-25 · off-duty-hotel-club · Shot results log themselves without a Zap
Alex asked for an agent instead of the Zap. A scheduled task now checks the Drive results folder every two hours and appends new files to the shot sheet's Results tab. Results gained Prompt, Cost, Credit pool and Note columns, and the version formula no longer reads IDs like GV3 as v3. Updated `learnings/notes/log-results-from-drive.md`. No checklist applies (no brand output).

## 2026-11-25 · off-duty-hotel-club · Locked house look and cast prep
Two private Recraft styles saved from people-free crops: "ODHC house look (Oriole pool)" and "ODHC house look (all hotels)", tested on two scenes (shot sheet LK1 to LK4). New playbook `learnings/playbooks/lock-cast-and-look.md`. Kling subjects for the cast and shirts are prepared but not uploaded, because Kling's upload host is blocked from the cloud; noted in `learnings/notes/what-a-thread-can-drive.md`. Ran `checklists/copy.md` on the playbook.

## 2026-11-25 · all · Pictures for the lessons
Alex asked for more images and examples in the lessons. New folder `learnings/images/` with three comparison sheets: the T3 test for `reuse-a-picture-that-works` (the post, words only, the post as image 2, Kling's copy), the T1 test for `frame-ai-pictures-with-a-layout-reference` (control, the blocking sketch, the result), and the Hôtel Solvane cove before and after generative expand for `make-vertical-cuts-for-stories` (that playbook sits on another open branch, so it links the image once both merge). A Pictures section added to the first two playbooks. In The Back Office the three playbooks now have before and after pictures and references, and Day note `day-2026-11-25` gained four pictures. All unpublished. Ran the copy checklist.

## 2026-11-25 · all · Day wrap: Flow through Chrome and naming from the prompt
Two private notes from the day's runs. `drive-flow-through-chrome`: a thread can queue Flow in Alex's signed-in Chrome, Nano Banana Pro stills there cost no Flow credits (40 keepers filed), and 12 Veo clips (8 Lite, 4 Fast, 160 credits) rendered in about three minutes. `name-results-from-the-prompt`: the local vision model in File Result picked the wrong shot at 90 per cent and its guesses on 40 Flow stills were unusable, so files are named from the shot ID in the prompt list. Day note `day-2026-11-25` rewritten in The Back Office to cover the whole day, unpublished. Ran the copy checklist.

## 2026-11-25 · off-duty-hotel-club · Social posts move to the brand type
Alex chose the brand pair for social ("new fonts"). Recorded in `decisions.md`, removed the Known drift line, and updated the type spec in `reuse-a-picture-that-works`: FreightBig Pro Book 56px lines and Neue Haas Unica 500 labels, from Adobe Fonts kit `lxh4muu`. The social factory's `build.py` is updated in project files. Ran the copy checklist.

## 2026-11-25 · off-duty-hotel-club · The Oriole pool post becomes a reference
Alex found the Oriole Palace pool post in Express and called it "absolutely perfect". Traced it to our own picture (`O01_oriole-palace_society.jpg`, Creative Cloud; post `oriole-1_O01.jpg`). Its prompt was never saved. New playbook `reuse-a-picture-that-works`: the six things that make it work, the type spec, and test T3 in the shot sheet (the picture as style and layout reference against the usual hero reference). Noted the social factory's type drift in the brand README. Ran the copy checklist.

## 2026-11-25 · off-duty-hotel-club · Hotel Marisol and the Surf Instructor
Added the seventh hotel to the system: `hotel-marisol` (terracotta `#a54a2a`), `garment-blue-jean` (`#62799a`, Comfort Colors 1717, matched by eye until the swatch arrives) and `ink-warm-white` (`#f7f4ec`). Crest master in `artwork/crests/heritage/`, screen crest in `assets/crests/`, Surf Instructor print files in `artwork/print-files/` (copied from storefront-kit `supply/`). README hotels table, merch range and `decisions.md` updated. Regenerated `tokens.css` and `index.html`.

Learnings: new lesson `print-file-on-generated-blank` in the product print playbook; the thread-reach note gains the blocked Recraft and Drive hosts, the Zapier-to-Drive route and Recraft's timeouts.

## 2026-11-25 · all · Picsart joins the studio
Alex has Picsart Professional. Added it to the private notes: what a thread can run (the connector reframes video and renders scenes for free but can't generate, so Alex generates on picsart.com) and the credit prices (Flux.2 Klein stills unlimited; other models cost credits at prices Picsart doesn't list). New lesson `picsart-for-what-nobody-else-has`: spend Picsart credits on models no other plan has. Added the `picsart` tool tag. Shot sheet rows PX1 to PX3. Ran the copy checklist.
## 2026-11-24 · off-duty-hotel-club · First layout-reference run, and the day's wrap
Logged the first T1 run in the layout-reference playbook. Every take had shown the lifeguard standing on his chair lowering a parasol, which the prompt itself asked for, so the line is fixed and the lesson `read-the-prompt-first` added. The control (T1a) on Recraft scored 11 and 11 of 15. The sketch takes (T1b) timed out on Recraft and still cost 60 credits, now in the private note on what a thread can drive. Ran the copy checklist.

## 2026-11-24 · off-duty-hotel-club · No Slim Aarons references
Alex settled it: we never reference Slim Aarons, and pictures carry no AI mention. Recorded in `decisions.md`. Took the name out of every prompt and the scoring note: the third score is now "Period look", and prompts describe a 1960s resort colour photograph for a travel magazine. Ran the copy checklist.

## 2026-11-24 · off-duty-hotel-club · Grain and vignette tried and dropped
Alex asked for a little grain and vignette to make pictures look more real. We tried both in the grade at two strengths on three pictures. He judged neither an improvement, so the grade is back as it was and the lesson came out of the product print playbook. Recorded in `decisions.md`.

## 2026-11-24 · off-duty-hotel-club · Picture process audit and a layout reference test
Audited how we make ODHC pictures against current advice from Google, OpenAI, Kling, Adobe and the ASA, and against the 27 scored Higgsfield takes (Claude Doc "ODHC picture process audit"). Added the playbook `learnings/playbooks/frame-ai-pictures-with-a-layout-reference.md` (status try): a wordless layout sketch as image 3, one job per reference, four takes per test. Added fail checks and the four-takes rule to the scoring note. Test rows T1a to T1c are in the shot sheet. Added `mend-in-firefly` to the product print playbook: near-keepers get mended with Generative Fill and Expand instead of a fresh take. Recorded Alex's call of no AI label in `decisions.md`. Ran the copy checklist.

## 2026-11-23 · off-duty-hotel-club · Shot results log themselves
Added the private note `learnings/notes/log-results-from-drive.md`. Files dropped in the Drive "ODHC shot results" folder now get a row in the shot sheet's new Results tab through a two-step Zap. Sheet formulas work out the ID, version, shot, tool, score and verdict from the file name, and My shots links each row to its newest file. Drive stays the store, and nothing goes to Cloudinary. Ran the copy checklist on the note.

## 2026-11-23 · all · AI learnings move into the repo
Added `learnings/`: one markdown file per playbook (reader's problem as the title, tool and model with the date tested, references, generic and ODHC prompts, settings, cost per usable result, what went wrong, the fix, status, and the making, tool and technique tags), plus three private working notes (scoring, credit prices, what a thread can run). The five playbooks mirror The Back Office's Playbook records slug for slug, so the site publishes from here. Gathered from the Photo Studio and Base44 builder notes, the social factory, the shot sheet and The Back Office data. CLAUDE.md and AGENTS.md now say to read it before running an AI tool and to add to it the same day. The drifting-buildings playbook was then updated to match The Back Office: the house change is now cut out of the clip for free, with a new lesson, `cut-past-the-change`. Ran the copy checklist.

## 2026-11-23 · off-duty-hotel-club · No italic second half, no contrast lines
The README allowed one "Line. *Italic line.*" hero headline; Alex's website rules ban it, and ban contrast lines in copy. README, decisions and the copy checklist now say so. The guest-book site and storefront-kit were rewritten to match. Ran the copy checklist.

## 2026-11-22 · off-duty-hotel-club · Guest-book site; Sélune drift noted
Built a public guest-book site in Base44 ("ODHC Guest Book", https://odhc-guest-book-9cdeb9ce.base44.app) for Instagram links: one page per hotel with its people and stories from storefront-kit `stories.js`, the uniform, and a waitlist on the store's Klaviyo list. Uses tokens.css and bundle.css as they are. Listed Hôtel Sélune under Known drift, since the store has it and this system doesn't. Ran the page and copy checklists.

## 2026-11-20 · off-duty-hotel-club · Type moves to Adobe Fonts
Alex approved FreightBig Pro for headings, Neue Haas Unica for text and Trajan Sans Pro 600 for the wordmark, after a side-by-side test on the live store. `fonts` and `families` in tokens.json now point at Adobe Fonts web kit `naj0wqi`, `bundle.css` loads the kit, and the README, merch notes and decisions say so. The crests stay Cinzel. Ran the page, copy and crest-and-print checklists.

## 2026-10-25 · off-duty-hotel-club · Head Gardener: brighter shirt, five-star crest
On Alex's notes: `garment-garden-green` became `garment-lawn-green` (#5a9e47), and two print inks were added, `ink-orange` for the job title and `ink-sage` for the hotel line and chest crest, making Head Gardener the one two-ink back, with its title stacked on two lines (`make_art.py` `stack=True`). The Villa Ceresa crest was redrawn without the spade and rake (swan before a loggia, cypresses, camellia, five stars). New artwork, crest and photography. Ran the crest-and-print, photography, page and copy checklists.

## 2026-10-23 · off-duty-hotel-club · Fifth hotel: Villa Ceresa, Head Gardener
Alex asked for a green Head Gardener shirt from a hotel in a picturesque part of Switzerland. Added Villa Ceresa (Lake Lugano, est. 1911, department 05): `hotel-ceresa` ink, `garment-garden-green`, the heritage crest (generated in the set's style with the four existing crests as reference, then traced by `trace_heritage.py`, which now also takes single-crest images), the back print from `make_art.py`, and `render_print.py`, which makes the 300 dpi and worn-ink PNGs. Copy that counted four hotels now says five. Ran the crest-and-print, photography, page and copy checklists.

## 2026-10-21 · edgework · Manila tokens and button arrows
Added `manila` and `manila-ink` for the essay folders on the new Edgework site, and allowed "→" inside buttons, matching what the site does. Ran the page and copy checklists against the site.

## 2026-10-21 · edgework · First version
New brand folder for Alex's public writing identity, Edgework (after Hunter S. Thompson). Holds the photographic mark library and TT2020 fonts as the master copy, tokens for the paper and night grounds, specs for the masthead, index card, file card, dispatch, Hey Rube band, marks, typed text, scrawl and button, and the settled decisions. Used by the private Owl Farm newsroom and the new public Edgework site. `build-preview.mjs` now reads an optional `meta.preview` block so a brand can name its own display and label styles; Off Duty Hotel Club's view is unchanged.

## 2026-10-15 · off-duty-hotel-club · Artwork and a one-page view
Added the crest source sheet, explorations, traced masters and scripts (`artwork/crests/`), every supplier print file (`artwork/print-files/`) and the original product renders (`assets/photography/source/`), copied from storefront-kit `supply/`. This repo is now the master copy of the artwork. Added `index.html`, a generated one-page view of colours, type, crests and components, checked in CI.

## 2026-10-15 · off-duty-hotel-club · Known drift cleared
storefront-kit#3 brings the live store in line with this system, so the drift list in the brand README is now empty.

## 2026-10-15 · off-duty-hotel-club · First version in GitHub
Brought in from the Design System artifact (version 1, captured from the Base44 storefront with the agreed improvements). Added in version 2 of `tokens.json`: motion, focus, breakpoint, layout, ratio, z-index and print tokens, plus phone sizes for display, headline, title and wordmark. Added `tokens.css` and its build script, specs for the storefront components the system didn't cover yet, `merch.md`, `decisions.md` and shared review checklists. Crest assets are the traced heritage vectors from storefront-kit, recoloured to each hotel's ink.
