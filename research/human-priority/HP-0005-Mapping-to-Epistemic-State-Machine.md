# HP-0005 — Mapping Human Priority onto the Epistemic State Machine

**Version:** 0.1  
**Status:** Research Draft — Experimental  
**Normative force:** None  
**Date:** 2026-09-10  
**Parent:** HP-0001 … HP-0004, RFC-0002 (EES)  

---

## 1. Purpose

To locate the Semantic Boundary and the Human Authority Invariant inside the existing Epistemic State Machine of RFC-0002 **without modifying** any normative transition rule.

---

## 2. Canonical States (reminder)

```
UNDEFINED → OBSERVED → CONTEXTUALIZED → HYPOTHESIZED
→ REASONED → VERIFIED → CONVERGED → CERTIFIED → COMMITTED
```

---

## 3. Placement of HP Concepts (DEFINED as research mapping)

| ESM State        | HP-relevant activity |
|------------------|----------------------|
| OBSERVED         | Raw native representation may exist; extraction \(\operatorname{ext}_i\) may begin |
| CONTEXTUALIZED   | Policy / authority context \(H\) and verification profile \(\mathcal{P}\) become available |
| HYPOTHESIZED     | Claim \(c\) is proposed; commitment \(K_i(c)\) can be formed |
| REASONED         | Evidence \(e_i\) is linked; Trace records the derivation |
| VERIFIED         | \(\operatorname{ver}\) runs; may use \(\operatorname{Compatible}_{\mathcal{P}}\) |
| CONVERGED        | Multi-agent compatibility / validator agreement is recorded |
| CERTIFIED        | Optional attestation layer |
| COMMITTED        | Settlement; after this point only new EOs may refine / supersede |

**Critical observation:**

The Human Authority gate \(\operatorname{auth}\) is most naturally applied **before** a transition that has consequential external effect. In the current Canon the natural insertion points for research evaluation are:

- between CONVERGED and CERTIFIED, or
- between CERTIFIED and COMMITTED, or
- as a guard on any external action that is triggered by a COMMITTED object.

HP does **not** insert a new state into the machine. It adds a **guard condition** on selected transitions / external effects.

---

## 4. Fail-Closed Guard (CONJECTURED placement)

For any transition or external action \(a\) that is declared *consequential*:

\[
\text{allow}(a) \;\Rightarrow\; H(a) = \top
\]

This is exactly the Human Authority Invariant of HP-0003, restated as a guard relative to the State Machine.

---

## 5. Compatibility inside VERIFIED / CONVERGED

- Weak or strong \(\operatorname{Compatible}_{\mathcal{P}}\) is evaluated during the production of the Verification Record (VERIFIED) or during the convergence criterion (CONVERGED).
- It does not replace the existing GEVP procedures; it is a candidate internal predicate that profiles may adopt.

---

## 6. Non-interference with existing invariants

The mapping deliberately:

- does not reorder states,
- does not add or remove states,
- does not weaken EES-INV-001 … EES-INV-006,
- treats Human Priority as a cross-cutting guard, not as a new layer that overrides the machine.

---

## 7. Open questions

1. Exact transition(s) at which the authority guard is mandatory for consequential actions.
2. Whether a missing \(H\) should force a stay in CONVERGED / CERTIFIED or produce an explicit DENY record.
3. Interaction with Challenge / Retraction paths that move an EO “backwards” under GEVP.

---

**Status:** Research mapping only. No normative change proposed.  
