# HP-0004 — Compatible Relation under Heterogeneous Semantic Spaces

**Version:** 0.1  
**Status:** Research Draft — Experimental  
**Normative force:** None  
**Mathematical status:** Defined (weak) / Conjectured (strong)  
**Date:** 2026-09-10  
**Parent:** HP-0001, HP-0002 v0.2  

---

## Status Markers

| Element | Status |
|---------|--------|
| Weak compatibility (claim-identity) | DEFINED |
| Strong compatibility (evidence-level) | CONJECTURED |
| Profile-relative family of relations | DEFINED |
| Completeness / uniqueness theorems | OPEN |

---

## 1. Problem Statement

When two agents \(a_A\) and \(a_B\) operate in distinct native spaces

\[
S_A \;\neq\; S_B
\]

we cannot require equality of representations.  
We need a relation on *epistemic commitments* that still allows verification to treat them as mutually supporting evidence.

---

## 2. Profile-Relative Compatibility Family (DEFINED)

Let \(\mathcal{P}\) be a verification profile (semantic profile + validator set + thresholds).

We define a family of relations indexed by \(\mathcal{P}\):

\[
\operatorname{Compatible}_{\mathcal{P}} \;\subseteq\; \mathcal{K} \times \mathcal{K}
\]

**Required properties (DEFINED):**

1. **Reflexivity**  
   \(\operatorname{Compatible}_{\mathcal{P}}(K,K)\) for every well-formed \(K\).

2. **Symmetry**  
   \(\operatorname{Compatible}_{\mathcal{P}}(K_1,K_2) \;\Leftrightarrow\; \operatorname{Compatible}_{\mathcal{P}}(K_2,K_1)\).

3. **Independence from native equality**  
   \(\operatorname{Compatible}_{\mathcal{P}}(K_A,K_B)\) does **not** imply \(S_A = S_B\) or \(\operatorname{ext}_A = \operatorname{ext}_B\).

4. **Profile dependence**  
   The same pair of commitments may be compatible under one profile and incompatible under another.

Transitivity is **not** required (and is generally undesirable).

---

## 3. Weak Compatibility — Claim Identity (DEFINED)

The weakest useful relation used by the current toy model:

\[
\operatorname{Compatible}^{\text{weak}}_{\mathcal{P}}(K_A, K_B)
\quad:\Leftrightarrow\quad
\operatorname{claim}(K_A) = \operatorname{claim}(K_B)
\]

where \(\operatorname{claim}(K)\) is the declared claim identifier carried inside the commitment (independent of the native representation that produced it).

**Properties:**

- Satisfies reflexivity and symmetry.
- Extremely cheap to evaluate.
- Vulnerable to Mimicry (A1) — an adversary can simply copy the claim value.

This is the baseline. It is intentionally weak.

---

## 4. Strong Compatibility — Evidence-Level (CONJECTURED)

A stronger candidate (still research):

\[
\operatorname{Compatible}^{\text{strong}}_{\mathcal{P}}(K_A, K_B)
\quad:\Leftrightarrow\quad
\begin{aligned}
&\operatorname{claim}(K_A) = \operatorname{claim}(K_B) \\
&\land\;
\operatorname{EvidenceSupport}_{\mathcal{P}}(e_A, e_B) \\
&\land\;
\operatorname{ProvenanceConsistent}(p_A, p_B)
\end{aligned}
\]

where:

- \(\operatorname{EvidenceSupport}_{\mathcal{P}}\) is a profile-defined predicate that decides whether the two evidence objects are mutually corroborating under \(\mathcal{P}\);
- \(\operatorname{ProvenanceConsistent}\) checks that the provenance chains do not contain known contradictions or identity collisions.

**Open questions for \(\operatorname{EvidenceSupport}_{\mathcal{P}}\):**

1. Can it be defined without projecting both \(e_A\) and \(e_B\) into a shared human-interpretable metalanguage?
2. What is the minimal information that must survive extraction for the predicate to be non-vacuous?
3. How does it interact with continuous / high-dimensional evidence (vector, spectral, latent)?

Until these are answered, strong compatibility remains **CONJECTURED**.

---

## 5. Intermediate Layers (research menu)

Between weak and strong we can insert graded notions:

| Level | Name | Idea |
|-------|------|------|
| 0 | Claim identity | current toy |
| 1 | Claim + confidence band | claims equal and \(q\) within declared tolerance |
| 2 | Claim + evidence digest agreement | shared cryptographic summary under a common profile |
| 3 | Claim + policy-predicate agreement | both evidence objects support the same set of policy-relevant predicates |
| 4 | Full evidence support | strong form above |

Level 3 is currently the most promising research target: it stays close to the needs of Human Authority (policy predicates) while still allowing native spaces to remain opaque.

---

## 6. Multi-Agent Extension

For a finite set of commitments \(\{K_1,\dots,K_n\}\):

\[
\operatorname{Compatible}_{\mathcal{P}}(\{K_i\})
\quad:\Leftrightarrow\quad
\forall i,j.\; \operatorname{Compatible}_{\mathcal{P}}(K_i, K_j)
\]

(under the chosen strength).  
Weaker variants (e.g., majority-compatible) are admissible under a declared profile but are not defined here.

---

## 7. Relationship to Verification Map

Inside the Semantic Boundary:

\[
\operatorname{ver}(E, \mathcal{P})
\]

may use \(\operatorname{Compatible}_{\mathcal{P}}\) as one of its internal predicates when multiple evidence objects are present.  
Compatibility is therefore an input to the construction of the trust state \(T\), not a replacement for it.

---

## 8. Attack Surface (link to EXP-HP-002)

| Attack | Weak Compatible | Strong Compatible (if realised) |
|--------|-----------------|---------------------------------|
| A1 Mimicry | vulnerable | harder (needs evidence support) |
| A2 Evidence Pollution | still possible | detection surface increases |
| A3 Authority Bypass | orthogonal (handled by \(\operatorname{auth}\)) | orthogonal |
| A4 Equivocation | content-addressing still primary defence | same |

---

## 9. Immediate Engineering Consequence for the Toy Model

The current `toy_model.py` implements only **Weak Compatible**.  
The next executable step is to introduce an optional Level-1 / Level-2 check (claim + confidence band, and optional evidence-kind agreement) without claiming strong compatibility.

---

## 10. Non-Claims

- No claim that a unique or canonical Compatible relation exists.
- No claim that strong compatibility is currently computable for arbitrary native spaces.
- No normative force.

---

**Document status:** Research Draft v0.1  
**Maintainer track:** research/human-priority/  
