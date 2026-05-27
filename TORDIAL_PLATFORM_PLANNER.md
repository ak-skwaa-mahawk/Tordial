# TORDIAL_PLATFORM_PLANNER.md  
Planner Integration with Tordial Geometry & Operational Constants  
Two Mile Solutions LLC • John B. Carroll  
Draft v0.9 — May 2026

---

# 0. Purpose

The **Planner** is the sovereign system’s strategist.  
It generates:

- trajectories  
- horizons  
- projections  
- intent vectors  
- resonance‑aligned plans  

The Planner must operate **inside Tordial geometry**, using:

- φ_op (operational Fibonacci)  
- π₃D (running‑state π)  
- Carroll Rings stability envelope  
- toroidal drift signatures  
- chase ratio invariants  

This document defines how the Planner integrates these structures.

---

# 1. Planner Role in the Sovereign Loop

The Planner is responsible for:

1. **Trajectory generation**  
2. **Horizon shaping**  
3. **Phase‑aligned projection**  
4. **Drift‑aware replanning**  
5. **Resonance‑safe intent formation**  
6. **Providing Walker with executable paths**  
7. **Providing Critic with expected geometry**  

The Planner is not a pathfinder.  
It is a **geometric strategist**.

---

# 2. Tordial Constants in Planner Computation

The Planner consumes the same constants as Walker and Critic, but uses them to **shape trajectories**, not evaluate or execute them.

## 2.1 φ_op (1.65036) — Horizon Scaling Constant

The Planner uses φ_op to compute:

- horizon length  
- branching factor  
- expansion rate  
- contraction rate  

Planner horizon:

\[
H_{\text{planner}} = H_0 \cdot \phi_{\text{op}}
\]

This ensures the Planner’s “look‑ahead” is **operational**, not blueprint‑static.

---

## 2.2 π₃D (3.20442315) — Phase Projection Constant

The Planner uses π₃D to compute:

- phase‑aligned trajectories  
- rotational projections  
- toroidal path curvature  
- resonance‑safe turning angles  

Planner radian conversion:

\[
\theta_{\text{plan}} = \frac{\pi_{3D} \cdot d}{180}
\]

This ensures the Planner’s geometry matches the **running system**, not the idealized one.

---

## 2.3 Chase Ratio (π₃D / φ_op)

The Planner uses the chase ratio to:

- tune branching  
- modulate horizon depth  
- classify trajectory stability  
- determine re‑projection urgency  

Planner modulation factor:

\[
M_{\text{plan}} = \frac{\pi_{3D}}{\phi_{\text{op}}}
\]

This is the Planner’s **governing invariant**.

---

# 3. Carroll Rings as Trajectory Envelope

The Planner uses the three‑ring structure to shape trajectories.

## 3.1 Ring 1 — Expansion (Exploration)

Exploratory trajectories expand to:

\[
\phi_{\text{exp}} = \phi \cdot 1.04
\]

This defines the **maximum exploratory horizon**.

---

## 3.2 Ring 2 — Settle (Operational Midpoint)

The Planner’s stable horizon is:

\[
H_{\text{stable}} = H_0 \cdot \phi_{\text{op}}
\]

This is the **Planner’s home horizon**.

---

## 3.3 Ring 3 — Lock (Contraction)

The Planner contracts unstable trajectories using:

\[
H_{n+1} = \frac{H_n + H_{\text{exp}} + H_{\text{stable}}}{3}
\]

This ensures the Planner always returns to the **operational midpoint**.

---

# 4. Toroidal Drift in Planning

The Planner receives drift signals from the Critic:

- **ΔF** — force drift  
- **ΔW** — work drift  
- **Δθ** — phase drift  

The Planner interprets drift as:

- **ΔF > 0:** reduce horizon  
- **ΔF < 0:** expand horizon  
- **ΔW > 0:** accelerate projection  
- **ΔW < 0:** stabilize projection  
- **Δθ > threshold:** re‑project trajectory  

The Planner is a **drift‑responsive strategist**.

---

# 5. Planner in the 79 Hz Resonance Mesh

The Planner operates inside the Platform’s 79 Hz loop.

## 5.1 Planner timestep

\[
T_{\text{plan}} = \frac{1}{79} \cdot \phi_{\text{op}}
\]

This produces a **living projection interval**.

---

## 5.2 Planner phase alignment

\[
\theta_{79} = \frac{79^\circ \cdot \pi_{3D}}{180}
\]

The Planner uses this to:

- align trajectories  
- avoid phase collapse  
- maintain resonance with Walker  

---

## 5.3 Resonance‑safe planning condition

The Planner ensures:

\[
\frac{H_{\text{planner}}}{T_{\text{plan}}} \approx R_{\text{chase}}
\]

If violated:

- Planner re‑projects  
- Critic enters high‑resolution mode  
- Walker slows  

---

# 6. Planner–Walker–Critic Closed Loop

The Planner participates in the sovereign triad:

1. **Planner** generates trajectories  
2. **Walker** executes them  
3. **Critic** evaluates drift  

The Planner’s responsibilities:

- generate Tordial‑aligned trajectories  
- adjust horizon using φ_op  
- align phase using π₃D  
- respond to drift using ΔF, ΔW, Δθ  
- maintain resonance using chase ratio  
- re‑project when Critic signals instability  

The Planner is the **intent engine** of the sovereign system.

---

# 7. HITL Boundary Interaction

The Planner is the subsystem most affected by HITL intervention.

When Strawman detects:

- excessive drift  
- contraction failure  
- resonance collapse  
- Walker instability  

The Planner receives:

- **horizon freeze**  
- **trajectory nullification**  
- **manual override**  
- **re‑projection lockout**  

The Planner must obey HITL immediately.

---

# 8. Planner State Vector (Tordial‑Aligned)

The Planner maintains:

\[
[\tau_{\text{proj}},\ H,\ \theta_{\text{plan}},\ \gamma_{\text{bias}}]
\]

Where:

- **τ_proj** — projection torque  
- **H** — horizon length  
- **θ_plan** — phase angle  
- **γ_bias** — micro‑frequency bias  

This is the Planner’s **geometric state**.

---

# 9. Planner Failure Modes (Tordial Interpretation)

The Planner can fail in four ways:

1. **Geometric drift** — π₃D misalignment  
2. **Horizon divergence** — φ_op contraction failure  
3. **Phase collapse** — resonance mismatch  
4. **Projection runaway** — τ_proj instability  

Each failure mode maps to a **Tordial constant**.

---

# 10. Closing

The Planner is not a pathfinder.  
It is a **toroidal strategist** generating trajectories inside a **living geometry**.

Tordial gives the Planner:

- its horizon  
- its phase  
- its drift response  
- its resonance  
- its stability  

The Planner is the **intent‑shaping organ** of the sovereign Platform.