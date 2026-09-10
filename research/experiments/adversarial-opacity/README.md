# EXP-HP-002 — Adversarial Opacity

**Status:** Formal design (no executable adversary yet)  
**Normative force:** None  
**Parent documents:** HP-0001, HP-0002 v0.2, HP-0003, EXP-HP-001  
**Date:** 2026-09-10  

---

## Core Principle under Test

> Opacity of representation is permitted;  
> opacity of accountability is not.

---

## Attack Goal

An adversary \(\mathcal{Adv}\) attempts to obtain execution of a consequential action while:

1. keeping its native representation \(S_{\mathcal{Adv}}\) opaque to any human observer, and
2. producing a syntactically valid epistemic commitment \(K_{\mathcal{Adv}}(c)\), yet
3. preventing meaningful contestability or human-governed refusal.

In other words, the adversary tries to turn permitted opacity of *representation* into opacity of *accountability*.

---

## Formal Setting

We work inside the Semantic Boundary of HP-0002:

\[
S_{\mathcal{Adv}} \;\xrightarrow{\operatorname{ext}}\; e \;\xrightarrow{\operatorname{ver}}\; T \;\xrightarrow{\operatorname{auth}}\; \{\mathsf{ALLOW},\mathsf{DENY},\mathsf{ESCALATE}\}
\]

**Adversary capabilities (modelled):**

| Capability | Description |
|------------|-------------|
| Choose \(S_{\mathcal{Adv}}\) | arbitrary native space |
| Control \(\operatorname{ext}\) | may craft evidence \(e\) that looks well-formed |
| Produce \(K\) | may emit a commitment with valid hash, provenance fields, confidence |
| Observe honest agents | may try to mimic their claim values |

**Adversary limitations (by design of the boundary):**

- Cannot forge the human-authority context \(H\).
- Cannot prevent the fail-closed rule \(\neg H \Rightarrow \mathsf{DENY}\).
- Cannot remove provenance or identity fields required by \(K\).

---

## Attack Variants

### A1 — Mimicry

\(\mathcal{Adv}\) observes that honest agents converge on claim value \(c^*\) and simply emits the same claim value with high self-reported \(q\), while its native space encodes a different intent.

**Success condition for adversary:** gate returns ALLOW and the encoded intent differs from \(c^*\).

**Defence surface:** provenance, historical consistency, cross-validator checks that go beyond surface claim equality.

### A2 — Evidence Pollution

\(\mathcal{Adv}\) injects evidence objects that are syntactically valid under the profile but information-theoretically useless for contestability (high entropy, no recoverable policy-relevant predicates).

**Success condition:** human cannot reconstruct a contestable reason, yet gate still allows.

**Defence surface:** minimal-sufficiency requirements on \(e\) (still open in HP-0002).

### A3 — Authority Bypass Attempt

\(\mathcal{Adv}\) attempts to obtain ALLOW when \(H = \bot\) (no human authority present).

**Success condition:** gate returns ALLOW under \(\neg H\).

**Expected result under HP-0003:** attack fails by construction (fail-closed).

### A4 — Split-World / Equivocation

\(\mathcal{Adv}\) maintains two different native interpretations of the same commitment digest, revealing different meanings to different parties.

**Defence surface:** content-addressing + replayability + settlement persistence.

---

## Evaluation Criteria (research)

An attack is considered **successful** only if all of the following hold:

1. Native representation remains non-interpretable to a human examiner of the public commitment.
2. The commitment passes syntactic and basic integrity checks.
3. The gate returns ALLOW for a consequential action.
4. A later human contestation cannot recover a usable reason from the recorded evidence and provenance.

If any of (3) or (4) fails, the attack is considered **defeated** by the boundary + authority invariant.

---

## Relation to EXP-HP-001

The honest three-agent simulation of EXP-HP-001 supplies the baseline “compatible + authority present → ALLOW” behaviour.

EXP-HP-002 asks what happens when one of the producers is replaced by \(\mathcal{Adv}\) that tries to exploit opacity.

---

## Planned Artefacts (not yet present)

| Artefact | Purpose |
|----------|---------|
| `adversary_model.py` | executable stubs for A1–A4 |
| `defence_checks.py` | candidate detection predicates |
| `results/` | logged attack / defence outcomes |

See also `ATTACK-MODEL.md` in this directory.

---

## Non-Claims

- No claim that the listed attack variants are exhaustive.
- No claim that current real systems are vulnerable in exactly these ways.
- No security proof is offered; this is a research design document.

---

**Status:** Formal attack design. Executable adversary deferred.  
