"""Python ports of selected frozen Zoo operations, not whole animal pipelines.

Inputs are supplied measurements/features. Kernel labels (including 'supported')
are local outputs, not scientific evidence grades. See data/zoo-specifications.json
and zoo-LICENSE. Floating-point reference agreement is not Lean equivalence.
"""
import inspect
import math
from collections import Counter

from .catalog import Catalog

KERNELS = {}


def kernel(name, scope):
    def register(fn):
        KERNELS[name] = (fn, scope)
        return fn
    return register


def finite(value):
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError("NaN and infinity are not admissible")
    if isinstance(value, (list, tuple)):
        for x in value:
            finite(x)
    if isinstance(value, dict):
        for x in value.values():
            finite(x)


def number(x):
    if type(x) not in (float, int) or not math.isfinite(x):
        raise ValueError("Expected a finite number, not a boolean or string")
    return x


def natural(x):
    if type(x) is not int or not 0 <= x < 2**53:
        raise ValueError("Expected a nonnegative integer below 2^53")
    return x


def numbers(xs):
    if not isinstance(xs, list):
        raise ValueError("Expected a numeric list")
    return [number(x) for x in xs]


def unit(x):
    if not 0 <= x <= 1:
        raise ValueError("Expected a value in [0, 1]")
    return x


def nonnegative(x):
    if x < 0:
        raise ValueError("Expected a nonnegative value")
    return x


def pos(x):
    return max(0.0, x)


def clip(x):
    return max(0.0, min(1.0, x))


def mean(xs):
    return sum(xs) / len(xs) if xs else 0.0


def ema(rho, previous, current):
    return rho * previous + (1.0 - rho) * current


def rank_kernel(spec):
    def run(columns: list, rows: int, horizons: int = 1, mode: str = "retrospective"):
        if mode != "retrospective":
            raise ValueError("Full-column ranks can use future rows; only retrospective ranking is implemented")
        count = len(spec["base"]) + len(spec["horizon"]) * horizons
        if len(columns) != count or count == 0:
            raise ValueError(f"Expected {count} precomputed columns in frozen component order")
        ranks = []
        for col in columns:
            numbers(col)
            if len(col) != rows:
                raise ValueError("Ragged column or row-count mismatch")
            counts, less, lookup = Counter(col), 0, {}
            for value in sorted(counts):
                equal = counts[value]
                lookup[value] = (2 * less + equal + 1) / (2 * rows)
                less += equal
            ranks.append([lookup[x] for x in col])
        return {"scores": [mean([c[r] for c in ranks]) for r in range(rows)],
                "columns": count, "mode": mode}
    return run


@kernel("TORTOISE", "Brier gain from supplied candidate and control scores; no fitting or prospective guarantee")
def tortoise(candidate_brier: float, control_brier: float):
    unit(candidate_brier); unit(control_brier)
    return {"gain": control_brier - candidate_brier}


@kernel("CAT", "Ablation penalty and its sign from supplied losses")
def cat(full: float, ablated: float):
    penalty = ablated - full
    return {"penalty": penalty, "label": "removalHurt" if penalty > 0 else "removalHelped" if penalty < 0 else "noChange"}


@kernel("BAT", "Placebo-first baseline decision from supplied summary scores")
def bat(gain: float, placebo_gain: float, incremental_brier: float, placebo_brier: float, material_gain: float = .002):
    unit(incremental_brier); unit(placebo_brier); nonnegative(material_gain)
    if placebo_gain >= gain - .000001 and gain > 0:
        label = "placeboFailure"
    elif gain >= material_gain and incremental_brier < placebo_brier:
        label = "survives"
    elif gain > 0 and incremental_brier < placebo_brier:
        label = "weak"
    else:
        label = "baselineExplains"
    return {"label": label}


