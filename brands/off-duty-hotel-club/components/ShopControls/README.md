# ShopControls

The bar above the shop grid: collection tabs on the left, sort and the result count on the right.

- The consumer provides: the collections (the hotels), the selected one, the sort options and the count.
- A row between two `line` hairlines. Tabs are `body-sm`: `ink-3` at rest, `ink` with a 1px underline when selected.
- On phones the tabs scroll sideways without a visible scrollbar, and sort moves under them.
- Sort is a native select styled as text with a small chevron. "Clear filters" is a TextLink.
- With four shirts, keep it to the hotel tabs and sort. Add filters only when the range needs them.
