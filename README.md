# Gravit Canon — Final v1.1 / GEVP

> **Architecture is STABLE.** Future work is implementations, interoperability, and operational experience.

**Gravit** is an open network for verifiable knowledge transformations.

### IETF — POSTED ✅
**Latest:** `draft-gravit-gevp-05` — 2026-08-05 — POSTED
- TXT: https://www.ietf.org/archive/id/draft-gravit-gevp-05.txt
- HTML: https://www.ietf.org/archive/id/draft-gravit-gevp-05.html
- Datatracker: https://datatracker.ietf.org/doc/draft-gravit-gevp/
- Status: Submission status: Posted / 1 author / 5.1 KB / 3 pages

GEVP renamed from VCP to avoid collision with VeritasChain VCP (draft-kamimura-scitt-vcp).

**Core Invariant (engineering heuristic, NOT theorem):**
`C(manipulation) > C(validation) * 2.0`

**Theta:** 0.73 RECOMMENDED (pinned 7755f53: 1401/1500, TPR 93.4%, FPR 0.4%), range 0.70-0.80. No 67% Byzantine claim. h > 0.7, f < 0.3.

### Canon Structure
- ESM: RAW -> VALIDATED -> VERIFIED -> COMMITTED
- Persistence MAY (Ledger, IPFS, GSS, DB, Archive) — not MUST
- Signatures OPTIONAL
- Transport Bindings — separate

### Links
- Org: https://github.com/GravitOpenNetwork
- Website: https://gravit.space

### Citation
draft-gravit-gevp-05, Alex Konviser, IETF Individual Submission, 2026-08-05