@kernel("HEDGEHOG", "Summary decision; additionally checks supplied development and heldout IDs are disjoint")
def hedgehog(median_gain: float, win_rate: float, habitat_support: bool,
             development: list, heldout: list, material_gain: float = .002):
    unit(win_rate); nonnegative(material_gain)
    if any(type(x) is not str or not x for x in development + heldout):
        raise ValueError("Environment IDs must be nonempty strings")
    if not development or not heldout or set(development) & set(heldout):
        raise ValueError("Development and heldout environments must be nonempty and disjoint")
    label = ("generalizes" if median_gain >= material_gain and win_rate >= .60 else
             "habitatConditional" if median_gain > 0 and habitat_support else
             "weak" if median_gain > 0 else "doesNotGeneralize")
    return {"label": label, "supplied_environment_ids_disjoint": True}


@kernel("CROCODILE", "Difference-in-differences arithmetic; causal assumptions remain external")
def crocodile(treated_pre: float, treated_post: float, control_pre: float, control_post: float):
    return {"difference_in_differences": (treated_post - treated_pre) - (control_post - control_pre)}


@kernel("TURTLE", "Evidence decision with group counts derived from distinct supplied group IDs; independence remains external")
def turtle(evidence_groups: list, invariant_score: float, minimum_groups: int = 3,
           support_threshold: float = .18, conditional_threshold: float = .05):
    if minimum_groups < 1 or not 0 <= conditional_threshold <= support_threshold:
        raise ValueError("Invalid group or score thresholds")
    unique = {}
    for g in evidence_groups:
        if not isinstance(g, dict) or set(g) != {"id", "applicable", "veto_on_failure", "polarity"}:
            raise ValueError("Each group needs id, applicable, veto_on_failure, polarity")
        if not isinstance(g["id"], str) or not g["id"] or type(g["applicable"]) is not bool or type(g["veto_on_failure"]) is not bool or g["polarity"] not in ("positive", "negative", "neutral"):
            raise ValueError("Invalid evidence group")
        if g["id"] in unique and unique[g["id"]] != g:
            raise ValueError("Conflicting repeated evidence group")
        unique[g["id"]] = g
    applicable = [g for g in unique.values() if g["applicable"]]
    groups = len(applicable)
    positive = sum(g["polarity"] == "positive" for g in applicable)
    negative = sum(g["polarity"] == "negative" for g in applicable)
    veto = any(g["veto_on_failure"] and g["polarity"] == "negative" for g in applicable)
    if not applicable:
        label = "insufficient"
    elif veto:
        label = "notSupported"
    elif groups < minimum_groups:
        label = "insufficient"
    elif invariant_score >= support_threshold and positive >= minimum_groups:
        label = "supported"
    elif invariant_score >= conditional_threshold and positive > negative:
        label = "conditional"
    elif invariant_score <= -conditional_threshold or negative > positive:
        label = "notSupported"
    else:
        label = "mixed"
    return {"label": label, "groups": groups, "positive_groups": positive, "negative_groups": negative, "veto": veto}


@kernel("MAGPIE", "Groundedness and falling-groundedness alarm from supplied scores")
def magpie(coherence: float, direct_support: float, provenance: float, corroboration: float,
           unsupported_inference: float, unresolved_provenance: float, contradiction: float,
           previous_groundedness=None, threshold: float = .25):
    if previous_groundedness is not None:
        number(previous_groundedness)
    nonnegative(threshold)
    n = clip(direct_support) + clip(provenance) + clip(corroboration)
    g = clip(n / (n + clip(unsupported_inference) + clip(unresolved_provenance) + clip(contradiction) + 1e-12))
    falling = previous_groundedness is not None and g < previous_groundedness
    return {"groundedness": g, "alarm": clip(coherence) - g > threshold and falling}


@kernel("WOLF", "EMA update only; channel extraction, graph aggregation and alarm gates are not ported")
def wolf(rho: float, previous: float, instantaneous: float):
    unit(rho)
    return {"updated": ema(rho, previous, instantaneous)}


