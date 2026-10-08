# EFMW research engine v0.1

The three frozen catalogs are now connected by a runnable, auditable registry:

**102 Monolithic equations × 165 Einsteinian FieldSpace triplets × 46 Zoo animals
= 774,180 potential evaluation slots.**

Each slot has a stable key such as `ME-002/FS-EFM/TORTOISE`. The product is generated
on demand, so unused slots do not require 774,180 repeated records. Applicability
defaults to `unknown`. Imported audit dispositions and formalization claims do
not become new results.

The engine runs selected Zoo computations on explicitly supplied inputs. It does
not solve the 102 equations, simulate all triplet PDEs, train the animal models,
or establish their physical correspondence. Those tasks require defined adapters,
data and proof obligations.

## Run it

Use Python 3.10+ on Linux, macOS or WSL; the engine uses only the standard library.
Run these commands from the repository root. No package installation is needed.

```bash
python -m unittest discover -s research_engine/tests -v
python -m research_engine status
python -m research_engine.examples.demo --output /tmp/efmw-demo
```

Open `/tmp/efmw-demo/index.html` in a browser. It works offline. Choose a fresh
directory each time: the demo refuses to overwrite an existing evidence ledger.
The checked-in [dashboard](results/demo-v0.1/index.html) can also be downloaded and
opened locally. GitHub's file view displays source rather than rendering HTML.

The dashboard searches every equation, triplet statement and animal scope. Its
selectors inspect any of the 774,180 slots; the ledger view shows frozen plans,
inputs, outputs, errors and hashes. It is a read-only snapshot. Regenerate it after
new runs. Downloading its ledger JSON exports an array for review; the CLI's native
storage format remains the original JSONL ledger.

## What was executed

| Check | Observed result |
|---|---:|
| Automated test methods | 22 passed |
| Frozen upstream numerical fixture comparisons | 90 matched within 1e-12 relative/absolute tolerance |
| Distinct Zoo adapters exercised | 46 |
| Synthetic demonstration attempts | 48 |
| Computed demonstration outputs | 47 |
| Demonstration criteria met / unmet | 1 / 2 |
| Demonstration attempts without a criterion | 44 |
| Rejected malformed input | 1, retained in ledger |
| Accepted scientific applicability mappings | 0 |
| New formal proofs / scientific promotions | 0 / 0 |

[GitHub Actions verification passed](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/actions/runs/37714223807)
on Python 3.10 and 3.12, including fresh demo reproduction. The separate headless
browser job passed search, selectors, ledger inspection, download and mobile
layout checks. The tested implementation and artifact digests are recorded in
[github-ci.json](results/github-ci.json).

The tests also check the complete Cartesian count, 585 source statements, rank
ties and shape errors, prospective-ranking rejection, placebo/veto precedence,
duplicate evidence groups, parameter types, changed inputs and mappings, altered
code, concurrent ledger writers, tampering and incomplete writes. Prior
FieldSpace mutation controls also pass. See [verification](results/VERIFICATION.md)
and the [demo status](results/demo-v0.1/status.json).

These checks establish software behavior. The fixture expectations originate in
the same upstream Zoo project as the selected specifications; agreement is a
port regression check, not independent scientific replication or a Lean proof.

## Inspect and export the registry

```bash
python -m research_engine schema TORTOISE
python -m research_engine schema OWL
python -m research_engine slots --equation ME-002 --output /tmp/me002-slots.csv
python -m research_engine slots --output /tmp/all-774180-slots.csv
python -m research_engine --ledger research_engine/results/demo-v0.1/demo-ledger.jsonl verify
```

The default working ledger is `research_engine/.state/ledger.jsonl` and is ignored
by git. Choose `--ledger PATH` **before** the subcommand to use another ledger.
Only the synthetic demonstration is checked in. A run is local; the CLI makes no
network calls or automatic uploads.

## Freeze and execute your own test

The demo writes editable `mapping-proposal.json`, `tortoise-input.json` and
`tortoise-plan.json` examples. A plan contains the exact slot, hypothesis,
variables, assumptions, falsifier, matched baseline, known-result comparison,
evidence group, limitations, four audit obligations, a SHA256 input digest and an
optional criterion. Every new run must refer to a previously recorded plan hash.

