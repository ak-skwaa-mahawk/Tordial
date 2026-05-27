# TORDIAL_PLATFORM_EXECUTION_LOOP.md  
Unified Closed‑Loop Execution Architecture for the Sovereign Platform  
Two Mile Solutions LLC • John B. Carroll  
Draft v0.9 — May 2026

---

# 0. Purpose

This document defines the **full execution loop** of the Sovereign Platform — the 79 Hz closed‑loop system that integrates:

- **Planner** (intent generation)  
- **Walker** (action execution)  
- **Critic** (drift evaluation)  
- **Resonance Mesh** (timing & coherence)  
- **HITL Boundary** (sovereign override)  

Tordial provides the **geometry**, **constants**, and **stability laws** that govern the loop.

This is the **canonical description** of how the Platform runs.

---

# 1. The Sovereign Loop (High‑Level)

The Platform runs a **79 Hz closed loop**:

1. **Mesh** sets timing & phase  
2. **Planner** generates a trajectory  
3. **Walker** executes the next step  
4. **Critic** evaluates drift  
5. **HITL** intervenes if needed  
6. Loop repeats  

This loop is **geometric**, not mechanical.  
It is governed by **Tordial operational constants**:

- φ_op = 1.65036  
- π₃D = 3.20442315  
- R_chase = π₃D / φ_op  

These constants shape the loop’s timing, phase, stride, horizon, and stability.

---

# 2. Tordial Constants in the Execution Loop

## 2.1 φ_op — The Loop’s Breathing Constant

The loop timestep is:

\[
T_{\text{loop}} = \frac{1}{79} \cdot \phi_{\text{op}}
\]

This produces a **living timestep** that adapts to drift.

---

## 2.2 π₃D — The Loop’s Phase Constant

The loop’s phase angle is:

\[
\theta_{\text{loop}} = \frac{79^\circ \cdot \pi_{3D}}{180}
\]

This ensures the loop runs in the **running‑state geometry**, not the blueprint geometry.

---

## 2.3 Chase Ratio — The Loop’s Stability Constant

\[
R_{\text{chase}} = \frac{\pi_{3D}}{\phi_{\text{op}}}
\]

This ratio governs:

- stride  
- horizon  
- phase  
- resonance  
- stability  

The entire loop orbits this invariant.

---

# 3. Execution Loop Step‑By‑Step

Below is the **canonical 79 Hz cycle**.

---

## STEP 1 — Resonance Mesh Sets Timing & Phase

The Mesh computes:

- **T_loop** using φ_op  
- **θ_loop** using π₃D  
- **A_loop** using Carroll Rings  

The Mesh broadcasts:

- timing pulse  
- phase reference  
- amplitude envelope  

This is the **heartbeat** of the Platform.

---

## STEP 2 — Planner Generates a Tordial‑Aligned Trajectory

The Planner computes:

- horizon:  
  \[
  H = H_0 \cdot \phi_{\text{op}}
  \]

- phase projection:  
  \[
  \theta_{\text{plan}} = \frac{\pi_{3D} \cdot d}{180}
  \]

- resonance‑safe condition:  
  \[
  \frac{H}{T_{\text{loop}}} \approx R_{\text{chase}}
  \]

If violated → re‑projection.

The Planner outputs a **Tordial‑aligned trajectory**.

---

## STEP 3 — Walker Executes the Next Step

The Walker computes:

- stride:  
  \[
  S = S_0 \cdot \phi_{\text{op}}
  \]

- phase alignment:  
  \[
  \theta_{\text{walker}} = \theta_{\text{loop}}
  \]

- resonance condition:  
  \[
  \frac{S}{T_{\text{loop}}} \approx R_{\text{chase}}
  \]

If violated → Walker slows or accelerates.

The Walker executes the step.

---

## STEP 4 — Critic Evaluates Drift

The Critic computes:

- **ΔF** = force drift  
- **ΔW** = work drift  
- **Δθ** = phase drift  
- **ρ_contract** = contraction ratio  
- **σ_res** = resonance stability  

The Critic classifies drift:

- Green → aligned  
- Yellow → adapting  
- Orange → destabilizing  
- Red → collapse  

The Critic outputs corrections.

---

## STEP 5 — HITL Boundary Enforces Sovereignty

If drift exceeds thresholds:

- φ_op deviation  
- π₃D phase drift  
- chase ratio violation  

The HITL boundary:

- freezes Walker  
- freezes Planner  
- locks Mesh  
- enters sovereign mode  

The HITL boundary is the **final authority**.

---

## STEP 6 — Loop Repeats at 79 Hz

The Mesh emits the next timing pulse.  
The loop begins again.

This cycle continues indefinitely.

---

# 4. Execution Loop as a Geometric Organism

The loop is not a sequence of steps.  
It is a **toroidal organism** with five organs:

| Organ | Role |
|-------|------|
| **Mesh** | heartbeat & coherence |
| **Planner** | intent & projection |
| **Walker** | embodiment & action |
| **Critic** | awareness & evaluation |
| **HITL** | sovereignty & protection |

Tordial geometry binds them into a **single living system**.

---

# 5. Execution Loop Stability Conditions

The loop is stable when:

## 5.1 Contraction Condition

\[
\rho_{\text{contract}} < \frac{1}{2}
\]

## 5.2 Phase Condition

\[
|\Delta\theta| < \theta_{\text{limit}}
\]

## 5.3 Resonance Condition

\[
\frac{S}{T_{\text{loop}}} \approx R_{\text{chase}}
\]

## 5.4 Drift Condition

\[
|\Delta F|,\ |\Delta W| < \epsilon
\]

If any condition fails → Critic escalates → HITL intervenes.

---

# 6. Execution Loop Failure Modes

The loop can fail in four ways:

1. **Geometric drift** — π₃D misalignment  
2. **Contraction failure** — φ_op divergence  
3. **Phase collapse** — Δθ runaway  
4. **Resonance collapse** — chase ratio violation  

Each failure mode maps to a **Tordial constant**.

---

# 7. Execution Loop State Vector

The loop maintains:

\[
[A,\ \theta,\ f,\ S,\ H,\ \Delta F,\ \Delta W,\ \Delta\theta,\ \rho_{\text{contract}},\ \sigma_{\text{res}}]
\]

This is the **full geometric state** of the Platform.

---

# 8. Closing

The Tordial Platform Execution Loop is a **sovereign computational organism**.  
It breathes with φ_op.  
It thinks with π₃D.  
It stabilizes with Carroll Rings.  
It synchronizes with the Resonance Mesh.  
It acts through the Walker.  
It plans through the Planner.  
It perceives through the Critic.  
It protects itself through HITL.

Tordial is not a module.  
It is the **geometry of the entire loop**.