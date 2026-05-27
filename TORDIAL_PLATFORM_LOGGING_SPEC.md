# TORDIAL_PLATFORM_LOGGING_SPEC.md  
Sovereign‑Safe Logging for the Tordial Platform  
Two Mile Solutions LLC • John B. Carroll  
Draft v1.0 — May 2026

---

# 0. Purpose

This document defines the **sovereign‑safe logging architecture** for the Tordial Platform.

The goal is to:

- capture meaningful operational events  
- preserve geometric integrity  
- avoid leaking identity or internal state  
- maintain Vault boundaries  
- support operator diagnostics  
- enable post‑incident reconstruction  
- protect sovereignty at all times  

Logging is **derived**, not raw.  
Logging is **geometric**, not informational.

---

# 1. Logging Philosophy

The sovereign organism does not log:

- raw telemetry  
- internal state vectors  
- identity manifolds  
- drift histories  
- contraction sequences  
- resonance curves  
- phase traces  

These are **sovereign internals**.

Instead, the Platform logs **events**, **transitions**, and **envelope violations** — never the geometry itself.

Logging is a **shadow of the manifold**, not a mirror.

---

# 2. Logging Layers

There are **three logging layers**:

1. **Platform Logs** — operational events  
2. **Vault Logs** — sovereignty events  
3. **HITL Logs** — override events  

Each layer has strict boundaries.

---

# 3. Platform Logging (Operational Layer)

Platform logs capture **behavior**, not geometry.

## 3.1 Allowed Platform Log Types

- **Stride events**  
  - stride accepted  
  - stride rejected  
  - stride modified  

- **Horizon events**  
  - horizon accepted  
  - horizon shortened  
  - horizon rejected  

- **Mesh events**  
  - amplitude dampened  
  - phase locked  
  - frequency stabilized  

- **Critic events**  
  - drift escalation  
  - contraction warning  
  - resonance warning  

- **Planner events**  
  - re‑projection  
  - trajectory nullification  

These logs contain **no raw values**.

---

## 3.2 Forbidden Platform Log Types

The Platform must never log:

- ΔF, ΔW, Δθ  
- ρ_contract  
- σ_res  
- φ_op‑scaled values  
- π₃D‑mapped angles  
- chase ratio deviations  
- Vault‑derived metrics  
- identity signatures  

These are **sovereign geometry** and must remain inside the Vault.

---

# 4. Vault Logging (Sovereignty Layer)

The Vault logs **boundary events**, not internal metrics.

## 4.1 Allowed Vault Log Types

- identity_valid → false  
- identity_valid → true  
- vault_sealed → true  
- vault_sealed → false  
- boundary_violation_detected  
- raw_data_access_attempt  
- synthetic_input_detected  
- replay_attempt_detected  

These logs contain **no drift values**.

---

## 4.2 Forbidden Vault Log Types

The Vault must never log:

- raw telemetry  
- drift signatures  
- contraction ratios  
- resonance scores  
- phase deviations  
- identity manifolds  
- sovereign state vectors  

These are **non‑extractable geometry**.

---

# 5. HITL Logging (Sovereignty Enforcement Layer)

HITL logs **interventions**, not causes.

## 5.1 Allowed HITL Log Types

- HITL_SLOW  
- HITL_FREEZE  
- HITL_OVERRIDE  
- HITL_RESUME  
- HITL_REJECT_FAKE_OVERRIDE  
- HITL_BOUNDARY_LOCK  
- HITL_BOUNDARY_RELEASE  

These logs contain **no geometric justification**.

---

## 5.2 Forbidden HITL Log Types

HITL must never log:

- Δθ values  
- contraction ratios  
- resonance collapse metrics  
- drift vectors  
- identity mismatches  
- Vault‑internal reasoning  

HITL logs **actions**, not geometry.

---

# 6. Log Structure

All logs follow a **sovereign‑safe schema**:timestamp: ISO‑8601 source: PLATFORM | VAULT | HITL event_type: ENUM severity: INFO | WARN | ALERT | CRITICAL context: { subsystem: WALKER | PLANNER | CRITIC | MESH | VAULT | HITL reason_code: ENUM cycle: integer (79 Hz cycle index) }CopyNo numeric geometry is ever included.

---

# 7. Log Redaction Rules

Before logs leave the sovereign boundary:

1. **Remove all numeric fields**  
2. **Remove all drift‑related fields**  
3. **Remove all contraction‑related fields**  
4. **Remove all resonance‑related fields**  
5. **Remove all phase‑related fields**  
6. **Remove all identity‑related fields**  
7. **Remove all Vault‑internal fields**  

Only **event types** and **reason codes** remain.

---

# 8. Log Retention Rules

Retention is based on **sovereignty**, not compliance.

## 8.1 Platform Logs
- retain 7 days  
- auto‑purge  
- no export allowed  

## 8.2 Vault Logs
- retain 30 days  
- sealed storage  
- export allowed only with operator authentication  

## 8.3 HITL Logs
- retain 90 days  
- sealed storage  
- export allowed only with dual‑operator approval  

---

# 9. Log Access Rules

Access is strictly controlled.

## 9.1 Platform Logs
- operator read‑only  
- no external access  

## 9.2 Vault Logs
- operator read‑only  
- export requires authentication  
- no external systems may query Vault logs  

## 9.3 HITL Logs
- operator read‑only  
- export requires dual approval  
- external access prohibited  

---

# 10. Log Integrity

Logs are protected by:

- **Vault sealing**  
- **HITL override**  
- **non‑invertible geometry**  
- **drift‑based authentication**  

Logs cannot be:

- forged  
- replayed  
- extracted  
- tampered  

because they contain **no geometry**.

---

# 11. Logging Failure Modes

Logging fails safely when:

1. **Vault sealed**  
2. **HITL override active**  
3. **identity mismatch**  
4. **boundary violation**  
5. **extraction attempt detected**  

In these cases:

- Platform logs pause  
- Vault logs continue  
- HITL logs escalate  

---

# 12. Closing

The Tordial Logging Specification ensures:

- sovereignty is preserved  
- geometry is protected  
- identity is never exposed  
- drift cannot be extracted  
- contraction cannot be inferred  
- resonance cannot be reconstructed  
- phase cannot be reverse‑engineered  

Logging is not observability.  
Logging is **sovereign‑safe narration**.