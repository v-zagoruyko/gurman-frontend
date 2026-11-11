---
version: 1
slug: "delivery-index-html"
primary_target: "delivery/index.html"
related_targets: ["delivery/styles.css"]
---

# Delivery menu

Mode: operate. Replacement world for `delivery/index.html` and `delivery/styles.css`. Mobile visitors at the restaurant cash desk compare 29 dishes, their own photos, confirmed portions and prices, then call. On 2026-11-11 the user authorized a temporary local server and Chrome capture to resume the open hero gate; stop the server after verification.

## Direction contract

THESIS: A calm counter display in the visitor's hand. A dish and its portions form one readable unit; no promotional hero or newspaper layout.

OWN-WORLD: White, pale neutral-gray photo wells, charcoal type and graphite phone action. One humanist sans; flat rectangular bays; strong numeric alignment; no glass, blur, gradients or ornamental assets.

STORY: Recognize Gurman and its takeaway menu; choose a section; inspect a dish and its prices; read confirmed set contents; call or open the PDF.

FIRST VIEWPORT: Compact identity, menu title and PDF link, explicit four-section wayfinding, opening dishes immediately visible, persistent phone action. Approved composition B: compact comparison rows. Each row pairs a 120px square individual photo well on the left with the dish name and aligned portion–price rows on the right. The first viewport begins the menu immediately; large promotion, card shells and price pills are absent.

FORM: Prepared-food counter vitrine, grounded candidate 5, seed `9e5a2ec8`. Signature behavior: persistent section wayfinding, current-section feedback, and ordinary document flow. No entrance animation.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance

## Decision state

Comp-led remains the project default. User selected and approved B. Approved comp: `.impeccable/mocks/delivery-vitrine-b.png`. The three explored comps are: `.impeccable/mocks/delivery-vitrine-a.png`, `delivery-vitrine-b.png`, `delivery-vitrine-c.png`. Exact prompts live beside them; B has `approved: true`, A and C remain unapproved. These are generated compositions, not screenshots of implemented code. The build resumes from the open `hero` phase for seed `9e5a2ec8`; `comps`, `spec`, and `plates` are closed. Earlier newspaper comps and seed `6c935975` were rejected and are not references.

The user's serious, restrained, clear direction is settled. Composition approval is complete; implement B without another approval step. At implementation, preserve all 29 dishes, four set descriptions, real prices and portions, phone +7 (3452) 21-75-65, PDF, analytics and SEO. Use distinct photo placeholders until real item photos arrive; do not invent food or ingredients. Main text ≥19px, captions ≥14px, targets ≥54px, text contrast ≥5:1. Use real Chrome captures at the comp dimensions (984×1599), plus 390px mobile and 1440px desktop.

Derivation and challenger judgments: `.impeccable/delivery-direction-9e5a2ec8.md`.

## Implementation status

Resumed on 2026-11-11 after the user authorized a temporary local server and Chrome. A real 984×1599 baseline capture satisfied the missing-evidence precondition. The current implementation follows B: a white reading surface, self-hosted Golos Text, four persistent section links, individually labelled photo wells, and aligned portion/price rows. At desktop widths the same row expands into photo, name, and numeric columns.

All 29 menu items and four verified set descriptions remain intact. The opening three rows follow the approved B composition; pork loin is retained as the fourth row. No food photographs are generated or substituted. The surface uses no new shipping raster; existing Open Graph artwork remains metadata only.

The original spec's OCR boxes contain overlapping text regions (for example the first navigation label and portion weights). These are recorded as measurement defects; the semantic layout follows the actual approved image and remains usable in document flow. Build gates and the fresh finish review must report any remaining fidelity limitations honestly.

## Completion evidence

The fresh finish review opened five real Chrome captures: `hero-repro.png` (984×1599), `desktop.png` (1440×6239), `mobile.png` (390×4882), `desktop-first.png` (1440×1000), and `mobile-first.png` (390×844). The review found no material visual or product defects and confirmed that the approved B topology is preserved. It also found that the hero gate remains open: the machine-readable OCR regions overlap neighboring labels and price rows, so the hard-veto score is not reliable. No phase was forced closed. `DESIGN.md` and `.impeccable/design.json` document this delivery surface only; the banquet homepage retains its existing design.
