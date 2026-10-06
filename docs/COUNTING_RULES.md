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

## Verification update for the 181 entries

On 2026-10-05, T177–T181 passed the pinned Lean build and axiom audit.
The correct split is 176 earlier repository-backed promoted entries plus five
kernel-checked results in this audit repository. This run does not reverify
all 181 entries. See `results/lean/VERIFICATION.md`.

The ten new FieldSpace declarations are listed separately: elementary support
lemmas, counterexample corollaries and a vacuum condition. They are not
automatically ten independent theorem families or new physical laws.

The projected gluing repair adds 15 declarations (reconstruction, uniqueness,
completion, supporting lemmas and regression counterexamples). They remain
separate from the 181-entry registry. With the original ten, there are 25
FieldSpace audit declarations; this does not promote 25 physical laws or
claim 25 independent theorem families.
