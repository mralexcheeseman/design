# SignupForm

An email field and a submit action: the footer newsletter ("The staff noticeboard") and the per-shirt waitlist.

- The consumer provides: the label, one line of context, the button text, the thanks message and the privacy note.
- The field is an underline input: 1px `line-strong` bottom border, `body` text, no box and no radius. The visible label sits above it; a placeholder never replaces the label.
- The submit is a TextLink on the footer and a Button on the product page waitlist (the waitlist is the product page's primary action while orders are closed).
- States: idle, sending (button text "Sending"), done (the thanks line replaces the form: "Nearly there. Check your inbox to confirm." for double opt-in), error (one `body-sm` line in `accent`: "That didn't go through. Try again.").
- Never pre-tick consent, add a pop-up or ask for more than an email.
