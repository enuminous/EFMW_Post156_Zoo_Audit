# Repository lifecycle and duplication review — 2026-10-16

This review marks obsolete claims, historical entry points and duplicated files without treating every related repository as obsolete. No whole repository was shown to be safely replaceable in its entirety.

## Scope and evidence

Reviewed the default-branch README and source inventory of **119 public enuminous repositories**. The inventory contains 118 complete recursive Git trees; `OpenAI-math` has a root-tree-only inspection because its recursive response exceeded the available retrieval. The [machine-readable inventory](REPOSITORY_LIFECYCLE_2026-10-16.json) records every reviewed commit and disposition. The [duplicate ledger](DUPLICATE_FILES_2026-10-16.json) records exact file paths, commits and Git blob hashes.

The substantive source comparison covers Lean, Python, JavaScript, TypeScript and shell files, excluding Lake configuration and package initializers. It is not an exhaustive similarity search across binaries, generated pages or all programming languages. Equal Git blobs establish byte identity. One explicitly recorded normalization compares seven legacy Lean files after removing their leading `import Mathlib` line and blank line; it does not establish equivalence of the surrounding build contexts. Similar names, sparse READMEs, age and upstream fork status alone were not used as obsolescence evidence.

## Markings and current destinations

| Work | Marking | Evidence and current destination |
|---|---|---|
| [Einsteinian-156-Aristotle](https://github.com/enuminous/Einsteinian-156-Aristotle) | Superseded source-closure claim | Three reports marked: GLUING_AUDIT.md, GLOBAL_RECONSTRUCTION.md and RECONSTRUCTION.md. Shared output components do not imply the old full-vector premise. Use the closure counterexample and projected gluing contract linked below; the conditional abstract Lean theorem remains valid. |
| [Monlithic_EFMW_102_Lean4](https://github.com/enuminous/Monlithic_EFMW_102_Lean4) | Legacy parallel catalogue / partial duplicate | 105 exact source blobs shared with Monolithic-102-Zoo-Lean4, including all 102 leaf modules. Use integrated coverage for later work. The older Mathlib real-valued definitions are distinct and retained. |
| [Monolithic_Zoo_Run](https://github.com/enuminous/Monolithic_Zoo_Run) | Legacy standalone tranche / archival copy | Seven theorem-source bodies match the integrated legacy-mathlib/TURTLE-survivors copies after the declared prefix removal. The standalone package remains useful; the integrated legacy directory is excluded from its active build. |
| [Nightengale-Full-Zoo-Audit](https://github.com/enuminous/Nightengale-Full-Zoo-Audit) | Historical audit snapshot | 53 exact source blobs shared with Monolithic-Zoo-Lean4. The frozen diagnostic dataset is distinct. Old publication/build statements are historical, not the current upstream status. |
| [EFMW-FULL](https://github.com/enuminous/EFMW-FULL) | Historical EXP-001 result entry point | The stored transport limitation says a transcribed specification was executed without the frozen ZIP. Use EFMW-EXP-001/CONFIRMATORY_RECONCILIATION.md for the later frozen-run reproduction. Four substantive flat/package code groups are exact copies. |
| [medium](https://github.com/enuminous/medium) | Partial article duplication | Preferred existing location for 100 shared article files: 97 dated exports and 3 drafts. Unique articles remain in both archives. |
| [Medium2](https://github.com/enuminous/Medium2) | Partial article duplication | DUPLICATE_ARTICLES.md marks each of the 100 exact copies and links the preferred medium copy. Original article contents are preserved. |
| [Archimedes-Engine](https://github.com/enuminous/Archimedes-Engine) | Shared 2D core; distinct extension | Seven source/test blobs shared with Archimedes-3D. Observatory work remains distinct; neither project wholly supersedes the other. |
| [Archimedes-3D](https://github.com/enuminous/Archimedes-3D) | Shared 2D core; distinct extension | World 3D and its formal model remain distinct. Old MANIFEST.json publication fields describe packaging-time state. |
| [EFMW-Lagrangian](https://github.com/enuminous/EFMW-Lagrangian) | Duplicate Python layouts | catalogue.py, model.py and polynomial.py occur in both src/ and src/efmw_audit/. scripts/audit.py imports the package paths. The Lagrangian audit and continuum bridge remain distinct work. |
| [Ramtastic](https://github.com/enuminous/Ramtastic) | Intentional publication mirrors; already documented | Nine exact source groups include the audit/ and flat-download copies plus HingeRotation.lean. Existing README marks the flat bundle; preserved here without changing its frozen package checksums. |
| [P-NP](https://github.com/enuminous/P-NP) | Historical status already marked | The current README already labels LEAN_STATUS.md historical. No redundant edit was made. |

## Superseded claim and limits

The old FieldSpace source-application inference is explicitly superseded by the [closure audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/6fbd8beddf442e7adb752ec30ae054a25857602b/docs/FIELDSPACE_CLOSURE_AUDIT.md) and [projected gluing repair](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/6fbd8beddf442e7adb752ec30ae054a25857602b/docs/PROJECTED_GLUING_REPAIR.md). The repair changes the contract by restricting both field inputs and observed equation outputs. Uniqueness is in the specified component interaction class `|S ∪ {s}| ≤ k`, not unrestricted unique physical dynamics. The scalar counterexample to zero-padded full-vector gluing remains. Mixed current/stress, vacuum and conservation obligations remain open. Original reports are retained under visible supersession notices.

The current EXP-001 result is the [frozen-run reconciliation](https://github.com/enuminous/EFMW-EXP-001/blob/65134993069c2dc0c46a60fccd8bcdb2d951cdd3/CONFIRMATORY_RECONCILIATION.md). The older EFMW-FULL transport record is preserved, with its environment-sensitive timing figure. Copying results into another repository is not an independent replication.

The Nightengale audit freezes Zoo commit `94e0a9e2550a8fe62b03dc8213e3e3942c30899b` and Nightengale commit `849c39363beafc3dac70430bf1f032e7f7ce1623`. Its selected-endpoint results remain historical; this lifecycle review does not rerun them on current source. The structured-report repair in the current Zoo was separately verified by [Actions run 38831479150](https://github.com/enuminous/Monolithic-Zoo-Lean4/actions/runs/38831479150) at commit `0d616cd62cc9f061ff02b239eb2c7b3eb14a391d`. That run does not retroactively revalidate the historical diagnostic bundle.

## Work retained as distinct

- Canonical equation catalogues preserve source statements; Lean models prove propositions under explicit assumptions; Python repositories implement algorithms; audit repositories freeze selected runs. Their roles are different.
- The 46 animal implementations are not made obsolete by the Lean Zoo. Verified mathematical models, finite Python correspondence tests and incomplete end-to-end implementation equivalence remain separate claims.
- `Aristotle_EFMW_Lean`, the integrated 102 package, FieldSpace and the Lagrangian candidate contain different definitions, hypotheses and proof obligations. Shared scaffolding does not prove mathematical equivalence.
- `Medium3` has no exact article overlap with `medium` or `Medium2` in this comparison.
- `docs` contains starter-template material; `Harlequinn` has sparse purpose documentation. Neither observation supplies a supported successor relationship.
- GitHub-declared forks retain upstream lineage. They are not marked obsolete merely for being forks.

## Publication and verification

Changes are limited to status notices, review ledgers and affected current documentation checksum entries. Lean/Python/JavaScript sources, original article HTML, datasets, prediction freezes and historical package receipts remain unchanged. `Ramtastic`'s existing flat-bundle notice was recorded without editing its package. Other current manifests retain their existing unrelated entries; this review does not certify every historical manifest or deployment.

The notices and ledgers were checked against the pinned source trees, duplicate counts and copied-body comparisons. Existing text outside the marked notice blocks is preserved. New links use observed repository paths, and the per-file article links are pinned to the reviewed commits. No additional build or scientific validation is claimed by these documentation changes. Publication receipts are recorded in [LIFECYCLE_PUBLICATION_2026-10-16.json](LIFECYCLE_PUBLICATION_2026-10-16.json).

## Complete disposition index

“No obsolescence established” means this review found insufficient evidence to mark the repository; it does not certify that all its contents are current, unique or correct. Exact reviewed commits and README blob hashes are in the machine-readable inventory.

| Repository | Disposition |
|---|---|
| [accelerando-8192](https://github.com/enuminous/accelerando-8192) | upstream fork |
| [Alchemy-of-Emergence](https://github.com/enuminous/Alchemy-of-Emergence) | no obsolescence established |
| [Ant](https://github.com/enuminous/Ant) | no obsolescence established |
| [Archimedes-3D](https://github.com/enuminous/Archimedes-3D) | shared core distinct extension |
| [Archimedes-Engine](https://github.com/enuminous/Archimedes-Engine) | shared core distinct extension |
| [Archimedes-Field-Lab](https://github.com/enuminous/Archimedes-Field-Lab) | no obsolescence established |
| [Aristotle-102-Monolithic-Lean](https://github.com/enuminous/Aristotle-102-Monolithic-Lean) | no obsolescence established |
| [Aristotle-165-Einsteinian-Tensors](https://github.com/enuminous/Aristotle-165-Einsteinian-Tensors) | no obsolescence established |
| [Aristotle-Agreement-and-Surprise-Global-Equalibrium-from-Local-Repair](https://github.com/enuminous/Aristotle-Agreement-and-Surprise-Global-Equalibrium-from-Local-Repair) | no obsolescence established |
| [Aristotle-eNuminous](https://github.com/enuminous/Aristotle-eNuminous) | no obsolescence established |
| [Aristotle_EFMW_Lean](https://github.com/enuminous/Aristotle_EFMW_Lean) | no obsolescence established |
| [Avenue5](https://github.com/enuminous/Avenue5) | no obsolescence established |
| [Axolotl](https://github.com/enuminous/Axolotl) | no obsolescence established |
| [BackroomsProtocol-EFMW-Analysis](https://github.com/enuminous/BackroomsProtocol-EFMW-Analysis) | no obsolescence established |
| [Bat](https://github.com/enuminous/Bat) | no obsolescence established |
| [Beaver](https://github.com/enuminous/Beaver) | no obsolescence established |
| [Bison](https://github.com/enuminous/Bison) | no obsolescence established |
| [Bonobo](https://github.com/enuminous/Bonobo) | no obsolescence established |
| [Borges-Library-CollapseOmega](https://github.com/enuminous/Borges-Library-CollapseOmega) | no obsolescence established |
| [Butterfly](https://github.com/enuminous/Butterfly) | no obsolescence established |
| [Cadence-Zoo-Evidence](https://github.com/enuminous/Cadence-Zoo-Evidence) | no obsolescence established |
| [Cat](https://github.com/enuminous/Cat) | no obsolescence established |
| [Cat-Physics](https://github.com/enuminous/Cat-Physics) | no obsolescence established |
| [Chameleon](https://github.com/enuminous/Chameleon) | no obsolescence established |
| [Chimera](https://github.com/enuminous/Chimera) | no obsolescence established |
| [Circus](https://github.com/enuminous/Circus) | no obsolescence established |
| [Cobra](https://github.com/enuminous/Cobra) | no obsolescence established |
| [Codex-888](https://github.com/enuminous/Codex-888) | no obsolescence established |
| [Coherence-Prediction-Engine](https://github.com/enuminous/Coherence-Prediction-Engine) | no obsolescence established |
| [Crab](https://github.com/enuminous/Crab) | no obsolescence established |
| [Crocodile](https://github.com/enuminous/Crocodile) | no obsolescence established |
| [DePIN](https://github.com/enuminous/DePIN) | no obsolescence established |
| [docs](https://github.com/enuminous/docs) | starter template no obsolescence established |
| [Dolphin](https://github.com/enuminous/Dolphin) | no obsolescence established |
| [Dragon](https://github.com/enuminous/Dragon) | no obsolescence established |
| [Eagle](https://github.com/enuminous/Eagle) | no obsolescence established |
| [EFMW](https://github.com/enuminous/EFMW) | no obsolescence established |
| [EFMW-108-Minute-Tests](https://github.com/enuminous/EFMW-108-Minute-Tests) | no obsolescence established |
| [EFMW-Axioms](https://github.com/enuminous/EFMW-Axioms) | no obsolescence established |
| [EFMW-Constants-Problem](https://github.com/enuminous/EFMW-Constants-Problem) | no obsolescence established |
| [EFMW-CTX-001b](https://github.com/enuminous/EFMW-CTX-001b) | no obsolescence established |
| [efmw-equation-review](https://github.com/enuminous/efmw-equation-review) | upstream fork |
| [EFMW-EXP-001](https://github.com/enuminous/EFMW-EXP-001) | no obsolescence established |
| [EFMW-FULL](https://github.com/enuminous/EFMW-FULL) | historical result entry point |
| [EFMW-Lagrangian](https://github.com/enuminous/EFMW-Lagrangian) | internal source duplicates |
| [EFMW-Neutron-Star-Glitch-Resonance](https://github.com/enuminous/EFMW-Neutron-Star-Glitch-Resonance) | no obsolescence established |
| [efmw-research-cache](https://github.com/enuminous/efmw-research-cache) | upstream fork |
| [EFMW-Safety-001](https://github.com/enuminous/EFMW-Safety-001) | no obsolescence established |
| [EFMW-Scientific-Claims](https://github.com/enuminous/EFMW-Scientific-Claims) | no obsolescence established |
| [EFMW_Post156_Zoo_Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit) | review index and distinct audit |
| [Einsteinian-156-Aristotle](https://github.com/enuminous/Einsteinian-156-Aristotle) | superseded claims |
| [Elephant](https://github.com/enuminous/Elephant) | no obsolescence established |
| [Emergentology](https://github.com/enuminous/Emergentology) | no obsolescence established |
| [Extrauniversal-Warren-Report](https://github.com/enuminous/Extrauniversal-Warren-Report) | no obsolescence established |
| [Falcon](https://github.com/enuminous/Falcon) | no obsolescence established |
| [fieldcore](https://github.com/enuminous/fieldcore) | no obsolescence established |
| [FieldSpace](https://github.com/enuminous/FieldSpace) | no obsolescence established |
| [Fox](https://github.com/enuminous/Fox) | no obsolescence established |
| [Gecko](https://github.com/enuminous/Gecko) | no obsolescence established |
| [Harlequinn](https://github.com/enuminous/Harlequinn) | insufficient purpose evidence |
| [Hedgehog](https://github.com/enuminous/Hedgehog) | no obsolescence established |
| [Hive](https://github.com/enuminous/Hive) | no obsolescence established |
| [Horse](https://github.com/enuminous/Horse) | no obsolescence established |
| [I-Have-Guts](https://github.com/enuminous/I-Have-Guts) | no obsolescence established |
| [Jellyfish](https://github.com/enuminous/Jellyfish) | no obsolescence established |
| [JEV-EFMW-Syncretic-Layer](https://github.com/enuminous/JEV-EFMW-Syncretic-Layer) | no obsolescence established |
| [lean-worker](https://github.com/enuminous/lean-worker) | upstream fork |
| [Ligo_EFMW_Search](https://github.com/enuminous/Ligo_EFMW_Search) | no obsolescence established |
| [Lynx](https://github.com/enuminous/Lynx) | no obsolescence established |
| [Magpie](https://github.com/enuminous/Magpie) | no obsolescence established |
| [Mantis](https://github.com/enuminous/Mantis) | no obsolescence established |
| [Mathematics-and-Elite-Squad-Dynamics](https://github.com/enuminous/Mathematics-and-Elite-Squad-Dynamics) | no obsolescence established |
| [medium](https://github.com/enuminous/medium) | partial article duplicate |
| [Medium2](https://github.com/enuminous/Medium2) | partial article duplicate |
| [Medium3](https://github.com/enuminous/Medium3) | distinct archive |
| [meta-meme](https://github.com/enuminous/meta-meme) | upstream fork |
| [Mole](https://github.com/enuminous/Mole) | no obsolescence established |
| [Monlithic_EFMW_102_Lean4](https://github.com/enuminous/Monlithic_EFMW_102_Lean4) | legacy partial duplicate |
| [Monolithic-102-Zoo-Lean4](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) | no obsolescence established |
| [Monolithic-Zoo-Lean4](https://github.com/enuminous/Monolithic-Zoo-Lean4) | no obsolescence established |
| [Monolithic_102_EFMW](https://github.com/enuminous/Monolithic_102_EFMW) | no obsolescence established |
| [Monolithic_Zoo_Run](https://github.com/enuminous/Monolithic_Zoo_Run) | legacy parallel tranche |
| [monster](https://github.com/enuminous/monster) | upstream fork |
| [Moth](https://github.com/enuminous/Moth) | no obsolescence established |
| [MultiValuedClassicalAction-Lean4](https://github.com/enuminous/MultiValuedClassicalAction-Lean4) | no obsolescence established |
| [Multiverse-Simulator](https://github.com/enuminous/Multiverse-Simulator) | no obsolescence established |
| [Nightengale](https://github.com/enuminous/Nightengale) | no obsolescence established |
| [Nightengale-Full-Zoo-Audit](https://github.com/enuminous/Nightengale-Full-Zoo-Audit) | historical audit bundle |
| [Octopus](https://github.com/enuminous/Octopus) | no obsolescence established |
| [OpenAI-math](https://github.com/enuminous/OpenAI-math) | upstream fork |
| [oph-lab](https://github.com/enuminous/oph-lab) | upstream fork |
| [Orca](https://github.com/enuminous/Orca) | no obsolescence established |
| [Oroboros](https://github.com/enuminous/Oroboros) | no obsolescence established |
| [Owl](https://github.com/enuminous/Owl) | no obsolescence established |
| [P-NP](https://github.com/enuminous/P-NP) | historical status already marked |
| [papers](https://github.com/enuminous/papers) | no obsolescence established |
| [Penguin](https://github.com/enuminous/Penguin) | no obsolescence established |
| [Phoenix](https://github.com/enuminous/Phoenix) | no obsolescence established |
| [Pulse](https://github.com/enuminous/Pulse) | no obsolescence established |
| [Ramtastic](https://github.com/enuminous/Ramtastic) | intentional publication mirrors |
| [Raven](https://github.com/enuminous/Raven) | no obsolescence established |
| [Research-Program](https://github.com/enuminous/Research-Program) | no obsolescence established |
| [Rhino](https://github.com/enuminous/Rhino) | no obsolescence established |
| [Salmon](https://github.com/enuminous/Salmon) | no obsolescence established |
| [Shark](https://github.com/enuminous/Shark) | no obsolescence established |
| [Shepherd](https://github.com/enuminous/Shepherd) | no obsolescence established |
| [simself](https://github.com/enuminous/simself) | no obsolescence established |
| [Spider](https://github.com/enuminous/Spider) | no obsolescence established |
| [Termite](https://github.com/enuminous/Termite) | no obsolescence established |
| [Tortoise](https://github.com/enuminous/Tortoise) | no obsolescence established |
| [Turtle](https://github.com/enuminous/Turtle) | no obsolescence established |
| [Universal-Cognitive-Attractor](https://github.com/enuminous/Universal-Cognitive-Attractor) | no obsolescence established |
| [Verbinski-Protocol](https://github.com/enuminous/Verbinski-Protocol) | no obsolescence established |
| [Weasel](https://github.com/enuminous/Weasel) | no obsolescence established |
| [Whale](https://github.com/enuminous/Whale) | no obsolescence established |
| [Wolf](https://github.com/enuminous/Wolf) | no obsolescence established |
| [woodpecker](https://github.com/enuminous/woodpecker) | no obsolescence established |
| [Wrights-Law](https://github.com/enuminous/Wrights-Law) | no obsolescence established |
| [Zoo-Monster](https://github.com/enuminous/Zoo-Monster) | no obsolescence established |
