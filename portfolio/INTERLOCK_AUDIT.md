# eNuminous interlocking repository audit

Audit date: **2026-10-10 (Pacific)**. The machine-readable snapshot records UTC observation times and the exact source commits.

## Result and scope

The authenticated inventory contains **107 accessible repositories: 106 public and one private**. Every repository was included in the integration pass. This public report and directory contain only the 106 public repositories; the private repository receives the same public navigation without being listed here.

This is a complete repository-coverage audit of **root READMEs, HTML entry indexes, source paths, cross-repository navigation, Pages availability and observed CI**. It is not a fresh execution of every program, a Lean rebuild of every theorem corpus, a security audit, or an empirical validation of EFMW, OPH or Cadence.

The inventory combines repository listing and paginated search because the listing endpoint omitted seven recent repositories. All trees were scanned, including the large `OpenAI-math` fork; truncated tree responses were split into complete subtrees. Commit pins are in [repositories.json](repositories.json). The existing root `docs/AGENTS.md` was considered before its README edit.

## Navigation changes

- One shared top menu links the main EFMW, 102-equation, 165-triplet, Zoo, Lean, Engine, Papers and Audit destinations, plus every Pages repository.
- Every root README links to the public directory, major repositories and its own HTML indexes. Existing README filename casing is preserved.
- The [public repository directory](https://enuminous.github.io/EFMW/repositories.html) lists all 106 public repositories with README, source, Pages and index links. Every public repository can reach every other through this directory.
- Menus are embedded in each HTML entrypoint, including nested demos and the `medium` redirect destination. The audit dashboard's source template is updated so its menu survives regeneration.
- Ordinary links and native details controls work without a remote script. Existing local controls and page content are preserved.
- Four missing root READMEs are added: `medium`, `Medium2`, `Medium3`, and `papers`.

## Confirmed repairs

| Finding | Resolution |
|---|---|
| `Aristotle_EFMW_Lean` had Pages enabled but returned HTTP 404 | Added a root index linked to the actual status map and Lean source. It does not assert a new proof build. |
| `Medium3` identified itself as Medium2 and exposed no archive menu | Replaced the placeholder with a correctly titled, searchable archive index. |
| 239 links in the writing catalog used `/medium2/` | Corrected them to the repository's case-sensitive `/Medium2/` Pages path. |
| Two Monolithic 102 README destinations no longer existed | Pointed them to the existing `EQUATION_INDEX.md` and root `equations.json`. |
| Four `monster` documentation/proof links used old relative paths | Pointed them to the observed current files. |
| 73 nested `monster` index symlinks used an absolute path on the original author's computer | Replaced their targets with equivalent repository-relative paths; every target exists and receives the shared menu. |
| Five checksum entries for edited files were already stale | Recorded original and actual hashes, then refreshed the current inventories for changed files only. |
| `Verbinski-Protocol/SHA256SUMS.txt` included a checksum of itself | Removed the self-entry from the current inventory; prior content remains in Git history. |

Historical hashes and change classifications are recorded in [findings.json](findings.json). Existing mismatch observations concern the inspected README/index entries, not a claim that every file in every manifest was rehashed. Frozen experiment manifests remain unchanged; the pre-navigation README is linked by commit in the affected repository.

## Stragglers requiring further work

- [EFMW-Axioms](https://github.com/enuminous/EFMW-Axioms/actions/runs/37555311743): `Build formalization` failed; later checks were skipped.
- [EFMW-Constants-Problem](https://github.com/enuminous/EFMW-Constants-Problem/actions/runs/37558093921): `Build formalization` failed; later checks were skipped.
- `meta-meme/README.md` references `glossary.md`, which is absent from its tree. No reliable replacement was found, so the original link is recorded as unresolved rather than inventing content.
- HTML entrypoints exist without GitHub Pages enabled in **`Alchemy-of-Emergence`, `EFMW_Post156_Zoo_Audit`, `monster`, `oph-lab`, `papers`**. The directory routes these to source. No hosting or visibility settings were changed.
- The external ChatGPT-hosted Atlas returned an access error in this environment. Its live content could not be verified; the GitHub-hosted directory is independently usable.
- `Coherence-Prediction-Engine` has a failed older Pages workflow lane alongside a successful newer static deployment. Its live page returned 200; the old failure is retained as history, not labeled a current outage.

## Validation and limits

Before the changes, **24 of 25 enabled Pages roots returned HTTP 200**; `Aristotle_EFMW_Lean` returned 404. `/Medium/` returned 404 while the actual `/medium/` returned 200. The source audit checked 3679 extracted local and eNuminous link destinations in root READMEs and entry indexes. It does not include every external citation, dynamic JavaScript URL, or article body.

All 107 root README blocks and all tracked HTML entry indexes are checked for a single shared menu, real source destinations and portable symlink targets. New navigation is idempotent. Pages are checked again after rollout; [rollout.json](rollout.json) records commit receipts and [verification.json](verification.json) records the checks actually completed. A commit receipt is not by itself a live-deployment receipt.

Recorded CI is the latest run per observed workflow among up to 20 default-branch runs for repositories with root workflow definitions. A successful Pages deployment is not a Lean proof result. The two Lean failures remain explicit. Proof files, mathematical definitions, experimental data and acceptance criteria are outside this navigation change.

## Repository ledger

Every row has a root README and a route through the common directory. “Source” means Pages is not enabled; it is not a broken project. Workflow observations are from the source snapshot, before this rollout.

| Repository | Root | Destination | Index files | Observed workflows |
|---|---|---|---:|---|
| [Alchemy-of-Emergence](https://github.com/enuminous/Alchemy-of-Emergence) | [README](https://github.com/enuminous/Alchemy-of-Emergence/blob/main/README.md) | Source | 1 | No root workflow observed |
| [Ant](https://github.com/enuminous/Ant) | [README](https://github.com/enuminous/Ant/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Archimedes-3D](https://github.com/enuminous/Archimedes-3D) | [README](https://github.com/enuminous/Archimedes-3D/blob/main/README.md) | [Pages](https://enuminous.github.io/Archimedes-3D/) | 2 | Deploy static content to Pages: success |
| [Archimedes-Engine](https://github.com/enuminous/Archimedes-Engine) | [README](https://github.com/enuminous/Archimedes-Engine/blob/main/README.md) | [Pages](https://enuminous.github.io/Archimedes-Engine/) | 1 | Deploy static content to Pages: success; pages build and deployment: success |
| [Archimedes-Field-Lab](https://github.com/enuminous/Archimedes-Field-Lab) | [README](https://github.com/enuminous/Archimedes-Field-Lab/blob/main/README.md) | [Pages](https://enuminous.github.io/Archimedes-Field-Lab/) | 1 | Deploy Archimedes Field Lab: success; pages build and deployment: success |
| [Aristotle-102-Monolithic-Lean](https://github.com/enuminous/Aristotle-102-Monolithic-Lean) | [README](https://github.com/enuminous/Aristotle-102-Monolithic-Lean/blob/main/README.md) | [Pages](https://enuminous.github.io/Aristotle-102-Monolithic-Lean/) | 1 | No root workflow observed |
| [Aristotle-165-Einsteinian-Tensors](https://github.com/enuminous/Aristotle-165-Einsteinian-Tensors) | [README](https://github.com/enuminous/Aristotle-165-Einsteinian-Tensors/blob/main/README.md) | [Pages](https://enuminous.github.io/Aristotle-165-Einsteinian-Tensors/) | 1 | No root workflow observed |
| [Aristotle-Agreement-and-Surprise-Global-Equalibrium-from-Local-Repair](https://github.com/enuminous/Aristotle-Agreement-and-Surprise-Global-Equalibrium-from-Local-Repair) | [README](https://github.com/enuminous/Aristotle-Agreement-and-Surprise-Global-Equalibrium-from-Local-Repair/blob/main/README.md) | [Pages](https://enuminous.github.io/Aristotle-Agreement-and-Surprise-Global-Equalibrium-from-Local-Repair/) | 1 | No root workflow observed |
| [Aristotle_EFMW_Lean](https://github.com/enuminous/Aristotle_EFMW_Lean) | [README](https://github.com/enuminous/Aristotle_EFMW_Lean/blob/main/README.md) | [Pages](https://enuminous.github.io/Aristotle_EFMW_Lean/) | 1 | Deploy static content to Pages: success; CI: success |
| [Avenue5](https://github.com/enuminous/Avenue5) | [README](https://github.com/enuminous/Avenue5/blob/main/README.md) | [Pages](https://enuminous.github.io/Avenue5/) | 1 | Deploy static content to Pages: success |
| [Axolotl](https://github.com/enuminous/Axolotl) | [README](https://github.com/enuminous/Axolotl/blob/main/README.md) | Source | 0 | No root workflow observed |
| [BackroomsProtocol-EFMW-Analysis](https://github.com/enuminous/BackroomsProtocol-EFMW-Analysis) | [README](https://github.com/enuminous/BackroomsProtocol-EFMW-Analysis/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Bat](https://github.com/enuminous/Bat) | [README](https://github.com/enuminous/Bat/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Beaver](https://github.com/enuminous/Beaver) | [README](https://github.com/enuminous/Beaver/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Bison](https://github.com/enuminous/Bison) | [README](https://github.com/enuminous/Bison/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Bonobo](https://github.com/enuminous/Bonobo) | [README](https://github.com/enuminous/Bonobo/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Borges-Library-CollapseOmega](https://github.com/enuminous/Borges-Library-CollapseOmega) | [README](https://github.com/enuminous/Borges-Library-CollapseOmega/blob/main/README.md) | [Pages](https://enuminous.github.io/Borges-Library-CollapseOmega/) | 1 | Deploy static library to GitHub Pages: success; pages build and deployment: success |
| [Butterfly](https://github.com/enuminous/Butterfly) | [README](https://github.com/enuminous/Butterfly/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Cadence-Zoo-Evidence](https://github.com/enuminous/Cadence-Zoo-Evidence) | [README](https://github.com/enuminous/Cadence-Zoo-Evidence/blob/main/readme.md) | [Pages](https://enuminous.github.io/Cadence-Zoo-Evidence/) | 1 | No root workflow observed |
| [Cat](https://github.com/enuminous/Cat) | [README](https://github.com/enuminous/Cat/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Chameleon](https://github.com/enuminous/Chameleon) | [README](https://github.com/enuminous/Chameleon/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Chimera](https://github.com/enuminous/Chimera) | [README](https://github.com/enuminous/Chimera/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Circus](https://github.com/enuminous/Circus) | [README](https://github.com/enuminous/Circus/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Cobra](https://github.com/enuminous/Cobra) | [README](https://github.com/enuminous/Cobra/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Coherence-Prediction-Engine](https://github.com/enuminous/Coherence-Prediction-Engine) | [README](https://github.com/enuminous/Coherence-Prediction-Engine/blob/main/README.md) | [Pages](https://enuminous.github.io/Coherence-Prediction-Engine/) | 1 | Deploy static content to Pages: success; pages build and deployment: failure |
| [Crab](https://github.com/enuminous/Crab) | [README](https://github.com/enuminous/Crab/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Crocodile](https://github.com/enuminous/Crocodile) | [README](https://github.com/enuminous/Crocodile/blob/main/README.md) | Source | 0 | No root workflow observed |
| [DePIN](https://github.com/enuminous/DePIN) | [README](https://github.com/enuminous/DePIN/blob/main/README.md) | Source | 0 | No root workflow observed |
| [docs](https://github.com/enuminous/docs) | [README](https://github.com/enuminous/docs/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Dolphin](https://github.com/enuminous/Dolphin) | [README](https://github.com/enuminous/Dolphin/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Dragon](https://github.com/enuminous/Dragon) | [README](https://github.com/enuminous/Dragon/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Eagle](https://github.com/enuminous/Eagle) | [README](https://github.com/enuminous/Eagle/blob/main/README.md) | Source | 0 | No root workflow observed |
| [EFMW](https://github.com/enuminous/EFMW) | [README](https://github.com/enuminous/EFMW/blob/main/README.md) | [Pages](https://enuminous.github.io/EFMW/) | 1 | No root workflow observed |
| [EFMW-108-Minute-Tests](https://github.com/enuminous/EFMW-108-Minute-Tests) | [README](https://github.com/enuminous/EFMW-108-Minute-Tests/blob/main/README.md) | Source | 0 | No root workflow observed |
| [EFMW-Axioms](https://github.com/enuminous/EFMW-Axioms) | [README](https://github.com/enuminous/EFMW-Axioms/blob/main/README.md) | [Pages](https://enuminous.github.io/EFMW-Axioms/) | 1 | pages build and deployment: success; Lean: failure |
| [EFMW-Constants-Problem](https://github.com/enuminous/EFMW-Constants-Problem) | [README](https://github.com/enuminous/EFMW-Constants-Problem/blob/main/README.md) | [Pages](https://enuminous.github.io/EFMW-Constants-Problem/) | 1 | pages build and deployment: success; Lean: failure |
| [EFMW-CTX-001b](https://github.com/enuminous/EFMW-CTX-001b) | [README](https://github.com/enuminous/EFMW-CTX-001b/blob/main/README.md) | Source | 0 | No root workflow observed |
| [efmw-equation-review](https://github.com/enuminous/efmw-equation-review) | [README](https://github.com/enuminous/efmw-equation-review/blob/main/README.md) | Source | 0 | No root workflow observed |
| [EFMW-EXP-001](https://github.com/enuminous/EFMW-EXP-001) | [README](https://github.com/enuminous/EFMW-EXP-001/blob/main/README.md) | Source | 0 | No root workflow observed |
| [EFMW-FULL](https://github.com/enuminous/EFMW-FULL) | [README](https://github.com/enuminous/EFMW-FULL/blob/main/README.md) | Source | 0 | No root workflow observed |
| [EFMW-Neutron-Star-Glitch-Resonance](https://github.com/enuminous/EFMW-Neutron-Star-Glitch-Resonance) | [README](https://github.com/enuminous/EFMW-Neutron-Star-Glitch-Resonance/blob/main/README.md) | [Pages](https://enuminous.github.io/EFMW-Neutron-Star-Glitch-Resonance/) | 1 | Deploy static content to Pages: success; pages build and deployment: success |
| [efmw-research-cache](https://github.com/enuminous/efmw-research-cache) | [README](https://github.com/enuminous/efmw-research-cache/blob/main/README.md) | Source | 0 | No root workflow observed |
| [EFMW-Safety-001](https://github.com/enuminous/EFMW-Safety-001) | [README](https://github.com/enuminous/EFMW-Safety-001/blob/main/README.md) | Source | 0 | No root workflow observed |
| [EFMW-Scientific-Claims](https://github.com/enuminous/EFMW-Scientific-Claims) | [README](https://github.com/enuminous/EFMW-Scientific-Claims/blob/main/README.md) | [Pages](https://enuminous.github.io/EFMW-Scientific-Claims/) | 1 | Deploy static content to Pages: success; pages build and deployment: success |
| [EFMW_Post156_Zoo_Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit) | [README](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/README.md) | Source | 1 | EFMW research engine: success; Lean and FieldSpace audit: success |
| [Einsteinian-156-Aristotle](https://github.com/enuminous/Einsteinian-156-Aristotle) | [README](https://github.com/enuminous/Einsteinian-156-Aristotle/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Elephant](https://github.com/enuminous/Elephant) | [README](https://github.com/enuminous/Elephant/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Emergentology](https://github.com/enuminous/Emergentology) | [README](https://github.com/enuminous/Emergentology/blob/main/README.md) | [Pages](https://enuminous.github.io/Emergentology/) | 1 | Deploy static content to Pages: success; pages build and deployment: success |
| [Falcon](https://github.com/enuminous/Falcon) | [README](https://github.com/enuminous/Falcon/blob/main/README.md) | Source | 0 | No root workflow observed |
| [fieldcore](https://github.com/enuminous/fieldcore) | [README](https://github.com/enuminous/fieldcore/blob/main/README.md) | Source | 0 | No root workflow observed |
| [FieldSpace](https://github.com/enuminous/FieldSpace) | [README](https://github.com/enuminous/FieldSpace/blob/main/README.md) | [Pages](https://enuminous.github.io/FieldSpace/) | 1 | Deploy static content to Pages: success; pages build and deployment: success |
| [Fox](https://github.com/enuminous/Fox) | [README](https://github.com/enuminous/Fox/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Gecko](https://github.com/enuminous/Gecko) | [README](https://github.com/enuminous/Gecko/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Harlequinn](https://github.com/enuminous/Harlequinn) | [README](https://github.com/enuminous/Harlequinn/blob/master/README.md) | Source | 0 | No root workflow observed |
| [Hedgehog](https://github.com/enuminous/Hedgehog) | [README](https://github.com/enuminous/Hedgehog/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Hive](https://github.com/enuminous/Hive) | [README](https://github.com/enuminous/Hive/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Horse](https://github.com/enuminous/Horse) | [README](https://github.com/enuminous/Horse/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Jellyfish](https://github.com/enuminous/Jellyfish) | [README](https://github.com/enuminous/Jellyfish/blob/main/README.md) | Source | 0 | No root workflow observed |
| [JEV-EFMW-Syncretic-Layer](https://github.com/enuminous/JEV-EFMW-Syncretic-Layer) | [README](https://github.com/enuminous/JEV-EFMW-Syncretic-Layer/blob/main/README.md) | Source | 0 | No root workflow observed |
| [lean-worker](https://github.com/enuminous/lean-worker) | [README](https://github.com/enuminous/lean-worker/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Ligo_EFMW_Search](https://github.com/enuminous/Ligo_EFMW_Search) | [README](https://github.com/enuminous/Ligo_EFMW_Search/blob/main/readme.md) | Source | 0 | No root workflow observed |
| [Lynx](https://github.com/enuminous/Lynx) | [README](https://github.com/enuminous/Lynx/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Magpie](https://github.com/enuminous/Magpie) | [README](https://github.com/enuminous/Magpie/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Mantis](https://github.com/enuminous/Mantis) | [README](https://github.com/enuminous/Mantis/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Mathematics-and-Elite-Squad-Dynamics](https://github.com/enuminous/Mathematics-and-Elite-Squad-Dynamics) | [README](https://github.com/enuminous/Mathematics-and-Elite-Squad-Dynamics/blob/main/README.md) | [Pages](https://enuminous.github.io/Mathematics-and-Elite-Squad-Dynamics/) | 1 | No root workflow observed |
| [medium](https://github.com/enuminous/medium) | [README](https://github.com/enuminous/medium/blob/main/README.md) | [Pages](https://enuminous.github.io/medium/) | 2 | Deploy static content to Pages: success; pages build and deployment: success |
| [Medium2](https://github.com/enuminous/Medium2) | [README](https://github.com/enuminous/Medium2/blob/main/README.md) | [Pages](https://enuminous.github.io/Medium2/) | 1 | Deploy static content to Pages: success; pages build and deployment: success |
| [Medium3](https://github.com/enuminous/Medium3) | [README](https://github.com/enuminous/Medium3/blob/main/README.md) | [Pages](https://enuminous.github.io/Medium3/) | 1 | No root workflow observed |
| [meta-meme](https://github.com/enuminous/meta-meme) | [README](https://github.com/enuminous/meta-meme/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Mole](https://github.com/enuminous/Mole) | [README](https://github.com/enuminous/Mole/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Monlithic_EFMW_102_Lean4](https://github.com/enuminous/Monlithic_EFMW_102_Lean4) | [README](https://github.com/enuminous/Monlithic_EFMW_102_Lean4/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Monolithic-102-Zoo-Lean4](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) | [README](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Monolithic-Zoo-Lean4](https://github.com/enuminous/Monolithic-Zoo-Lean4) | [README](https://github.com/enuminous/Monolithic-Zoo-Lean4/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Monolithic_102_EFMW](https://github.com/enuminous/Monolithic_102_EFMW) | [README](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Monolithic_Zoo_Run](https://github.com/enuminous/Monolithic_Zoo_Run) | [README](https://github.com/enuminous/Monolithic_Zoo_Run/blob/main/README.md) | Source | 0 | No root workflow observed |
| [monster](https://github.com/enuminous/monster) | [README](https://github.com/enuminous/monster/blob/main/README.md) | Source | 150 | No root workflow observed |
| [Moth](https://github.com/enuminous/Moth) | [README](https://github.com/enuminous/Moth/blob/main/README.md) | Source | 0 | No root workflow observed |
| [MultiValuedClassicalAction-Lean4](https://github.com/enuminous/MultiValuedClassicalAction-Lean4) | [README](https://github.com/enuminous/MultiValuedClassicalAction-Lean4/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Nightengale](https://github.com/enuminous/Nightengale) | [README](https://github.com/enuminous/Nightengale/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Nightengale-Full-Zoo-Audit](https://github.com/enuminous/Nightengale-Full-Zoo-Audit) | [README](https://github.com/enuminous/Nightengale-Full-Zoo-Audit/blob/main/readme.md) | Source | 0 | No root workflow observed |
| [Octopus](https://github.com/enuminous/Octopus) | [README](https://github.com/enuminous/Octopus/blob/main/README.md) | Source | 0 | No root workflow observed |
| [OpenAI-math](https://github.com/enuminous/OpenAI-math) | [README](https://github.com/enuminous/OpenAI-math/blob/main/README.md) | Source | 0 | No root workflow observed |
| [oph-lab](https://github.com/enuminous/oph-lab) | [README](https://github.com/enuminous/oph-lab/blob/main/README.md) | Source | 1 | OPH Stage 4 Lean: success |
| [Orca](https://github.com/enuminous/Orca) | [README](https://github.com/enuminous/Orca/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Owl](https://github.com/enuminous/Owl) | [README](https://github.com/enuminous/Owl/blob/main/README.md) | Source | 0 | No root workflow observed |
| [papers](https://github.com/enuminous/papers) | [README](https://github.com/enuminous/papers/blob/main/README.md) | Source | 1 | No root workflow observed |
| [Penguin](https://github.com/enuminous/Penguin) | [README](https://github.com/enuminous/Penguin/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Phoenix](https://github.com/enuminous/Phoenix) | [README](https://github.com/enuminous/Phoenix/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Pulse](https://github.com/enuminous/Pulse) | [README](https://github.com/enuminous/Pulse/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Raven](https://github.com/enuminous/Raven) | [README](https://github.com/enuminous/Raven/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Rhino](https://github.com/enuminous/Rhino) | [README](https://github.com/enuminous/Rhino/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Salmon](https://github.com/enuminous/Salmon) | [README](https://github.com/enuminous/Salmon/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Shark](https://github.com/enuminous/Shark) | [README](https://github.com/enuminous/Shark/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Shepherd](https://github.com/enuminous/Shepherd) | [README](https://github.com/enuminous/Shepherd/blob/main/README.md) | Source | 0 | No root workflow observed |
| [simself](https://github.com/enuminous/simself) | [README](https://github.com/enuminous/simself/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Spider](https://github.com/enuminous/Spider) | [README](https://github.com/enuminous/Spider/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Termite](https://github.com/enuminous/Termite) | [README](https://github.com/enuminous/Termite/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Tortoise](https://github.com/enuminous/Tortoise) | [README](https://github.com/enuminous/Tortoise/blob/main/README.md) | [Pages](https://enuminous.github.io/Tortoise/) | 1 | No root workflow observed |
| [Turtle](https://github.com/enuminous/Turtle) | [README](https://github.com/enuminous/Turtle/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Universal-Cognitive-Attractor](https://github.com/enuminous/Universal-Cognitive-Attractor) | [README](https://github.com/enuminous/Universal-Cognitive-Attractor/blob/main/README.md) | [Pages](https://enuminous.github.io/Universal-Cognitive-Attractor/) | 1 | No root workflow observed |
| [Verbinski-Protocol](https://github.com/enuminous/Verbinski-Protocol) | [README](https://github.com/enuminous/Verbinski-Protocol/blob/main/README.md) | [Pages](https://enuminous.github.io/Verbinski-Protocol/) | 1 | Deploy static content to Pages: success; pages build and deployment: success |
| [Weasel](https://github.com/enuminous/Weasel) | [README](https://github.com/enuminous/Weasel/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Whale](https://github.com/enuminous/Whale) | [README](https://github.com/enuminous/Whale/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Wolf](https://github.com/enuminous/Wolf) | [README](https://github.com/enuminous/Wolf/blob/main/README.md) | Source | 0 | No root workflow observed |
| [woodpecker](https://github.com/enuminous/woodpecker) | [README](https://github.com/enuminous/woodpecker/blob/main/README.md) | Source | 0 | No root workflow observed |
| [Zoo-Monster](https://github.com/enuminous/Zoo-Monster) | [README](https://github.com/enuminous/Zoo-Monster/blob/main/README.md) | Source | 0 | No root workflow observed |

## Maintenance

Use the [navigation maintenance guide](README.md) and the canonical template. Public registry snapshots exclude private repositories. Rollback is a normal revert of each recorded navigation commit; no forced branch updates are used.
