# EFMW Post-156 Theorem & Zoo Audit

<!-- ENUMINOUS-UNIFIED-NAV:START -->
## Repository navigation

**eNuminous network:** [All public repositories](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md) · [EFMW](https://github.com/enuminous/EFMW) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [Frozen Lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Zoo](https://github.com/enuminous/Tortoise) · [Papers](https://github.com/enuminous/papers) · [Quantum geometry](https://github.com/enuminous/Base888-Quantum-Geometry)

**This project:** [Repository home](https://github.com/enuminous/EFMW_Post156_Zoo_Audit) · [Subject index](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md#core-efmw-and-review)

<details open>
<summary><strong>On this page</strong></summary>

- [Executive result](#executive-result)
  - [Working counts](#working-counts)
- [Main scientific finding](#main-scientific-finding)
- [Repository map](#repository-map)
- [Status vocabulary](#status-vocabulary)
- [Scientific caution](#scientific-caution)
- [License](#license)


</details>

**Related repositories:** [Monolithic-Zoo-Lean4](https://github.com/enuminous/Monolithic-Zoo-Lean4) · [Monolithic-102-Zoo-Lean4](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Tortoise](https://github.com/enuminous/Tortoise) · [EFMW](https://github.com/enuminous/EFMW) · [efmw-equation-review](https://github.com/enuminous/efmw-equation-review) · [EFMW-Scientific-Claims](https://github.com/enuminous/EFMW-Scientific-Claims) · [EFMW-CTX-001b](https://github.com/enuminous/EFMW-CTX-001b) · [Monolithic_102_EFMW](https://github.com/enuminous/Monolithic_102_EFMW) · [papers](https://github.com/enuminous/papers)

> **Evidence boundary:** A link between projects is navigation, not an assertion of proven equivalence, experimental validation, or shared authorship. See each repository’s own status and review notes.
<!-- ENUMINOUS-UNIFIED-NAV:END -->


> **External reviewers: START HERE → [Reviewed scope and reproduction guide](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/REVIEW_START_HERE.md) · [What this does not claim](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/WHAT_THIS_DOES_NOT_CLAIM.md) · [Claims-to-evidence register](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/CLAIMS_EVIDENCE_REGISTER.md).** These documents index evidence; they do not certify every repository.


<!-- ENUMINOUS-LIFECYCLE:START -->
**Lifecycle review — 2026-10-16: repository lifecycle review published.**

[Review of 119 public repositories](portfolio/REPOSITORY_LIFECYCLE_2026-10-16.md) identifies superseded claims, historical entry points and exact duplicate files, with pinned source evidence and retained distinctions between models, implementations and experiments.

[Portfolio review and evidence](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/portfolio/REPOSITORY_LIFECYCLE_2026-10-16.md).
<!-- ENUMINOUS-LIFECYCLE:END -->

**Repository network audit (2026-10-10):** [All-repository integration report](portfolio/INTERLOCK_AUDIT.md), [public directory](https://enuminous.github.io/EFMW/repositories.html), and [navigation maintenance](portfolio/README.md). This pass checks navigation, source paths, publication status and recorded CI; it does not revalidate the scientific corpus.


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
