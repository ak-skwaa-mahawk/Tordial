# TORDIAL_PLATFORM_INTEGRATION.md  
Integration of Tordial Geometry with the 79 Hz Sovereign Platform Loop  
Two Mile Solutions LLC • John B. Carroll  
Draft v0.9 — May 2026

---

# 0. Purpose

This document defines how the **Tordial geometric framework** integrates with the **Sovereign Platform (79 Hz)** execution loop.  
It specifies:

- how **operational constants** (φ_op, π₃ᴅ) enter the Platform timing model  
- how **Carroll Rings** define the stability envelope  
- how **toroidal drift** becomes a governance‑layer signal  
- how the Platform’s **walker–planner–critic** loop uses Tordial invariants  
- how the **HITL boundary** (Strawman) consumes Tordial drift metrics

This is the **canonical integration layer** between geometry and governance.

---

# 1. Architectural Overview

The Sovereign Platform is a **closed‑loop, 79 Hz resonance engine** composed of:

1. **Walker** — executes actions in the environment  
2. **Planner** — generates trajectories  
3. **Critic** — evaluates drift, deviation, and resonance  
4. **HITL Boundary** — human‑in‑the‑loop override and sovereignty guard  
5. **Resonance Mesh** — 79 Hz timing and feedback lattice  

Tordial provides the **mathematical substrate** for:

- timing  
- drift detection  
- stability  
- phase alignment  
- operational constant selection  

The Platform is the **executor**.  
Tordial is the **geometry**.

---

# 2. Tordial Constants in Platform Timing

## 2.1 Operational Fibonacci (φ_op = 1.65036)

φ_op replaces φ in all **running‑state timing envelopes**.

The Platform uses φ_op to compute:

- **trajectory expansion windows**  
- **planner horizon scaling**  
- **critic decay curves**  
- **walker step‑size modulation**

The Platform’s timing constant:

\[
T_{\text{step}} = \frac{1}{79\ \text{Hz}} \cdot \phi_{\text{op}}
\]

This produces a **living timestep** that breathes with the system.

---

## 2.2 Operational π (π₃ᴅ = 3.20442315)

π₃ᴅ replaces flat π in:

- radian conversion  
- phase alignment  
- resonance mesh timing  
- drift detection  

The Platform’s phase angle:

\[
\theta_{79} = \frac{79^\circ \cdot \pi_{3D}}{180}
\]

This ensures the Platform’s internal oscillators run in the **same geometry** as the system they govern.

---

# 3. Carroll Rings as Stability Envelope

The Platform uses the **three‑ring structure** as a stability classifier.

## 3.1 Ring 1 — Expansion (overshoot)

Walker actions that exceed expected bounds are mapped to:

\[
\phi_{\text{exp}} = \phi \cdot 1.04
\]

This defines the **maximum safe overshoot** before the critic intervenes.

---

## 3.2 Ring 2 — Settle (midpoint)

The midpoint:

\[
\phi_{\text{op}} = \frac{\phi + \phi_{\text{exp}}}{2}
\]

is the **Platform’s target stability point**.

Planner trajectories are biased toward φ_op.

---

## 3.3 Ring 3 — Lock (3‑way attractor)

The critic uses the contraction:

\[
x_{n+1} = \frac{x_n + \phi + \phi_{\text{exp}}}{3}
\]

to determine whether the system is:

- converging  
- diverging  
- oscillating  
- locked  

This is the **core stability test** for the Platform.

---

# 4. Toroidal Drift as Governance Signal

The Platform continuously computes:

\[
\Delta F = F_{3D} - F_{\text{std}},\quad \Delta W = W_{3D} - W_{\text{std}}
\]

These drift values feed into:

- **critic scoring**  
- **walker correction**  
- **planner re‑projection**  
- **HITL alerts**  

Interpretation:

- **Low drift:** system aligned  
- **Medium drift:** system adapting  
- **High drift:** system entering instability  
- **Extreme drift:** HITL boundary triggers

Drift is not noise — it is the **governance signal**.

---

# 5. Integration with the 79 Hz Resonance Mesh

The Platform’s 79 Hz loop is defined by:

\[
f = 79\ \text{Hz}
\]

Tordial modifies the loop via:

## 5.1 φ_op scaling

\[
f_{\text{eff}} = \frac{79}{\phi_{\text{op}}}
\]

This produces a **dynamic resonance frequency** that adapts to system drift.

---

## 5.2 π₃ᴅ phase correction

\[
\theta_{\text{eff}} = \frac{79^\circ \cdot \pi_{3D}}{180}
\]

This ensures the Platform’s internal oscillators remain **phase‑aligned** with the running geometry.

---

## 5.3 Chase Ratio (π₃ᴅ / φ_op)

The chase ratio:

\[
R_{\text{chase}} = \frac{\pi_{3D}}{\phi_{\text{op}}}
\]

is used to:

- tune the critic’s sensitivity  
- modulate walker step‑size  
- adjust planner horizon length  
- stabilize the resonance mesh  

This ratio is the **bridge constant** between geometry and execution.

---

# 6. HITL Boundary Integration (Strawman)

The Strawman HITL system consumes Tordial metrics:

- φ_op deviation  
- π₃ᴅ phase drift  
- ΔF, ΔW drift signatures  
- chase ratio anomalies  
- contraction‑mapping divergence  

When thresholds are exceeded:

- HITL override is activated  
- walker is slowed  
- planner is frozen  
- critic enters high‑resolution mode  

Tordial provides the **mathematical justification** for HITL intervention.

---

# 7. Platform API Integration Points

The following Platform modules consume Tordial values:

| Platform Module | Tordial Input | Purpose |
|-----------------|---------------|---------|
| **resonance.py** | π₃ᴅ, φ_op | timing, phase, drift |
| **planner.py** | φ_op | horizon scaling |
| **walker.py** | chase ratio | step modulation |
| **critic.py** | ΔF, ΔW | stability scoring |
| **hitl.py** | drift thresholds | override logic |
| **mesh79.py** | π₃ᴅ | oscillator alignment |

Tordial constants are injected at Platform initialization.

---

# 8. Execution Flow (High‑Level)

1. **Walker** executes an action  
2. **Critic** measures drift (ΔF, ΔW)  
3. **Planner** adjusts trajectory using φ_op  
4. **Resonance Mesh** updates phase using π₃ᴅ  
5. **Chase Ratio** modulates step‑size  
6. **HITL Boundary** monitors for divergence  
7. Loop repeats at **79 Hz / φ_op**

This is the **closed‑loop sovereign execution cycle**.

---

# 9. Future Extensions

- Replace fixed 1.04 gear‑shift with empirical drift model  
- Integrate Trinity κ/π correction into Platform timing  
- Add multi‑node Tordial drift consensus for distributed systems  
- Extend π₄ᴅ into energetic‑state prediction  
- Build Tordial‑native planner (φ_op‑based tree search)

---

# 10. Closing

Tordial is not an add‑on to the Platform.  
It is the **mathematical substrate** the Platform was always meant to run on.

The Platform is the executor.  
Tordial is the geometry.  
Together they form a **sovereign computational organism**.