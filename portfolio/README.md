# Repository navigation maintenance

The [interlocking audit](INTERLOCK_AUDIT.md) records the source snapshot, findings and limits. The [public directory](https://enuminous.github.io/EFMW/repositories.html) connects every public repository.

`repositories.json` is the public snapshot. `navigation.json` sets the major destinations. `navigation-template.html` is the exact shared bar, with `__REPOSITORY_URL__` and `__README_URL__` as per-repository slots. Menus are embedded locally so they work without a shared JavaScript service. The all-Pages list and registry are snapshot data, not an automatic discovery service.

To check or refresh a local checkout:

```bash
python portfolio/navigation.py /path/to/checkout --repository EFMW
python portfolio/navigation.py /path/to/checkout --repository EFMW --write
```

The first command only checks. The second updates the marked root README block, tracked index files, the audit dashboard template, and affected entries in current checksum inventories. It preserves other content and historical freeze manifests. It does not commit, push, enable Pages, or change access settings. Review the diff before publishing.

When adding a repository, update the public registry and the canonical template together, then refresh the affected checkouts. Do not put private repository names or URLs in this directory. For a new Pages deployment, verify its actual URL before adding it to the menu; otherwise link its GitHub source.

Markers are `ENUMINOUS-NETWORK` in Markdown and `ENUMINOUS-NAV` in HTML. The bar uses scoped styles, ordinary links and native details controls. Existing local navigation stays intact. The menu is not a claim registry or a scientific validation badge.

Frozen evidence receipts remain historical. `EFMW-108-Minute-Tests/FREEZE_MANIFEST.sha256` still describes its original README, linked from that repository's navigation note. All experimental data and prediction freezes remain unchanged.

## October 13, 2026 refresh

The [refresh report](NAVIGATION_REFRESH_2026-10-13.md) records nine additions and verified publication links. `recent_repositories` in `navigation.json` drives the compact recent-project links in every root README. The HTML template contains the matching Recent menu and the verified All Pages menu. `page_urls` in each registry record maps source indexes to URLs that were actually checked; do not infer published paths from repository paths. The `source_commit` values identify the pre-refresh inventory. Historical audit and freeze receipts remain unchanged.
