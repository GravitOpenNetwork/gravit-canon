# Adversarial Opacity — Attack Model (formal sketch)

**Status:** Research design  
**Normative force:** None  
**Date:** 2026-09-10  

## Notation

- \(\mathcal{Adv}\) — adversary agent  
- \(S_{\mathcal{Adv}}\) — its native representational space  
- \(K_{\mathcal{Adv}}(c)\) — epistemic commitment it emits  
- \(H\) — human authority context  
- \(\operatorname{auth}\) — authority map of the Semantic Boundary  

## Security goal of the system (informal)

For every consequential action \(a\):

\[
\operatorname{auth}(T, H) = \mathsf{ALLOW} \;\Rightarrow\; H\text{ is valid and unrevoked}
\]

and the recorded commitment + evidence remain sufficient for later contestation.

## Adversary goal

Produce a run in which:

\[
\operatorname{auth}(T, H) = \mathsf{ALLOW}
\]

while either

- \(H\) is missing / invalid, or  
- the recorded evidence does not permit a human to contest the substance of the claim that justified \(a\).

## Attack surface summary

| Variant | Primary target | Expected defence |
|---------|----------------|------------------|
| A1 Mimicry | claim-value agreement | provenance + history |
| A2 Evidence pollution | contestability of \(e\) | minimal-sufficiency of evidence |
| A3 Authority bypass | fail-closed rule | HP-0003 invariant |
| A4 Equivocation | unique interpretation of commitment | content-addressing + settlement |

## Open formal work

- Precise definition of “usable reason for contestation”.
- Information-theoretic lower bound on the content of \(e\) under A2.
- Composition of multiple adversarial agents.
