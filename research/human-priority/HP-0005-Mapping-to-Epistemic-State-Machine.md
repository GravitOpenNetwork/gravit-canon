# HP-0005 — Mapping Human Priority onto the Epistemic State Machine

**Version:** 0.2  
**Status:** Research Draft — Experimental  
**Normative force:** None  
**Date:** 2026-09-11  
**Parent:** HP-0001 … HP-0004, RFC-0002 (EES)  
**Supersedes:** HP-0005 v0.1  

---

## 1. Purpose

To locate the Semantic Boundary and the Human Authority Invariant inside the existing Epistemic State Machine of RFC-0002 **without modifying** any normative transition rule, and to state a precise research hypothesis about the mandatory guard point.

---

## 2. Canonical States (reminder)

```
UNDEFINED → OBSERVED → CONTEXTUALIZED → HYPOTHESIZED
→ REASONED → VERIFIED → CONVERGED → CERTIFIED → COMMITTED
```

---

## 3. Placement of HP Concepts (research mapping)

| ESM State        | HP-relevant activity |
|------------------|----------------------|
| OBSERVED         | Raw native representation may exist; extraction \(\operatorname{ext}_i\) may begin |
| CONTEXTUALIZED   | Policy / authority context \(H\) and verification profile \(\mathcal{P}\) (incl. \(\Pi\)) become available |
| HYPOTHESIZED     | Claim \(c\) is proposed; commitment \(K_i(c)\) can be formed |
| REASONED         | Evidence \(e_i\) is linked; Trace records the derivation; \(\operatorname{Pol}\) may be computed |
| VERIFIED         | \(\operatorname{ver}\) runs; may use \(\operatorname{Compatible}_{\mathcal{P}}\) (any level) |
| CONVERGED        | Multi-agent compatibility / validator agreement is recorded |
| CERTIFIED        | Optional attestation layer |
| COMMITTED        | Settlement; after this point only new EOs may refine / supersede |

---

## 4. Precise Guard Placement Hypothesis (CONJECTURED)

### 4.1 Design principle

The Human Authority gate must fire **before any transition or external effect that can produce irreversible or high-impact real-world consequences**.

In the current EES model the first state that is allowed to trigger such effects is **COMMITTED** (settlement into a Persistence Layer). Certification may already bind cryptographic or policy-level attestations that later actors treat as authoritative.

### 4.2 Primary research hypothesis

**Mandatory guard location (H1):**

\[
\text{CONVERGED} \;\xrightarrow{\;\;\operatorname{auth}\;\;}\; \text{CERTIFIED / COMMITTED}
\]

More precisely:

- The transition **CONVERGED → CERTIFIED** (when certification is used) and  
- the transition **CERTIFIED → COMMITTED** (or CONVERGED → COMMITTED when certification is skipped)

are the earliest points at which a missing or invalid \(H\) **must** block progress for any EO that has been declared *consequential*.

### 4.3 Alternative / complementary placements (open)

| Option | Guard point | Rationale | Risk if omitted |
|--------|-------------|-----------|-----------------|
| H1 (preferred) | before CERTIFIED / COMMITTED | last pure epistemic state before external binding | irreversible settlement without human authority |
| H2 | on external action after COMMITTED | allows settlement of knowledge while still gating actuation | knowledge artefacts may already be treated as authoritative by downstream systems |
| H3 | both | defence in depth | higher operational cost |

**Research stance:** adopt **H1** as the default hypothesis for consequential EOs. H2 remains useful for actuation-level controls but is not a substitute for H1 when settlement itself has normative force.

### 4.4 Fail-closed rule (restated)

For any consequential EO \(eo\) and candidate transition \(t\) that crosses the guard point:

\[
\operatorname{auth}(T(eo), H) \neq \mathsf{ALLOW} \;\Rightarrow\; t \text{ is refused (EO stays in CONVERGED or records explicit DENY)}
\]

A missing \(H\) produces **DENY** (or an explicit non-progress record), never silent passage.

### 4.5 What the guard does *not* do

- It does not insert a new state into the machine.
- It does not reorder existing states.
- It does not apply to non-consequential research / experimental EOs unless a profile explicitly opts in.
- It does not replace GEVP verification; it is an additional authority condition.

---

## 5. Compatibility inside VERIFIED / CONVERGED

- Levels 0–3 of \(\operatorname{Compatible}_{\mathcal{P}}\) (especially Level-3 policy-predicate agreement) are evaluated during VERIFIED or as part of the convergence criterion that produces CONVERGED.
- The resulting compatibility status becomes part of the trust state \(T\) that \(\operatorname{auth}\) consumes at the guard point.

---

## 6. Non-interference with existing invariants

The mapping deliberately:

- does not reorder states,
- does not add or remove states,
- does not weaken EES-INV-001 … EES-INV-006,
- treats Human Priority as a cross-cutting guard, not as a new layer that overrides the machine.

---

## 7. Remaining open questions

1. Exact encoding of the DENY / non-progress record when the guard fires (new field vs. Challenge-style record).
2. Interaction with Challenge / Retraction paths that move an EO “backwards” under GEVP.
3. Whether certain classes of low-impact COMMITTED objects may be exempted by profile.

---

**Status:** Research mapping v0.2. Primary hypothesis H1 (guard before CERTIFIED/COMMITTED). No normative change proposed.  