```bash
python -m research_engine hash /tmp/efmw-demo/tortoise-input.json
python -m research_engine map /tmp/efmw-demo/mapping-proposal.json
python -m research_engine freeze /tmp/efmw-demo/tortoise-plan.json
# Copy the full "hash" from the returned plan record:
python -m research_engine run PLAN_HASH /tmp/efmw-demo/tortoise-input.json
python -m research_engine dashboard --output /tmp/current-efmw-atlas.html
```

`hash` uses the exact file bytes, including whitespace. Update `input_sha256`
before freezing a modified input. A changed input, mapping, catalog or executable
requires a new plan. Error runs remain in the ledger and return exit code 2.
A valid computation whose criterion is `not_met` returns exit code 0: execution
succeeded, while the declared expectation failed. Inspect both fields.

Criteria select an output field (including paths such as `scores.0`) and use
`eq`, `gt`, `ge`, `lt` or `le`. A `met` result means only that this declared output
condition held. It cannot promote a mathematical proof or empirical claim.

### Applicability decisions

| Status | Meaning |
|---|---|
| `unknown` | No applicable adapter established; default for every unrecorded slot |
| `proposed` | A candidate embedding and input interpretation have been written down |
| `accepted` | A named reviewer declares the explicit embedding acceptable for this slot |
| `inapplicable` | A recorded reason excludes this combination; execution is blocked |

`accepted` is a recorded reviewer declaration, not authentication or automatic
mathematical validation. Every mapping must cover the kernel's required input
names with meanings and units, specify equation/triplet roles, and retain
assumptions and evidence sources. Revisions append a new event. Old decisions
and plans remain available. The most recent decision controls future execution.

Two run modes are supported. `synthetic` exercises software and may use an unknown
or proposed mapping; it cannot clear that mapping. `research_retro` requires an
accepted mapping for the frozen catalog. All four anti-circularity obligations
are recorded as caller declarations with source pointers. They are not verified
by the presence of a boolean. No prospective certification mode is implemented.
The plan timestamp establishes order within the execution record, not when the
author first saw the outcome.

The demonstration assigns all 46 kernels to `ME-002/FS-EFM` solely to exercise the
three-axis machinery. This assignment is **not** a scientific route recommendation.
Its one `proposed` TORTOISE mapping describes missing work explicitly.

### Evidence and failures

- `computed` means the selected arithmetic/decision kernel executed successfully.
- `criterion_outcome` separately reports `met`, `not_met`, `not_specified` or
  `not_evaluated`.
- Every run retains its inputs, digest, output when available, failure details,
  frozen plan hash, code/catalog digests and declared evidence group.
- Runs retain `scientific_status: unassessed` and `formal_status: unassessed`.
  This release contains no scientific promotion function.
- Repeated runs on one slot or one source group are not counted as independent
  confirmations. Different group names alone also do not prove independence.
- TURTLE derives counts from supplied distinct applicable group IDs, rejects
  conflicting copies, and preserves veto precedence. Its local output label
  `supported` remains an algorithmic label, not a scientific evidence grade.

The JSONL ledger uses an exclusive POSIX lock for each write transaction, SHA256
links, sequential numbers and fsync. Verification detects altered content,
reordering and incomplete tails relative to a trusted ledger head. Anyone with
write access can rewrite and rehash the entire file or remove a complete suffix;
retain published head hashes or git history as external anchors. This is not a
signed, authenticated or distributed log. Do not delete damaged tails silently.

## Selected kernel coverage and limits

The source Zoo snapshot describes **uncompiled draft Lean formalizations**. The
Python ports do not compile those files or prove floating-point equivalence.
The operations are frozen to the referenced source definitions. Numeric inputs
must be finite, types are strict, specified domain ranges are checked, and unknown
parameters are rejected. Counts must be nonnegative integers below 2^53; ancestry
traversal has explicit resource limits. These are adapter domain restrictions.

The 17 rank adapters are OWL, OCTOPUS, GECKO, HIVE, EAGLE, CRAB, SHEPHERD, PULSE,
FOX, SPIDER, RAVEN, DOLPHIN, ANT, MOTH, SHARK, PENGUIN and DRAGON. Each takes
precomputed columns in its frozen component order and averages percentile ranks
with average ties. Required column count is `base + horizons × per_horizon`.
[Component definitions](data/zoo-ranked-components.json) specify the input order.
Clipping, inversion, rolling features and other feature transformations described
there must already have been applied. The adapter does **not** extract them from
raw observations. Full-column ranks may see future rows, so these kernels enforce
retrospective mode. Empty datasets return no scores; ragged inputs are errors.

