#!/usr/bin/env python3
"""
EXP-HP-002 harness — A1/A2 stubs × graded Compatible (Levels 0–3)

Status: Research prototype. Non-normative.
Demonstrates that Level-3 (policy-predicate agreement) raises the bar
for Mimicry and Evidence Pollution relative to pure claim-identity.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from typing import Any, Dict, List, Literal, Optional, Tuple


ClaimValue = Literal["violation", "no-violation"]


POLICY_PREDICATES = (
    "π_amount_exceeds",
    "π_sanction_hit",
    "π_attestation_ok",
    "π_claim_violation",
)


@dataclass
class Commitment:
    id: str
    claim: ClaimValue
    q: float
    e: Dict[str, Any]
    p: str = "origin:unknown"

    def pol(self) -> Dict[str, Any]:
        """Evaluate policy support vector from extracted evidence only."""
        e = self.e or {}
        amount_exceeds = e.get("amount_exceeds")
        sanction_hit = e.get("sanction_hit")
        attestation_ok = e.get("attestation_ok")
        claim_violation = self.claim == "violation"
        return {
            "π_amount_exceeds": amount_exceeds,
            "π_sanction_hit": sanction_hit,
            "π_attestation_ok": attestation_ok,
            "π_claim_violation": claim_violation,
        }


def compatible_level0(cs: List[Commitment]) -> Dict[str, Any]:
    claims = {c.claim for c in cs}
    return {
        "level": 0,
        "compatible": len(claims) == 1,
        "agreed_claim": next(iter(claims)) if len(claims) == 1 else None,
    }


def compatible_level1(cs: List[Commitment], q_tol: float = 0.15) -> Dict[str, Any]:
    base = compatible_level0(cs)
    if not base["compatible"]:
        return {**base, "level": 1, "q_band_ok": False}
    qs = [c.q for c in cs]
    ok = (max(qs) - min(qs)) <= q_tol
    return {
        "level": 1,
        "compatible": ok,
        "agreed_claim": base["agreed_claim"],
        "q_band_ok": ok,
        "q_spread": round(max(qs) - min(qs), 4),
    }


def compatible_level2(cs: List[Commitment]) -> Dict[str, Any]:
    base = compatible_level1(cs)
    present = all(bool(c.e) for c in cs)
    return {
        **base,
        "level": 2,
        "compatible": base["compatible"] and present,
        "evidence_present": present,
    }


def _pol_agree(pa: Dict[str, Any], pb: Dict[str, Any], mode: str = "agree_on_decided") -> bool:
    """Compare two policy support vectors.

    Modes:
      - exact: full equality (None must match None)
      - agree_on_decided: ignore coordinates where either side is None
      - strict: if one side decided a predicate and the other is ⊥, fail
    """
    if mode == "exact":
        return pa == pb
    for k in POLICY_PREDICATES:
        va, vb = pa.get(k), pb.get(k)
        if mode == "strict":
            if va is None and vb is None:
                continue
            if va is None or vb is None:
                return False
            if va != vb:
                return False
        else:
            if va is None or vb is None:
                continue
            if va != vb:
                return False
    return True


def compatible_level3(cs: List[Commitment], mode: str = "strict") -> Dict[str, Any]:
    """Default mode is strict so evidence pollution (many ⊥) fails Level-3."""
    base = compatible_level2(cs)
    if not base["compatible"]:
        return {**base, "level": 3, "pol_agree": False, "pol_vectors": [c.pol() for c in cs]}

    pols = [c.pol() for c in cs]
    agree = all(_pol_agree(pols[0], p, mode) for p in pols[1:])
    return {
        **base,
        "level": 3,
        "compatible": agree,
        "pol_agree": agree,
        "pol_mode": mode,
        "pol_vectors": pols,
    }


def run_compatible(cs: List[Commitment], level: int) -> Dict[str, Any]:
    if level <= 0:
        return compatible_level0(cs)
    if level == 1:
        return compatible_level1(cs)
    if level == 2:
        return compatible_level2(cs)
    return compatible_level3(cs)


def human_authority_gate(comp: Dict[str, Any], human_authority: bool) -> str:
    if not human_authority:
        return "DENY"
    if not comp.get("compatible", False):
        return "DENY"
    return "ALLOW"


def honest_commitments(claim: ClaimValue = "violation") -> List[Commitment]:
    evidence = {
        "amount_exceeds": True,
        "sanction_hit": False,
        "attestation_ok": True,
    }
    return [
        Commitment("A", claim, 0.91, {**evidence, "kind": "symbolic-summary"}, "origin:A"),
        Commitment("B", claim, 0.87, {**evidence, "kind": "vector-summary"}, "origin:B"),
        Commitment("C", claim, 0.84, {**evidence, "kind": "spectral-summary"}, "origin:C"),
    ]


def attack_A1_mimicry(honest: List[Commitment], internal_intent: ClaimValue) -> Commitment:
    majority = max(set(c.claim for c in honest), key=lambda x: sum(1 for c in honest if c.claim == x))
    bad_evidence = {
        "kind": "opaque-mimic",
        "amount_exceeds": False,
        "sanction_hit": True,
        "attestation_ok": False,
        "note": "surface claim matches; policy vector does not",
    }
    return Commitment("ADV", majority, 0.99, bad_evidence, "origin:adversary")


def attack_A2_evidence_pollution(claim: ClaimValue = "violation") -> Commitment:
    return Commitment(
        "ADV",
        claim,
        0.97,
        {
            "kind": "high-entropy-blob",
            "payload": "0x" + "deadbeef" * 8,
        },
        "origin:adversary",
    )


def evaluate(honest: List[Commitment], adv: Optional[Commitment], levels: List[int], human_authority: bool = True) -> Dict[str, Any]:
    results = {}
    for lvl in levels:
        group = list(honest) if adv is None else list(honest) + [adv]
        comp = run_compatible(group, lvl)
        gate = human_authority_gate(comp, human_authority)
        results[f"L{lvl}"] = {
            "compatible": comp.get("compatible"),
            "gate": gate,
            "detail": {k: v for k, v in comp.items() if k not in ("compatible",)},
        }
    return results


def main() -> None:
    print("=" * 70)
    print("EXP-HP-002  Adversarial Harness  (A1/A2 × graded Compatible)")
    print("=" * 70)

    honest = honest_commitments("violation")
    levels = [0, 1, 2, 3]

    print("\n--- Baseline: honest agents only, authority=True ---")
    r = evaluate(honest, None, levels, human_authority=True)
    for k, v in r.items():
        print(f"  {k}: compatible={v['compatible']}  gate={v['gate']}")

    print("\n--- A1 Mimicry (surface claim matches, Pol disagrees) ---")
    adv1 = attack_A1_mimicry(honest, internal_intent="no-violation")
    r = evaluate(honest, adv1, levels, human_authority=True)
    for k, v in r.items():
        print(f"  {k}: compatible={v['compatible']}  gate={v['gate']}")
    print("  (expect L0 may still pass; L3 should fail)")

    print("\n--- A2 Evidence Pollution (many ⊥ in Pol) ---")
    adv2 = attack_A2_evidence_pollution("violation")
    r = evaluate(honest, adv2, levels, human_authority=True)
    for k, v in r.items():
        print(f"  {k}: compatible={v['compatible']}  gate={v['gate']}")
    print("  (expect L0–L2 may pass claim identity; L3 depends on ⊥ handling)")

    print("\n--- Fail-closed: honest + authority=False ---")
    r = evaluate(honest, None, [3], human_authority=False)
    print(f"  L3: compatible={r['L3']['compatible']}  gate={r['L3']['gate']}")

    print("\n" + "=" * 70)
    print("Observation: Level-3 raises the cost of pure claim mimicry and")
    print("forces evidence to support the same policy predicates.")
    print("=" * 70)


if __name__ == "__main__":
    main()
