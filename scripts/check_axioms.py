#!/usr/bin/env python3
"""Reject incomplete proof logs and nonstandard theorem dependencies."""
import re
import sys
from pathlib import Path
text = Path(sys.argv[1]).read_text()
audit = Path(__file__).resolve().parents[1] / 'lean/ProofAudit.lean'
expected = re.findall(r'^#print axioms (\S+)$', audit.read_text(), re.M)
reports = re.findall(
    r"'([^']+)'\s+(?:depends on axioms:\s*\[([^\]]*)\]|does not depend on any axioms)", text)
names = [name for name, _ in reports]
if len(names) != len(set(names)) or set(names) != set(expected):
    raise SystemExit(f'Incomplete or duplicate dependency reports. '
                     f'Missing: {sorted(set(expected) - set(names))}; '
                     f'unexpected: {sorted(set(names) - set(expected))}')
allowed = {'propext', 'Classical.choice', 'Quot.sound'}
for _, report in reports:
    dependencies = {x.strip() for x in report.split(',') if x.strip()}
    if dependencies - allowed:
        raise SystemExit('Unexpected proof dependencies: ' + str(dependencies - allowed))
print(f'PASS: {len(reports)} named reports, standard foundational axioms only')