The other 29 adapters expose the following selected operations. Use `schema NAME`
for exact parameter names and defaults; the [frozen source bundle](data/zoo-specifications.json)
also preserves additional upstream operations that are **not** all ported here.

| Animal | Implemented computation |
|---|---|
| TORTOISE | Brier gain from two supplied scores |
| CAT | Ablation penalty and sign |
| BAT | Placebo-first baseline decision |
| HEDGEHOG | Summary decision plus supplied environment-ID disjointness |
| CROCODILE | Difference-in-differences arithmetic |
| TURTLE | Applicability/veto/group decision with duplicate-group control |
| MAGPIE | Groundedness and falling-groundedness alarm |
| WOLF | EMA update |
| ELEPHANT | Active event filter and bounded lineage |
| CHAMELEON | Unexplained and noise-adjusted distances |
| JELLYFISH | Dynamic edge weight and single-node health update |
| BEAVER | Effectiveness/collateral/verification/bounds/rollback gates |
| MANTIS | Calibration, precursor and intervention decision |
| BISON | Served demand, queue and overflow |
| WEASEL | Supplied counterexample filter |
| SALMON | Unresolved mass and bounded ancestry |
| ORCA | Four-field handoff integrity |
| MOLE | Hidden-failure gap and coverage gate |
| LYNX | Novelty/yield arithmetic and emergence gates |
| HORSE | Workload penalty |
| TERMITE | Single-agent snapshot update |
| PHOENIX | Recovery completeness and finite-window stability |
| COBRA | Persistent divergence and confidence-weighted risk |
| WHALE | Cumulative deviation and history gap |
| FALCON | Latency, reaction margin and missed-hazard gate |
| RHINO | Performance retention |
| BONOBO | Exploitation sum and cooperative score |
| AXOLOTL | Recovery, efficiency and resilience |
| BUTTERFLY | One nonlinear clipped layer step |

Branch ordering and awkward boundaries are retained: BAT's placebo gate comes
first; TURTLE checks no-applicable before veto; PHOENIX's zero-length stability
window is vacuously true and labeled as such; WHALE's zero window retains its
upstream behavior. SALMON exhaustion remains distinct from a resolved origin.
ELEPHANT adds an explicit termination reason to its otherwise source-shaped list.
Causal assumptions, genuine rollback, graph scheduling, novelty, meaningful
invariants and independent outcomes remain external obligations.

## Frozen provenance

| Catalog | Repository | Commit |
|---|---|---|
| Canonical 102 equations | `enuminous/Monolithic_102_EFMW` | `26a3c057a80f4c60566a543427d6d85fc1aa349f` |
| 165 triplet source | `enuminous/Einsteinian-156-Aristotle` | `7e60205d2370c335ebe2cafe89d6e0bbe842ba01` |
| Canonical 46 and selected specs | `enuminous/Monolithic-Zoo-Lean4` | `94e0a9e2550a8fe62b03dc8213e3e3942c30899b` |
| Prior equation audit, imported metadata only | `enuminous/Monolithic-102-Zoo-Lean4` | `05e6d093e1d22c9fded9ee3d2f10b0d56d53e256` |

[provenance.json](data/provenance.json) hashes every frozen input. Canonical equation
IDs, titles and formulas are copied without correction. Triplet IDs sort the
sector letters; source headings, order and statement text are retained. The
165 source-derived records are checked against the existing strict FieldSpace
parser. Shared letters do not establish a physical mapping. Original Zoo source
attribution, per-animal upstream SHAs, scope exclusions and draft proof statuses
remain in [coverage](data/zoo-coverage.json). The reused Zoo specifications retain
their [MIT license](data/zoo-LICENSE); this does not relicense other corpus items.

## Next concrete research task

Resolve the single candidate `ME-002/FS-EFM/TORTOISE` adapter: define φ ↔ φ_F,
units, metric/derivative conventions, source and interaction terms; derive a
specific forecast and matched baseline; supply independent heldout outcomes; then
review that mapping. A source-free, massless scalar limit may be a useful
comparison, but that limiting agreement would not establish the full coupled
system. The previous conditional gluing proof, mixed-current specification,
vacuum stress and conservation obligations remain separate work.
