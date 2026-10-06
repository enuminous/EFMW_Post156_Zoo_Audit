# FieldSpace source-level closure audit

**Follow-up:** the specification gap described below is addressed by the
[projected gluing repair](PROJECTED_GLUING_REPAIR.md). It proves conditional
reconstruction and uniqueness in an explicit component-indexed interaction
class, plus a full-vector completion preserving observed equations. The
physical current, stress, vacuum and conservation obligations remain open.

Target: `enuminous/Einsteinian-156-Aristotle` at
`7e60205d2370c335ebe2cafe89d6e0bbe842ba01`.
The exact 64,859-byte source is frozen in `sources/fieldspace/` and checked
against Git blob `ac6313fe4a2b02a28ac8fb34519c5f96f6ea2bd8`.

## Executed source audit

The checked-in parser reads every scalar and gauge dynamical equation, checks
its coefficient/factor support, rejects unfamiliar syntax, and compares the
retained equation components on all shared-pair slices. It verifies all 165
charts and 585 statements. It does not parse tensor calculus or certify PDEs.

| Overlap class | Count | Status before a completion |
|---|---:|---|
| Explicit shared components only | 1,008 | Source comparisons agree |
| Interaction stress required | 288 | Undefined in source |
| Mixed current required | 612 | Undefined in source |
| Both required | 72 | Undefined in source |
| Total | 1,980 | Not a full-vector gluing certificate |

There are 3,600 scalar/gauge component comparisons and zero mismatches in the
explicit retained terms. Stress equations are counted but not passed by a
symbolic tensor evaluator. The current checks compare the explicit parts;
discarding the unknown mixed current requires the proposed support completion.
Six mutation/integrity tests now cover the complete overlap spectrum and exercise coefficient corruption, missing charts,
changed shared components, incorrect mixed-current support, and the frozen input.

## Proposed support completion

`EFMWPost156Audit/FieldSpaceClosure.lean` defines, for real amplitudes a,b,c
and coefficients in an arbitrary real module V,

    Xi(a,b,c) = (a*b*c) • K
    T(a,b,c) = (a*b) • Pab + (a*c) • Pac + (b*c) • Pbc + (a*b*c) • Q.

The proof targets establish vanishing of Xi whenever any amplitude is zero,
the pair restriction `T(a,b,0) = (a*b) • Pab`, and independence from the removed
chart's coefficients. A nonzero example prevents an all-zero construction.
These are explicit algebraic completion choices, not definitions extracted
from the original source and not a conserved physical current/stress tensor.
An amplitude map, physical units and tensor/gauge transformations remain open.

## New obstruction: different overlap predicates

The upstream `GluingCompatible` compares **the entire residual vector** on an
intersection. The source audit compares only equations for **shared sectors**.
These predicates are not interchangeable.

A concrete source-shaped specialization uses the charts FWT and FWI and sets
only `lambda_TF = 1`; all other coefficients can be zero. On the shared FW
slice let phi_F = 1 and phi_W = 0. The FWT chart's T equation retains the value
1, while the FWI chart has no T equation. If missing equations are padded by
zero, its T component is 0. All shared-component comparisons still agree.

The Lean targets exhibit this counterexample and derive that this encoding
has no full-vector extension. This does not refute the generic upstream gluing
theorem, nor does it prove that every possible encoding fails. It refutes the
inference from the available shared-component audit to that theorem's premise.
This example lies entirely in the scalar sector: defining T and Xi cannot fix it.

## Additional gravity obligation: vacuum stress

The EFM chart includes `-g_mu_nu V(phi_F)`. On removing F this leaves
`-g_mu_nu V(0)`. The EMS chart instead loses a gauge contribution, which is
zero when that field is zero. With identical mixed pair stress, agreement
requires `g_mu_nu V(0) = 0`. A nonzero metric component requires `V(0) = 0`.
One could instead specify a consistent vacuum subtraction/cosmological-term
convention; that would be an explicit model choice. The source has not supplied it.

## Conservation remains independent

The imported `scalar_current_extra_equation` and `linear_profile_obstruction`
retain their original scope: flat coordinates, constant diagonal metric,
smooth fields, antisymmetric gauge strength, and conserved remaining currents.
Support properties alone imply neither a Noether identity nor the required
conservation law. A proposed mixed-current compensation must be demonstrated
and must also respect its zero-slice behavior.

## Verdict and next obligation

- **Demonstrated computationally:** the exact source inventory, overlap counts,
  explicit retained-term comparisons, and mutation controls.
- **Kernel-checked on 2026-10-05:** support-construction lemmas, a counterexample to
  the missing predicate implication, and the vacuum-stress condition.
- **Not established:** full source gluing, unique global physical dynamics,
  a master action, conservation closure, or empirical validation.

The 972 overlaps are not promoted to unconditional source-level passes.
The mathematical follow-up now specifies both restriction maps, proves the
projected reconstruction theorem with a precise uniqueness class, and supplies
compatible full-vector completions. See `PROJECTED_GLUING_REPAIR.md` and its
execution evidence. This resolves the missing theorem at the specification
level. Source-level closure still requires vacuum conventions, physical mixed
objects and conservation. The old zero-padded counterexample remains valid.

## Reproduce

    python3 scripts/audit_fieldspace.py
    python3 scripts/test_fieldspace_audit.py
    lake update
    lake exe cache get
    lake build
    lake env lean lean/ProofAudit.lean > results/lean/axioms.log
    python3 scripts/check_axioms.py results/lean/axioms.log

Lean and Mathlib are v4.28.0; the FieldSpace dependency is pinned to the SHA
above. `.github/workflows/lean-audit.yml` performs actual compilation and
preserves the build/dependency logs. The ten audit lemmas and five older candidates passed the build and axiom
check; that historical run is recorded in `results/lean/VERIFICATION.md`.
The projected repair has a separate execution record under
`results/lean/projected-gluing/`.

## Known-result classification

The support identities are elementary multilinear algebra; the vacuum result
is ordinary algebra. The shared-component counterexample is an application-
specific specification finding, not a new physical law. The prior Möbius
gluing theorem remains a conditional mathematical result.
