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

**Passed in [GitHub Actions run 37714223807](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/actions/runs/37714223807)**
on implementation commit `317379c6416fab8df79b854a12d67cc1c7782865`.
All three jobs succeeded: Python 3.10, Python 3.12 and the dashboard browser test.
Both Python jobs verified the preserved ledger and independently regenerated the
demonstration in a fresh directory.

The headless browser check confirmed all 102/165/46 selectors, mapping changes,
search, the 48-row ledger, retained errors, JSON download, source records,
mobile-width overflow and absence of JavaScript errors. It retained
[desktop/mobile screenshots](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/actions/runs/37714223807/artifacts/11523321111).
The artifact has GitHub's stated expiry of 2027-01-06; the workflow can regenerate
it. [github-ci.json](github-ci.json) preserves job IDs, the browser success output,
tested commit, executable digest and screenshot archive digest.

Local static checks also passed. The successful browser execution was remote:
local Chromium was unavailable and its attempted download returned an invalid
archive. No successful local browser render is claimed.

## Scope

The original Zoo Lean files remain an upstream uncompiled draft snapshot. Numeric
fixture agreement does not prove equivalence to Lean or establish physical
truth. Existing Lean gluing results and their earlier build evidence remain in
their original audit records; this change does not rerun or expand those proofs.