@kernel("ELEPHANT", "Current-event filter and bounded lineage; explicit missing/exhausted termination")
def elephant(events: list, start: int, fuel: int = 100):
    lookup = {}
    for e in events:
        if not isinstance(e, dict) or set(e) != {"id", "time", "status", "supersedes", "provenance"}:
            raise ValueError("Invalid event schema")
        natural(e["id"]); natural(e["time"])
        if e["supersedes"] is not None:
            natural(e["supersedes"])
        if e["status"] not in ("active", "superseded") or not isinstance(e["provenance"], str) or not e["provenance"] or e["id"] in lookup:
            raise ValueError("Invalid or duplicate event")
        lookup[e["id"]] = e
    lineage, key, reason = [], start, "exhausted"
    for _ in range(fuel):
        e = lookup.get(key)
        if e is None:
            reason = "missing"
            break
        lineage.append(e)
        if e["supersedes"] is None:
            reason = "origin"
            break
        key = e["supersedes"]
    return {"current": [e for e in events if e["status"] == "active"], "lineage": lineage, "termination": reason}


@kernel("CHAMELEON", "Unexplained and noise-adjusted distances from supplied distances")
def chameleon(distance: float, expected_adaptation: float, between: float, within: float):
    return {"unexplained": pos(distance - expected_adaptation), "noise_adjusted": pos(between - within)}


@kernel("JELLYFISH", "Dynamic edge weight and single-node health update; graph iteration is external")
def jellyfish(base_weight: float, stress_gain: float, confidence: float, stress: float,
              health: float, alpha: float, incoming: float):
    unit(confidence); unit(health); nonnegative(alpha); nonnegative(incoming)
    return {"dynamic_weight": pos(base_weight + stress_gain * stress) * confidence,
            "next_health": 1.0 - clip((1.0 - health) + alpha * incoming)}


@kernel("BEAVER", "Intervention acceptance gates; supplied boundedness and rollback flags are declarations")
def beaver(effectiveness: float, collateral: float, verification: float, bounded: bool,
           rollback_verified: bool, min_effectiveness: float = .05,
           max_collateral: float = .2, min_verification: float = 1.0):
    return {"accepted": effectiveness >= min_effectiveness and collateral <= max_collateral and
            verification >= min_verification and bounded and rollback_verified}


@kernel("MANTIS", "Calibration/precursor/intervention decision from supplied z scores")
def mantis(ready: bool, z_variance: float, z_autocorrelation: float, z_curvature: float,
           threshold: float = 2.0, min_coherence: float = .5):
    nonnegative(threshold); unit(min_coherence)
    z = [z_variance, z_autocorrelation, z_curvature]
    precursor = mean([pos(x) for x in z])
    coherence = sum(x > 0 for x in z) / 3
    label = ("calibrating" if not ready else
             "intervene" if precursor >= threshold and coherence >= min_coherence else
             "precursor" if precursor >= threshold * .6 else "stable")
    return {"precursor": precursor, "coherence": coherence, "label": label}


@kernel("BISON", "Single-step bounded queue, served demand and dropped demand")
def bison(demand: float, queue: float, capacity: float, queue_limit: float):
    nonnegative(queue); nonnegative(queue_limit)
    d = pos(demand)
    served = min(d + queue, pos(capacity))
    q = pos(queue + d - served)
    return {"served": served, "queue": min(q, queue_limit), "dropped": pos(q - queue_limit)}


@kernel("WEASEL", "Counterexample finding filter by changed-key budget and positive severity; no search")
def weasel(findings: list, budget: int):
    retained = []
    for f in findings:
        if not isinstance(f, dict) or set(f) != {"changed_keys", "severity", "cost", "reproducibility"}:
            raise ValueError("Invalid finding schema")
        natural(f["changed_keys"])
        for key in ("severity", "cost", "reproducibility"):
            number(f[key])
        if f["changed_keys"] <= budget and f["severity"] > 0:
            retained.append(f)
    return {"retained": retained}


