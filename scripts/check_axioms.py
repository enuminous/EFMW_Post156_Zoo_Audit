#!/usr/bin/env python3
"""Reject incomplete proof logs and nonstandard theorem dependencies."""
import re
import sys
from pathlib import Path
text = Path(sys.argv[1]).read_text()
reports = re.findall(r"depends on axioms: \[([^\]]*)\]", text)
empty = len(re.findall(r'does not depend on any axioms', text))
if len(reports) + empty != 18:
    raise SystemExit(f'Expected 18 complete dependency reports, got {len(reports) + empty}')
allowed = {'propext', 'Classical.choice', 'Quot.sound'}
for report in reports:
    dependencies = {x.strip() for x in report.split(',') if x.strip()}
    if dependencies - allowed:
        raise SystemExit('Unexpected proof dependencies: ' + str(dependencies - allowed))
print('PASS: 18 reports, standard foundational axioms only')
