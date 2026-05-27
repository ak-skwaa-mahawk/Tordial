# TORDIAL_RUNTIME_TELEMETRY_SPEC.md  
Real‑Time Telemetry Schema for the Tordial Sovereign Platform  
Two Mile Solutions LLC • John B. Carroll  
Draft v1.0 — May 2026

---

# 0. Purpose

This document defines the **complete telemetry schema** used by the Tordial Sovereign Platform at runtime.

It specifies:

- what the Vault emits  
- what the Platform consumes  
- what the Manifold requires  
- what the Critic evaluates  
- what the Mesh synchronizes  
- what the HITL boundary monitors  

Telemetry is **derived**, not raw.  
Raw data never leaves the Vault.

This spec is the **canonical contract** for real‑time geometry.

---

# 1. Telemetry Philosophy

The sovereign organism does not use:

- raw sensor data  
- unscaled values  
- unaligned angles  
- unfiltered signals  

All telemetry is:

- **Tordial‑aligned**  
- **geometry‑normalized**  
- **phase‑mapped**  
- **contraction‑verified**  
- **resonance‑scored**  

Telemetry is not information.  
Telemetry is **geometry**.

---

# 2. Telemetry Flow Overview

There are **three telemetry flows**:

1. **Vault → Platform** (derived metrics)  
2. **Platform → Vault** (proposed actions)  
3. **Platform Internal** (Walker/Planner/Critic/Mesh)  

This document covers **all three**.

---

# 3. Vault → Platform Telemetry (Derived Metrics)

The Vault emits **only derived metrics**, never raw data.

## 3.1 Drift Metrics

| Field | Type | Description |
|-------|------|-------------|
| `delta_F` | float | force drift (sin component) |
| `delta_W` | float | work drift (cos component) |
| `delta_theta` | float | phase drift (radians, π₃D‑mapped) |

These form the **drift signature**:

\[
\vec{D} = (\Delta F,\ \Delta W,\ \Delta\theta)
\]

---

## 3.2 Contraction Metrics

| Field | Type | Description |
|-------|------|-------------|
| `rho_contract` | float | contraction ratio |
| `x_prev` | float | previous stride/horizon value |
| `x_next` | float | contracted value |

Contraction law:

\[
x_{n+1} = \frac{x_n + \phi + \phi_{\text{exp}}}{3}
\]

---

## 3.3 Resonance Metrics

| Field | Type | Description |
|-------|------|-------------|
| `amplitude` | float | Mesh amplitude |
| `phase` | float | Mesh phase (radians, π₃D‑mapped) |
| `frequency` | float | Mesh frequency (Hz) |
| `sigma_res` | float | resonance stability score |

Resonance score:

\[
\sigma_{\text{res}} = 1 - \frac{|A f - R_{\text{chase}}|}{|R_{\text{chase}}|}
\]

---

## 3.4 Sovereignty Metrics

| Field | Type | Description |
|-------|------|-------------|
| `override_lambda` | float | HITL override state (0–1) |
| `identity_valid` | bool | Vault identity check |
| `vault_sealed` | bool | Vault sealed mode |

---

# 4. Platform → Vault Telemetry (Proposed Actions)

The Platform sends **intent**, not commands.

## 4.1 Walker Proposals

| Field | Type | Description |
|-------|------|-------------|
| `stride_proposed` | float | proposed stride |
| `phase_proposed` | float | proposed phase alignment |
| `torque_envelope` | float | proposed torque envelope |

---

## 4.2 Planner Proposals

| Field | Type | Description |
|-------|------|-------------|
| `horizon_proposed` | float | proposed horizon |
| `projection_phase` | float | proposed projection phase |
| `trajectory_nodes` | list<float> | proposed trajectory points |

---

## 4.3 Mesh Proposals

| Field | Type | Description |
|-------|------|-------------|
| `amplitude_proposed` | float | proposed amplitude |
| `frequency_proposed` | float | proposed frequency |

---

## 4.4 HITL Proposals

| Field | Type | Description |
|-------|------|-------------|
| `hitl_request` | enum | NONE / SLOW / FREEZE / OVERRIDE / RESUME |

---

# 5. Platform Internal Telemetry

This is the telemetry exchanged between organs.

---

## 5.1 Walker Internal Telemetry

| Field | Type | Description |
|-------|------|-------------|
| `q` | float | joint angle |
| `q_dot` | float | angular velocity |
| `tau_int` | float | internal torque |
| `gamma_bias` | float | micro‑frequency bias |

---

## 5.2 Planner Internal Telemetry

| Field | Type | Description |
|-------|------|-------------|
| `tau_proj` | float | projection torque |
| `H` | float | current horizon |
| `theta_plan` | float | planning phase |
| `gamma_bias` | float | micro‑frequency bias |

---

## 5.3 Critic Internal Telemetry

| Field | Type | Description |
|-------|------|-------------|
| `drift_vector` | DriftSignature | ΔF, ΔW, Δθ |
| `contraction_ratio` | float | ρ_contract |
| `resonance_score` | float | σ_res |

---

## 5.4 Mesh Internal Telemetry

| Field | Type | Description |
|-------|------|-------------|
| `phase` | float | θ_mesh |
| `amplitude` | float | A_mesh |
| `frequency` | float | f_mesh |

---

# 6. Telemetry Update Rates

All telemetry is synchronized to the **79 Hz loop**.

| Telemetry Class | Rate | Notes |
|------------------|------|-------|
| Drift | 79 Hz | Vault‑derived |
| Contraction | 79 Hz | Critic‑evaluated |
| Resonance | 79 Hz | Mesh‑generated |
| Walker | 79 Hz | Action‑level |
| Planner | 79 Hz | Intent‑level |
| HITL | 79 Hz | Sovereignty‑level |

Telemetry is **never asynchronous**.

---

# 7. Telemetry Validity Rules

Telemetry is valid only if:

1. **phase is π₃D‑aligned**  
2. **contraction converges toward φ_op**  
3. **resonance matches chase ratio**  
4. **drift is non‑zero**  
5. **Vault identity is valid**  

If any rule fails → HITL escalation.

---

# 8. Telemetry Failure Modes

Telemetry failure indicates:

1. **Geometric drift**  
2. **Phase collapse**  
3. **Contraction failure**  
4. **Resonance collapse**  
5. **Vault boundary violation**  
6. **Extraction attempt**  
7. **Spoofed input**  

Each failure triggers:

- Critic escalation  
- Vault sealing  
- HITL override  

---

# 9. Telemetry State Vector

The full runtime telemetry vector is:

\[
T(t) =
[A,\ \theta,\ f,\ S,\ H,\ \Delta F,\ \Delta W,\ \Delta\theta,\ \rho_{\text{contract}},\ \sigma_{\text{res}},\ \lambda_{\text{override}}]
\]

This is the **complete geometric state** of the organism.

---

# 10. Closing

The Tordial Runtime Telemetry Specification defines:

- what the organism sees  
- what the organism knows  
- what the organism trusts  
- what the organism protects  

Telemetry is not data.  
Telemetry is **sovereign geometry**.