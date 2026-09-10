# HP-0002 — Semantic Boundary Model

**Version:** 0.2  
**Status:** Research Draft — Experimental  
**Normative force:** None  
**Mathematical status:** Defined / Conjectured  
**Date:** 2026-09-10  
**Parent:** HP-0001  
**Supersedes:** HP-0002 v0.1  

---

## Status Markers

| Element | Status |
|---------|--------|
| Core definitions of \(S_i, E_i, T, \partial\) | DEFINED |
| Extraction and verification maps | DEFINED |
| Minimal interface requirements | DEFINED |
| Compatibility relation | CONJECTURED |
| Completeness / minimality theorems | OPEN |
| Implementation claims | none |

This document has **no normative force** on ARCH-001 or any RFC.

---

## 1. Purpose

To give a precise mathematical structure to the **Semantic Boundary** — the interface that permits epistemic verification and human authority decisions without requiring a total translation of an agent-native representational space into a human-interpretable space.

---

## 2. Primitive Spaces (DEFINED)

Let \(\mathcal{A} = \{a_1,\dots,a_n\}\) be a finite set of agents.

For each agent \(a_i \in \mathcal{A}\):

- \(S_i\) — agent-native semantic / representational space (arbitrary set; may be discrete, continuous, multimodal, latent, spectral, etc.).
- \(S_H\) — a designated human-interpretable space (natural language statements, diagrams, policy predicates, etc.).

We **do not** assume the existence of a total function \(\tau_i : S_i \to S_H\).

We introduce three auxiliary spaces that are required to be well-defined independently of any particular \(S_i\):

| Symbol | Name | Intended content |
|--------|------|------------------|
| \(\mathcal{E}\) | Evidence space | structured objects that can be attached to an Epistemic Object |
| \(\mathcal{K}\) | Commitment space | epistemic commitments \(K_i(c)\) |
| \(\mathcal{T}\) | Trust-state space | reliability / authority-relevant evaluations |

---

## 3. Semantic Boundary (DEFINED)

The **Semantic Boundary** of agent \(a_i\) is the triple

\[
\partial_i = \bigl( \operatorname{ext}_i,\; \operatorname{ver},\; \operatorname{auth} \bigr)
\]

where the maps are:

\[
\begin{align*}
\operatorname{ext}_i &: S_i \times \mathcal{C} \to \mathcal{E} \\
\operatorname{ver}  &: \mathcal{E} \times \mathcal{P} \to \mathcal{T} \\
\operatorname{auth} &: \mathcal{T} \times \mathcal{H} \to \{\mathsf{ALLOW}, \mathsf{DENY}, \mathsf{ESCALATE}\}
\end{align*}
\]

| Symbol | Meaning |
|--------|---------|
| \(\mathcal{C}\) | set of claims |
| \(\mathcal{P}\) | verification policy / profile (includes validator set, thresholds, semantic profile) |
| \(\mathcal{H}\) | human-authority context (authorisations, revocations, policy decisions) |

**Composition** that realises the boundary:

\[
S_i \;\xrightarrow{\operatorname{ext}_i}\; E_i \;\xrightarrow{\operatorname{ver}}\; T \;\xrightarrow{\operatorname{auth}}\; \{\mathsf{ALLOW},\mathsf{DENY},\mathsf{ESCALATE}\}
\]

Human interpretability of elements of \(S_i\) is **not** required for the composition to be well-defined.

---

## 4. Epistemic Commitment Revisited (DEFINED)

A claim \(c \in \mathcal{C}\) that may have consequential effect is admissible only if the producing agent supplies a commitment

\[
K_i(c) = \bigl( id_i,\; h_i,\; p_i,\; \tau_i,\; e_i,\; q_i \bigr) \in \mathcal{K}
\]

with the following constraints:

1. \(e_i = \operatorname{ext}_i(s, c)\) for some \(s \in S_i\) (evidence is the image of extraction).
2. \(h_i\) is a content-addressable digest of the relevant commitment fields (exact hash function left to profile).
3. \(p_i\) (provenance) is non-empty and cryptographically or registry-backed.
4. \(\tau_i\) places the commitment in a partial order compatible with the Trace model of the Canon.

The commitment lives in \(\mathcal{K}\), which is required to be independent of the particular geometry of \(S_i\).

---

## 5. Extraction Map — Formal Properties (DEFINED / CONJECTURED)

**Defined properties** that \(\operatorname{ext}_i\) MUST satisfy:

- **Determinism under fixed profile**  
  Given identical inputs and identical extraction profile, \(\operatorname{ext}_i\) yields identical \(e_i\) (up to declared equivalence).

