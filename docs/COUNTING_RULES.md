# Counting and Promotion Rules

The audit deliberately separates four different numbers:

1. **Lean declarations** — every declaration named `theorem`, including helper lemmas.
2. **Substantive theorem results** — helper lemmas and purely local proof infrastructure removed.
3. **Independent theorem families** — equivalent reformulations and duplicate integer/real abstractions collapsed.
4. **Independent scientific laws** — only relations with distinct empirical content, not every mathematical corollary.

## Promotion rule

A post-baseline result is promoted only if it is:

- traceable to a repository source or explicitly marked Lean-pending;
- not merely a proof helper;
- not an obvious syntactic restatement of a baseline theorem;
- not a generic arithmetic identity being rebranded as EFMW novelty;
- not an empirical claim presented as established without data.

## Why 176, not 169

The earlier 169 count captured the 156 baseline plus 13 substantive `PhysicalTest.lean` results. A later cross-check found seven nonredundant theorem families in the separate `Monolithic_Zoo_Run` survivor tranche that were not safely collapsible into those 13.

Thus the present repository-backed promoted count is:

`156 + 13 + 7 = 176`.

## Why 181 is only a working count

T177–T181 are new derivations from the inspected formulas. They are mathematically stated and supplied as Lean targets, but this audit package does not claim they have been kernel-checked.

Therefore:

- **176** = repository-backed promoted count
- **181** = working count including five Lean-pending candidates
