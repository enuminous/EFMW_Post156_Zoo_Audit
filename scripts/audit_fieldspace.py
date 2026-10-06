#!/usr/bin/env python3
"""Exact-source, componentwise overlap audit. No PDE/physics certification.

The parser rejects unrecognized scalar/gauge syntax. It compares shared equation
components only; it deliberately does not substitute this test for full-vector
GluingCompatible. Unknown mixed terms are recorded before a completion is used.
"""
import argparse
import ast
import csv
import hashlib
import itertools
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'sources/fieldspace/EFMW_165_field_equations.txt'
EXPECTED_BLOB = 'ac6313fe4a2b02a28ac8fb34519c5f96f6ea2bd8'
UPSTREAM = '7e60205d2370c335ebe2cafe89d6e0bbe842ba01'
SECTORS = frozenset('EMSFW TIRHPA'.replace(' ', ''))
SCALARS = SECTORS - set('EMS')

def parse(text):
    pieces = re.split(r'^=== Triplet (\([^\n]+\)) ===\n', text, flags=re.M)
    charts = {}
    inventory = Counter()
    for heading, body in zip(pieces[1::2], pieces[2::2]):
        chart = frozenset(ast.literal_eval(heading))
        if len(chart) != 3 or not chart <= SECTORS or chart in charts:
            raise ValueError('Invalid or duplicate chart: ' + heading)
        equations = {}
        for line in body.splitlines():
            if line.startswith('Scalar '):
                sector, rhs = line[len('Scalar '):].split(': ', 1)
                base = f'□_g φ_{sector} + m_{sector}^2 φ_{sector} + ξ_{sector} R φ_{sector}'
                if not rhs.startswith(base + ' + ') or not rhs.endswith(' = 0'):
                    raise ValueError('Unrecognized scalar equation: ' + line)
                terms = rhs[len(base) + 3:-4].split(' + ')
                parsed = []
                for term in terms:
                    match = re.fullmatch(r'λ_([A-Z]{2,3}) (.+)', term)
                    if not match or match[1][0] != sector:
                        raise ValueError('Unrecognized scalar term: ' + term)
                    factors = match[2]
                    support = set(re.findall(r'φ_([A-Z])', factors))
                    for token, field in [('ℜ', 'E'), ('F_{αβ}F^{αβ}', 'M'), ('S_{αβ}S^{αβ}', 'S')]:
                        if token in factors:
                            support.add(field)
                            factors = factors.replace(token, '')
                    factors = re.sub(r'φ_[A-Z]', '', factors).strip()
                    if factors or support != set(match[1][1:]) or not support <= chart - {sector}:
                        raise ValueError('Coefficient/factor support mismatch: ' + term)
                    parsed.append((term, frozenset(support)))
                if len(parsed) != 3:
                    raise ValueError('Expected two pair terms and one triple term')
                equations[sector] = (base, parsed)
                inventory['scalar'] += 1
            elif line.startswith('  ∇_μ '):
                lhs, rhs = line.strip().split(' = ', 1)
                sector = {'F': 'M', 'S': 'S'}[lhs[4]]
                parsed = []
                for term in rhs.split(' + '):
                    match = re.fullmatch(r'κ_([A-Z]{2,3}) (.+)', term)
                    if not match or match[1][0] != sector:
                        raise ValueError('Unrecognized gauge term: ' + term)
                    if match[2] == 'Ξ^ν':
                        if set(match[1]) != chart:
                            raise ValueError('Mixed-current index mismatch')
                        support = chart  # proposed completion, not source-derived
                    else:
                        other = match[1][1:]
                        if len(other) != 1 or match[2] not in (
                            f'φ_{other} ∇^ν φ_{other}', 'J_{' + other + '}^ν'):
                            raise ValueError('Unrecognized current: ' + term)
                        support = frozenset(other)
                    parsed.append((term, support))
                if len(parsed) != 3:
                    raise ValueError('Expected two pair currents and one mixed current')
                equations[sector] = (lhs, parsed)
                inventory['gauge_dynamics'] += 1
            elif line.startswith('GR (Einstein):'):
                equations['E'] = (line, [])
                inventory['einstein'] += 1
            elif line.startswith('  ∇_['):
                inventory['bianchi'] += 1
            elif line.strip() and line.strip() not in ('M-gauge:', 'S-gauge:'):
                raise ValueError('Unrecognized statement: ' + line)
        if set(equations) != chart:
            raise ValueError('Missing equation in ' + heading)
        charts[chart] = equations
    expected = {frozenset(x) for x in itertools.combinations(sorted(SECTORS), 3)}
    if set(charts) != expected:
        raise ValueError('Atlas is incomplete')
    return charts, dict(inventory)

