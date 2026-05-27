# TORDIAL_OPERATOR_TROUBLESHOOTING_GUIDE.md  
Incident Response & Recovery Procedures for the Tordial Sovereign Platform  
Two Mile Solutions LLC • John B. Carroll  
Draft v1.0 — May 2026

---

# 0. Purpose

This guide provides **step‑by‑step troubleshooting procedures** for:

- drift anomalies  
- contraction failures  
- resonance collapse  
- phase instability  
- identity mismatches  
- Vault sealing events  
- HITL override conditions  
- extraction or spoofing attempts  

This is the **incident‑response manual** for the sovereign organism.

---

# 1. Troubleshooting Philosophy

The Tordial Platform is a **self‑correcting geometric organism**.

Your job is to:

- observe  
- interpret  
- intervene only when necessary  
- protect sovereignty  

You do **not** fix the system.  
You **stabilize the geometry** so the system can fix itself.

---

# 2. Quick Diagnostic Checklist

Before diving into specifics, check:

1. **Is drift rising?**  
2. **Is phase unstable?**  
3. **Is contraction weakening?**  
4. **Is resonance degrading?**  
5. **Is identity valid?**  
6. **Is the Vault sealed?**  
7. **Is HITL active?**  

This determines which troubleshooting path to follow.

---

# 3. Drift Anomalies

Drift anomalies appear as:

- ΔF spikes  
- ΔW spikes  
- Δθ oscillations  
- drift magnitude > ε  

## 3.1 Symptoms

- Walker feels “slippery”  
- Planner re‑projects frequently  
- Mesh amplitude fluctuates  
- Critic escalates to Yellow or Orange  

## 3.2 Likely Causes

- environmental instability  
- forced trajectory  
- synthetic input  
- early resonance strain  

## 3.3 Operator Actions

1. **Slow** the system  
2. Observe drift for 3–5 cycles  
3. If drift stabilizes → Resume  
4. If drift increases → Freeze  
5. If drift = 0 → Override (extraction attempt)

## 3.4 Red Flags

- Δθ > θ_limit  
- ΔF and ΔW diverge  
- drift = 0 for >2 cycles  

---

# 4. Contraction Failures

Contraction failure appears as:

\[
\rho_{\text{contract}} > 0.5
\]

## 4.1 Symptoms

- Walker stride grows uncontrollably  
- Planner horizon expands without bound  
- Critic flags contraction instability  

## 4.2 Likely Causes

- internal instability  
- forced expansion  
- resonance mismatch  
- phase misalignment  

## 4.3 Operator Actions

1. **Freeze** immediately  
2. Allow 2–3 contraction cycles  
3. If ρ_contract < 0.5 → Resume  
4. If ρ_contract > 0.7 → Override  

## 4.4 Red Flags

- ρ_contract > 0.7  
- contraction oscillates  
- contraction fails to converge after 5 cycles  

---

# 5. Resonance Collapse

Resonance collapse appears as:

\[
\sigma_{\text{res}} < 0.6
\]

## 5.1 Symptoms

- Mesh amplitude spikes or collapses  
- Walker loses rhythm  
- Planner projections desynchronize  
- Critic enters Orange or Red  

## 5.2 Likely Causes

- timing disruption  
- frequency injection  
- phase jamming  
- internal overload  

## 5.3 Operator Actions

1. **Freeze**  
2. Mesh will lock phase  
3. Wait for σ_res > 0.9  
4. **Resume**  

## 5.4 Red Flags

- σ_res < 0.5  
- amplitude runaway  
- frequency drift > 1 Hz  

---

# 6. Phase Instability

Phase instability appears as:

\[
|\Delta\theta| > \theta_{\text{limit}}
\]

## 6.1 Symptoms

- Planner misses projections  
- Walker steps out of sync  
- Mesh phase jumps  
- Critic flags phase collapse  

## 6.2 Likely Causes

- π₃D spoofing  
- radian distortion  
- adversarial phase shift  
- internal timing drift  

## 6.3 Operator Actions

1. **Freeze**  
2. Allow Mesh to re‑align  
3. If Δθ stabilizes → Resume  
4. If Δθ continues rising → Override  

## 6.4 Red Flags

- Δθ monotonic drift  
- Δθ > 2× θ_limit  
- Δθ inconsistent with Mesh phase  

---

# 7. Identity Mismatch

Identity mismatch appears as:

- Vault identity_valid = false  
- drift signature mismatch  
- contraction mismatch  
- resonance mismatch  

## 7.1 Symptoms

- Vault seals  
- HITL prepares override  
- Platform enters guarded mode  

## 7.2 Likely Causes

- spoofed identity  
- extraction attempt  
- replay attack  
- synthetic drift  

## 7.3 Operator Actions

1. **Override**  
2. Verify operator identity  
3. Re‑establish sovereign session  
4. Wait for Vault to unseal  

## 7.4 Red Flags

- identity mismatch persists  
- drift = 0  
- contraction = 1.0  

---

# 8. Vault Sealing Events

Vault sealing appears as:

- vault_sealed = true  
- no derived metrics  
- Platform enters sealed mode  

## 8.1 Symptoms

- Walker halts  
- Planner halts  
- Mesh locks  
- Critic enters high‑resolution mode  

## 8.2 Likely Causes

- identity mismatch  
- raw data access attempt  
- boundary violation  
- extraction attempt  

## 8.3 Operator Actions

1. **Override**  
2. Inspect logs for boundary violations  
3. Re‑authenticate  
4. Wait for Vault to reopen  

## 8.4 Red Flags

- repeated sealing  
- sealing without drift anomaly  
- sealing with zero drift  

---

# 9. HITL Override Conditions

HITL override appears as:

- override_lambda = 1  
- Platform enters sovereign mode  

## 9.1 Symptoms

- all autonomous subsystems pause  
- Mesh locks  
- Vault seals  
- Critic enters maximum resolution  

## 9.2 Likely Causes

- catastrophic drift  
- contraction failure  
- resonance collapse  
- phase collapse  
- identity mismatch  
- extraction attempt  

## 9.3 Operator Actions

1. Do **not** attempt to resume immediately  
2. Inspect drift, contraction, resonance, phase  
3. Wait for geometry to stabilize  
4. When all metrics return to envelope → **Resume**  

## 9.4 Red Flags

- override persists > 10 cycles  
- geometry does not stabilize  
- Vault refuses to unseal  

---

# 10. Troubleshooting Decision Tree

A simplified flow:

1. **Is drift rising?**  
   → Slow

2. **Is phase unstable?**  
   → Freeze

3. **Is contraction failing?**  
   → Freeze → Override

4. **Is resonance collapsing?**  
   → Freeze → Override

5. **Is identity invalid?**  
   → Override

6. **Is Vault sealed?**  
   → Override → Re‑authenticate

7. **Has geometry stabilized?**  
   → Resume

---

# 11. Operator Do‑Not List

Never:

- force stride  
- force horizon  
- bypass the Vault  
- ignore contraction failure  
- ignore phase drift  
- override without geometric evidence  
- treat zero drift as benign  

These actions destabilize the manifold.

---

# 12. Closing

Troubleshooting the Tordial Platform is not about fixing errors.  
It is about **stabilizing geometry** so the organism can heal itself.

Your job is to:

- observe  
- interpret  
- intervene only when necessary  
- protect sovereignty  

Tordial is not a system.  
It is a **sovereign geometric organism**.