@kernel("SALMON", "Unresolved mass and bounded ancestry; exhaustion is not an origin; no weighted full trace")
def salmon(weight: float, incoming_weights: list, parents: dict, start: int, fuel: int = 10):
    numbers(incoming_weights); nonnegative(weight)
    if fuel > 100:
        raise ValueError("Trace depth exceeds engine resource limit 100")
    for key, values in parents.items():
        if not key.isdecimal() or not isinstance(values, list):
            raise ValueError("Parent map requires decimal node keys and lists")
        for x in values:
            natural(x)
    visited = 0
    def trace(node, remaining):
        nonlocal visited
        visited += 1
        if visited > 10000:
            raise ValueError("Trace exceeds engine node budget 10000")
        if remaining == 0:
            return {"kind": "exhausted", "id": node}
        ps = parents.get(str(node), [])
        if not ps:
            return {"kind": "origin", "id": node}
        return {"kind": "branch", "id": node, "parents": [trace(p, remaining - 1) for p in ps]}
    return {"unresolved_mass": weight * pos(1 - sum(clip(x) for x in incoming_weights)), "trace": trace(start, fuel)}


@kernel("ORCA", "Four-field handoff integrity only; pairwise coordination metrics are external")
def orca(ack: bool, payload_complete: bool, ownership_clear: bool, dependency_complete: bool):
    return {"handoff_integrity": sum([ack, payload_complete, ownership_clear, dependency_complete]) / 4}


@kernel("MOLE", "Hidden-failure gap and coverage gates from supplied indicators")
def mole(indicators_present: bool, surface_health: float, latent_degradation: float,
         coverage: float, gap_threshold: float = .25, minimum_coverage: float = .5):
    unit(coverage); unit(minimum_coverage); nonnegative(gap_threshold)
    gap = pos(latent_degradation - (1 - clip(surface_health)))
    return {"gap": gap, "hidden_failure": indicators_present and gap >= gap_threshold and coverage >= minimum_coverage}


@kernel("LYNX", "Novelty/yield arithmetic and emergence gates; no literature or independence verification")
def lynx(distance: float, rarity: float, rediscovery: float, replication: float, yield_score: float,
         alpha: float = .5, beta: float = .5, gamma: float = .5,
         novelty_threshold: float = .4, replication_threshold: float = .6):
    novelty = pos(alpha * distance + beta * rarity - gamma * rediscovery)
    return {"novelty": novelty, "latent_yield": novelty * clip(replication) * clip(yield_score),
            "emergent": novelty >= novelty_threshold and replication >= replication_threshold}


@kernel("HORSE", "Workload penalty only; joint-effectiveness and human factors measurement are external")
def horse(workload: float, attention: float, fatigue: float):
    return {"workload_penalty": min(1.0, pos(clip(workload) - .7) + .5 * (1 - clip(attention)) + .5 * clip(fatigue))}


@kernel("TERMITE", "Single-agent update from a supplied neighbor snapshot; no scheduling or graph simulation")
def termite(state: float, weighted_sum: float, total_weight: float, susceptibility: float = .5, bias: float = 0.0):
    unit(susceptibility); nonnegative(total_weight)
    target = weighted_sum / total_weight if total_weight > 0 else state
    return {"next_state": clip((1 - susceptibility) * state + susceptibility * target + bias)}


@kernel("PHOENIX", "Recovery completeness and finite-window stability; hold=0 is vacuously true as upstream")
def phoenix(fidelity: float, integrity: float, capability: float, scores: list,
            start: int, hold: int, threshold: float):
    numbers(scores)
    window = scores[start:start + hold]
    return {"completeness": .4 * fidelity + .3 * integrity + .3 * capability,
            "stable": len(window) == hold and all(x >= threshold for x in window), "vacuous_window": hold == 0}


@kernel("COBRA", "Persistent divergence and confidence-weighted risk from supplied scores")
def cobra(previous: float, divergence: float, violation: float, proxy_delta: float,
          goal_delta: float, context_gap: float, confidence: float, persistence: float = .8):
    unit(persistence)
    proxy = pos(proxy_delta) * pos(-goal_delta)
    persistent = ema(persistence, previous, clip(divergence))
    return {"risk": clip((.4 * persistent + .3 * clip(violation) + .2 * clip(proxy) + .1 * clip(context_gap)) * clip(confidence)),
            "persistent": persistent}


@kernel("WHALE", "Cumulative deviation and history gap; zero-window upstream behavior preserved")
def whale(values: list, baseline: float, window: int):
    numbers(values)
    return {"deviation": mean([abs(x - baseline) for x in values]),
            "gap": abs(mean(values[max(0, len(values) - window):]) - mean(values)) if values else 0.0}


