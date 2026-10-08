# Research engine v0.1 verification

The preserved demonstration is synthetic. No observed EFMW measurements, accepted
physical mappings, new formal proofs or scientific promotions are included.

## Local execution

- Python 3.12.14, POSIX execution environment.
- `python -m unittest discover -s research_engine/tests -v`: **22 tests passed**.
  This includes **90 frozen upstream numeric comparisons** with relative and
  absolute tolerances of 1e-12, plus execution of all **46** adapters.
- `python scripts/test_fieldspace_audit.py`: **6 existing mutation tests passed**.
- CLI `map → freeze → run → dashboard → verify`: passed in a fresh temporary ledger.
- Generated HTML: unique element IDs, parseable embedded JSON containing all
  102/165/46 records, no unresolved template marker, and valid JavaScript syntax.
- Ledger/source verification passed. The SHA256 head is retained in
  [status.json](demo-v0.1/status.json); plans also pin the exact code and catalog.

The [Python test log](python-tests.log) and [FieldSpace test log](fieldspace-tests.log)
preserve these command outputs.

## Demonstration outcomes

| Measure | Result |
|---|---:|
| Potential slots | 774,180 |
| Unknown applicability | 774,179 |
| Proposed mappings | 1 |
| Accepted mappings | 0 |
| Frozen plans / synthetic attempts | 48 / 48 |
| Successful computations | 47 |
| Unmet criteria | 2, retained |
| Invalid input | 1, retained |
| Research attempts | 0 |
| New formal proofs / scientific promotions | 0 / 0 |

One unmet criterion is BAT's placebo veto; the other is negative TORTOISE gain.
The error case supplies a string where a numeric Brier score is required.
Repeated copies in TURTLE's example remain one group and yield `insufficient`.

## Browser verification

Local browser execution was unavailable: the environment had no Chromium binary
and the attempted browser download returned an invalid archive. Static checks
passed; this is not presented as a successful local browser render.

The new `EFMW research engine` GitHub Actions workflow separately runs Python
3.10/3.12 tests and a pinned Playwright browser check. The browser check exercises
all three catalog selectors, mapping changes, search, the 48-row ledger, retained
errors, JSON download, sources, mobile-width overflow and JavaScript errors, and
retains desktop/mobile screenshots. Its remote result is recorded after execution.

## Scope

The original Zoo Lean files remain an upstream uncompiled draft snapshot. Numeric
fixture agreement does not prove equivalence to Lean or establish physical
truth. Existing Lean gluing results and their earlier build evidence remain in
their original audit records; this change does not rerun or expand those proofs.
