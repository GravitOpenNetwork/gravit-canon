# EXP-HP-001 — Semantic Space Simulation

**Status:** Scaffold + minimal executable prototype  
**Normative force:** None  
**Parent documents:** HP-0001, HP-0002 v0.2, HP-0003  
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

## Execution Flow (toy)

```
Task
  |
  |─► Agent A (symbolic)  ──ext_A──► K_A
  |─► Agent B (vector)    ──ext_B──► K_B
  |└► Agent C (colour)    ──ext_C──► K_C
                |
                ▼
         Compatibility check
         (same claim value + optional confidence band)
                |
                ▼
         Trust state T  (simple aggregate)
                |
                ▼
         Human Authority gate
                |
        ┌───────┬───────┐
        |               |
     ALLOW            DENY
   (only if H=True)
```

---

## Fail-Closed Gate

```python
def human_authority_gate(T, H):
    if not H:
        return "DENY"
    # additional policy checks may be added
    return "ALLOW" if T["compatible"] else "DENY"
```

If the human-authority flag is absent or false, execution is refused regardless of validator agreement.

---

## Files in this directory

| File | Role |
|------|------|
| `README.md` | this document |
| `toy_model.py` | minimal executable prototype |
| `run_example.sh` | convenience runner |

---

## How to run

```bash
cd research/experiments/semantic-space-simulation
python3 toy_model.py
```

Expected behaviour:

- three commitments are printed (native forms remain opaque to the human reader);
- compatibility is reported;
- when `HUMAN_AUTHORITY = False` the gate returns DENY;
- when `HUMAN_AUTHORITY = True` and claims agree, the gate returns ALLOW.

---

## Success criteria (research)

1. Native representations stay non-interpretable to a human reader of the commitment objects.
2. Compatibility can still be decided from the commitment layer.
3. Fail-closed behaviour is observable by toggling the human-authority flag.

---

## Non-claims

- This is not a simulation of real multi-agent AI systems.
- Colour space is a deliberate toy stand-in, not a claim about perceptual AI.
- No performance, security or scalability claims are made.

---

**Status:** Scaffold + first executable prototype.  
