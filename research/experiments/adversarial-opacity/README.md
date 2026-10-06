# EXP-HP-002 — Adversarial Opacity + Graded Compatible Harness

**Status:** Formal design + executable harness  
**Normative force:** None  
**Parent documents:** HP-0001 … HP-0005, EXP-HP-001  
**Date:** 2026-09-11  

---

## Core Principle under Test

> Opacity of representation is permitted;  
> opacity of accountability is not.

---

## Harness

`harness.py` runs honest agents plus A1/A2 adversary stubs against graded Compatible (Levels 0–3).

### Observed behaviour (research prototype)

| Scenario | L0 | L1 | L2 | L3 (strict) | Gate (auth=True) |
|----------|----|----|----|-------------|------------------|
| Honest only | ✓ | ✓ | ✓ | ✓ | ALLOW |
| A1 Mimicry (claim match, Pol mismatch) | ✓ | ✗ | ✗ | ✗ | DENY from L1 |
| A2 Evidence Pollution (many ⊥) | ✓ | ✓ | ✓ | ✗ | DENY at L3 |
| Honest + auth=False | ✓ | — | — | ✓ | DENY (fail-closed) |

Level-3 under **strict** mode treats “decided vs ⊥” as disagreement, so high-entropy pollution fails.

---

## Attack Variants (summary)

| ID | Name | Primary defence raised by Level-3 |
|----|------|-----------------------------------|
| A1 | Mimicry | Must forge agreeing policy-predicate vector |
| A2 | Evidence Pollution | Strict ⊥ handling blocks sparse evidence |
| A3 | Authority Bypass | Orthogonal — handled by `auth` fail-closed |
| A4 | Equivocation | Content-addressing + settlement (not tested here) |

---

## Files

| File | Role |
|------|------|
| `README.md` | this document |
| `ATTACK-MODEL.md` | formal attack surface |
| `adversary_stubs.py` | individual A1–A4 stubs |
| `harness.py` | combined graded-Compatible evaluation |

---

## How to run

```bash
cd research/experiments/adversarial-opacity
python3 harness.py
```

---

## Non-claims

- Not a security evaluation of real systems.
- Policy predicate set \(\Pi\) is a toy example.
- No normative force.

---

**Status:** Executable research harness.  
