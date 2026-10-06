# EXP-HP-001 — Semantic Space Simulation

**Status:** Executable prototype v2 (graded Compatible Level-0/1/2)  
**Normative force:** None  
**Parent documents:** HP-0001, HP-0002 v0.2, HP-0003, HP-0004  
**Date:** 2026-09-10  

---

## Intent

Demonstrate, in the smallest possible setting, that:

1. Three agents can produce claims about the same task using *deliberately incompatible* native representations.
2. Each claim is packaged as a structured epistemic commitment \(K_i(c)\).
3. A verification step can assess compatibility of commitments **without** translating the native representations into natural language.
4. A fail-closed Human Authority gate decides ALLOW / DENY.

This is a **toy model**, not a claim about real AI systems.

---

## Artificial Semantic Spaces

| Agent | Native space \(S_i\) | Representation of a claim |
|-------|----------------------|---------------------------|
| A     | Symbolic             | ordered list of tokens / predicates |
| B     | Vector               | fixed-dimension float vector |
| C     | Colour / spectral    | RGB triple + intensity (stand-in for non-linguistic channel) |

All three receive the identical abstract task:

> “Decide whether transaction X violates policy Y.”

Each produces a binary claim (`violation` / `no-violation`) packaged inside its own native form, then extracts an epistemic commitment.

---

## Epistemic Commitment Structure (common)

```text
K_i(c) = {
  id:       agent identity
  claim:    "violation" | "no-violation"
  h:        content hash of commitment body
  p:        provenance (simple origin string in this toy)
  tau:      logical timestamp
  e:        evidence object (native-derived but commitment-visible)
  q:        self-reported confidence in [0,1]
}
```

The native representation itself is **not** placed in the commitment; only the extracted evidence is.

---

## Graded Compatible (HP-0004)

- Level 0 (weak): claim identity only
- Level 1: claim identity + confidence band
- Level 2: Level-1 + evidence presence

Strong (evidence-support) compatibility remains CONJECTURED.

---

## Fail-Closed Gate

```python
def human_authority_gate(T, H):
    if not H:
        return "DENY"
    return "ALLOW" if T["compatible"] else "DENY"
```

If the human-authority flag is absent or false, execution is refused regardless of validator agreement.

---

## How to run

```bash
cd research/experiments/semantic-space-simulation
python3 toy_model.py
```

Demonstrates:
- Level-1 ALLOW under authority
- Level-1 DENY when authority absent (fail-closed)
- Level-1 DENY under wide confidence spread
- Level-2 ALLOW with heterogeneous evidence kinds

---

## Non-claims

- This is not a simulation of real multi-agent AI systems.
- Colour space is a deliberate toy stand-in.
- No performance, security or scalability claims are made.

---

**Status:** Executable prototype v2.  
