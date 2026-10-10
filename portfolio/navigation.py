#!/usr/bin/env python3
"""Check or refresh the shared navigation in an existing local repository checkout."""
import argparse, hashlib, html, json, pathlib, re, subprocess, urllib.parse

HERE=pathlib.Path(__file__).resolve().parent
START='<!-- ENUMINOUS-NAV:START -->';END='<!-- ENUMINOUS-NAV:END -->'
MSTART='<!-- ENUMINOUS-NETWORK:START -->';MEND='<!-- ENUMINOUS-NETWORK:END -->'

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('checkout',type=pathlib.Path)
    p.add_argument('--repository',help='Repository name; defaults to checkout directory name')
    p.add_argument('--write',action='store_true',help='Apply changes; default only checks')
    args=p.parse_args();root=args.checkout.resolve();name=args.repository or root.name
    if not re.fullmatch(r'[A-Za-z0-9_.-]+',name):p.error('Invalid repository name')
    config=json.loads((HERE/'navigation.json').read_text())
    registry=json.loads((HERE/'repositories.json').read_text())['repositories']
    record=next((r for r in registry if r['name']==name),None)
    paths=subprocess.check_output(['git','-C',str(root),'ls-files','-z'],text=True).split('\0');paths=[x for x in paths if x]
    rp=next((x for x in paths if re.fullmatch(r'readme.md',x,re.I)),'README.md')
    indexes=sorted(x for x in paths if x.lower().endswith('index.html'))
    src='https://github.com/enuminous/'+name;branch=(record or {}).get('branch','main')
    published=(record or {}).get('pages_url')
    md=MSTART+'\n**eNuminous network:** [All repositories]('+config['directory']+') · '+' · '.join('['+label+']('+url+')' for label,url in config['major_links'])+'\n\n[Repository]('+src+')'
    md+=(' · [Published page]('+published+')' if published else ' · This repository is linked through its source; GitHub Pages is not enabled.')+'\n'
    if indexes:
        md+='\n<details>\n<summary>Repository indexes ('+str(len(indexes))+')</summary>\n\n'
        for path in indexes:
            md+='- ['+path+']('+src+'/blob/'+urllib.parse.quote(branch,safe='')+'/'+urllib.parse.quote(path)+')'+(' · [Open page]('+published+urllib.parse.quote(path)+')' if published else '')+'\n'
        md+='\n</details>\n'
    md+=MEND
    nav=(HERE/'navigation-template.html').read_text().rstrip().replace('__REPOSITORY__',html.escape(name,quote=True))
    changed={}
    c=(root/rp).read_text() if (root/rp).exists() else '# '+name+'\n'
    if MSTART in c:new=re.sub(re.escape(MSTART)+r'.*?'+re.escape(MEND),lambda _:md,c,flags=re.S)
    else:
        # Keep YAML frontmatter and the first heading before the menu.
        offset=0
        if c.startswith('---\n'):
            m=re.search(r'\n---\s*\n',c[4:]);offset=m.end()+4 if m else 0
        m=re.match(r'(\s*# [^\n]+\n)',c[offset:]);offset+=m.end() if m else 0
        new=c[:offset].rstrip()+'\n\n'+md+'\n\n'+c[offset:].lstrip()
    if new!=c:changed[rp]=new
    for path in indexes+(['research_engine/dashboard.html'] if (root/'research_engine/dashboard.html').exists() else [])+(['repositories.html'] if name=='EFMW' and (root/'repositories.html').exists() else []):
        f=root/path
        if f.is_symlink():continue
        c=f.read_text()
        if START in c:new=re.sub(re.escape(START)+r'.*?'+re.escape(END),lambda _:nav,c,flags=re.S)
        else:
            m=re.search(r'<body\b[^>]*>',c,re.I)
            if not m:raise SystemExit('No HTML body: '+path)
            new=c[:m.end()]+'\n'+nav+'\n'+c[m.end():]
        if new!=c:changed[path]=new
    # Refresh only affected entries in current manifests; never rewrite historical freeze receipts.
    for path in paths:
        if '/' in path or not re.search(r'manifest|sha256',path,re.I) or 'freeze' in path.casefold():continue
        f=root/path
        if not f.is_file() or f.suffix=='.html':continue
        try:c=f.read_text()
        except UnicodeError:continue
        def replace(m):
            fp=m[3].removeprefix('./')
            if fp==path:return ''
            return hashlib.sha256(changed[fp].encode()).hexdigest()+m[2]+m[3] if fp in changed else m.group()
        new=re.sub(r'^([a-f0-9]{64})(\s+\*?)([^\r\n]+)$',replace,c,flags=re.M)
        if path=='MANIFEST.md' and 'README.md' in changed:
            new=re.sub(r'(`README\.md` — `)[a-f0-9]{64}(`)',lambda m:m[1]+hashlib.sha256(changed['README.md'].encode()).hexdigest()+m[2],new)
        if new!=c:changed[path]=new
    print(json.dumps({'repository':name,'mode':'write' if args.write else 'check','changed_files':list(changed)},indent=2))
    if args.write:
        for path,c in changed.items():(root/path).write_text(c)
    elif changed:raise SystemExit(1)

if __name__=='__main__':main()
