# HP-0002 — Semantic Boundary Model

**Version:** 0.1  
**Status:** Research Draft — Experimental  
**Normative force:** None  
**Date:** 2026-09-10  
**Parent:** HP-0001  

---

## 1. Purpose

To formalise the notion of a **Semantic Boundary** that permits verification and authority decisions without requiring full human interpretability of agent-native representations.

---

## 2. Definitions (DEFINED)

**Agent-native space** \(S_i\): any representational system employed by agent \(i\) (symbolic, vector, multimodal, latent, spectral, temporal patterns, etc.).

**Epistemic evidence** \(E_i\): the subset of information extracted from \(S_i\) that can be attached to an Epistemic Object and subjected to verification.

**Trust state** \(T\): an evaluable reliability / authority-relevant state derived from evidence, provenance, consensus behaviour and policy.

**Semantic Boundary**: the interface

\[
S_i \;\xrightarrow{\text{extraction}}\; E_i \;\xrightarrow{\text{verification}}\; T
\]

---

## 3. Minimal Requirements on the Boundary

For any claim that may trigger consequential action, the boundary MUST expose:

1. Identity of the producing agent  
2. Provenance of the claim and evidence  
3. Content-addressable or hashable commitment  
4. Temporal positioning  
5. Verification interface (possibly operating inside the same non-human space)  
6. Explicit authority boundary (human-sanctioned or not)

Human-readable interpretation is **optional**, not mandatory, at the verification stage.

---

## 4. Relationship to Interpretability

The boundary deliberately separates:

- **Verification path** — can remain machine-native  
- **Authority path** — must terminate in a human-governed decision point for consequential actions

This realises the HCI Independence Principle of HP-0001.

---

## 5. Open Questions

- What is the minimal information content of \(E_i\) that still permits meaningful human contestability?
- Can validator consensus occur entirely inside a shared non-human profile before any human-readable summary is generated?
- How does the boundary interact with Challenge / Retraction mechanisms already present in GEVP?

---

**Status:** Research sketch. No theorems claimed.  
