# Components

Postmark is built on the shared storefront (`storefront-kit/src`), the same components Off Duty Hotel Club uses. Their specs are in `../../off-duty-hotel-club/components/` and apply here with Postmark's tokens, with these differences:

- **HotelCard becomes DestinationCard:** the ring postmark on `stone`, then the number in the destination ink, the destination name and its pattern line.
- **Wordmark:** one line, "POSTMARK" in `wordmark` (Barlow Condensed 600, 0.22em tracking). No second line.
- **ProductCard:** name ("Amalfi Crossbody"), then the pattern line ("Lemons and majolica"), then the price. No heart.
- **SizePicker:** not used. Straps have no options.

Write a component README here before building anything Postmark-only.
