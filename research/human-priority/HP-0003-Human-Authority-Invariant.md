# HP-0003 — Human Authority Invariant

**Version:** 0.1  
**Status:** Research Draft — Experimental  
**Normative force:** None  
**Date:** 2026-09-10  
**Parent:** HP-0001  

---

## 1. Statement (CONJECTURED)

For every consequential action \(a\):

\[
\text{Execute}(a) \;\Rightarrow\; V(a) \land P(a) \land C(a) \land H(a)
\]

and

\[
\neg H(a) \;\Rightarrow\; \neg\text{Execute}(a)
\]

where:

- \(V(a)\) — Epistemic Validity (claim and evidence satisfy the chosen semantic profile and verification rules)
- \(P(a)\) — Policy Validity (action is permitted under declared policy)
- \(C(a)\) — Consensus / Verification Validity (required validator set or equivalent has converged)
- \(H(a)\) — Human Authority Validity (required human-governed authorisation is present and unrevoked)

The system is required to be **fail-closed** with respect to \(H\).

---

## 2. Design Intent

This invariant is intended to become machine-checkable once the four predicates are given precise definitions relative to the Epistemic State Machine and Settlement layer.

It does not require that every intermediate state be human-interpretable. It requires that the final gate before execution of consequential action pass through human authority.

---

## 3. Non-Claims

- No claim is made that current implementations already enforce this invariant.
- No claim is made about the concrete form of “human authority” (single human, multi-signature, institutional process, etc.). That is a policy-layer question.
- The invariant does not prohibit fully automated low-consequence actions that fall outside the declared “consequential” set.

---

## 4. Relation to Existing Invariants

HP-0003 does not override EES-INV-001 … EES-INV-006. It is a candidate additional cross-cutting constraint under research evaluation.

---

**Status:** Conjectured invariant. Formal proof obligations not yet discharged.  
