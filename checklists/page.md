# Page review

## Look at it
- [ ] Rendered and screenshotted at 1440px and 390px wide (`review-desktop`, `review-phone`), not just read as code.
- [ ] Clicked through what the change touches: add to bag (with and without a required size), bag, search, saved, checkout, mobile menu, preview panel.

## Tokens
- [ ] Every colour, font, size, space, radius, shadow and duration is a token. No stray hex or rgba values in components.
- [ ] Nothing is set below 12px, on any breakpoint.
- [ ] Type uses the named styles (display, headline, title, body, body-sm, label, wordmark). No one-off sizes.
- [ ] Corners follow the brand's radius rule; shadows only where the brand allows them.

## Hierarchy and patterns
- [ ] One solid button per view, for its primary action. Everything else is a text link.
- [ ] The italic second-line headline appears only in the hero.
- [ ] None of: badges, ticker strips, quick-add on hover, heart bubbles, arrows on links, captions over photos, a back/front toggle on cards.
- [ ] The accent is used only where the brand README allows (focus, errors, small counts). Hotel or collection colours stay small.
- [ ] Product grid is three across on desktop, two on phones; a lone last card keeps its width.

## Accessibility
- [ ] Body text 4.5:1 against its ground; control borders and focus rings 3:1.
- [ ] Every control can be reached by keyboard and shows the focus ring (`focus-width`, `focus-offset`, `focus-color`).
- [ ] Every tap target is at least `tap-target` (44px).
- [ ] Icon-only buttons have an accessible name. Images have alt text, or empty alt when decorative.
- [ ] With reduced motion on, transitions and reveals are off and nothing is hidden.

## Motion
- [ ] Transitions use `ease` and `duration-fast`, `duration-slow` or `duration-slower`. Photos scale to `hover-scale`; buttons never lift.
