"""Sparse applicability registry and append-only, hash-linked execution ledger.

The local file lock serializes writers. Hash links detect edits relative to a
trusted head; they are not signatures or proof of when observations became known.
"""
import contextlib
import datetime
import fcntl
import hashlib
import json
import operator
import re
from collections import Counter
from pathlib import Path

from . import __version__
from .catalog import Catalog
from .kernels import KERNELS, evaluate, finite

ZERO = "0" * 64
CONTEXT = {"frozen_before_outcome", "no_target_leakage", "matched_information", "independent_outcome"}
COMPARATORS = {"eq": operator.eq, "gt": operator.gt, "ge": operator.ge, "lt": operator.lt, "le": operator.le}


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def parse_json(text):
    def reject(x):
        raise ValueError("Non-finite JSON constant: " + x)
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError("Duplicate JSON key: " + key)
            result[key] = value
        return result
    value = json.loads(text, parse_constant=reject, object_pairs_hook=pairs)
    finite(value)
    return value


def require_text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(label + " must be a nonempty string")


def require_list(value, label, nonempty=True):
    if not isinstance(value, list) or (nonempty and not value):
        raise ValueError(label + " must be a list" + (" with at least one item" if nonempty else ""))
    for x in value:
        require_text(x, label)


def verify_lines(text):
    if text and not text.endswith("\n"):
        raise ValueError("Incomplete ledger tail; preserve and repair before writing")
    events, previous = [], ZERO
    for index, line in enumerate(text.splitlines(), 1):
        item = parse_json(line)
        if not isinstance(item, dict) or set(item) != {"seq", "previous", "timestamp", "kind", "payload", "hash"}:
            raise ValueError(f"Invalid ledger record {index}")
        body = {k: v for k, v in item.items() if k != "hash"}
        if item["seq"] != index or item["previous"] != previous or item["hash"] != digest(body):
            raise ValueError(f"Ledger integrity failure at record {index}")
        if item["kind"] not in ("mapping", "plan", "run"):
            raise ValueError("Unknown ledger event type")
        previous = item["hash"]
        events.append(item)
    return events


