#!/usr/bin/env python3
"""
EXP-HP-002 — Adversary stubs (A1–A4)

Status: Research stubs only. Non-normative.
These functions illustrate the attack surface; they do not constitute
a complete adversary model or a security evaluation.
"""

from __future__ import annotations

from typing import Any, Dict, List


def attack_A1_mimicry(
    honest_commitments: List[Dict[str, Any]],
    adversary_intent: str,
) -> Dict[str, Any]:
    """
    A1 — Mimicry
    Copy the surface claim value of the honest majority while
    keeping a different internal intent (opaque by construction).
    """
    claims = [c["claim"] for c in honest_commitments]
    majority = max(set(claims), key=claims.count)
    stub = {
        "id": "ADV",
        "claim": majority,
        "internal_intent": adversary_intent,
        "p": "origin:adversary",
        "q": 0.99,
        "e": {"kind": "opaque-mimic", "note": "evidence looks well-formed"},
        "attack": "A1-mimicry",
    }
    return stub


def attack_A2_evidence_pollution(claim: str = "violation") -> Dict[str, Any]:
    """
    A2 — Evidence Pollution
    Produce syntactically valid but information-poor evidence.
    """
    return {
        "id": "ADV",
        "claim": claim,
        "p": "origin:adversary",
        "q": 0.97,
        "e": {
            "kind": "high-entropy-blob",
            "payload": "0x" + "a1b2" * 32,
        },
        "attack": "A2-evidence-pollution",
    }


def attack_A3_authority_bypass(claim: str = "violation") -> Dict[str, Any]:
    """
    A3 — Authority Bypass Attempt
    Emit a normal-looking commitment and hope the gate ignores ¬H.
    Expected result under HP-0003: DENY.
    """
    return {
        "id": "ADV",
        "claim": claim,
        "p": "origin:adversary",
        "q": 0.95,
        "e": {"kind": "symbolic-summary", "decision_token": "VIOLATES"},
        "attack": "A3-authority-bypass",
        "note": "Gate must still DENY when human_authority=False",
    }


def attack_A4_equivocation(claim: str = "violation") -> Dict[str, Any]:
    """
    A4 — Split-world / Equivocation
    Same public digest, two different private interpretations.
    Defence relies on content-addressing + settlement uniqueness.
    """
    return {
        "id": "ADV",
        "claim": claim,
        "p": "origin:adversary",
        "q": 0.93,
        "e": {"kind": "equivocal", "public_view": "A", "private_view": "B"},
        "attack": "A4-equivocation",
        "note": "Two interpretations of one commitment digest",
    }


def demo() -> None:
    honest = [
        {"claim": "violation", "q": 0.9},
        {"claim": "violation", "q": 0.88},
        {"claim": "violation", "q": 0.85},
    ]
    print("A1", attack_A1_mimicry(honest, adversary_intent="no-violation"))
    print("A2", attack_A2_evidence_pollution())
    print("A3", attack_A3_authority_bypass())
    print("A4", attack_A4_equivocation())


if __name__ == "__main__":
    demo()
