"""Mutation checks for the source-to-overlap translation boundary."""
import unittest
from audit_fieldspace import SOURCE, parse, audit, run

class SourceAuditTests(unittest.TestCase):
    def test_frozen_source(self):
        result, failures = run(None)
        self.assertEqual(result['charts'], 165)
        self.assertEqual(sum(result['inventory'].values()), 585)
        self.assertEqual(result['overlap_categories'],
                         dict(current=612, explicit=1008, stress=288, stress_and_current=72))
        self.assertEqual(result['compared_scalar_gauge_components'], 3600)
        self.assertEqual(failures, [])

    def test_changed_pair_coefficient_is_detected(self):
        # Deliberately corrupt one pair term into a different coupling symbol.
        source = SOURCE.read_text().replace('λ_FW φ_W', 'λ_FT φ_W', 1)
        with self.assertRaisesRegex(ValueError, 'support mismatch'):
            parse(source)

    def test_deleted_triplet_is_rejected(self):
        source = SOURCE.read_text()
        source = source[:source.rfind('=== Triplet')]
        with self.assertRaisesRegex(ValueError, 'incomplete'):
            parse(source)

    def test_shared_component_mismatch_is_detected(self):
        charts, _ = parse(SOURCE.read_text())
        chart = frozenset('FWT')
        base, terms = charts[chart]['F']
        charts[chart]['F'] = (base, [('2*' + term if term == 'λ_FW φ_W' else term, support)
                                    for term, support in terms])
        rows, _ = audit(charts)
        self.assertTrue(any(row['explicit_shared_components'].startswith('mismatch') for row in rows))

    def test_wrong_current_support_is_rejected(self):
        source = SOURCE.read_text().replace('κ_MEF Ξ^ν', 'κ_MWF Ξ^ν', 1)
        with self.assertRaisesRegex(ValueError, 'index mismatch'):
            parse(source)

if __name__ == '__main__':
    unittest.main()
