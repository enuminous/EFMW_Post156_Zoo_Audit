import copy
import hashlib
import itertools
import json
import math
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from unittest.mock import patch

from research_engine.catalog import Catalog, DATA, ROOT, read
from research_engine.dashboard import render
from research_engine.engine import Engine, Ledger, canonical, parse_json, verify_lines
from research_engine.examples.cases import cases, fixture_bindings
from research_engine.examples.demo import plan, proposal
from research_engine.kernels import KERNELS, evaluate
from scripts.audit_fieldspace import parse as parse_fieldspace


def metric(output, path):
    for key in path.split("."):
        output = output[int(key)] if isinstance(output, list) else output[key]
    return output


class CatalogTests(unittest.TestCase):
    def test_frozen_sources_and_full_cartesian_count(self):
        catalog = Catalog()
        self.assertEqual(len(catalog.verify()), 9)
        self.assertEqual(sum(1 for _ in catalog.slots()), 774180)
        self.assertEqual(sum(1 for _ in catalog.slots(equation="ME-002")), 7590)
        self.assertEqual(sum(1 for _ in catalog.slots(triplet="FS-EFM", animal="BAT")), 102)
        self.assertEqual(set(KERNELS), set(catalog.zoo))
        self.assertEqual(len(catalog.ranked), 17)
        with self.assertRaises(ValueError):
            next(catalog.slots(equation="ME-103"))

    def test_exact_fieldspace_extraction(self):
        text = (ROOT / "sources/fieldspace/EFMW_165_field_equations.txt").read_text()
        parsed, counts = parse_fieldspace(text)
        self.assertEqual(sum(counts.values()), 585)
        for triplet in Catalog().triplets:
            self.assertIn(frozenset(triplet["sectors"]), parsed)
            self.assertIn("=== Triplet " + triplet["source_heading"] + " ===\n" + "\n".join(triplet["statements"]), text)

    def test_prior_status_not_imported_as_mapping_or_evidence(self):
        with tempfile.TemporaryDirectory() as d:
            report = Engine(Path(d) / "ledger").report()
            self.assertEqual(report["applicability"]["unknown"], 774180)
            self.assertEqual(report["runs"], 0)
            self.assertEqual(report["new_formal_proofs"], 0)


