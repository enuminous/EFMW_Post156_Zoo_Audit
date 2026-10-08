# EFMW Post-156 Theorem & Zoo Audit

**New: [EFMW research engine v0.1](research_engine/README.md)** connects the frozen
102-equation, 165-triplet and 46-animal catalogs into **774,180 potential evaluation
slots**. It includes 46 selected Python kernel adapters, an explicit applicability
registry, a hash-linked evidence ledger, a CLI and a
[standalone dashboard](research_engine/results/demo-v0.1/index.html) (download and
open locally). The preserved demonstration is synthetic: 48 attempts, 47 computed
outputs, two unmet criteria and one rejected input. No scientific mapping has yet
been accepted and no new law or formal proof is promoted by this engine.

**2026-10-05 verification update:** [Lean build and axiom audit passed](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/actions/runs/37333546590).
T177–T181 are now kernel-checked in this repository. The new
[FieldSpace closure audit](docs/FIELDSPACE_CLOSURE_AUDIT.md) adds ten checked
lemmas covering an explicit support construction, a counterexample to the
shared-component/full-vector implication, and a vacuum-stress condition.
The 972 conditional overlaps are **not** promoted to full source gluing.
See [verification evidence](results/lean/VERIFICATION.md).

**2026-10-06 projected gluing repair — [Lean verification passed](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/actions/runs/37483623891):** the
[repair report](docs/PROJECTED_GLUING_REPAIR.md) defines restriction of both
fields and equation components, proves reconstruction with an explicit
interaction bound, and supplies compatible full-vector completions. It also
preserves the old counterexample and demonstrates why ordinary three-body
dependence alone does not give projected uniqueness. Execution evidence is
recorded in [the repair verification record](results/lean/projected-gluing/VERIFICATION.md).
All 15 repair declarations and 33 named dependency reports passed. The expanded
source audit makes 9,900 explicit component comparisons with zero mismatches.


**Audit date:** 2026-09-07  
**Scope:** Monolithic 102 equations; Aristotle EFMW Lean baseline; Monolithic Zoo survivor tranche; canonical 46-animal EFMW Zoo.

## Executive result

This repository freezes the current audit state after comparing the 156-theorem Aristotle baseline with later `PhysicalTest.lean` results and the separate Monolithic Zoo survivor work.

### Working counts

- **102** canonical source equations
- **156** frozen Aristotle baseline theorem count
- **20** additional repository-backed promoted theorem families beyond that baseline
- **176** repository-backed promoted registry entries total
- **5** audit results T177–T181, **kernel-checked in this repository on 2026-10-05**
- **181** registry entries including those five checked results
- **25** FieldSpace audit theorem declarations (10 original + 15 projected-gluing results), recorded separately from the registry count

The 181 figure must **not** be described as 181 kernel-checked theorems. The defensible split is:

> **176 earlier repository-backed promoted entries + 5 results kernel-checked in this audit repository.**

The present build does not reverify the entire earlier 176-entry corpus. The
FieldSpace declarations include helper results and counterexamples; they are
not automatically promoted as independent theorem families.

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
- `EFMWPost156Audit/ProjectedGluing.lean` — projected gluing, reconstruction, completion and regression proofs
- `docs/PROJECTED_GLUING_REPAIR.md` — corrected specification and remaining obligations
- `lean/README.md` — build status and integration notes
- `lakefile.toml`, `lean-toolchain` — pinned to the same Lean/Mathlib version used by the upstream Aristotle project at audit time

## Status vocabulary

- **REPOSITORY-BACKED** — theorem/result exists in inspected repository source.
- **PROMOTED** — counted as substantively distinct after helper/rephrasing deduplication.
- **KERNEL-CHECKED IN AUDIT REPO** — accepted by the pinned Lean build with theorem dependency reports retained.
- **DERIVED — LEAN PENDING** — a derivation awaiting that build gate; the original status of T177–T181, now superseded.
- **CANDIDATE PHYSICAL LAW** — a model relation with distinct empirical content; not an experimentally established law of nature.
- **STANDARD / INTERNAL** — mathematically valid consequence, but not a novel physical law.

## Scientific caution

Formal proof establishes consequences of stated definitions and postulates. It does not establish that EFMW describes nature. Physical-law status requires independent empirical confirmation.

No new fundamental law was promoted solely to increase the count.

## License

No new license is imposed by this audit package. Before public release, the repository owner should choose a license compatible with the upstream materials used or referenced.
