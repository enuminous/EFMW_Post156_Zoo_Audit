# T001–T156 Baseline

This audit treats the user's **156-theorem Aristotle set** as a frozen exclusion baseline.

The present repository does **not** invent names or statements for all 156 baseline entries where they were not independently reconstructed during this audit. Instead it records the post-baseline delta precisely.

## Why

A theorem registry becomes misleading if it fills missing baseline rows with guessed titles or duplicated helper lemmas. The counting rule here is therefore:

1. Accept **156** as the frozen baseline count for this audit.
2. Compare later repository-backed theorem families against known Aristotle sector files.
3. Promote only substantively distinct results beyond the baseline.
4. Keep new audit derivations separate until Lean checking.

For a future immutable 181-row canonical registry, the next step is to extract and enumerate every promoted theorem from the complete Aristotle Lean source tree, then merge this post-156 delta by theorem identity rather than by count alone.
