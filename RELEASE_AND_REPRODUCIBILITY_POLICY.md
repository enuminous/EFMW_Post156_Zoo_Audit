# Release naming, tags, hashes, pins and gates — proposal v0.1

**Tags are human-readable labels. SHA IDs are the immutable content referents. Neither substitutes for evidence.**

1. Review one well-defined claim/source version at a time. Pin the **full 40-character Git commit SHA** and, where relevant, SHA-256 of input files, datasets and outputs.
2. Create a descriptive annotated release tag *after* confirming the commit, e.g. `me-003-flat-v1.0.0`. Protect tag names using repo rules, record peeled commit SHA, tagger/date and signed release evidence; do **not** automatically tag historical short hash `01f51acb` without verifying its precise repository, full SHA, scope and ancestry.
3. Pin Lean via a checked-in `lean-toolchain`, Mathlib via a checked-in `lake-manifest.json`; pin Python via hashed lockfile (`pip --require-hashes` or equivalent). Do not invent checksum values. Pinned `requirements.txt` versions alone are weaker than hash-locked artifacts.
4. Provide a repo-local, clean-run command with platform/environment prerequisites, artifacts and reproducible log. A one-command top-level release suite can orchestrate **only explicitly integrated repositories**, not arbitrary research repositories.
5. A release labeled *formal pass* requires observed successful Lean compilation, `#print axioms` or equivalent dependency audit and a proof statement matching the advertised mathematical claim.
6. A release labeled *empirical pass* requires executed predeclared tests, appropriate comparator and controls, frozen outcome measures and reproducible data provenance. Do not equate simulation with observation.
7. Fix contradictory claim-register statuses **before** marking a release reviewed. Maintain historical facts and clearly distinguish freeze-time statuses from post-run results.
8. Classify portfolio repos `reviewed-release`, `active-research`, `historical`, `superseded`, or `external/fork`. Actual GitHub archiving is a separate reviewed decision and is not mandated for all noncanonical work.
9. Record rights/attribution and original licenses before representing third-party contributions as Monolithic-owned or sublicensable.

**Release cannot be certified by documentation edits alone.** A README that says "verified" without a contemporaneous build/test artifact must be treated as unverified.
