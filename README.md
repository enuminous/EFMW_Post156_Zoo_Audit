# EFMW Post-156 Theorem & Zoo Audit

**Audit date:** 2026-09-07  
**Scope:** Monolithic 102 equations; Aristotle EFMW Lean baseline; Monolithic Zoo survivor tranche; canonical 46-animal EFMW Zoo.

## Executive result

This repository freezes the current audit state after comparing the 156-theorem Aristotle baseline with later `PhysicalTest.lean` results and the separate Monolithic Zoo survivor work.

### Working counts

- **102** canonical source equations
- **156** frozen Aristotle baseline theorem count
- **20** additional repository-backed promoted theorem families beyond that baseline
- **176** repository-backed promoted registry entries total
- **5** newly derived theorem candidates from the present audit, **Lean pending**
- **181** working entries if those five candidates are included as unverified derivations

The 181 figure must **not** be described as 181 kernel-checked theorems. The defensible split is:

> **176 repository-backed promoted entries + 5 derived, Lean-pending candidates.**

## Main scientific finding

The audit does **not** support inflating the result into a large number of new physical laws.

The strongest distinct physical relations remain:

1. **Scalar propagation relation**
   \[
   (1-\alpha^2)\omega^2 = c^2 k^2,
   \qquad
   v_\phi = \frac{c}{\sqrt{1-\alpha^2}}.
   \]

2. **Residual-rotation Friedmann relation**
   \[
   \Delta H^2 = \frac{\Omega_U^2}{a^2}.
   \]

The new Zoo pass mainly adds **identifiability and falsification structure**. Most notably:

> **Curvature–Rotation Degeneracy:**  
> within the presently formalized Friedmann model,
> \[
> H_{\rm EFMW}^2(k,\Omega_U)
> =
> H_{\Lambda{\rm CDM}}^2(k-\Omega_U^2).
> \]
> Therefore expansion-history data alone cannot identify constant residual rotation independently of curvature.

## Repository map

- `registry/POST_156_REGISTRY.csv` — T157–T181
- `registry/POST_156_REGISTRY.md` — readable registry
- `registry/BASELINE.md` — scope and counting rule for T001–T156
- `zoo/CANONICAL_46_PASS.md` — complete 46-animal audit
- `docs/CANDIDATE_LAWS.md` — surviving law-level content
- `docs/NEW_DERIVATIONS.md` — T177–T181 derivations
- `docs/COUNTING_RULES.md` — anti-inflation rules
- `sources/PROVENANCE.md` — upstream repositories/files and known SHAs
- `EFMWPost156Audit/DerivedCandidates.lean` — Lean targets for T177–T181
- `lean/README.md` — build status and integration notes
- `lakefile.toml`, `lean-toolchain` — pinned to the same Lean/Mathlib version used by the upstream Aristotle project at audit time

## Status vocabulary

- **REPOSITORY-BACKED** — theorem/result exists in inspected repository source.
- **PROMOTED** — counted as substantively distinct after helper/rephrasing deduplication.
- **DERIVED — LEAN PENDING** — algebraically/mathematically derived in this audit but not claimed kernel-checked here.
- **CANDIDATE PHYSICAL LAW** — a model relation with distinct empirical content; not an experimentally established law of nature.
- **STANDARD / INTERNAL** — mathematically valid consequence, but not a novel physical law.

## Scientific caution

Formal proof establishes consequences of stated definitions and postulates. It does not establish that EFMW describes nature. Physical-law status requires independent empirical confirmation.

No new fundamental law was promoted solely to increase the count.

## License

No new license is imposed by this audit package. Before public release, the repository owner should choose a license compatible with the upstream materials used or referenced.
