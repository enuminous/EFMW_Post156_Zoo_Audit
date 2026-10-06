# Lean verification

T177–T181 and the ten FieldSpace audit lemmas passed Lean 4.28.0 on
2026-10-05. All 18 dependency reports (including three upstream results)
contain only `propext`, `Classical.choice`, and `Quot.sound`.

See [verification evidence](../results/lean/VERIFICATION.md) for the tested
commit, CI run, exact dependencies, build logs and the preserved first failure.

## Reproduce

```sh
lake update
git diff --exit-code lake-manifest.json
lake exe cache get
lake build
lake env lean lean/ProofAudit.lean > results/lean/axioms.log
python3 scripts/check_axioms.py results/lean/axioms.log
```

The FieldSpace mixed-term construction is a proposed algebraic completion.
The projected gluing repair resolves the mathematical restriction-map gap
and proves reconstruction and uniqueness under the documented interaction
bound. Physical source instantiation and conservation remain unresolved.
See `docs/PROJECTED_GLUING_REPAIR.md` and the separate execution record
under `results/lean/projected-gluing/`.

`lean/ProofAudit.lean` now names 33 audit targets: 30 local declarations
(5 original candidates, 10 closure-audit lemmas, 15 projected-gluing results)
and 3 upstream results. The checker verifies the exact names and rejects
missing, duplicate or unexpected reports and nonstandard dependencies.

The projected repair passed on 2026-10-06: all 33 named reports use only the
standard foundational axioms. See [repair verification](../results/lean/projected-gluing/VERIFICATION.md).
