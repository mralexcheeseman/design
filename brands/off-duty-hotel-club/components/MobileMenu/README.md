# MobileMenu

The phone navigation: a drawer from the left holding the nav items.

- The consumer provides: the nav items and the close action.
- A `drawer-width` panel on `paper`, full width below the phone breakpoint, over `scrim`, with `shadow-drawer`.
- Items are set in `title` (serif) on `line` hairlines, each at least `tap-target` tall.
- Opens over `duration-slow` with `ease`. Escape and the scrim close it; focus returns to the menu button.
- No icons, images or promotions inside the menu.
