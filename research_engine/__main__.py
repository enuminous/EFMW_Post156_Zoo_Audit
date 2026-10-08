"""Run with python -m research_engine --help from the repository root."""
import argparse
import csv
import hashlib
import json
import sys
from pathlib import Path

from .catalog import ROOT
from .engine import Engine, mappings, parse_json
from .kernels import describe


def main(argv=None):
    parser = argparse.ArgumentParser(description="EFMW 102 × 165 × 46 research registry")
    parser.add_argument("--ledger", type=Path, default=ROOT / "research_engine/.state/ledger.jsonl")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status", help="Catalog, applicability and execution counts")
    sub.add_parser("verify", help="Verify frozen sources and the entire ledger hash chain")
    p = sub.add_parser("schema", help="Exact kernel parameters and implemented scope")
    p.add_argument("animal")
    p = sub.add_parser("hash", help="SHA256 of exact input-file bytes for a frozen plan")
    p.add_argument("file", type=Path)
    for command in ("map", "freeze"):
        p = sub.add_parser(command, help="Append an explicit " + ("applicability decision" if command == "map" else "execution plan"))
        p.add_argument("file", type=Path)
    p = sub.add_parser("run", help="Execute a frozen plan and retain success or error")
    p.add_argument("plan_hash")
    p.add_argument("input", type=Path)
    p = sub.add_parser("slots", help="Stream all or filtered potential slots as CSV")
    p.add_argument("--equation")
    p.add_argument("--triplet")
    p.add_argument("--animal")
    p.add_argument("--output", type=Path, required=True)
    p = sub.add_parser("dashboard", help="Generate a standalone searchable HTML dashboard")
    p.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        engine = Engine(args.ledger)
        command = args.command
        if command == "hash":
            print(hashlib.sha256(args.file.read_bytes()).hexdigest())
            return 0
        if command in ("status", "verify"):
            result = engine.report()
        elif command == "schema":
            result = describe(args.animal.upper())
        elif command == "map":
            result = engine.map(parse_json(args.file.read_text(encoding="utf-8")))
        elif command == "freeze":
            result = engine.freeze(parse_json(args.file.read_text(encoding="utf-8")))
        elif command == "run":
            result = engine.run(args.plan_hash, args.input.read_bytes())
        elif command == "slots":
            latest = mappings(engine.ledger.read())
            args.output.parent.mkdir(parents=True, exist_ok=True)
            count = 0
            with args.output.open("w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["equation", "triplet", "animal", "applicability"])
                for slot in engine.catalog.slots(args.equation, args.triplet, args.animal):
                    status = latest.get(slot, {}).get("payload", {}).get("status", "unknown")
                    writer.writerow(slot.split("/") + [status])
                    count += 1
            result = {"output": str(args.output), "potential_slots": count}
        elif command == "dashboard":
            from .dashboard import render
            render(engine, args.output)
            result = {"output": str(args.output), "head": engine.report()["head"]}
        print(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False))
        return 2 if command == "run" and result["payload"]["status"] == "error" else 0
    except (ValueError, KeyError, OSError) as error:
        print("error: " + str(error), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
