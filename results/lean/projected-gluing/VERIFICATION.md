# Executed projected-gluing verification — 2026-10-06

- Result: **PASS**.
- Tested commit: `0b8de0d44f62f72e334a6825a31a5bd9cb6a85cf`.
- CI run: https://github.com/enuminous/EFMW_Post156_Zoo_Audit/actions/runs/37483623891.
- Job: `112337932239` (`verify`).
- Lean: v4.28.0, compiler `7e01a1bf5c70fc6167d49c345d3bf80596e9a79b`.
- Mathlib: `8f9d9cff6bd728b17a24e163c9402775d9e6a365`.
- Upstream FieldSpace: `7e60205d2370c335ebe2cafe89d6e0bbe842ba01`.
- `lake build`: successful (8,033 Lake jobs, not a theorem count).
- Local declarations checked: 5 T177–T181 results, 10 prior closure-audit lemmas,
  and 15 new projected-gluing declarations; 30 local declarations in total.
- Named axiom reports checked: 33, including three upstream results.
- Observed dependencies: only `propext`, `Classical.choice`, `Quot.sound`.
- Source integrity/mutation tests: six passed in CI and locally.
- Explicit retained scalar/gauge component comparisons: 9,900, zero mismatches.
- Evidence artifact: `11421559940`; ZIP SHA-256 `65fff9e0d7ba114bd863f0f584fa767b3625e71ca440647abbab5dab8535568e`.

The build, axiom and version logs are copied from that artifact. Its source
reports and dependency manifest match the committed files byte for byte.
The final documentation/evidence commit leaves the tested Lean and Python
proof/audit code unchanged. One unused-section-variable linter warning remains;
it does not introduce an axiom or affect the proof result.

`checker-controls.log` records an additional local gate check using the real
33-report log. The checker accepts it and rejects a removed report, a duplicate,
an injected `sorryAx`, an unexpected theorem and the stale 18-report log.
The historical verification record and logs in the parent directory are retained.

## Preserved failed attempts

1. Commit `e74afb41553d4637dd436c5a03b416cfd2560bb7`,
   run https://github.com/enuminous/EFMW_Post156_Zoo_Audit/actions/runs/37406165963,
   job `112084115181`: ambiguous imported names and unfinished local proof steps.
   `first-build-failure.log` retains the build portion of the job log.
2. Commit `bedd1354368bc1f50ea13a46e8f33f2ec5917f2e`,
   run https://github.com/enuminous/EFMW_Post156_Zoo_Audit/actions/runs/37482757143,
   job `112334898468`: two rewrites in the added full-vector completion bridge
   needed explicit function-application reduction. `second-build-failure.log`
   retains the build portion of that job log.

The final correction supplies explicit `change` steps. No mathematical
assumption, chart equation or theorem statement was weakened to pass the gate.

## Proven scope

The corrected input/output restriction contract has a reconstruction theorem
and a uniqueness theorem in the stated component-indexed interaction class.
A full-vector completion preserves the observed chart equations. Regression
proofs preserve the old zero-padding obstruction and reject unrestricted
ordinary-three-body uniqueness.

This resolves the mathematical gluing specification gap. It does not identify
physical mixed currents or stresses, choose a vacuum convention, prove the
source's conservation closure, establish empirical validity, or reverify all
176 earlier registry entries.
