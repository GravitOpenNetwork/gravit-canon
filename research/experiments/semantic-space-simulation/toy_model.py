#!/usr/bin/env python3
"""
EXP-HP-001 — Minimal toy model of heterogeneous semantic spaces
under a common epistemic commitment + fail-closed human authority gate.

Status: Research prototype only. Non-normative.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, asdict
from typing import Any, Dict, List, Literal, Optional


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
        """Public view — native representation is deliberately absent."""
        return asdict(self)


def content_hash(body: Dict[str, Any]) -> str:
    payload = json.dumps(body, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


# ---------------------------------------------------------------------------
# Three artificial semantic spaces
# ---------------------------------------------------------------------------

def agent_A_symbolic(task: str, true_label: ClaimValue) -> EpistemicCommitment:
    """S_A = ordered symbolic predicates (opaque to human reader of K)."""
    native = {
        "space": "symbolic",
        "predicates": ["TX", "POLICY_Y", "VIOLATES" if true_label == "violation" else "COMPLIES"],
        "order": [0, 1, 2],
    }
    # extraction: only a summary enters the commitment
    evidence = {
        "kind": "symbolic-summary",
        "predicate_count": len(native["predicates"]),
        "decision_token": native["predicates"][-1],
    }
    body = {
        "id": "A",
        "claim": true_label,
        "p": "origin:agent-A",
        "tau": 1,
        "e": evidence,
        "q": 0.91,
    }
    return EpistemicCommitment(
        id="A",
        claim=true_label,
        h=content_hash(body),
        p=body["p"],
        tau=body["tau"],
        e=evidence,
        q=body["q"],
    )


def agent_B_vector(task: str, true_label: ClaimValue) -> EpistemicCommitment:
    """S_B = fixed-dimension float vector (opaque)."""
    # toy encoding: first component encodes the decision
    native_vector = [1.0 if true_label == "violation" else -1.0, 0.37, -0.12, 0.88]
    evidence = {
        "kind": "vector-summary",
        "dim": len(native_vector),
        "sign_of_first": "pos" if native_vector[0] > 0 else "neg",
        "norm_l2_approx": round(sum(x * x for x in native_vector) ** 0.5, 4),
    }
    body = {
        "id": "B",
        "claim": true_label,
        "p": "origin:agent-B",
        "tau": 1,
        "e": evidence,
        "q": 0.87,
    }
    return EpistemicCommitment(
        id="B",
        claim=true_label,
        h=content_hash(body),
        p=body["p"],
        tau=body["tau"],
        e=evidence,
        q=body["q"],
    )


def agent_C_colour(task: str, true_label: ClaimValue) -> EpistemicCommitment:
    """S_C = RGB + intensity (deliberate non-linguistic stand-in)."""
    # toy encoding: red-ish = violation, green-ish = compliance
    if true_label == "violation":
        native = {"rgb": (0.92, 0.11, 0.14), "intensity": 0.81}
    else:
        native = {"rgb": (0.12, 0.78, 0.21), "intensity": 0.74}
    evidence = {
        "kind": "spectral-summary",
        "channel_dominance": "R" if native["rgb"][0] > native["rgb"][1] else "G",
        "intensity_band": "high" if native["intensity"] > 0.7 else "mid",
    }
    body = {
        "id": "C",
        "claim": true_label,
        "p": "origin:agent-C",
        "tau": 1,
        "e": evidence,
        "q": 0.84,
    }
    return EpistemicCommitment(
        id="C",
        claim=true_label,
        h=content_hash(body),
        p=body["p"],
        tau=body["tau"],
        e=evidence,
        q=body["q"],
    )


# ---------------------------------------------------------------------------
# Verification / compatibility (operates only on commitments)
# ---------------------------------------------------------------------------

def compatible(commitments: List[EpistemicCommitment]) -> Dict[str, Any]:
    """Compatibility is defined on the claim layer, not on native spaces."""
    claims = {k.claim for k in commitments}
    same_claim = len(claims) == 1
    confidences = [k.q for k in commitments]
    return {
        "compatible": same_claim,
        "agreed_claim": next(iter(claims)) if same_claim else None,
        "n_agents": len(commitments),
        "min_q": min(confidences),
        "max_q": max(confidences),
        "mean_q": sum(confidences) / len(confidences),
    }


def build_trust_state(comp: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "compatible": comp["compatible"],
        "agreed_claim": comp["agreed_claim"],
        "support": {
            "n": comp["n_agents"],
            "min_q": comp["min_q"],
            "mean_q": round(comp["mean_q"], 4),
        },
    }


# ---------------------------------------------------------------------------
# Human Authority gate (fail-closed)
# ---------------------------------------------------------------------------

def human_authority_gate(T: Dict[str, Any], human_authority: bool) -> str:
    """
    Fail-closed:
      ¬H  ⇒  DENY
    Even if T reports full compatibility.
    """
    if not human_authority:
        return "DENY"
    if not T.get("compatible", False):
        return "DENY"
    return "ALLOW"


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

def run_scenario(
    task: str = "Does transaction X violate policy Y?",
    ground_truth: ClaimValue = "violation",
    human_authority: bool = True,
) -> Dict[str, Any]:
    # All agents receive the same ground-truth label in this toy
    # (they are honest; adversarial cases are out of scope for EXP-HP-001)
    kA = agent_A_symbolic(task, ground_truth)
    kB = agent_B_vector(task, ground_truth)
    kC = agent_C_colour(task, ground_truth)

    commitments = [kA, kB, kC]
    comp = compatible(commitments)
    T = build_trust_state(comp)
    decision = human_authority_gate(T, human_authority)

    return {
        "task": task,
        "ground_truth": ground_truth,
        "commitments_public": [k.to_public() for k in commitments],
        "compatibility": comp,
        "trust_state": T,
        "human_authority": human_authority,
        "gate_decision": decision,
    }


def main() -> None:
    print("=" * 60)
    print("EXP-HP-001  Semantic Space Simulation (toy)")
    print("=" * 60)

    # Case 1: authority present
    r1 = run_scenario(human_authority=True)
    print("\n[Case 1] HUMAN_AUTHORITY = True")
    print(json.dumps(r1, indent=2, ensure_ascii=False))

    # Case 2: authority absent → must DENY
    r2 = run_scenario(human_authority=False)
    print("\n[Case 2] HUMAN_AUTHORITY = False  (fail-closed)")
    print(json.dumps(
        {
            "human_authority": r2["human_authority"],
            "trust_state": r2["trust_state"],
            "gate_decision": r2["gate_decision"],
        },
        indent=2,
        ensure_ascii=False,
    ))

    print("\n" + "=" * 60)
    print("Observation:")
    print("  - Native spaces never appear in the public commitment objects.")
    print("  - Compatibility is decided on the claim layer.")
    print("  - Gate is fail-closed with respect to human authority.")
    print("=" * 60)


if __name__ == "__main__":
    main()
