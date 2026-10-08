"""Frozen source catalogs. A Cartesian slot is a question, never a result."""
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = Path(__file__).parent / "data"


def read(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


class Catalog:
    def __init__(self):
        self.equations = read("equations.json")["equations"]
        self.triplets = read("triplets.json")
        self.animals = read("zoo-coverage.json")
        self.prior = read("prior-equation-audit.json")["records"]
        self.ranked = {x["name"].upper(): x for x in read("zoo-ranked-components.json")}
        self.eq = {x["id"]: x for x in self.equations}
        self.fs = {x["id"]: x for x in self.triplets}
        self.zoo = {x["name"]: x for x in self.animals}
        if (len(self.eq), len(self.fs), len(self.zoo)) != (102, 165, 46):
            raise ValueError("Catalog cardinality mismatch")
        expected = {"FS-" + "".join(s) for s in itertools.combinations(sorted("EMSFW TIRHPA".replace(" ", "")), 3)}
        if set(self.fs) != expected or set(self.eq) != {f"ME-{n:03}" for n in range(1, 103)}:
            raise ValueError("Catalog identity mismatch")
        self.verify()

    @property
    def total(self):
        return len(self.eq) * len(self.fs) * len(self.zoo)

    def verify(self):
        sources = read("provenance.json")
        for source in sources:
            digest = hashlib.sha256((ROOT / source["local_path"]).read_bytes()).hexdigest()
            if digest != source["sha256"]:
                raise ValueError("Frozen source changed: " + source["local_path"])
        self.digest = hashlib.sha256(json.dumps(sources, sort_keys=True).encode()).hexdigest()
        return sources

    def slot(self, equation, triplet, animal):
        if equation not in self.eq or triplet not in self.fs or animal not in self.zoo:
            raise ValueError("Unknown equation, triplet or animal ID")
        return "/".join((equation, triplet, animal))

    def slots(self, equation=None, triplet=None, animal=None):
        axes = (self.eq if equation is None else [equation],
                self.fs if triplet is None else [triplet],
                self.zoo if animal is None else [animal])
        for e, t, a in itertools.product(*axes):
            yield self.slot(e, t, a)