class KernelTests(unittest.TestCase):
    def setUp(self):
        self.inputs = cases()

    def test_all_90_upstream_numeric_fixtures(self):
        fixtures = read("zoo-reference-fixtures.json")
        bindings = fixture_bindings()
        self.assertEqual(len(fixtures), 90)
        self.assertEqual({f["label"] for f in fixtures}, set(bindings))
        for f in fixtures:
            with self.subTest(fixture=f["label"]):
                animal, path = bindings[f["label"]]
                actual = metric(evaluate(animal, self.inputs[animal]), path)
                self.assertTrue(math.isclose(actual, f["expected"], rel_tol=1e-12, abs_tol=1e-12), (actual, f))

    def test_all_46_adapters_execute_finite_outputs(self):
        self.assertEqual(set(self.inputs), set(KERNELS))
        for name in KERNELS:
            with self.subTest(animal=name):
                canonical(evaluate(name, self.inputs[name]))

    def test_branch_order_sign_and_domain_controls(self):
        checks = [
            ("TORTOISE", "gain", .02), ("CAT", "penalty", .1),
            ("BAT", "label", "placeboFailure"), ("HEDGEHOG", "label", "generalizes"),
            ("CROCODILE", "difference_in_differences", 2), ("TURTLE", "label", "insufficient"),
            ("ELEPHANT", "termination", "origin"), ("BEAVER", "accepted", False),
            ("MANTIS", "label", "calibrating"), ("SALMON", "trace.parents.0.kind", "exhausted"),
            ("MOLE", "hidden_failure", True), ("PHOENIX", "stable", True),
            ("FALCON", "latency.missed", True), ("BONOBO", "exploitation", .1),
        ]
        for name, field, expected in checks:
            with self.subTest(animal=name):
                actual = metric(evaluate(name, self.inputs[name]), field)
                if type(expected) is float:
                    self.assertAlmostEqual(actual, expected)
                else:
                    self.assertEqual(actual, expected)
        self.assertEqual(len(evaluate("WEASEL", self.inputs["WEASEL"])["retained"]), 1)
        self.assertEqual(evaluate("CAT", {"full": 2, "ablated": 1})["label"], "removalHelped")
        self.assertEqual(evaluate("RHINO", {"baseline": 0, "after": 0})["retention"], 1)
        self.assertEqual(evaluate("RHINO", {"baseline": 0, "after": 1})["retention"], 0)
        self.assertEqual(evaluate("FALCON", dict(self.inputs["FALCON"], alarm_time=None)), {"latency": None})

    def test_rank_ties_empty_and_retrospective_only(self):
        for animal in Catalog().ranked:
            inp = self.inputs[animal]
            with self.subTest(animal=animal):
                self.assertEqual(evaluate(animal, inp)["scores"], [.25, .625, .625, 1])
                empty = dict(inp, columns=[[] for _ in inp["columns"]], rows=0)
                self.assertEqual(evaluate(animal, empty)["scores"], [])
                for invalid in (dict(inp, mode="prospective"), dict(inp, rows=5), dict(inp, columns=[])):
                    with self.assertRaises(ValueError):
                        evaluate(animal, invalid)

    def test_no_bool_strings_nonfinite_or_unknown_fields_in_numbers(self):
        for invalid in (True, "0.2", float("nan"), float("inf"), -.1, 1.01):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                evaluate("TORTOISE", {"candidate_brier": invalid, "control_brier": .2})
        with self.assertRaises(ValueError):
            evaluate("TORTOISE", dict(self.inputs["TORTOISE"], unnoticed_parameter=1))
        with self.assertRaises(ValueError):
            evaluate("HEDGEHOG", dict(self.inputs["HEDGEHOG"], heldout=["development-a"]))

    def test_independence_deduplication_and_veto(self):
        inp = self.inputs["TURTLE"]
        self.assertEqual(evaluate("TURTLE", inp)["groups"], 1)
        groups = [dict(inp["evidence_groups"][0], id=str(i)) for i in range(3)]
        self.assertEqual(evaluate("TURTLE", dict(inp, evidence_groups=groups))["label"], "supported")
        groups.append({"id": "veto", "applicable": True, "veto_on_failure": True, "polarity": "negative"})
        self.assertEqual(evaluate("TURTLE", dict(inp, evidence_groups=groups))["label"], "notSupported")
        groups = [dict(g, applicable=False) for g in groups]
        self.assertEqual(evaluate("TURTLE", dict(inp, evidence_groups=groups))["label"], "insufficient")
        conflict = inp["evidence_groups"] + [dict(inp["evidence_groups"][0], polarity="negative")]
        with self.assertRaises(ValueError):
            evaluate("TURTLE", dict(inp, evidence_groups=conflict))

    def test_boundary_semantics_preserved_and_exhaustion_visible(self):
        p = evaluate("PHOENIX", dict(self.inputs["PHOENIX"], hold=0, start=999))
        self.assertTrue(p["stable"])
        self.assertTrue(p["vacuous_window"])
        self.assertEqual(evaluate("WHALE", {"values": [2, 4], "baseline": 0, "window": 0})["gap"], 3)
        self.assertEqual(evaluate("WHALE", {"values": [], "baseline": 2, "window": 1}), {"deviation": 0, "gap": 0})
        self.assertEqual(evaluate("ELEPHANT", dict(self.inputs["ELEPHANT"], fuel=0))["termination"], "exhausted")
        self.assertEqual(evaluate("SALMON", dict(self.inputs["SALMON"], fuel=0))["trace"]["kind"], "exhausted")


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "ledger.jsonl"
        self.engine = Engine(self.path)
        self.raw = b'{"candidate_brier":0.1,"control_brier":0.2}'
        self.spec = plan("TORTOISE", self.raw, {"metric": "gain", "operator": "gt", "value": 0})

    def run_plan(self, spec=None, raw=None):
        frozen = self.engine.freeze(spec or self.spec)
        return self.engine.run(frozen["hash"], self.raw if raw is None else raw)["payload"]

    def test_research_blocked_until_explicit_review(self):
        research = dict(self.spec, mode="research_retro")
        with self.assertRaisesRegex(ValueError, "accepted mapping"):
            self.engine.freeze(research)
        self.engine.map(proposal())
        with self.assertRaisesRegex(ValueError, "accepted mapping"):
            self.engine.freeze(research)
        self.engine.map(dict(proposal(), status="accepted", reviewer="test-only reviewer declaration"))
        result = self.run_plan(research)
        self.assertEqual(result["status"], "computed")
        self.assertEqual(result["scientific_status"], "unassessed")
        self.assertEqual(result["formal_status"], "unassessed")

    def test_synthetic_computation_does_not_clear_unknown_mapping(self):
        self.assertEqual(self.run_plan()["criterion_outcome"], "met")
        report = self.engine.report()
        self.assertEqual(report["applicability"]["unknown"], 774180)
        self.assertEqual(report["scientific_promotions"], 0)
        self.assertEqual(report["declared_research_groups"], 0)

    def test_negative_result_and_bad_input_both_retained(self):
        raw = b'{"candidate_brier":0.3,"control_brier":0.2}'
        negative = dict(self.spec, input_sha256=hashlib.sha256(raw).hexdigest())
        self.assertEqual(self.run_plan(negative, raw)["criterion_outcome"], "not_met")
        raw = b'{"candidate_brier":"bad","control_brier":0.2}'
        invalid = dict(self.spec, input_sha256=hashlib.sha256(raw).hexdigest())
        self.assertEqual(self.run_plan(invalid, raw)["status"], "error")
        self.assertEqual(self.engine.report()["run_statuses"], {"computed": 1, "error": 1})
        self.assertEqual(len(self.engine.ledger.read()), 4)

    def test_nonfinite_duplicate_or_malformed_json_retained_as_errors(self):
        for raw in (b'{"x":NaN}', b'{"x":1,"x":2}', b'{oops', b'\xff'):
            spec = dict(self.spec, input_sha256=hashlib.sha256(raw).hexdigest())
            self.assertEqual(self.run_plan(spec, raw)["status"], "error")
        self.assertEqual(self.engine.report()["runs"], 4)

    def test_changed_input_engine_mapping_are_blocked(self):
        p = self.engine.freeze(self.spec)
        self.assertIn("Input digest", self.engine.run(p["hash"], self.raw + b' ')["payload"]["error"])
        with patch("research_engine.engine.engine_digest", return_value="f" * 64):
            self.assertIn("Engine or catalog changed", self.engine.run(p["hash"], self.raw)["payload"]["error"])
        self.engine.map(proposal())
        self.assertIn("Applicability decision changed", self.engine.run(p["hash"], self.raw)["payload"]["error"])

    def test_inapplicable_slot_blocks_even_synthetic_execution(self):
        self.engine.map(dict(proposal(), status="inapplicable"))
        self.assertIn("explicitly inapplicable", self.run_plan()["error"])

    def test_repeated_runs_not_counted_as_independent_groups(self):
        self.engine.map(dict(proposal(), status="accepted"))
        p = self.engine.freeze(dict(self.spec, mode="research_retro"))
        for _ in range(3):
            self.engine.run(p["hash"], self.raw)
        r = self.engine.report()
        self.assertEqual(r["computed_slots"], 1)
        self.assertEqual(r["declared_research_groups"], 1)
        self.assertEqual(r["research_runs"], 3)

    def test_ledger_tamper_reorder_and_incomplete_tail_detection(self):
        self.run_plan()
        original = self.path.read_text()
        for damaged in (original.replace('"computed"', '"promoted"'), "\n".join(reversed(original.splitlines())) + "\n", original[:-1]):
            with self.subTest(damaged=damaged[:50]), self.assertRaises(ValueError):
                verify_lines(damaged)
        self.path.write_text(original[:-1])
        with self.assertRaisesRegex(ValueError, "Incomplete ledger"):
            self.engine.freeze(self.spec)

    def test_concurrent_writers_preserve_chain(self):
        def writer(i):
            return Engine(self.path).map(dict(proposal(), reason="Concurrent proposal " + str(i)))
        with ThreadPoolExecutor(max_workers=4) as pool:
            records = list(pool.map(writer, range(12)))
        self.assertEqual(len({r["hash"] for r in records}), 12)
        self.assertEqual(len(self.engine.ledger.read()), 12)

    def test_mapping_measurements_and_plan_schema_are_strict(self):
        bad = proposal()
        bad["adapter"]["measurements"] = {"not_a_parameter": "dimensionless"}
        with self.assertRaises(ValueError):
            self.engine.map(bad)
        with self.assertRaises(ValueError):
            self.engine.freeze(dict(self.spec, mode="prospective"))
        with self.assertRaises(ValueError):
            self.engine.freeze(dict(self.spec, hidden_target_change=True))
        with self.assertRaises(ValueError):
            self.engine.freeze(dict(self.spec, context={}))

    def test_bad_criterion_records_computation_and_error(self):
        result = self.run_plan(dict(self.spec, criterion={"metric": "absent", "operator": "gt", "value": 0}))
        self.assertEqual(result["status"], "error")
        self.assertIn("output", result)
        self.assertEqual(result["criterion_outcome"], "not_evaluated")

    def test_dashboard_script_payload_escapes_html(self):
        self.run_plan(dict(self.spec, hypothesis="</script><script>alert('x')</script>"))
        target = render(self.engine, Path(self.temp.name) / "index.html")
        html = target.read_text()
        self.assertNotIn("</script><script>alert", html)
        self.assertIn("\\u003c/script>", html)
        self.assertNotIn("__EFMW_DATA__", html)


if __name__ == "__main__":
    unittest.main()
