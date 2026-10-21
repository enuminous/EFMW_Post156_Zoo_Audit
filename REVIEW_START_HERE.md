# START HERE — eNuminous independent review entry point

**Status: curated navigation and evidence boundaries, October 21, 2026. NOT a portfolio-wide verification certificate.**

## Read this before the equations

[WHAT THIS DOES NOT CLAIM](WHAT_THIS_DOES_NOT_CLAIM.md) explains the limits of the corpus. [CLAIMS_EVIDENCE_REGISTER.md](CLAIMS_EVIDENCE_REGISTER.md) states exactly where selected claims stand. Both are part of the reviewer entry point, not optional disclaimers.

## Choose a review route

| Reviewer | First artifact | What to verify | What not to infer |
|---|---|---|---|
| Formal mathematics | [Monolithic-102-Zoo-Lean4 coverage](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/main/analysis/COVERAGE.md) | Specific Lean theorem, definitions, actual toolchain, axiom report, release SHA | Proof of original physical equation without specialization |
| Empirical methods | [EFMW-EXP-001 reconciliation](https://github.com/enuminous/EFMW-EXP-001/blob/main/CONFIRMATORY_RECONCILIATION.md) | 40 frozen-seed synthetic reproduction, controls, timing and false positives | External/production replication |
| Claims/provenance audit | [Post156 audit](portfolio/INTERLOCK_AUDIT.md) and [lifecycle inventory](portfolio/REPOSITORY_LIFECYCLE_2026-10-16.md) | Source-to-claim mapping, duplicate or superseded records | That every Zoo audit test ran on every repository |
| Business/assurance | [Monolithic Zoo certified auditor proposal](https://github.com/enuminous/papers/blob/main/Monolithic-Zoo-Certified-Auditor-Licensing-Business-Model.md) | Proposed audit record and demonstration gates | An already licensed/accredited technician network |

## Canonical is claim-specific, not repo-global

A repository with an impressive name is not automatically canonical. For each reviewed claim: identify one **source commit SHA**, one **specification/document version**, one **test artifact**, one **review disposition** and the **limits of that evidence**. Published branch tips are not immutable reviews. Release tags are optional readable pointers; include full SHAs and guard tags from moving.

## Reproduction checklist

1. Download exactly the referenced source commit, not whatever `main` contains today.
2. Read `lean-toolchain`, `lake-manifest.json`, Python lockfiles and fixture checksums in the **relevant individual project**; there is no one-command build for the entire corpus.
3. Run the project's declared command; record exit code, Lean axiom dependencies, actual numerical outputs, platform and timestamp.
4. Compare claimed results with linked frozen protocol and negative controls. If no independent build was run, label **NOT REPRODUCED**.
5. Do not count a conditional toy model, a syntax-valid theorem, or an exploratory simulation as empirical validation.

**No archiving action is recommended without completing a per-repository owner/dependency/provenance review.** The [119-repository inventory](portfolio/REPOSITORY_LIFECYCLE_2026-10-16.md) is a historical 2026-10-16 snapshot, not a current census.

## Suggested reviewed release process

See [RELEASE_AND_REPRODUCIBILITY_POLICY.md](RELEASE_AND_REPRODUCIBILITY_POLICY.md). At present this page indexes candidate evidence, not a claim that the full portfolio passes independent review.