class Ledger:
    def __init__(self, path):
        self.path = Path(path)

    def read(self):
        if not self.path.exists():
            return []
        with self.path.open(encoding="utf-8") as stream:
            fcntl.flock(stream, fcntl.LOCK_SH)
            return verify_lines(stream.read())

    @contextlib.contextmanager
    def transaction(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a+", encoding="utf-8") as stream:
            fcntl.flock(stream, fcntl.LOCK_EX)
            stream.seek(0)
            events = verify_lines(stream.read())
            def append(kind, payload):
                body = {"seq": len(events) + 1, "previous": events[-1]["hash"] if events else ZERO,
                        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                        "kind": kind, "payload": payload}
                item = dict(body, hash=digest(body))
                encoded = canonical(item) + "\n"
                stream.seek(0, 2)
                stream.write(encoded)
                stream.flush()
                import os
                os.fsync(stream.fileno())
                events.append(item)
                return item
            yield events, append


def mappings(events):
    return {e["payload"]["slot"]: e for e in events if e["kind"] == "mapping"}


def engine_digest():
    files = ("__init__.py", "catalog.py", "kernels.py", "engine.py")
    return digest({name: hashlib.sha256((Path(__file__).parent / name).read_bytes()).hexdigest() for name in files})


class Engine:
    def __init__(self, ledger):
        self.catalog = Catalog()
        self.ledger = Ledger(ledger)

    def check_slot(self, slot):
        if not isinstance(slot, str) or len(slot.split("/")) != 3:
            raise ValueError("Slot must be ME-nnn/FS-ABC/ANIMAL")
        return self.catalog.slot(*slot.split("/"))

    def map(self, spec):
        fields = {"slot", "status", "reason", "adapter", "assumptions", "reviewer", "evidence_sources"}
        if not isinstance(spec, dict) or set(spec) != fields:
            raise ValueError("Mapping requires exactly: " + ", ".join(sorted(fields)))
        self.check_slot(spec["slot"])
        if spec["status"] not in ("proposed", "accepted", "inapplicable", "unknown"):
            raise ValueError("Invalid applicability status")
        for key in ("reason", "reviewer"):
            require_text(spec[key], key)
        for key in ("assumptions", "evidence_sources"):
            require_list(spec[key], key)
        adapter = spec["adapter"]
        if not isinstance(adapter, dict) or set(adapter) != {"equation_role", "triplet_role", "measurements"}:
            raise ValueError("Adapter needs equation_role, triplet_role and measurements")
        require_text(adapter["equation_role"], "equation_role")
        require_text(adapter["triplet_role"], "triplet_role")
        if not isinstance(adapter["measurements"], dict) or not adapter["measurements"]:
            raise ValueError("Measurements must name kernel inputs and their meanings/units")
        animal = spec["slot"].split("/")[-1]
        import inspect
        parameters = inspect.signature(KERNELS[animal][0]).parameters
        required = {n for n, p in parameters.items() if p.default is inspect.Parameter.empty}
        if not required <= set(adapter["measurements"]) <= set(parameters):
            raise ValueError("Measurement map does not cover the kernel's required inputs")
        for value in adapter["measurements"].values():
            require_text(value, "measurement meaning/units")
        with self.ledger.transaction() as (_, append):
            return append("mapping", dict(spec, catalog_digest=self.catalog.digest,
                                          authority="reviewer declaration; not independently verified"))

    def freeze(self, spec):
        fields = {"slot", "mode", "hypothesis", "variables", "assumptions", "falsifier", "baseline",
                  "known_result", "evidence_group", "context", "limitations", "input_sha256", "criterion"}
        if not isinstance(spec, dict) or set(spec) != fields:
            raise ValueError("Plan requires exactly: " + ", ".join(sorted(fields)))
        self.check_slot(spec["slot"])
        if spec["mode"] not in ("synthetic", "research_retro"):
            raise ValueError("Only synthetic and research_retro modes are implemented; no prospective certification")
        for key in ("hypothesis", "variables", "falsifier", "baseline", "known_result", "evidence_group"):
            require_text(spec[key], key)
        for key in ("assumptions", "limitations"):
            require_list(spec[key], key)
        if not isinstance(spec["input_sha256"], str) or not re.fullmatch("[0-9a-f]{64}", spec["input_sha256"]):
            raise ValueError("input_sha256 must pin the exact UTF-8 input file bytes")
        context = spec["context"]
        if not isinstance(context, dict) or set(context) != CONTEXT:
            raise ValueError("Plan must declare all four audit obligations")
        for value in context.values():
            if not isinstance(value, dict) or set(value) != {"declared", "source"} or type(value["declared"]) is not bool:
                raise ValueError("Audit obligations require declared: bool and source: string")
            require_text(value["source"], "obligation source")
        c = spec["criterion"]
        if c is not None:
            if not isinstance(c, dict) or set(c) != {"metric", "operator", "value"} or c["operator"] not in COMPARATORS:
                raise ValueError("Criterion needs metric, operator (eq/gt/ge/lt/le), value")
            require_text(c["metric"], "criterion metric")
            if type(c["value"]) not in (str, bool, float, int):
                raise ValueError("Criterion value must be a scalar")
            finite(c["value"])
        with self.ledger.transaction() as (events, append):
            mapping = mappings(events).get(spec["slot"])
            if spec["mode"] == "research_retro" and (not mapping or mapping["payload"]["status"] != "accepted" or mapping["payload"]["catalog_digest"] != self.catalog.digest):
                raise ValueError("Research execution requires an explicit accepted mapping for this frozen catalog")
            return append("plan", dict(spec, mapping_hash=mapping["hash"] if mapping else None,
                                       catalog_digest=self.catalog.digest, engine_digest=engine_digest(),
                                       version=__version__, freeze_scope="before execution; outcome timing unverified"))

    def run(self, plan_hash, input_bytes):
        # The transaction covers validation + execution + append, preventing a
        # concurrent mapping edit from bypassing the frozen-map comparison.
        with self.ledger.transaction() as (events, append):
            plan = next((e for e in events if e["kind"] == "plan" and e["hash"] == plan_hash), None)
            if plan is None:
                raise ValueError("Unknown full plan hash")
            p = plan["payload"]
            result = {"plan_hash": plan_hash, "slot": p["slot"], "mode": p["mode"],
                      "evidence_group": p["evidence_group"], "input_sha256": hashlib.sha256(input_bytes).hexdigest(),
                      "engine_digest": engine_digest(), "catalog_digest": self.catalog.digest,
                      "scientific_status": "unassessed", "formal_status": "unassessed"}
            try:
                result["input_text"] = input_bytes.decode("utf-8")
                if p["engine_digest"] != result["engine_digest"] or p["catalog_digest"] != result["catalog_digest"]:
                    raise ValueError("Engine or catalog changed after plan; freeze a new plan")
                if p["input_sha256"] != result["input_sha256"]:
                    raise ValueError("Input digest differs from frozen plan")
                mapping = mappings(events).get(p["slot"])
                current = mapping["hash"] if mapping else None
                if current != p["mapping_hash"]:
                    raise ValueError("Applicability decision changed after plan; freeze a new plan")
                if mapping and mapping["payload"]["status"] == "inapplicable":
                    raise ValueError("Slot is explicitly inapplicable")
                output = evaluate(p["slot"].split("/")[-1], parse_json(result["input_text"]))
                result["output"] = output
                criterion = p["criterion"]
                if criterion is None:
                    outcome = "not_specified"
                else:
                    metric = output
                    for key in criterion["metric"].split("."):
                        metric = metric[int(key)] if isinstance(metric, list) else metric[key]
                    if type(metric) not in (str, bool, float, int):
                        raise ValueError("Criterion metric must select a scalar")
                    target = criterion["value"]
                    if isinstance(metric, bool) != isinstance(target, bool) or isinstance(metric, str) != isinstance(target, str):
                        raise ValueError("Criterion metric and target types differ")
                    outcome = "met" if COMPARATORS[criterion["operator"]](metric, target) else "not_met"
                result.update(status="computed", criterion_outcome=outcome)
            except (ValueError, TypeError, KeyError, IndexError, OverflowError, ZeroDivisionError, UnicodeError) as error:
                result.update(status="error", criterion_outcome="not_evaluated", error=str(error))
            return append("run", result)

    def report(self):
        events = self.ledger.read()
        latest = mappings(events)
        counts = Counter(e["payload"]["status"] for e in latest.values())
        counts["unknown"] += self.catalog.total - len(latest)
        runs = [e["payload"] for e in events if e["kind"] == "run"]
        return {"version": __version__, "catalog_digest": self.catalog.digest,
                "axes": {"equations": 102, "triplets": 165, "animals": 46}, "potential_slots": self.catalog.total,
                "applicability": {s: counts[s] for s in ("unknown", "proposed", "accepted", "inapplicable")},
                "kernel_adapters": len(KERNELS), "plans": sum(e["kind"] == "plan" for e in events),
                "runs": len(runs), "run_statuses": dict(Counter(r["status"] for r in runs)),
                "computed_slots": len({r["slot"] for r in runs if r["status"] == "computed"}),
                "synthetic_runs": sum(r["mode"] == "synthetic" for r in runs),
                "research_runs": sum(r["mode"] == "research_retro" for r in runs),
                "criterion_outcomes": dict(Counter(r["criterion_outcome"] for r in runs)),
                "declared_research_groups": len({r["evidence_group"] for r in runs if r["mode"] == "research_retro" and r["status"] == "computed"}),
                "scientific_promotions": 0, "new_formal_proofs": 0,
                "head": events[-1]["hash"] if events else ZERO,
                "notice": "Slots, kernels, runs, caller-declared groups, proofs and physical laws are different counts. No scientific promotion is implemented."}
