---
name: Gurman Delivery Menu
description: A calm delivery menu that keeps each dish, its portions, and prices easy to compare.
colors:
  paper: "#F3EDDC"
  ink: "#2E1A2A"
  muted: "#674F62"
  photo-well: "#E9E1D2"
  divider: "#D4CBC0"
  action: "#5B2346"
typography:
  display:
    fontFamily: "PT Serif, Georgia, Times New Roman, serif"
    fontSize: "calc(32 * var(--unit))"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.025em"
  display-wide:
    fontFamily: "PT Serif, Georgia, Times New Roman, serif"
    fontSize: "3rem"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.025em"
  body:
    fontFamily: "Golos Text, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
    fontSize: "19px"
    fontWeight: 400
    lineHeight: 1.5
  dish-title:
    fontFamily: "Golos Text, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
    fontSize: "calc(20 * var(--unit))"
    fontWeight: 600
    lineHeight: 1.3
  dish-title-wide:
    fontFamily: "Golos Text, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
    fontSize: "25px"
    fontWeight: 600
    lineHeight: 1.3
rounded:
  photo: "calc(8 * var(--unit))"
  action: "calc(8 * var(--unit))"
spacing:
  unit: "clamp(1px, 0.25641vw, 2.52308px)"
  gutter: "max(1rem, calc(11 * var(--unit)))"
components:
  section-link:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.muted}"
    height: "54px"
  photo-placeholder:
    backgroundColor: "{colors.photo-well}"
    textColor: "{colors.muted}"
    rounded: "{rounded.photo}"
  portion-comparison:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
  call-button:
    backgroundColor: "{colors.action}"
    textColor: "{colors.paper}"
    rounded: "{rounded.action}"
    height: "54px"
---

# Design System: Gurman Delivery Menu

## Overview

**Creative North Star: “Спокойная витрина” (a calm counter display).** This design system documents `/delivery/` only. The banquet homepage keeps its existing visual design.

The page presents each item as one comparison unit: an individual photo well, a dish name, and aligned portion–price rows. Section links keep the long menu easy to navigate, while the call action stays available at the edge of the viewport.

**Key Characteristics:**

- Warm cream palette shared with the restaurant homepage, with cherry navigation and phone action.
- Flat rows and thin dividers instead of card shells.
- Every dish has its own neutral photo placeholder until a real item photo is supplied.
- PT Serif carries the restaurant name and headings; Golos Text keeps dish names and prices easy to scan.

## Colors

The surface uses the homepage cream, plum ink, warm placeholders, and cherry accents.

### Primary

- **Charcoal Ink** (`colors.ink`): headings, dish names, and the active navigation label.
- **Graphite Action** (`colors.action`): the persistent phone action, kept separate from ordinary text.

### Neutral

- **Paper White** (`colors.paper`): the page ground and light text on the action button.
- **Photo-Well Gray** (`colors.photo-well`): empty image areas; it signals missing photography without imitating food.
- **Muted Gray** (`colors.muted`): address, inactive navigation, counts, and placeholder captions.
- **Divider Gray** (`colors.divider`): thin rules between portions and dishes.

**The Honest Image Rule.** A photo well stays neutral and clearly marked until a real photo for that dish is available.

## Typography

**Display Font:** PT Serif (with Georgia and serif fallbacks)

**Body Font:** Golos Text (with system sans-serif fallbacks)

**Character:** A single open, humanist sans-serif family keeps Russian copy readable and lets prices carry emphasis through weight and alignment.

### Hierarchy

- **Display** (600, 32px on phones / 48px on desktop, 1.15 line-height): the page title.
- **Section title** (600, 23px at the base unit, 1.2 line-height): menu section headings.
- **Dish title** (600, 20px mobile / 25px desktop, 1.3 line-height): the item name.
- **Body** (400, 19px, 1.5 line-height): address, portions, and supporting text.
- **Caption** (400, at least 14px): photo-placeholder label and compact supporting details.

**Type roles.** Use PT Serif at weight 700 for the wordmark, page title, and section headings. Use Golos Text for dish names, descriptions, portions, prices, and controls. Keep the existing comparison layout.

## Layout

The layout is fluid and centered, with an 11-unit minimum gutter and a maximum content width of 61.5rem at compact widths and 66rem above 1100px. The first viewport moves directly from identity and title to four section links and the first dish rows.

Below 1100px, each dish uses a photo well beside its name and stacked portion–price lines. At desktop widths, the photo stays 8.75rem square and the name and numeric comparison occupy separate columns. The section navigation sticks to the top; the phone action remains fixed at the bottom. At very narrow widths, the section links wrap into two rows and the photo column becomes compact.

## Elevation & Depth

The surface is flat: it uses no shadows, gradients, or blur. Depth and grouping come from the pale photo wells, fine dividers, and the contrast of the graphite phone action against the white page.

## Shapes

Dish rows are open and rectangular, separated by a single thin rule. Photo wells and the phone action use gently rounded corners (8px at the mobile base unit and about 10px at desktop). Do not add pill-shaped price badges or decorative card frames.

## Components

### Section navigation

Plain text links sit above a fine divider. The current section uses charcoal text, a heavier weight, and a short underline. Keep all four links visible and give each a touch target at least 54px high.

### Dish row

Each row pairs one dish with one photo well. Keep the name adjacent to its portion–price comparison; align prices to the right and separate multiple portions with a fine rule.

### Photo placeholder

Use an individual pale-gray well with a simple camera outline and the two-line label “Фото блюда / пока нет”. It is a temporary state, not an illustration or substitute stock photo.

### Phone action and PDF link

The phone action is a wide cherry link with white text and the confirmed delivery number. Keep the PDF as an underlined text link near the restaurant wordmark; both stay visually direct and easy to identify.

## Do's and Don'ts

### Do:

- **Do** preserve every verified dish, portion, price, and set description.
- **Do** give every dish its own clearly labelled photo well until its real photo is supplied.
- **Do** keep the ordinary body text at least 19px, captions at least 14px, touch targets at least 54px, and text contrast at least 5:1.
- **Do** keep the page usable without JavaScript and preserve its phone and PDF paths.

### Don't:

- **Don't** generate food imagery, reuse one dish photo for other items, or invent ingredients.
- **Don't** introduce newspaper columns, promotional hero photography, price pills, gradients, or ornamental illustration.
- **Don't** add unverified service claims, menu details, or ordering flows.

## 2026-11-11 brand refinement

Approved direction: an everyday Gurman menu, with usability first. Reuse the homepage cream (#F3EDDC) and cherry (#5B2346), PT Serif for the wordmark and headings, and Golos Text for menu data. Keep comparison rows, placeholders, sticky navigation and phone ordering. No ornaments or gold decorations. Earlier screenshots and finish-review evidence describe the monochrome iteration, not this final palette. Current visual browser verification is unavailable because the browser access host is missing; calculated text contrast is at least 5:1. The design sidecar remains a historical export of the earlier iteration.
