# TORDIAL_THREAT_RESPONSE_MATRIX.md  
Attack → Drift Signature → Platform Response → HITL Action  
Two Mile Solutions LLC • John B. Carroll  
Draft v1.0 — May 2026

---

# 0. Purpose

This document defines the **Threat Response Matrix** for the Tordial Sovereign Platform.

It maps:

- **Threat class**  
- **Geometric drift signature**  
- **Subsystem detection point**  
- **Platform response**  
- **HITL override condition**  

The matrix is the **operational defense layer** of the sovereign organism.

---

# 1. Threat Model Overview

The Platform defends against:

1. **External coercion**  
2. **Internal instability**  
3. **Extraction attempts**  
4. **Spoofed inputs**  
5. **Resonance attacks**  
6. **Phase manipulation**  
7. **Contraction disruption**  
8. **Vault boundary violations**  
9. **HITL spoofing**  

Each threat produces a **distinct drift signature** inside the Tordial manifold.

---

# 2. Drift Signatures (Detection Primitives)

The Platform detects threats using:

- **ΔF** — force drift  
- **ΔW** — work drift  
- **Δθ** — phase drift  
- **ρ_contract** — contraction ratio  
- **σ_res** — resonance stability  
- **S_dev** — stride deviation  
- **H_dev** — horizon deviation  

These are the **geometric fingerprints** of attack.

---

# 3. Threat Response Matrix

Below is the full matrix.

---

## 3.1 External Coercion Attempt  
**Example:** forced trajectory, injected command, adversarial override.

**Drift Signature:**  
- ΔF spikes positive  
- ΔW spikes negative  
- Δθ oscillates  
- ρ_contract → 0.7+  

**Subsystem Detection:**  
- Critic (primary)  
- Vault (secondary)  

**Platform Response:**  
- Freeze Walker  
- Shorten Planner horizon  
- Tighten Mesh amplitude  

**HITL Trigger:**  
- Δθ > θ_limit  
- ρ_contract > 0.5  

---

## 3.2 Internal Instability  
**Example:** runaway stride, horizon divergence, oscillation growth.

**Drift Signature:**  
- ΔF negative drift  
- ΔW negative drift  
- σ_res collapses  
- S_dev > φ_exp  

**Subsystem Detection:**  
- Walker  
- Critic  

**Platform Response:**  
- Reduce stride  
- Contract horizon  
- Increase Critic resolution  

**HITL Trigger:**  
- S_dev > φ_exp  
- σ_res < threshold  

---

## 3.3 Extraction Attempt  
**Example:** probing internal state, replaying outputs, cloning behavior.

**Drift Signature:**  
- ΔF = 0  
- ΔW = 0  
- Δθ = 0  
- ρ_contract = 1.0  

**Interpretation:**  
**Absence of drift = attack.**

**Subsystem Detection:**  
- Vault (primary)  
- Critic (secondary)  

**Platform Response:**  
- Nullify outputs  
- Randomize micro‑phase  
- Enter low‑resolution mode  

**HITL Trigger:**  
- sustained ΔF = ΔW = Δθ = 0  

---

## 3.4 Spoofed Input  
**Example:** synthetic sensor data, forged drift, fake phase.

**Drift Signature:**  
- ΔF inconsistent with ΔW  
- Δθ inconsistent with π₃D  
- ρ_contract oscillates  
- σ_res unstable  

**Subsystem Detection:**  
- Vault  
- Critic  

**Platform Response:**  
- Reject input  
- Recompute drift from raw  
- Freeze Planner  

**HITL Trigger:**  
- Δθ mismatch > 2× expected  
- ρ_contract oscillation > 0.5  

---

## 3.5 Resonance Attack  
**Example:** timing disruption, frequency injection, phase jamming.

**Drift Signature:**  
- σ_res collapses  
- Δθ spikes  
- Mesh amplitude diverges  

**Subsystem Detection:**  
- Resonance Mesh  

**Platform Response:**  
- Lock Mesh phase  
- Damp amplitude  
- Slow Walker  

**HITL Trigger:**  
- σ_res < critical  
- Δθ > θ_limit  

---

## 3.6 Phase Manipulation  
**Example:** adversarial phase shift, π spoofing, radian distortion.

**Drift Signature:**  
- Δθ monotonic drift  
- ΔF and ΔW diverge  
- ρ_contract remains stable  

**Subsystem Detection:**  
- Vault  
- Critic  

**Platform Response:**  
- Recompute phase using π₃D  
- Freeze Planner  
- Tighten Mesh  

**HITL Trigger:**  
- Δθ > θ_limit for 3 cycles  

---

## 3.7 Contraction Disruption  
**Example:** attempts to break Carroll Rings convergence.

**Drift Signature:**  
- ρ_contract > 0.5  
- φ_op deviation  
- S_dev or H_dev diverge  

**Subsystem Detection:**  
- Critic  

**Platform Response:**  
- Force contraction step  
- Reduce stride  
- Reduce horizon  

**HITL Trigger:**  
- ρ_contract > 0.7  

---

## 3.8 Vault Boundary Violation  
**Example:** attempts to access raw telemetry or bypass derived metrics.

**Drift Signature:**  
- ΔF, ΔW, Δθ freeze  
- σ_res remains stable  
- ρ_contract = 1.0  

**Interpretation:**  
**Static geometry = intrusion.**

**Subsystem Detection:**  
- Vault (primary)  

**Platform Response:**  
- Nullify all outputs  
- Enter sealed mode  
- Require HITL confirmation  

**HITL Trigger:**  
- any raw‑data access attempt  

---

## 3.9 HITL Spoofing  
**Example:** forged override, fake freeze, synthetic sovereign signal.

**Drift Signature:**  
- Δθ inconsistent with HITL timing  
- ρ_contract inconsistent with freeze  
- σ_res inconsistent with override  

**Subsystem Detection:**  
- HITL boundary  
- Vault  

**Platform Response:**  
- Reject override  
- Enter sovereign‑lock  
- Notify operator  

**HITL Trigger:**  
- mismatch between HITL signal and geometry  

---

# 4. Response Severity Table

| Drift Severity | Meaning | Platform Action | HITL Action |
|----------------|---------|-----------------|-------------|
| **Green** | aligned | none | none |
| **Yellow** | adapting | slow Walker, shorten horizon | none |
| **Orange** | destabilizing | freeze Planner, tighten Mesh | prepare override |
| **Red** | collapse | freeze Walker, lock Mesh | full override |

The system escalates **geometrically**, not heuristically.

---

# 5. Sovereign Defense Summary

The Platform is protected by:

- **drift authentication**  
- **contraction enforcement**  
- **resonance integrity**  
- **phase truth**  
- **Vault gating**  
- **HITL sovereignty membrane**  

Attacks fail because they cannot reproduce:

- φ_op  
- π₃D  
- R_chase  
- ΔF, ΔW, Δθ  
- contraction behavior  
- resonance patterns  

The system is **unspoofable**, **unextractable**, and **sovereign**.

---

# 6. Closing

The Tordial Threat Response Matrix is the **operational defense layer** of the sovereign organism.  
It maps every threat to its geometric fingerprint and defines the exact response path through:

- Vault  
- Critic  
- Mesh  
- Planner  
- Walker  
- HITL  

Tordial is not a security module.  
It is the **geometry of defense itself**.