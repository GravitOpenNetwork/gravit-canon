# Gravit Canon — Research Track

**Status:** Informative / Research  
**Not normative.** Documents in this directory do **not** form part of the
normative Gravit Canon (ARCH-001 + RFC-0001…0006).

## Purpose

Phase B separates **research and formal exploration** from the stable
specification baseline.

Material here may:

- sketch mathematical models,
- record open problems,
- propose candidate profiles (e.g. ZKP),
- document the status of engineering parameters (cost model, θ_critical),
- explore cross-cutting concerns such as Human Priority over non-human semantic spaces,

but MUST NOT be cited as if it conferred normative force on the RFCs.

## Documents

### Core research notes

| File | Title | Status |
|------|-------|--------|
| `FM-001-Epistemic-Foundations.md` | Formal sketches for EES invariants & execution | Research draft |
| `NOTE-cost-model-and-theta.md` | Status of cost model and θ_critical | Research note |
| `NOTE-zkp-profile-sketch.md` | Zero-knowledge methods as future Registry profiles | Research sketch |

### Human Priority track (HP)

| File | Title | Status |
|------|-------|--------|
| `human-priority/HP-0001-Human-Priority-over-Non-Human-Semantic-Spaces.md` | Formal foundations of Human Priority | Research Draft v0.1 (Experimental) |
| `human-priority/HP-0002-Semantic-Boundary-Model.md` | Semantic Boundary (formal maps \(\operatorname{ext},\operatorname{ver},\operatorname{auth}\)) | Research Draft v0.2 |
| `human-priority/HP-0003-Human-Authority-Invariant.md` | Fail-closed Human Authority Invariant | Research Draft v0.1 |
| `human-priority/HP-0004-Compatible-Relation.md` | Graded Compatible (Levels 0–3 DEFINED, Level-4 CONJECTURED) | Research Draft v0.2 |
| `human-priority/HP-0005-Mapping-to-Epistemic-State-Machine.md` | Mapping HP guards onto EES; primary hypothesis H1 (before CERTIFIED/COMMITTED) | Research Draft v0.2 |

### Mathematics (supporting notes)

| File | Title | Status |
|------|-------|--------|
| `mathematics/semantic-space.md` | Working definitions for \(S_i\) | Research notes |
| `mathematics/semantic-boundary.md` | Formal signature of \(\partial_i\) | Research notes |
| `mathematics/epistemic-commitment.md` | Structure of \(K_i(c)\) | Research notes |
| `mathematics/graviteron-model.md` | Multi-component reliability representation | Research hypothesis |

### Experiments

| Directory | Intent | Status |
|-----------|--------|--------|
| `experiments/semantic-space-simulation/` | Three artificial semantic spaces + graded Compatible + fail-closed gate | Executable prototype v2 |
| `experiments/adversarial-opacity/` | A1/A2 × graded Compatible harness + stubs | Executable harness |
| `experiments/validator-divergence/` | (reserved) | — |

## Rules

1. No document in `/research` may override ARCH-001 or the RFCs.
2. Empirical claims require pinned data, traces, or public references.
3. “Proof” language is restricted to clearly scoped mathematical claims;
   security or Byzantine-resilience claims remain open unless formally
   established elsewhere.
4. Promotion of any research result into a normative RFC requires an
   Architecture Decision Record (ADR) and explicit revision of the
   target RFC.
5. Every research claim should carry an explicit status marker:
   `DEFINED` / `ASSUMED` / `CONJECTURED` / `PROVED` / `IMPLEMENTED` /
   `EMPIRICALLY TESTED` / `FALSIFIED`.

## Relationship to Phase A

Phase A hardened the normative core without scope explosion.  
Phase B holds the ambitious formal and cryptographic work in a quarantine
where overclaim is easier to prevent and easier to review.

The Human Priority track explores a cross-cutting concern:
preservation of human rights, agency and contestability when machine
representational spaces are no longer human-interpretable. It does not
modify existing invariants.
