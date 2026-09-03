Gravit Canon — Final v1.1 / GEVP + VEDS

    Architecture is STABLE. Two-track IETF architecture POSTED. Future work is implementations, interoperability, and operational experience.

Gravit is an open network for verifiable knowledge transformations — from checkbox transparency to auditable trust.
IETF — Two-Track POSTED ✅

Latest — Two-Track:
Track	Document	Revision	Date	Status
Mechanism (HOW)	draft-gravit-gevp	07	2026-08-12	POSTED
Policy (WHAT)	draft-gravit-verifiable-epistemic-decision	00	2026-08-09	POSTED
GEVP-07 — Mechanism | HOW to verify

    TXT: https://www.ietf.org/archive/id/draft-gravit-gevp-07.txt
    HTML: https://www.ietf.org/archive/id/draft-gravit-gevp-07.html
    Datatracker: https://datatracker.ietf.org/doc/draft-gravit-gevp/
    Diff 06→07: https://author-tools.ietf.org/iddiff?url2=draft-gravit-gevp-07

What changed from 06:

    Section 10 VEDS Conformance Mapping — normative mapping between GEVP ESM and VEDS taxonomy
    RAW → not admissible, VALIDATED → ≤ Speculative Claim, VERIFIED → Probabilistic Assessment, COMMITTED (h>0.7/f<0.3) → Verified Fact
    Aggregation Restriction = No Aggregation Laundering (VEDS 4.1.2)

Stable since 05:

    ESM: RAW -> VALIDATED -> VERIFIED -> COMMITTED
    Persistence MAY (Ledger, IPFS, GSS, DB, Archive) — not MUST
    Signatures OPTIONAL, Transport Bindings separate

VEDS-00 — Policy | WHAT to enforce

    TXT: https://www.ietf.org/archive/id/draft-gravit-verifiable-epistemic-decision-00.txt
    HTML: https://www.ietf.org/archive/id/draft-gravit-verifiable-epistemic-decision-00.html
    Datatracker: https://datatracker.ietf.org/doc/draft-gravit-verifiable-epistemic-decision/

Defines:

    Taxonomy: Verified Fact / Probabilistic Assessment / Speculative Claim
    Failure States: REJECTED / DEGRADED / PENDING
    Decision Record format, traceability, auditability, Conformance Statement
    Threat model 4.6.1 → Security 6 + Residual Risks
    Mechanism-agnostic by design (Variant A): GEVP is Informative example only [GEVP] — no downref per RFC 3967/4897
    Verified idnits: Checking references for intended status: Proposed Standard — No issues found here — 0/0/2/0

Two-Track Architecture

EU AI Act Art.50
IETF TWO-TRACK

GEVP-07 — Mechanism | HOW to verify          VEDS-00 — Policy | WHAT to enforce
ESM: RAW → VALIDATED → VERIFIED → COMMITTED  Taxonomy: Verified Fact / Probabilistic / Speculative
θ = 0.73, h>0.7 • f<0.3                      Failure: REJECTED / DEGRADED / PENDING
         <--- Conformance Mapping Section 10 --->

    GEVP = HOW: verifiable provenance (who created, what verified, when, theta-score)
    VEDS = WHAT: reproducible, auditable, fail-closed behavioral guarantees

For EU AI Act Art.50 (mandatory disclosure from Aug 2026): together = auditable trust.
Core Invariants

    Engineering heuristic, NOT theorem: C(manipulation) > C(validation) * 2.0
    Theta: 0.73 RECOMMENDED (pinned 7755f53: 1401/1500, TPR 93.4%, FPR 0.4%), range 0.70-0.80
    Convergence: h > 0.7 honest, f < 0.3 faulty — no 67% Byzantine claim
    GEVP renamed from VCP to avoid collision with VeritasChain VCP (draft-kamimura-scitt-vcp)

Implementation Status

    MVR 0.1.0-mvr: https://github.com/GravitOpenNetwork/gravit-canon/tree/main/mvr
    Calibration SHA: 7755f53, TPR 93.4%, FPR 0.4%, theta 0.73 RECOMMENDED
    Next: interop tests against both specs

Links

    Org: https://github.com/GravitOpenNetwork
    Website: https://gravit.space
    IETF folder: https://github.com/GravitOpenNetwork/gravit-canon/tree/main/ietf
    Issues: https://github.com/GravitOpenNetwork/gravit-canon/issues

Citation

draft-gravit-gevp-07, Alex Konviser, IETF Individual Submission, 2026-08-12
draft-gravit-verifiable-epistemic-decision-00, Alex Konviser, IETF Individual Submission, 2026-08-09

Validation:

    GEVP-07: author-tools.ietf.org — well-formed, 0 dup, 0 missing xrefs, 0 non-ASCII
    VEDS-00: idnits 2.17.1 — 0 errors, 0 flaws, 2 warnings (known -00 boilerplate), 0 comments — "No issues found here" for Proposed Standard

