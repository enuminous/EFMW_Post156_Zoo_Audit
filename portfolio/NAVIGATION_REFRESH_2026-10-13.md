# Repository navigation refresh — October 13, 2026

This refresh adds nine repositories created since the prior 106-public-repository catalog. The directory now contains **115 public repositories**, with **34 verified GitHub Pages sites**.

The [public directory](https://enuminous.github.io/EFMW/repositories.html) is the common entry point. Every public root README links to it, the major destinations, and the nine recent projects. Each existing regular index page has the shared Recent and All Pages menus plus direct links to its own README and repository. Existing local navigation and scientific content are preserved.

## Recent additions

| Repository | README | Published page or source |
|---|---|---|
| [Oroboros](https://github.com/enuminous/Oroboros) | [README](https://github.com/enuminous/Oroboros/blob/main/README.md) | [Published page](https://enuminous.github.io/Oroboros/) |
| [P-NP](https://github.com/enuminous/P-NP) | [README](https://github.com/enuminous/P-NP/blob/main/README.md) | [Published page](https://enuminous.github.io/P-NP/) |
| [Research-Program](https://github.com/enuminous/Research-Program) | [README](https://github.com/enuminous/Research-Program/blob/main/README.md) | [Published page](https://enuminous.github.io/Research-Program/) |
| [I-Have-Guts](https://github.com/enuminous/I-Have-Guts) | [README](https://github.com/enuminous/I-Have-Guts/blob/main/README.md) | [Published page](https://enuminous.github.io/I-Have-Guts/) |
| [Wrights-Law](https://github.com/enuminous/Wrights-Law) | [README](https://github.com/enuminous/Wrights-Law/blob/main/README.md) | [Published page](https://enuminous.github.io/Wrights-Law/) |
| [Aristotle-eNuminous](https://github.com/enuminous/Aristotle-eNuminous) | [README](https://github.com/enuminous/Aristotle-eNuminous/blob/main/README.md) | [Published page](https://enuminous.github.io/Aristotle-eNuminous/) |
| [Multiverse-Simulator](https://github.com/enuminous/Multiverse-Simulator) | [README](https://github.com/enuminous/Multiverse-Simulator/blob/main/README.md) | [Published page](https://enuminous.github.io/Multiverse-Simulator/) |
| [accelerando-8192](https://github.com/enuminous/accelerando-8192) | [README](https://github.com/enuminous/accelerando-8192/blob/main/README.md) | [HTML source (Pages disabled)](https://github.com/enuminous/accelerando-8192/blob/main/docs/index.html) |
| [Codex-888](https://github.com/enuminous/Codex-888) | [README](https://github.com/enuminous/Codex-888/blob/main/README.md) | [Published page](https://enuminous.github.io/Codex-888/) |

Alchemy-of-Emergence was already cataloged but now has an enabled, verified Pages site. Its published-page link and the shared All Pages list are updated too. The upstream live-site link in the accelerando-8192 fork remains intact; the eNuminous fork is linked as source because its own Pages deployment is disabled.

## Coverage and validation

- 115 public root READMEs updated.
- 117 regular index files updated, plus the audit dashboard template and central repository directory.
- 34 site roots and 36 index-page URLs returned HTTP 200 before publication.
- 343 unique navigation URLs checked against live-page observations or the current public source inventory.
- All existing page content outside the navigation blocks preserved exactly; README content preserved apart from changing the Aristotle-eNuminous dashboard link to its verified hosted URL.
- A second maintenance pass produced no changes: the operation is idempotent.
- Current checksum entries for changed presentation files refreshed. Historical freeze receipts and experimental data are unchanged.
- Both copies of repositories.json match. Source commits identify the inventory before this navigation refresh.

73 symbolic-link index entries in monster were left as links; regular targets were processed. OpenAI-math was inspected at its root only: its large upstream proof archive was not rescanned or rewritten. Private repositories are excluded from the public catalog and were not modified. This is a navigation refresh, not a scientific re-audit or a claim that every unrelated historical link works.

## Maintenance

See [the maintenance guide](README.md), [navigation.py](navigation.py), [navigation configuration](navigation.json), and [the shared HTML template](navigation-template.html). New projects belong in the registry and the recent-project configuration; published URLs should be verified before entering the menu. The script only emits Open page links for the explicit, checked page_urls mapping.

[Publication receipts and checks](navigation-refresh-2026-10-13.json) record the resulting repository commits. The report repository's own commit is the commit containing this file.
