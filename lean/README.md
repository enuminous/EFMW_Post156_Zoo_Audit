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
Full source gluing and conservation remain unresolved; see the closure audit.
