# QuantityStepper

Minus, the number, plus.

- The consumer provides: the quantity, the min (1) and max, and the change handler.
- A 1px `line-strong` box, square corners. Buttons are Lucide plus and minus at 1.5px, each at least `tap-target`.
- The number uses tabular figures. Minus is disabled at the minimum; removing a line is the bag's "Remove" action, never quantity zero.
- Buttons have accessible names ("Decrease quantity", "Increase quantity").
