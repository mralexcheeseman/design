# Header

The sticky bar under the announcement bar: navigation left, Wordmark centred, search and bag right.

- The consumer provides: the nav items (Shop, The hotels, Story), the bag count and the current page.
- A three-column grid, `header-height` tall (64px below the tablet breakpoint), on `paper`. A 1px `line` appears under it once the page scrolls.
- Nav items are `body-sm` in `ink`; the current page and hover get a 1px underline that draws in over `duration-slow`.
- Bag shows its count; the count sits in a `radius-full` dot in `accent` only when above zero.
- Below the tablet breakpoint: the nav collapses into the MobileMenu button on the left, and search and bag become 20px Lucide icons with accessible names.
- Never put a promo, a second row of links or the preview notice in the header.
