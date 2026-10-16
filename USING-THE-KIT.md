# Using the design kit
Checked 16 October 2026 for Off Duty Hotel Club.

## Start here
The brand README, tokens.json, components, decisions.md and merch.md in brands/off-duty-hotel-club are the design source. Read them before creating a page, email, advert or product asset. GitHub wins when the Claude artifact or an old Figma file differs. The Factory recovery library is an inventory, not a replacement for this kit.

## Everyday workflow
1. State the deliverable, audience and action: for example, a welcome email leading to the collection.
2. Reuse approved crests and images; preserve exact hotel names and the dry, deadpan voice. Clearly describe the hotels as fictional.
3. Use existing tokens and component specs. Add a specification before introducing a new component.
4. Review the draft at desktop and phone sizes. Run the relevant page, copy, photography or print checklists.
5. Save changes on a branch, record them in CHANGELOG.md and open a pull request. Alex reviews public output and spending.
6. When tokens change, regenerate tokens.css and index.html, update the corresponding storefront theme, and record the revision used in Figma. Update the Claude artifact or explicitly mark it as behind.

## Website and signup
Implementation belongs in storefront-kit. Use SignupForm: visible email label, underline field, sending/success/error states, no popup and no extra personal fields. The footer invitation is “The staff noticeboard”. A specification is not a connected subscription service: verify provider acceptance, confirmation, consent, duplicate handling and unsubscribe end to end.

## Figma
Use a clearly named Off Duty working file and record the design repository revision on its cover. Recreate colours, text styles and components from the current kit, then use instances. Preserve the approved crests rather than generating new versions. Figma and GitHub are not automatically synchronised. The older Ecommerce Design Library file has not been verified as a complete mirror of this kit.

## HTML email
Use the brand colours, voice and imagery, but create email-specific components with documented fallbacks. Do not paste web components or CSS directly into an email. Keep text and buttons live, provide font fallbacks, use hosted email-compatible images, and test Gmail, Outlook, Apple Mail, mobile and dark mode. Add working sender details, unsubscribe and a plain-text alternative. Klaviyo remains the proposed nurture platform; account access, sender authentication and integration are unverified. No email templates or sending integration were found in this design snapshot.

## Artwork
Screen assets are in assets/; supplier masters are in artwork/. Working sample copies are in storefront-kit/supply. The current snapshot has four chest exports but only Security and Ski Patrol back exports. It is not a complete four-shirt supplier pack. Traced masters still need cleanup and supplier/sample approval. Production approval cannot be inferred from a successful build.

## Checks and limits
- GitHub Actions passed token/preview freshness checks for dcd89fa5ff9e09abc4fddb3547065a0ab1b2b46b; a subsequent Postmark addition also has a successful run. These are generated-file checks, not visual or checkout tests.
- Every Off Duty colour token matched the fetched storefront theme.
- 22 components have specifications; nine folders have visual previews, including Cover. Many interactive components are intentionally spec-only.
- Preview references were checked against the repository tree. Cover linked to a missing README; this branch adds it.
- Cover's decorative colour blocks and fixed 960px width conflict with customer-facing brand rules. Treat it as a legacy library cover, not an approved reusable campaign layout.
- merch.md's Printful/Prodigi sample paragraph conflicts with the 15 October Factory brief proposing Inkthreadable/Shirt Monkey. Confirm actual supplier feedback before relying on it.
- Local Node execution failed on system OpenSSL access even after an escalated retry. Desktop/phone rendering, live checkout, Figma parity and subscriber capture have not passed review in this audit.
- Page checklist: partial source review only, visual/interaction items pending. Copy checklist: applied to this operational guide; it is not customer campaign copy. Photography/print release checks: not passed; no artwork was changed.

## Reusable brief
“Use mralexcheeseman/design, brands/off-duty-hotel-club as the source of truth. Read AGENTS.md, the brand README, tokens, components and decisions first. Create [deliverable] for [audience] with [primary action]. Reuse existing artwork and preserve the brand voice. Run the applicable checklists, show desktop/mobile output, and report anything unverified. Do not publish, send emails, order samples or spend money without Alex's approval.”

## Next practical deliverable
One HTML welcome email and the inline signup form, both using this kit. Confirm the email account and site source first, build drafts, test subscription and rendering, then seek approval for publication and sending.
