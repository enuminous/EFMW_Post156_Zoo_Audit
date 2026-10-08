"""Small inspectable input cases, including the frozen upstream numeric fixtures."""
from research_engine.catalog import Catalog


def cases():
    data = {
        "TORTOISE": {"candidate_brier": .12, "control_brier": .14},
        "CAT": {"full": .2, "ablated": .3},
        "BAT": {"gain": .01, "placebo_gain": .02, "incremental_brier": .1, "placebo_brier": .2},
        "HEDGEHOG": {"median_gain": .003, "win_rate": .7, "habitat_support": False, "development": ["development-a"], "heldout": ["heldout-b"]},
        "CROCODILE": {"treated_pre": 1, "treated_post": 4, "control_pre": 2, "control_post": 3},
        "TURTLE": {"evidence_groups": [{"id": "one-shared-source", "applicable": True, "veto_on_failure": False, "polarity": "positive"}] * 3, "invariant_score": .9},
        "MAGPIE": {"coherence": .9, "direct_support": .8, "provenance": .7, "corroboration": .6, "unsupported_inference": .2, "unresolved_provenance": .1, "contradiction": .3},
        "WOLF": {"rho": .85, "previous": 0, "instantaneous": 1},
        "ELEPHANT": {"events": [{"id": 1, "time": 1, "status": "superseded", "supersedes": None, "provenance": "synthetic original"}, {"id": 2, "time": 2, "status": "active", "supersedes": 1, "provenance": "synthetic revision"}], "start": 2, "fuel": 3},
        "CHAMELEON": {"distance": 2, "expected_adaptation": .5, "between": 1, "within": 0},
        "JELLYFISH": {"base_weight": .4, "stress_gain": .2, "confidence": .8, "stress": .5, "health": .9, "alpha": .5, "incoming": .2},
        "BEAVER": {"effectiveness": .1, "collateral": .1, "verification": 1, "bounded": True, "rollback_verified": False},
        "MANTIS": {"ready": False, "z_variance": 3, "z_autocorrelation": 3, "z_curvature": 3},
        "BISON": {"demand": 10, "queue": 2, "capacity": 3, "queue_limit": 5},
        "WEASEL": {"findings": [{"changed_keys": 1, "severity": 2, "cost": .2, "reproducibility": 1}, {"changed_keys": 2, "severity": 3, "cost": .1, "reproducibility": 1}], "budget": 1},
        "SALMON": {"weight": 2, "incoming_weights": [.25, .25], "parents": {"0": [1]}, "start": 0, "fuel": 1},
        "ORCA": {"ack": True, "payload_complete": False, "ownership_clear": True, "dependency_complete": True},
        "MOLE": {"indicators_present": True, "surface_health": .9, "latent_degradation": .7, "coverage": .8},
        "LYNX": {"distance": 2, "rarity": 2, "rediscovery": .5, "replication": .8, "yield_score": .9},
        "HORSE": {"workload": .8, "attention": .7, "fatigue": .2},
        "TERMITE": {"state": .2, "weighted_sum": .8, "total_weight": 1, "susceptibility": .5, "bias": .1},
        "PHOENIX": {"fidelity": .5, "integrity": 1, "capability": .8, "scores": [.9, .95], "start": 0, "hold": 2, "threshold": .8},
        "COBRA": {"previous": 0, "divergence": .8, "violation": .3, "proxy_delta": 0, "goal_delta": 0, "context_gap": .2, "confidence": .9},
        "WHALE": {"values": [1, 2, 4], "baseline": 1, "window": 1},
        "FALCON": {"event_time": 1, "hazard_time": 3, "delay": 1, "alarm_time": 2},
        "RHINO": {"baseline": 2, "after": 1},
        "BONOBO": {"gains": [.2, -.1], "efficiency": .8, "stability": .9, "fairness_dispersion": .1, "resolution": .8},
        "AXOLOTL": {"reference_function": 1, "damaged_function": .2, "adapted_function": .8, "cost": .3, "transformation": .3, "invariant_retention": 1},
        "BUTTERFLY": {"state": 1.2, "base": .1, "gain": .5, "threshold": 1, "incoming": 0},
    }
    catalog = Catalog()
    for animal, spec in catalog.ranked.items():
        data[animal] = {"columns": [[0, 1, 1, 3] for _ in range(len(spec["base"]) + len(spec["horizon"]))], "rows": 4, "horizons": 1}
    return data


def fixture_bindings():
    # Each binding selects the Python output corresponding to the frozen Lean
    # expression. Expected values are read from the upstream file, never computed
    # with the implementation being checked.
    names = {
        "magpie.groundedness": ("MAGPIE", "groundedness"),
        "wolf.update": ("WOLF", "updated"),
        "chameleon.noiseAdjusted": ("CHAMELEON", "noise_adjusted"),
        "jellyfish.dynamicWeight": ("JELLYFISH", "dynamic_weight"),
        "jellyfish.nextHealth": ("JELLYFISH", "next_health"),
        "bison.served": ("BISON", "served"), "bison.queue": ("BISON", "queue"), "bison.dropped": ("BISON", "dropped"),
        "orca.handoff": ("ORCA", "handoff_integrity"),
        "lynx.novelty": ("LYNX", "novelty"), "lynx.yield": ("LYNX", "latent_yield"),
        "horse.workload": ("HORSE", "workload_penalty"),
        "termite.step": ("TERMITE", "next_state"),
        "phoenix.completeness": ("PHOENIX", "completeness"),
        "cobra.risk": ("COBRA", "risk"),
        "whale.deviation": ("WHALE", "deviation"), "whale.gap": ("WHALE", "gap"),
        "rhino.retention": ("RHINO", "retention"),
        "axolotl.recovery": ("AXOLOTL", "recovery"), "axolotl.efficiency": ("AXOLOTL", "efficiency"), "axolotl.resilience": ("AXOLOTL", "resilience"),
        "butterfly.step": ("BUTTERFLY", "next_state"),
    }
    for name in Catalog().ranked:
        for row in range(4):
            names[name.lower() + ".rank" + str(row)] = (name, "scores." + str(row))
    return names
