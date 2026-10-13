#!/usr/bin/env python3
"""Check or refresh the shared navigation in an existing local repository checkout."""
import argparse
import hashlib
import html
import json
import pathlib
import re
import subprocess
import urllib.parse

HERE = pathlib.Path(__file__).resolve().parent
START = '<!-- ENUMINOUS-NAV:START -->'
END = '<!-- ENUMINOUS-NAV:END -->'
MSTART = '<!-- ENUMINOUS-NETWORK:START -->'
MEND = '<!-- ENUMINOUS-NETWORK:END -->'


def url_path(path):
    return urllib.parse.quote(path, safe='/')


def replace_marked(content, start, end, replacement):
    if content.count(start) != 1 or content.count(end) != 1:
        raise ValueError('Missing or duplicate navigation markers')
    return re.sub(re.escape(start) + r'.*?' + re.escape(end),
                  lambda _: replacement, content, count=1, flags=re.S)


def render_changes(root, name, paths, config, registry, template):
    records = {r['name']: r for r in registry['repositories']}
    record = records[name]
    src = record['repository_url']
    branch = urllib.parse.quote(record['branch'], safe='')
    rp = record['readme_path']
    published = record.get('pages_url')
    indexes = record['indexes']
    page_urls = record.get('page_urls', {})
    md = MSTART + '\n**eNuminous network:** [All repositories](' + config['directory'] + ') · '
    md += ' · '.join('[' + label + '](' + url + ')' for label, url in config['major_links'])
    md += '\n\n[Repository](' + src + ')'
    if published:
        md += ' · [Published page](' + published + ')'
    elif record.get('pages_enabled'):
        md += ' · GitHub Pages is configured; its live URL was not verified in this snapshot.'
    else:
        md += ' · This repository is linked through its source; GitHub Pages is not enabled.'
    md += '\n'
    recent = [records[n] for n in config.get('recent_repositories', []) if n in records]
    if recent:
        md += '\n<details>\n<summary>Recent repositories (' + str(len(recent)) + ')</summary>\n\n'
        for r in recent:
            md += '- [' + r['name'] + '](' + r['repository_url'] + ') · [README](' + r['readme_url'] + ')'
            if r.get('pages_url'):
                md += ' · [Page](' + r['pages_url'] + ')'
            elif r.get('indexes'):
                md += ' · [Page source](' + r['repository_url'] + '/blob/' + urllib.parse.quote(r['branch'], safe='') + '/' + url_path(r['indexes'][0]) + ')'
            md += '\n'
        md += '\n</details>\n'
    if indexes:
        md += '\n<details>\n<summary>Repository indexes (' + str(len(indexes)) + ')</summary>\n\n'
        for path in indexes:
            md += '- [' + path + '](' + src + '/blob/' + branch + '/' + url_path(path) + ')'
            if path in page_urls:
                md += ' · [Open page](' + page_urls[path] + ')'
            md += '\n'
        md += '\n</details>\n'
    md += MEND
    slots = {'__REPOSITORY__': name, '__REPOSITORY_URL__': src,
             '__README_URL__': record['readme_url']}
    nav = template.rstrip()
    for slot, value in slots.items():
        nav = nav.replace(slot, html.escape(value, quote=True))
    if re.search(r'__[A-Z_]+__', nav):
        raise ValueError('Unresolved navigation template slot')
    changed = {}
    c = (root / rp).read_text()
    if MSTART in c or MEND in c:
        new = replace_marked(c, MSTART, MEND, md)
    else:
        offset = 0
        if c.startswith('---\n'):
            m = re.search(r'\n---\s*\n', c[4:])
            if not m:
                raise ValueError('Unclosed README frontmatter')
            offset = m.end() + 4
        m = re.match(r'(\s*# [^\n]+\n)', c[offset:])
        offset += m.end() if m else 0
        new = c[:offset].rstrip() + '\n\n' + md + '\n\n' + c[offset:].lstrip()
    if new != c:
        changed[rp] = new
    extra = ['research_engine/dashboard.html'] if 'research_engine/dashboard.html' in paths else []
    if name == 'EFMW' and 'repositories.html' in paths:
        extra.append('repositories.html')
    for path in indexes + extra:
        f = root / path
        if f.is_symlink():
            continue
        c = f.read_text()
        if START in c or END in c:
            new = replace_marked(c, START, END, nav)
        else:
            m = re.search(r'<body\b[^>]*>', c, re.I)
            if m:
                offset = m.end()
            else:
                # HTML permits omitted body tags; these pages start with main or h1.
                m = re.search(r'<(?:main|h1)\b', c, re.I)
                if not m:
                    raise ValueError('No HTML body insertion point: ' + path)
                offset = m.start()
            new = c[:offset] + '\n' + nav + '\n' + c[offset:]
        if new != c:
            changed[path] = new
    # Preserve historical freeze receipts; update only current checksum inventories.
    for path in paths:
        if '/' in path or not re.search(r'manifest|sha256', path, re.I) or 'freeze' in path.casefold():
            continue
        f = root / path
        if not f.is_file() or f.suffix == '.html':
            continue
        try:
            c = f.read_text()
        except UnicodeError:
            continue
        def update_hash(m):
            fp = m[3].removeprefix('./')
            if fp == path:
                return m.group()
            if fp in changed:
                return hashlib.sha256(changed[fp].encode()).hexdigest() + m[2] + m[3]
            return m.group()
        new = re.sub(r'^([a-f0-9]{64})(\s+\*?)([^\r\n]+)$', update_hash, c, flags=re.M)
        if path == 'MANIFEST.md' and rp in changed:
            new = re.sub(r'(`' + re.escape(rp) + r'` — `)[a-f0-9]{64}(`)',
                         lambda m: m[1] + hashlib.sha256(changed[rp].encode()).hexdigest() + m[2], new)
        if new != c:
            changed[path] = new
    return changed


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('checkout', type=pathlib.Path)
    p.add_argument('--repository', help='Repository name; defaults to checkout directory name')
    p.add_argument('--write', action='store_true', help='Apply changes; default only checks')
    args = p.parse_args()
    root = args.checkout.resolve()
    name = args.repository or root.name
    if not re.fullmatch(r'[A-Za-z0-9_.-]+', name):
        p.error('Invalid repository name')
    config = json.loads((HERE / 'navigation.json').read_text())
    registry = json.loads((HERE / 'repositories.json').read_text())
    paths = subprocess.check_output(['git', '-C', str(root), 'ls-files', '-z'], text=True).split('\0')
    template = (HERE / 'navigation-template.html').read_text()
    changed = render_changes(root, name, [x for x in paths if x], config, registry, template)
    print(json.dumps({'repository': name, 'mode': 'write' if args.write else 'check',
                      'changed_files': list(changed)}, indent=2))
    if args.write:
        for path, c in changed.items():
            (root / path).write_text(c)
    elif changed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
