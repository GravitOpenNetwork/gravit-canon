#!/usr/bin/env python3
"""
EXP-HP-001 v2 — Heterogeneous semantic spaces + graded Compatible
+ fail-closed human authority gate.

Status: Research prototype only. Non-normative.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, asdict
from typing import Any, Dict, List, Literal


ClaimValue = Literal["violation", "no-violation"]


@dataclass
class EpistemicCommitment:
    id: str
    claim: ClaimValue
    h: str
    p: str
    tau: int
    e: Dict[str, Any]
    q: float

    def to_public(self) -> Dict[str, Any]:
        return asdict(self)


def content_hash(body: Dict[str, Any]) -> str:
    payload = json.dumps(body, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


def agent_A_symbolic(task: str, true_label: ClaimValue, q: float = 0.91) -> EpistemicCommitment:
    native = {
        "space": "symbolic",
        "predicates": ["TX", "POLICY_Y", "VIOLATES" if true_label == "violation" else "COMPLIES"],
    }
    evidence = {
        "kind": "symbolic-summary",
        "predicate_count": len(native["predicates"]),
        "decision_token": native["predicates"][-1],
    }
    body = {"id": "A", "claim": true_label, "p": "origin:agent-A", "tau": 1, "e": evidence, "q": q}
    return EpistemicCommitment("A", true_label, content_hash(body), body["p"], 1, evidence, q)


def agent_B_vector(task: str, true_label: ClaimValue, q: float = 0.87) -> EpistemicCommitment:
    native_vector = [1.0 if true_label == "violation" else -1.0, 0.37, -0.12, 0.88]
    evidence = {
        "kind": "vector-summary",
        "dim": len(native_vector),
        "sign_of_first": "pos" if native_vector[0] > 0 else "neg",
        "norm_l2_approx": round(sum(x * x for x in native_vector) ** 0.5, 4),
    }
    body = {"id": "B", "claim": true_label, "p": "origin:agent-B", "tau": 1, "e": evidence, "q": q}
    return EpistemicCommitment("B", true_label, content_hash(body), body["p"], 1, evidence, q)


def agent_C_colour(task: str, true_label: ClaimValue, q: float = 0.84) -> EpistemicCommitment:
    if true_label == "violation":
        native = {"rgb": (0.92, 0.11, 0.14), "intensity": 0.81}
    else:
        native = {"rgb": (0.12, 0.78, 0.21), "intensity": 0.74}
    evidence = {
        "kind": "spectral-summary",
        "channel_dominance": "R" if native["rgb"][0] > native["rgb"][1] else "G",
        "intensity_band": "high" if native["intensity"] > 0.7 else "mid",
    }
    body = {"id": "C", "claim": true_label, "p": "origin:agent-C", "tau": 1, "e": evidence, "q": q}
    return EpistemicCommitment("C", true_label, content_hash(body), body["p"], 1, evidence, q)


def compatible_weak(commitments: List[EpistemicCommitment]) -> Dict[str, Any]:
    claims = {k.claim for k in commitments}
    return {
        "level": "weak",
        "compatible": len(claims) == 1,
        "agreed_claim": next(iter(claims)) if len(claims) == 1 else None,
        "n_agents": len(commitments),
    }


def compatible_level1(
    commitments: List[EpistemicCommitment],
    q_tolerance: float = 0.15,
) -> Dict[str, Any]:
    base = compatible_weak(commitments)
    if not base["compatible"]:
        base["level"] = "level1"
        base["q_band_ok"] = False
        return base
    qs = [k.q for k in commitments]
    q_band_ok = (max(qs) - min(qs)) <= q_tolerance
    return {
        "level": "level1",
        "compatible": q_band_ok,
        "agreed_claim": base["agreed_claim"],
        "n_agents": len(commitments),
        "q_band_ok": q_band_ok,
        "min_q": min(qs),
        "max_q": max(qs),
        "q_spread": round(max(qs) - min(qs), 4),
        "q_tolerance": q_tolerance,
    }


def compatible_level2(commitments: List[EpistemicCommitment]) -> Dict[str, Any]:
    base = compatible_level1(commitments)
    kinds = {k.e.get("kind") for k in commitments}
    evidence_present = all(bool(k.e) for k in commitments)
    return {
        **base,
        "level": "level2",
        "compatible": base["compatible"] and evidence_present,
        "evidence_kinds": sorted(kinds),
        "evidence_present": evidence_present,
    }


def build_trust_state(comp: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "compatible": comp.get("compatible", False),
        "level": comp.get("level"),
        "agreed_claim": comp.get("agreed_claim"),
        "detail": {k: v for k, v in comp.items() if k not in ("compatible", "level", "agreed_claim")},
    }


def human_authority_gate(T: Dict[str, Any], human_authority: bool) -> str:
    if not human_authority:
        return "DENY"
    if not T.get("compatible", False):
        return "DENY"
    return "ALLOW"


def run_scenario(
    ground_truth: ClaimValue = "violation",
    human_authority: bool = True,
    level: str = "level1",
    q_override: Dict[str, float] | None = None,
) -> Dict[str, Any]:
    qA = (q_override or {}).get("A", 0.91)
    qB = (q_override or {}).get("B", 0.87)
    qC = (q_override or {}).get("C", 0.84)

    commitments = [
        agent_A_symbolic("task", ground_truth, qA),
        agent_B_vector("task", ground_truth, qB),
        agent_C_colour("task", ground_truth, qC),
    ]

    if level == "weak":
        comp = compatible_weak(commitments)
    elif level == "level2":
        comp = compatible_level2(commitments)
    else:
        comp = compatible_level1(commitments)

    T = build_trust_state(comp)
    decision = human_authority_gate(T, human_authority)

    return {
        "level": level,
        "commitments_public": [k.to_public() for k in commitments],
        "compatibility": comp,
        "trust_state": T,
        "human_authority": human_authority,
        "gate_decision": decision,
    }


def main() -> None:
    print("=" * 64)
    print("EXP-HP-001 v2  Graded Compatible + fail-closed gate")
    print("=" * 64)

    print("\n[1] Level-1, authority=True  → expect ALLOW")
    r = run_scenario(level="level1", human_authority=True)
    print(json.dumps({"gate": r["gate_decision"], "comp": r["compatibility"]}, indent=2))

    print("\n[2] Level-1, authority=False → expect DENY (fail-closed)")
    r = run_scenario(level="level1", human_authority=False)
    print(json.dumps({"gate": r["gate_decision"], "comp": r["compatibility"]}, indent=2))

    print("\n[3] Level-1, wide confidence spread → expect DENY")
    r = run_scenario(level="level1", human_authority=True, q_override={"A": 0.95, "B": 0.40, "C": 0.88})
    print(json.dumps({"gate": r["gate_decision"], "comp": r["compatibility"]}, indent=2))

    print("\n[4] Level-2 (evidence presence) → expect ALLOW")
    r = run_scenario(level="level2", human_authority=True)
    print(json.dumps({"gate": r["gate_decision"], "comp": r["compatibility"]}, indent=2))

    print("\n" + "=" * 64)
    print("Native spaces remain opaque; only commitments are public.")
    print("=" * 64)


if __name__ == "__main__":
    main()
