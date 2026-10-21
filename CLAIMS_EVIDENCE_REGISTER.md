# Claims-to-evidence reconciliation register — reviewer slice v0.1

**Date:** 2026-10-21. This is an initial *targeted* cross-repository reconciliation, not an exhaustive audit of 119 repositories. Repository claims may have changed after this date. Do not interpret status as independent build verification.

| ID | Claim and reference | Strongest located evidence | Disposition and required qualifier |
|---|---|---|---|
| EXP-001 | [EFMW-EXP-001 confirmatory result](https://github.com/enuminous/EFMW-EXP-001/blob/main/CONFIRMATORY_RECONCILIATION.md) | Reconciliation reports 40 frozen synthetic seeds, +16.5 median paired warning-lead gain, Wilcoxon p≈0.003923 and reproducible hashes | **REPORTED REPRODUCTION, synthetic only.** No production superiority or independent external replication established by this entry. |
| FULL-EXP | [EFMW-FULL lifecycle header](https://github.com/enuminous/EFMW-FULL/blob/main/README.md) | Describes historical transcribed-specification execution and points to the frozen-run reconciliation | **HISTORICAL, NOT ADDITIONAL REPLICATION.** Old to-do wording is historical; conflicts must be resolved by dates/lineage, not count both as independent results. |
| ME-003 | [Monolithic-102 analysis coverage](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/main/analysis/COVERAGE.md) | Describes real C² flat Cartesian inverse metric contraction equal to ME-004 with c≠0 | **PARTIAL SPECIALIZATION.** Curved generality remains open; current repository prose is not itself a fresh independent Lean build. |
| CAT-49 | [Analytic coverage](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/main/analysis/COVERAGE.md) | Current report: 21 explicit analytic models and 28 partial/counterexample results for 49 formerly catalogue-only entries | **MATHEMATICAL WORK, NOT 49 PHYSICAL VALIDATIONS.** Confirm current ledger/build before release. |
| ROT | [Two Paths to Rotation](https://github.com/enuminous/papers/blob/main/Two-Paths-to-Rotation.md) | Written explicit planar hinge -> rigid flow -> vorticity identities | **STANDARD GEOMETRIC BRIDGE.** Cross-project integrated Lean kernel build and physical uniqueness not established. |
| C1-VORT | [Frozen two-free-scalar construction](https://github.com/enuminous/papers/blob/main/research/cmb-alignment/nonzero-vorticity/v1/DERIVATION.md) | Conditional local fixed-background result; independent numerical stress-eigensystem reconstruction | **LOCAL CONDITIONAL RESULT, not EFMW-specific.** No Einstein constraint cosmology or observed global axis. |
| GRID | [EFMW-Grid](https://github.com/enuminous/EFMW-Grid) | Prior equal-budget PI-plus-lag comparator did not support aspirational savings claim | **DO NOT CLAIM 20–25% energy savings.** Physical savings unverified. |
| CERT | [Proposed Zoo certification model](https://github.com/enuminous/papers/blob/main/Monolithic-Zoo-Certified-Auditor-Licensing-Business-Model.md) | Proposal, scenarios, proposed audit parameters | **BUSINESS HYPOTHESIS.** No accredited external technician scheme, forecast certainty or established license revenue. |

## Release-blocking discrepancy policy

- If two artifacts assert incompatible statuses for the **same experiment/version/date**, mark the claim **CONFLICT / NOT RELEASE READY**, log both quoted fields and file SHAs, and reconcile against dated executions.
- `passed` requires a specific gate, frozen test revision, command, result and evidence file. `unexecuted` applies to a frozen plan **at its freeze date** and must not be silently overwritten.
- Retire an obsolete claim by visible supersession note pointing to the retained historical source and replacement, never by erasing provenance.
- Not finding conflicting wording in this targeted slice is **not** a whole-portfolio pass.

## Priority uncompleted work

1. Full text-level claim scan across the 119-repository inventory and newer repos, including all current `EFMW-FULL` experiment status fields.
2. Independent Lean build of ME-003 and all planned release theorem targets on pinned toolchains.
3. Confirm release commits and checksum signatures. Only create/approve named immutable release tags once the source commits and builds are verified.