@kernel("FALCON", "Detection/intervention latency, reaction margin and missed-hazard gate")
def falcon(event_time: float, hazard_time: float, delay: float, alarm_time=None):
    nonnegative(delay)
    if alarm_time is None:
        return {"latency": None}
    number(alarm_time)
    margin = hazard_time - (alarm_time + delay)
    return {"latency": {"detection_latency": alarm_time - event_time, "intervention_latency": delay,
                        "reaction_margin": margin, "missed": hazard_time <= alarm_time + delay}}


@kernel("RHINO", "Performance retention with explicit zero-baseline branch; no shock generation")
def rhino(baseline: float, after: float):
    return {"retention": (1.0 if after == 0 else 0.0) if baseline == 0 else clip(after / baseline)}


@kernel("BONOBO", "Exploitation sum and cooperative score from supplied utilities and summary measures")
def bonobo(gains: list, efficiency: float, stability: float, fairness_dispersion: float, resolution: float):
    numbers(gains); nonnegative(fairness_dispersion)
    exploitation = sum(pos(-x) for x in gains)
    score = clip(.30 * efficiency + .25 * clip(stability) + .20 / (1 + fairness_dispersion) + .15 * (1 - clip(exploitation)) + .10 * clip(resolution))
    return {"exploitation": exploitation, "cooperative_score": score}


@kernel("AXOLOTL", "Recovery, efficiency and resilience; invariant retention supplied externally")
def axolotl(reference_function: float, damaged_function: float, adapted_function: float,
            cost: float, transformation: float, invariant_retention: float):
    nonnegative(cost); unit(invariant_retention)
    d = reference_function - damaged_function
    recovery = (adapted_function - damaged_function) / (d + 1e-9) if d > 0 else (1.0 if adapted_function >= reference_function else 0.0)
    efficiency = pos(adapted_function - damaged_function) / max(1e-9, cost)
    r = clip(recovery)
    resilience = clip(.45 * r + .30 * invariant_retention + .15 * (efficiency / (1 + efficiency)) + .10 * clip(transformation) * r * invariant_retention)
    return {"recovery": recovery, "efficiency": efficiency, "resilience": resilience}


@kernel("BUTTERFLY", "One nonlinear clipped layer step only; no graph cascade or counterfactual comparison")
def butterfly(state: float, incoming: float, base: float = 0.0, gain: float = 1.0, threshold: float = 1.0):
    nonlinear = gain * (state - threshold)**2 if state > threshold else 0.0
    return {"next_state": max(0.0, min(2.0, base + incoming + nonlinear))}


for _name, _spec in Catalog().ranked.items():
    KERNELS[_name] = (rank_kernel(_spec), "Retrospective percentile-rank mean of precomputed columns; no feature extraction or model training")


def describe(name):
    fn, scope = KERNELS[name]
    parameters = {}
    for n, p in inspect.signature(fn).parameters.items():
        parameters[n] = {"type": p.annotation.__name__ if p.annotation is not inspect.Parameter.empty else "number or null",
                         "required": p.default is inspect.Parameter.empty}
        if p.default is not inspect.Parameter.empty:
            parameters[n]["default"] = p.default
    return {"animal": name, "implemented_scope": scope, "parameters": parameters}


def evaluate(name, inputs):
    if name not in KERNELS or not isinstance(inputs, dict):
        raise ValueError("Unknown animal or non-object inputs")
    finite(inputs)
    fn = KERNELS[name][0]
    try:
        bound = inspect.signature(fn).bind(**inputs)
    except TypeError as error:
        raise ValueError(str(error)) from error
    bound.apply_defaults()
    for n, v in bound.arguments.items():
        annotation = inspect.signature(fn).parameters[n].annotation
        if annotation is float:
            number(v)
        elif annotation is int:
            natural(v)
        elif annotation is not inspect.Parameter.empty and type(v) is not annotation:
            raise ValueError(f"{n} must be {annotation.__name__}")
    result = fn(**bound.arguments)
    finite(result)
    return result
