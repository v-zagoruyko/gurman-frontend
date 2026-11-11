# Detector follow-up

The Impeccable 4.3.1 detector ran once after implementation.

- 40 `cramped-padding` findings are repeated across centred photo placeholders and portion separators. Photo labels and icons are centred inside fixed-aspect neutral wells; the actual screenshots are the authority for whether an inset is missing. Portion rows have vertical `calc(4 * var(--unit))` padding; the detector does not resolve that custom-unit arithmetic.
- 4 `tight-leading` findings are resolved for multi-line dish titles by setting line-height to 1.3. Body and verified set descriptions use 1.5. Two-line placeholder captions and the concise phone control deliberately inherit the approved composition's compact treatment.

No ignore rule was added and the detector was not rerun.
