# HP-0004 — Compatible Relation under Heterogeneous Semantic Spaces

**Version:** 0.2  
**Status:** Research Draft — Experimental  
**Normative force:** None  
**Mathematical status:** Defined (Levels 0–3) / Conjectured (Level 4)  
**Date:** 2026-09-11  
**Parent:** HP-0001, HP-0002 v0.2  
**Supersedes:** HP-0004 v0.1  

---

## Status Markers

| Element | Status |
|---------|--------|
| Weak compatibility (claim-identity) | DEFINED |
| Level-1 (claim + confidence band) | DEFINED |
| Level-2 (evidence presence) | DEFINED |
| **Level-3 (policy-predicate agreement)** | **DEFINED (research)** |
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

Let \(\mathcal{P}\) be a verification profile (semantic profile + validator set + thresholds + **policy predicate set** \(\Pi\)).

We define a family of relations indexed by \(\mathcal{P}\):

\[
\operatorname{Compatible}_{\mathcal{P}} \;\subseteq\; \mathcal{K} \times \mathcal{K}
\]

**Required properties (DEFINED):**

1. **Reflexivity** — \(\operatorname{Compatible}_{\mathcal{P}}(K,K)\) for every well-formed \(K\).
2. **Symmetry** — \(\operatorname{Compatible}_{\mathcal{P}}(K_1,K_2) \Leftrightarrow \operatorname{Compatible}_{\mathcal{P}}(K_2,K_1)\).
3. **Independence from native equality** — does **not** imply \(S_A = S_B\) or \(\operatorname{ext}_A = \operatorname{ext}_B\).
4. **Profile dependence** — the same pair may be compatible under one profile and incompatible under another.

Transitivity is **not** required.

---

## 3. Graded Ladder (DEFINED / CONJECTURED)

| Level | Name | Definition (sketch) | Status |
|-------|------|---------------------|--------|
| 0 | Claim identity | \(\operatorname{claim}(K_A)=\operatorname{claim}(K_B)\) | DEFINED |
| 1 | Claim + confidence band | Level-0 + \(\lvert q_A - q_B\rvert \le \theta_q\) | DEFINED |
| 2 | Evidence presence | Level-1 + non-empty evidence objects | DEFINED |
| **3** | **Policy-predicate agreement** | Level-2 + agreement on a declared set of policy predicates | **DEFINED (research)** |
| 4 | Strong (evidence support) | Level-3 + \(\operatorname{EvidenceSupport}_{\mathcal{P}}\) + provenance consistency | CONJECTURED |

---

## 4. Level-3 — Policy-Predicate Agreement (DEFINED as research construct)

### 4.1 Motivation

Human Authority ultimately cares about **policy-relevant facts**, not about the geometry of \(S_i\).  
Level-3 therefore lifts compatibility from surface claim values to a small set of predicates that a human (or a human-governed policy engine) can contest.

### 4.2 Formal definition

Let \(\Pi = \{\pi_1,\dots,\pi_m\}\) be a finite set of **policy predicates** declared by the verification profile \(\mathcal{P}\).  
Each predicate \(\pi_j\) is a boolean-valued function that can be evaluated from the *extracted evidence* \(e_i\) without requiring access to the full native space \(S_i\).

For a commitment \(K_i\) define the **policy support vector**:

\[
\operatorname{Pol}(K_i) \;=\; \bigl( \pi_1(e_i),\; \pi_2(e_i),\; \dots,\; \pi_m(e_i) \bigr) \in \{0,1,\bot\}^m
\]

where \(\bot\) means “evidence insufficient to decide \(\pi_j\)”.

**Level-3 compatibility:**

\[
\operatorname{Compatible}^{\text{L3}}_{\mathcal{P}}(K_A, K_B)
\quad:\Leftrightarrow\quad
\begin{aligned}
&\operatorname{Compatible}^{\text{L2}}_{\mathcal{P}}(K_A, K_B) \\
&\land\;
\operatorname{Pol}(K_A) \;\approx_{\mathcal{P}}\; \operatorname{Pol}(K_B)
\end{aligned}
\]

The relation \(\approx_{\mathcal{P}}\) is itself profile-defined. Minimal useful forms:

| Variant | Meaning |
|---------|---------|
| Exact | \(\operatorname{Pol}(K_A) = \operatorname{Pol}(K_B)\) (no \(\bot\) mismatch allowed) |
| Agree-on-decided | for every \(j\) where both sides are decided, the values coincide |
| Threshold | Hamming agreement on decided coordinates \(\ge \tau\) |
| **Strict** | decided-vs-\(\bot\) counts as disagreement |

### 4.3 Key design properties

1. **Native opacity preserved** — evaluation of \(\pi_j\) uses only \(e_i = \operatorname{ext}_i(s,c)\), never the raw \(s \in S_i\).
2. **Human contestability** — each \(\pi_j\) is chosen so that a human can understand and challenge the predicate itself.
3. **Profile locality** — different domains declare different \(\Pi\). No universal ontology requirement.
4. **Fail-soft / strict on \(\bot\)** — profile chooses whether insufficient evidence blocks agreement.

### 4.4 Example policy predicates (toy, non-normative)

For the running “transaction X vs policy Y” task:

```text
π_amount_exceeds   : amount > limit ?
π_sanction_hit     : counterparty ∈ sanctions ?
π_attestation_ok   : required attestation present ?
π_claim_violation  : claimed decision == "violation"
```

### 4.5 Relation to Mimicry (A1) and Evidence Pollution (A2)

- **A1 Mimicry** becomes harder: the adversary must also forge evidence that evaluates to the same \(\operatorname{Pol}\) vector.
- **A2 Evidence Pollution** is directly attacked under strict mode: polluted evidence produces many \(\bot\), which prevents Level-3 compatibility.

---

## 5. Weak / Strong reminders

**Weak (Level-0)** remains the cheapest baseline and is intentionally vulnerable to pure claim copying.

**Strong (Level-4)** still requires a non-trivial \(\operatorname{EvidenceSupport}_{\mathcal{P}}\) that does not collapse to a shared human metalanguage. It stays CONJECTURED.

---

## 6. Multi-Agent Extension

\[
\operatorname{Compatible}^{\text{L3}}_{\mathcal{P}}(\{K_i\})
\quad:\Leftrightarrow\quad
\forall i,j.\; \operatorname{Compatible}^{\text{L3}}_{\mathcal{P}}(K_i, K_j)
\]

---

## 7. Relationship to Verification Map and Human Authority

```
evidence → Pol vectors → Compatible^L3 → T → auth(H)
```

Level-3 is the natural bridge between machine-native evidence and the Human Authority gate.

---

## 8. Open Problems (explicit)

1. Minimal size and expressive power of \(\Pi\) that still yields meaningful contestability.
2. Stable definition of \(\approx_{\mathcal{P}}\) under partial evidence (\(\bot\)).
3. Composition when agents extract different subsets of the same underlying \(\Pi\).
4. Robustness against adaptive adversaries that learn the predicate set.

---

## 9. Non-Claims

- No claim that a unique or canonical \(\Pi\) exists.
- No claim that Level-3 is currently computable for arbitrary real-world evidence.
- No normative force on ARCH-001 or any RFC.

---

**Document status:** Research Draft v0.2  
**Maintainer track:** research/human-priority/  
