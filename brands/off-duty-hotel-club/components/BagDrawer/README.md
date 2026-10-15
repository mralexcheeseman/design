# BagDrawer

The bag, sliding in from the right.

- The consumer provides: the line items (photo, role, size, quantity, price), the subtotal and the checkout action.
- A `drawer-width` panel on `paper` with `shadow-drawer` over `scrim`; full width below the phone breakpoint. The heading "Your bag" is `title`.
- Each line: a 4:5 thumbnail on `stone`, the role, "Size M" in `body-sm` `ink-2`, a QuantityStepper and a "Remove" text button.
- The footer is sticky: subtotal, one block Button ("Checkout"), and the one preview line allowed in the bag.
- Empty: an EmptyState ("Your bag is empty.") with a TextLink to the shop.
- Escape and the scrim close it; focus is trapped inside while open and returns to the bag button.
