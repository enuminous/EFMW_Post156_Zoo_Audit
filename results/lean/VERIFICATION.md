# Executed Lean verification — 2026-10-05

- Result: **PASS**.
- Tested source commit: `b833ea5f77c55b6d021b4dc6483d456fd0b3ecfa`.
- CI run: https://github.com/enuminous/EFMW_Post156_Zoo_Audit/actions/runs/37333546590.
- Job: `111842444418` (`verify`).
- Lean: v4.28.0, compiler commit `7e01a1bf5c70fc6167d49c345d3bf80596e9a79b`.
- Mathlib: `8f9d9cff6bd728b17a24e163c9402775d9e6a365`.
- FieldSpace: `7e60205d2370c335ebe2cafe89d6e0bbe842ba01`.
- Build: `lake build`, completed successfully (8,032 Lake jobs, not a theorem count).
- Checked local theorem declarations: five T177–T181 results and ten FieldSpace audit lemmas.
- Axiom reports: 18, including three upstream gluing/conservation results.
- Allowed dependencies observed: `propext`, `Classical.choice`, `Quot.sound` only.
- Source/mutation controls: five tests passed in CI and locally.
- Evidence ZIP artifact: `11355641305`, SHA-256
  `685d4272417a964c39d35820258ab5b06d360eb619160a46d286dbea3672b730`.

`build.log`, `axioms.log`, and `version.log` are copied from that CI artifact.
The committed dependency manifest is the one produced by the successful run.
This metadata update preserves the tested Lean proof files unchanged.
The Python CSV writer was subsequently given an explicit LF terminator;
its five tests pass and both generated source-audit outputs reproduce the
committed bytes exactly. No source equations or mathematical statements changed.

## Preserved unsuccessful attempt

Run https://github.com/enuminous/EFMW_Post156_Zoo_Audit/actions/runs/37246746056
built T177–T181 and the upstream modules, then stopped on an unfinished
constructor-inequality proof step. `first-build-failure.log` preserves that
failure. The successful revision added the explicit contradiction proof;
it did not change the theorem statement or introduce an assumption.

## Boundaries

Kernel checking establishes the stated algebraic lemmas and counterexample.
It does not close the original 972 source obligations, validate a physical
current/stress tensor, establish empirical EFMW validity, or reverify the
entire earlier 176-entry theorem registry.