- **Provenance preservation**  
  \(\operatorname{ext}_i\) may not discard identity or provenance that is required by the commitment structure.

- **Non-requirement of invertibility**  
  \(\operatorname{ext}_i\) need not be injective or surjective. Information loss relative to \(S_i\) is permitted.

**Conjectured properties** under investigation:

- **Minimal sufficiency**  
  There exists a minimal information content of \(e_i\) such that human contestability of consequential claims remains possible.

- **Profile relativity**  
  Different semantic profiles may induce different \(\operatorname{ext}_i\) for the same underlying \(S_i\).

---

## 6. Verification Map (DEFINED)

\[
\operatorname{ver} : \mathcal{E} \times \mathcal{P} \to \mathcal{T}
\]

\(\operatorname{ver}\) evaluates evidence against a declared verification policy \(\mathcal{P}\).  
It may itself operate entirely inside a non-human representation; the only requirement is that its output \(T \in \mathcal{T}\) is evaluable by the authority map.

Typical components of \(T\) (illustrative, not normative):

- provenance integrity indicator  
- reproducibility / replay indicator  
- validator-convergence indicator  
- historical-consistency indicator  
- policy-compliance indicator  

No claim is made that \(T\) is a scalar. Multi-component trust states are admissible (see Graviteron research notes).

---

## 7. Authority Map and Fail-Closed Property (DEFINED relative to HP-0003)

\[
\operatorname{auth} : \mathcal{T} \times \mathcal{H} \to \{\mathsf{ALLOW}, \mathsf{DENY}, \mathsf{ESCALATE}\}
\]

**Fail-closed axiom (from HP-0003, restated):**

\[
\operatorname{auth}(T, H) = \mathsf{ALLOW} \quad\text{only if}\quad H \text{ contains a valid, unrevoked human authorisation for the action.}
\]

Equivalently:

\[
\neg H(a) \;\Rightarrow\; \operatorname{auth}(\cdot,\cdot) \neq \mathsf{ALLOW}
\]

This is the point at which Human Priority is enforced, independently of whether any human ever inspected the original \(s \in S_i\).

---

## 8. Compatibility across Heterogeneous Boundaries (CONJECTURED)

Let two agents \(a_A, a_B\) produce commitments \(K_A(c), K_B(c)\) for the “same” claim \(c\).

We do **not** require \(S_A = S_B\) or \(\operatorname{ext}_A = \operatorname{ext}_B\).

We seek a relation

\[
\operatorname{Compatible}_{\mathcal{P}}(K_A, K_B) \;\subseteq\; \mathcal{K} \times \mathcal{K}
\]

that is:

- reflexive and symmetric under a fixed profile \(\mathcal{P}\);
- strong enough that \(\operatorname{ver}\) can treat the pair as mutually supporting evidence;
- weak enough that it does not collapse to equality of native representations.

Exact definition of \(\operatorname{Compatible}_{\mathcal{P}}\) remains an open research problem. Candidate approaches include:

- agreement on a declared claim identifier after projection into a common metalanguage of claims;
- agreement on a set of policy-relevant predicates;
- statistical or cryptographic agreement on digests derived under a shared verification profile.

---

## 9. Relationship to Existing Canon Primitives

| Canon primitive | Role at the Semantic Boundary |
|-----------------|-------------------------------|
| Epistemic Object (EOS) | carrier of \(K_i(c)\) and of \(e_i\) |
| Trace | realisation of temporal / provenance ordering |
| GEVP | possible concrete realisation of \(\operatorname{ver}\) |
| Settlement | persistence of allowed commitments |
| EES-INV-001…006 | remain binding; \(\partial_i\) may not violate them |

The Boundary is a *cross-cutting interface*, not a replacement for any existing layer.

---

## 10. Open Problems (explicit)

1. Minimal information-theoretic characterisation of \(e_i\) that still supports meaningful human contestability.
2. Construction of a non-trivial \(\operatorname{Compatible}_{\mathcal{P}}\) that does not force a shared human-interpretable metalanguage.
3. Interaction of \(\operatorname{ext}_i\) with Challenge / Retraction (GEVP).
4. Whether \(\operatorname{ver}\) can be made to operate entirely inside a non-human space while still producing a \(T\) that \(\operatorname{auth}\) can safely consume.
5. Compositionality: behaviour of \(\partial_i\) when agents themselves invoke other agents with different boundaries.

---

## 11. Non-Claims

- No claim that current systems implement \(\partial_i\).
- No claim of completeness or minimality theorems.
- No numerical thresholds.
- No normative force.

---

**Document status:** Research Draft v0.2  
**Last updated:** 2026-09-10  
**Maintainer track:** research/human-priority/  
