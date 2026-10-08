"""Run: python -m research_engine.examples.demo --output /tmp/efmw-demo

Refuses to overwrite an existing ledger. All inputs are synthetic. The example
slot assignments exercise the registry; they do not establish physical mappings.
"""
import argparse
import hashlib
import json
from pathlib import Path

from research_engine.catalog import Catalog
from research_engine.dashboard import render
from research_engine.engine import CONTEXT, Engine
from research_engine.examples.cases import cases


def plan(animal, raw, criterion=None):
    return {
        "slot": "ME-002/FS-EFM/" + animal, "mode": "synthetic",
        "hypothesis": "Software fixture for the frozen " + animal + " operation; no physical hypothesis tested.",
        "variables": "Supplied synthetic numbers in kernel-native units; no measured EFMW fields.",
        "assumptions": ["Inputs are software fixtures", "The slot assignment is illustrative and has no validated physical adapter"],
        "falsifier": "A numerical mismatch or failed declared criterion rejects this fixture expectation.",
        "baseline": "Frozen selected Zoo operation and conventional arithmetic, not an experimental baseline.",
        "known_result": "Previously specified Zoo kernel; no new scientific result or novelty claimed.",
        "evidence_group": "synthetic-kernel-fixtures-v1",
        "context": {k: {"declared": False, "source": "Synthetic software fixture; obligation not established"} for k in CONTEXT},
        "limitations": ["No scientific applicability established", "No prospective or empirical validation", "No formal equivalence proof"],
        "input_sha256": hashlib.sha256(raw).hexdigest(), "criterion": criterion,
    }


def proposal():
    return {
        "slot": "ME-002/FS-EFM/TORTOISE", "status": "proposed", "reviewer": "engine author; proposal only",
        "reason": "Candidate scalar propagation experiment: identify Monolithic φ with φ_F on an explicitly fixed background. A physical measurement adapter and review are still missing.",
        "adapter": {"equation_role": "Candidate scalar propagation predictor from ME-002",
                    "triplet_role": "Scalar F component of FS-EFM; gauge/gravity components impose separate obligations",
                    "measurements": {"candidate_brier": "Dimensionless Brier score of a specified ME-002-derived binary forecast on heldout outcomes; predictor and outcomes not yet supplied",
                                     "control_brier": "Dimensionless Brier score of a matched conventional forecast on exactly the same outcomes; baseline not yet supplied"}},
        "assumptions": ["Explicit definition of φ ↔ φ_F and all units is required", "A common background metric and derivative convention must be fixed", "Source, mass, nonminimal and interaction terms must be reconciled", "Score computation and matched outcomes require independent verification"],
        "evidence_sources": ["https://github.com/enuminous/Monolithic_102_EFMW/blob/26a3c057a80f4c60566a543427d6d85fc1aa349f/equations.json", "sources/fieldspace/EFMW_165_field_equations.txt", "research_engine/data/zoo-specifications.json:Tortoise.lean"],
    }


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def build(destination):
    out = Path(destination)
    out.mkdir(parents=True, exist_ok=True)
    ledger = out / "demo-ledger.jsonl"
    if ledger.exists():
        raise ValueError("Preserving existing demo ledger; select a fresh output directory")
    engine = Engine(ledger)
    write_json(out / "mapping-proposal.json", proposal())
    engine.map(proposal())
    sample_inputs = cases()
    write_json(out / "kernel-inputs.json", sample_inputs)
    for animal in Catalog().zoo:
        raw = (json.dumps(sample_inputs[animal], sort_keys=True) + "\n").encode()
        criterion = None
        if animal == "TORTOISE":
            criterion = {"metric": "gain", "operator": "gt", "value": 0}
            (out / "tortoise-input.json").write_bytes(raw)
        if animal == "BAT":
            criterion = {"metric": "label", "operator": "eq", "value": "survives"}
        p = plan(animal, raw, criterion)
        if animal == "TORTOISE":
            write_json(out / "tortoise-plan.json", p)
        frozen = engine.freeze(p)
        engine.run(frozen["hash"], raw)
    # A valid calculation with a negative result, and an invalid schema, both stay.
    for inputs in ({"candidate_brier": .3, "control_brier": .2},
                   {"candidate_brier": "not-a-number", "control_brier": .2}):
        raw = json.dumps(inputs).encode()
        frozen = engine.freeze(plan("TORTOISE", raw, {"metric": "gain", "operator": "gt", "value": 0}))
        engine.run(frozen["hash"], raw)
    write_json(out / "status.json", engine.report())
    render(engine, out / "index.html")
    return engine.report()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(build(args.output), indent=2))
