# Semantic Boundary — Formal Notes

**Status:** Research mathematics  
**Normative force:** None  
**Parent:** HP-0002 v0.2  
**Date:** 2026-09-10  

## Signature

\[
\partial_i = (\operatorname{ext}_i,\; \operatorname{ver},\; \operatorname{auth})
\]

\[
\begin{align*}
\operatorname{ext}_i &: S_i \times \mathcal{C} \to \mathcal{E} \\
\operatorname{ver}  &: \mathcal{E} \times \mathcal{P} \to \mathcal{T} \\
\operatorname{auth} &: \mathcal{T} \times \mathcal{H} \to \{\mathsf{ALLOW},\mathsf{DENY},\mathsf{ESCALATE}\}
\end{align*}
\]

## Working axioms (ASSUMED)

1. \(\operatorname{ext}_i\) need not be invertible.
2. \(\operatorname{ver}\) may operate without reference to \(S_H\).
3. \(\operatorname{auth}(T,H)=\mathsf{ALLOW}\) only under valid human authority context \(H\).

## Open formal questions

- Existence of a minimal sufficient \(e_i\) for contestability.
- Definition of \(\operatorname{Compatible}_{\mathcal{P}}\).
- Whether the composition \(\operatorname{auth}\circ\operatorname{ver}\circ\operatorname{ext}_i\) can be made continuous / measurable under reasonable topologies on the spaces.
