# SizePicker

The required size choice on a product page: six square buttons, none selected by default.

- The consumer provides: the sizes (XS to XXL), the selected size, sold-out sizes (disabled, struck through) and the error text.
- Start with nothing selected. If Add to bag is pressed without a size, show "Choose a size first." in `accent` below. Never default to XS.
- Borders use `line-strong` so they read at 3:1. The selected size is an `ink` fill.
- "Size guide" is a TextLink that opens the fit modal.