def restrict_component(equation, shared):
    base, terms = equation
    return base, tuple(sorted(term for term, support in terms if support <= shared))

def audit(charts, shared_sizes=(2,)):
    rows = []
    comparisons = 0
    for a, b in itertools.combinations(sorted(charts, key=lambda x: ''.join(sorted(x))), 2):
        shared = a & b
        if len(shared) not in shared_sizes:
            continue
        stress = 'E' in shared
        current = bool(shared & set('MS'))
        failures = []
        for sector in sorted(shared - {'E'}):
            comparisons += 1
            if restrict_component(charts[a][sector], shared) != restrict_component(charts[b][sector], shared):
                failures.append(sector)
        category = ('stress_and_current' if stress and current else
                    'stress' if stress else 'current' if current else 'explicit')
        rows.append(dict(chart_a=''.join(sorted(a)), chart_b=''.join(sorted(b)),
                         shared=''.join(sorted(shared)), category=category,
                         explicit_shared_components='mismatch:' + ','.join(failures) if failures else 'match',
                         mixed_terms='not_defined_in_source' if stress or current else 'not_applicable'))
    return rows, comparisons

def run(output, check_hash=True, text=None):
    data = SOURCE.read_bytes() if text is None else text.encode()
    blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    if check_hash and blob != EXPECTED_BLOB:
        raise ValueError('Frozen source blob mismatch')
    charts, inventory = parse(data.decode())
    rows, comparisons = audit(charts)
    projected_rows, projected_comparisons = audit(charts, shared_sizes=(1, 2))
    spectrum = Counter(len(a & b) for a, b in itertools.combinations(charts, 2))
    counts = dict(sorted(Counter(row['category'] for row in rows).items()))
    mismatches = [row for row in rows if row['explicit_shared_components'] != 'match']
    projected_mismatches = [row for row in projected_rows
                           if row['explicit_shared_components'] != 'match']
    result = dict(source_commit=UPSTREAM, source_git_blob=blob,
                  source_sha256=hashlib.sha256(data).hexdigest(),
                  charts=len(charts), inventory=inventory, shared_pair_overlaps=len(rows),
                  overlap_categories=counts, compared_scalar_gauge_components=comparisons,
                  explicit_mismatches=len(mismatches),
                  mixed_support_closure='candidate_completion_only',
                  global_unique_reconstruction='not_established_for_source',
                  projected_gluing_theorem='proved_conditionally_in_ProjectedGluing.lean',
                  projected_overlap_audit=dict(
                      nonempty_distinct_overlaps=len(projected_rows),
                      overlap_sizes=dict(sorted(Counter(str(len(row['shared']))
                                                       for row in projected_rows).items())),
                      empty_overlaps_vacuous=spectrum[0],
                      compared_scalar_gauge_components=projected_comparisons,
                      explicit_mismatches=len(projected_mismatches),
                      categories=dict(sorted(Counter(row['category']
                                                     for row in projected_rows).items())),
                      scope='Explicit shared components; mixed support and tensor/vacuum obligations remain conditional.'),
                  additional_obligations=[
                      'Instantiate the proved projected gluing theorem with physical equation maps and establish IsComponentKBody for any proposed global model.',
                      'Specify scalar vacuum stress V(0) or a consistent subtraction rule.',
                      'Keep a common background metric/derivative convention across charts.',
                      'Specify pure-sector supports of J_E, J_M, J_S and gauge/curvature invariants.',
                      'Resolve conservation constraints independently of support closure.'
                  ])
    if output:
        output.mkdir(parents=True, exist_ok=True)
        (output / 'summary.json').write_text(json.dumps(result, indent=2) + '\n')
        with (output / 'overlaps.csv').open('w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator='\n')
            writer.writeheader()
            writer.writerows(rows)
        with (output / 'projected_overlaps.csv').open('w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=list(projected_rows[0]), lineterminator='\n')
            writer.writeheader()
            writer.writerows(projected_rows)
    return result, projected_mismatches

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=ROOT / 'results/fieldspace')
    args = parser.parse_args()
    result, mismatches = run(args.output)
    print(json.dumps(result, indent=2))
    raise SystemExit(bool(mismatches))
