# Lean Targets

`../EFMWPost156Audit/DerivedCandidates.lean` contains self-contained theorem targets for T177–T181 using the same algebraic forms as the audited EFMW scalar and Friedmann relations.

## Important status

These five targets are included as **DERIVED — LEAN PENDING**.

This ZIP was generated without a local Lean executable, so no claim is made that this file has passed `lake build` in this environment.

The package pins:
- Lean `v4.28.0`
- Mathlib `v4.28.0`

to match the inspected upstream Aristotle project.

## Intended workflow

```bash
lake update
lake build
```

If all five compile, update their registry status from `DERIVED — LEAN PENDING` to `KERNEL-CHECKED IN AUDIT REPO`, record the commit SHA, and leave the scientific/empirical status unchanged.

Formal proof still does not establish physical truth.
