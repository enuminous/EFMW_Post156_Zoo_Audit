# FieldSpace projected gluing repair

## Frozen target and explicit change of specification

This repair is based on audit commit
`936d09f7c134c369dfb1f7750c3653a252994e19` and the unchanged FieldSpace source at
`7e60205d2370c335ebe2cafe89d6e0bbe842ba01`.

The old premise compared every residual-vector component, even an equation
that one chart did not contain. The source supplies equations only for sectors
in a chart. The corrected contract restricts both field inputs and equation
outputs. This is an explicit replacement specification; it does not make the
old zero-padded full-vector assertion true.

For a finite sector set, let `r_U` set field components outside U to zero and
let `p_U` discard equation components outside U. Both maps are instances of
`FieldSpace.restrict`, applied to their respective types. They compose by
intersection, using upstream `restrict_restrict`.

The compatibility condition is

    p_(A ∩ B) f_A(r_(A ∩ B) φ) = p_(A ∩ B) f_B(r_(A ∩ B) φ).

A reconstructed equation family must satisfy

    p_A F(r_A φ) = p_A f_A(r_A φ).

`ProjectedCompatible` and `ProjectedRestrictsTo` express these contracts
component by component. `projectedCompatible_iff_output_restriction` proves
the first equivalence explicitly. An empty output overlap imposes no equations.

## Exact existence and uniqueness theorem

For each output sector s, define the allowed support sets by

    D_s = {S : |S ∪ {s}| ≤ k}.

`IsComponentKBody k F` means that component F_s is a sum of terms depending
on field sets in D_s. The equation label counts among the k sectors, even
when the term does not depend on its field value. For k = 3, a term may involve
s and at most two other sectors, or at most two other sectors alone.

For k no greater than the number of sectors, the new theorems establish

    ProjectedCompatible k f
      iff there exists a unique F with
          IsComponentKBody k F and ProjectedRestrictsTo k F f.

The general existence and uniqueness results are separate declarations.
`fieldSpace_projected_atlas_gluing` packages them as a single `∃!` result for
the eleven-sector, 165-triplet atlas. The value types are generic: fields need
a zero, and equation values form an additive commutative group.

This is a precise uniqueness class, not a claim of unrestricted uniqueness
or unique physical dynamics. It does not assume an extension exists.

## Reconstruction and anti-circularity

For each s and each allowed S, choose a k-chart τ(s,S) containing S ∪ {s}.
Such a chart exists by the cardinality bound. Define

    h_(s,S)(φ) = Σ_(U ⊆ S) (-1)^(|S|-|U|) f_τ(s,S)(r_U φ)_s,
    F(φ)_s = Σ_(S ∈ D_s) h_(s,S)(φ).

The proof then establishes all of the following:

1. Each h_(s,S) depends only on S.
2. On a chart A containing s, terms with S not contained in A cancel.
3. For S contained in A, projected compatibility transfers the local values
   from τ(s,S) to A. Möbius inversion then recovers f_A's s component.
4. Every function in the declared interaction class is recovered by the same
   inversion. Its chart restrictions therefore determine it uniquely.

The premises are finite coverage, the stated types and projected overlap
agreement. Neither the desired extension nor its uniqueness is a premise.
The formal proof reuses the upstream Boolean-lattice identities, not the
inapplicable full-vector extension theorem.

## Bridge to a full-vector completion

`projected_full_vector_completion` also constructs a compatible full-vector
family after obtaining F:

    g_A(φ) = F(r_A φ).

It proves the original upstream `RestrictsTo` and `GluingCompatible` predicates
for g, and proves that g preserves every observed component of f on every
chart slice. Missing components are supplied by reconstruction. They are not
forced to zero. This gives a justified full-vector completion without changing
any of the chart equations that the projected contract observes.

## Two regression counterexamples

The old FWT/FWI example is preserved. Its chart equation is

    f_A(φ)_s = φ_F if s = T and s ∈ A, and 0 otherwise.

It has no old full-vector extension, as already checked. It does have the
explicit repaired extension

    F(φ)_s = φ_F if s = T, and 0 otherwise.

On a chart lacking T, no T equation is observed. The two results coexist;
`repair_preserves_full_vector_obstruction` checks them together.

The uniqueness bound is necessary. Let

    H(φ)_T = φ_F φ_W φ_I, with all other components zero.

H is an ordinary three-body function. Every triplet containing T omits at
least one of F, W and I, so its observed T component is zero. Thus H and the
zero function have identical projected triplet data but differ globally.
`ordinary_three_body_not_unique` proves this counterexample. H is excluded by
the repaired bound because its input support together with T has four sectors.

## Source audit and remaining obligations

The executable audit now checks every nonempty overlap of distinct charts,
including the singleton overlaps required by the theorem.

| Overlap | Chart pairs | Explicit scalar/gauge comparisons | Explicit mismatches |
|---|---:|---:|---:|
| Two shared sectors | 1,980 | 3,600 | 0 |
| One shared sector | 6,930 | 6,300 | 0 |
| No shared sectors | 4,620 | 0; output condition is vacuous | 0 |
| Total | 13,530 | 9,900 | 0 |

Same-chart comparisons are identities. The old pair report is retained;
`results/fieldspace/projected_overlaps.csv` adds the complete nonempty report.
Six integrity/mutation controls accompany this computation.

These are comparisons of explicit retained source terms. A zero mismatch
count does not certify undefined current/stress terms or tensor calculus.
Across nonempty overlaps, 6,048 have only explicit shared components; 2,862
involve mixed current and/or stress obligations. The earlier 972 figure
counts those obligations on shared-pair overlaps only.

| Obligation | Status |
|---|---|
| Match the gluing contract to the chart's equation components | Resolved by the projected definitions |
| Reconstruct from that contract and state a valid uniqueness class | Kernel-checked in `ProjectedGluing.lean`; execution evidence recorded separately |
| Preserve the old failure and prevent unrestricted uniqueness claims | Explicit regression proofs |
| Compare explicit source terms on all required overlaps | Demonstrated computationally; 9,900 comparisons |
| Define physical mixed current and stress, with units and transformations | Unresolved; existing support formulas remain proposed completions |
| Choose scalar vacuum convention (`V(0)=0` or justified subtraction) | Unresolved model choice; the prior necessary condition is preserved |
| Establish conservation and a typed physical source-to-Lean model | Unresolved |

The repair closes the mathematical specification gap. It does not upgrade
the 972 pair obligations, or the expanded 2,862 nonempty-overlap obligations,
to unconditional physical-source passes.

## Known-result classification and verification gate

The method is Boolean-lattice Möbius inversion with an output-indexed support
bound. It adapts the already formalized upstream argument; no new physical
law or mathematical priority claim is made. The application-specific result
is a corrected theorem that matches the source audit's observation rule.

Success requires a pinned Lean build, named dependency reports for every
audited theorem with no additional axioms, both regression counterexamples,
and the exact-source/mutation checks. Failed attempts are retained in the
execution record. See `results/lean/projected-gluing/VERIFICATION.md` for the
tested commit, successful build, 33 named axiom reports and both preserved
failed attempts. All 15 repair declarations passed on 2026-10-06.
