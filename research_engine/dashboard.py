"""Self-contained read-only snapshot; no live remote data or CDN dependencies."""
import json
from pathlib import Path

from .catalog import read
from .kernels import describe


def render(engine, destination):
    catalog = engine.catalog
    data = {"report": engine.report(), "equations": catalog.equations,
            "triplets": catalog.triplets, "animals": catalog.animals,
            "prior": catalog.prior, "sources": read("provenance.json"),
            "kernels": {a: describe(a) for a in catalog.zoo}, "events": engine.ledger.read()}
    template = Path(__file__).with_name("dashboard.html").read_text(encoding="utf-8")
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"), allow_nan=False).replace("<", "\\u003c")
    output = template.replace("__EFMW_DATA__", payload)
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(output, encoding="utf-8")
    return destination
