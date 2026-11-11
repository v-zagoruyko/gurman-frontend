# Delivery build checks — 2026-11-11

## Product data

A standard-library HTMLParser comparison against the exact pre-edit snapshot confirmed equality for all 29 dish identifiers, dish names, portion labels, numeric price values, and four verified set descriptions. There are 29 individual `.dish-photo` elements. Opening order follows approved B (pork neck, pork ribs, chicken assortment); pork loin remains fourth. Category photography and the hidden repeated ingredient filler were removed. No ingredients or service promises were introduced.

The two phone links retain `tel:+73452217565` and `call_delivery`; the PDF link retains `/files/menu-delivery.pdf`, its analytics identifiers, and a descriptive accessible name. Canonical, Open Graph, title, and description remain. Metrics initialize only on the production hostname, so the localhost browser checks cannot send page statistics.

## Implementation

Static HTML/CSS; no package or build configuration and no typecheck/lint command exist. No dependency was added. Golos Text is self-hosted as `assets/fonts/golos-text.ttf` (184,292 bytes) with `assets/fonts/OFL-Golos-Text.txt`. Source: the Google Fonts repository, `ofl/golostext/GolosText[wght].ttf` and `ofl/golostext/OFL.txt`, fetched 2026-11-11. No new raster image ships with the delivery page; the existing Open Graph image is unchanged metadata.

The current section is reflected by `aria-current="location"`; all four section anchors and all menu rows work without JavaScript. Scroll updates are throttled with `requestAnimationFrame`. No entrance animation, smooth scrolling, or animated transition is used, so reduced-motion needs no separate animation override. The sticky navigation and fixed phone action keep the primary browsing path in view.

## Mechanical checks

- `git diff --check`: clean.
- Text contrast from CSS sRGB values: ink on white 15.99:1; muted on white 6.88:1; placeholder text on photo well 6.02:1; white on phone action 11.00:1.
- Main reading text is at least 19px, labels at least 14px, interactive targets at least 54px.
- The Impeccable detector ran once; full output is `detector.json`, interpretation and the one mechanical correction are in `detector-notes.md`.

## Evidence limits

The preserved spec has OCR box errors: some first/second portion labels point at the same or neighboring line, and the selected navigation label points at the section title. Closed comps/spec/plates are intentionally unchanged. Build-state artifact metadata was corrected from `null` to `delivery/index.html` after the first hero pass scanned unrelated SVG icons in the banquet homepage. The real approved comp and fresh Chrome captures remain visual authorities; no image is fabricated to satisfy a gate.

Fresh Chrome captures: `hero-repro.png` 984×1599; `desktop.png` 1440×6239; `mobile.png` 390×4882; `desktop-first.png` 1440×1000; `mobile-first.png` 390×844. All files were opened and found valid. Hero overall 0.8895/`match` still has hard-veto crop findings; build phase remains honestly open. The 0.6052/`drift` final diff compared the portrait reference with a full-page desktop capture, so its region scores are not a valid fidelity comparison. The fresh reviewer opened the paired crops and found no material visual defects; desktop intentionally spreads each comparison row into photo/name/numbers columns.
