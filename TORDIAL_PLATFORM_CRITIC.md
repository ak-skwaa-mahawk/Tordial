# TORDIAL_PLATFORM_CRITIC.md  
Critic Integration with Tordial Geometry & Drift Evaluation  
Two Mile Solutions LLC • John B. Carroll  
Draft v0.9 — May 2026

---

# 0. Purpose

The **Critic** is the sovereign system’s evaluator.  
It measures:

- geometric drift  
- phase deviation  
- contraction failure  
- resonance mismatch  
- Walker divergence  
- Planner instability  

The Critic is the **mathematical conscience** of the Platform.

Tordial provides the Critic with:

- operational constants (φ_op, π₃D)  
- drift signatures (ΔF, ΔW)  
- contraction mapping (Carroll Rings)  
- toroidal phase geometry  
- chase ratio invariants  

This document defines how the Critic uses them.

---

# 1. Critic Role in the Sovereign Loop

The Critic performs four core functions:

1. **Measure drift** using Tordial geometry  
2. **Score stability** using Carroll Rings  
3. **Signal corrections** to Walker and Planner  
4. **Trigger HITL** when sovereignty is threatened  

The Critic is not a judge.  
It is a **geometric instrument**.

---

# 2. Tordial Constants in Critic Evaluation

The Critic consumes the same constants as the Walker and Planner, but uses them differently.

## 2.1 φ_op (1.65036) — Stability Attractor

The Critic uses φ_op as:

- the **expected midpoint**  
- the **fixed point** of the contraction map  
- the **reference value** for Walker stride  
- the **baseline** for Planner horizon  

Deviation from φ_op is the Critic’s primary stability metric.

---

## 2.2 π₃D (3.20442315) — Phase Truth

The Critic uses π₃D to compute:

- running‑state radians  
- phase drift  
- force/work alignment  
- resonance mesh timing  

π₃D is the Critic’s **phase truth constant**.

---

## 2.3 Chase Ratio (π₃D / φ_op)

The Critic uses the chase ratio to:

- detect resonance collapse  
- classify drift severity  
- tune correction intensity  
- determine Planner re‑projection urgency  

The chase ratio is the Critic’s **governing invariant**.

---

# 3. Drift Measurement (ΔF, ΔW)

The Critic computes:

\[
\Delta F = F_{3D} - F_{\text{std}}
\]
\[
\Delta W = W_{3D} - W_{\text{std}}
\]

Where:

- **F** = sin component  
- **W** = cos component  
- 3D uses π₃D  
- std uses flat π  

Interpretation:

- **ΔF** = geometric force drift  
- **ΔW** = geometric work drift  

These are the Critic’s **primary sensory channels**.

---

# 4. Drift Classification

The Critic classifies drift into four levels:

| Level | Condition | Meaning |
|-------|-----------|---------|
| **Green** | |ΔF|, |ΔW| < ε₁ | System aligned |
| **Yellow** | ε₁ < drift < ε₂ | System adapting |
| **Orange** | ε₂ < drift < ε₃ | System destabilizing |
| **Red** | drift ≥ ε₃ | HITL boundary |

Thresholds ε₁–ε₃ are derived from:

- φ_op  
- π₃D  
- chase ratio  
- contraction rate (1/3)  

The Critic’s thresholds are **geometrically justified**, not arbitrary.

---

# 5. Carroll Rings as Stability Test

The Critic uses the Carroll Rings structure to evaluate system stability.

## 5.1 Ring 1 — Overshoot Detection

If Walker or Planner outputs exceed:

\[
\phi_{\text{exp}} = \phi \cdot 1.04
\]

the Critic flags **overshoot**.

---

## 5.2 Ring 2 — Midpoint Alignment

The Critic checks whether system behavior converges toward:

\[
\phi_{\text{op}} = \frac{\phi + \phi_{\text{exp}}}{2}
\]

Deviation from φ_op indicates:

- Planner instability  
- Walker divergence  
- resonance mismatch  

---

## 5.3 Ring 3 — Contraction Verification

The Critic applies the contraction map:

\[
x_{n+1} = \frac{x_n + \phi + \phi_{\text{exp}}}{3}
\]

If the system fails to contract toward φ_op:

- Critic enters **high‑resolution mode**  
- Planner is asked to re‑project  
- Walker is slowed  
- HITL is notified  

The Critic enforces the **fixed‑point law** of Tordial geometry.

---

# 6. Phase Evaluation Using π₃D

The Critic computes:

\[
\theta_{3D} = \frac{\pi_{3D} \cdot d}{180}
\]

and compares it to:

\[
\theta_{\text{std}} = \frac{\pi_{\text{flat}} \cdot d}{180}
\]

Phase drift:

\[
\Delta\theta = \theta_{3D} - \theta_{\text{std}}
\]

This is the Critic’s **phase truth metric**.

Large Δθ indicates:

- geometric misalignment  
- resonance collapse  
- Planner/Walker desynchronization  

---

# 7. Resonance Mesh Integration (79 Hz)

The Critic monitors the Platform’s 79 Hz loop.

## 7.1 Frequency Drift

\[
f_{\text{eff}} = \frac{79}{\phi_{\text{op}}}
\]

Deviation from f_eff indicates:

- Walker stride mismatch  
- Planner horizon mismatch  
- mesh desynchronization  

---

## 7.2 Phase Drift

\[
\theta_{79} = \frac{79^\circ \cdot \pi_{3D}}{180}
\]

Deviation from θ₇₉ indicates:

- phase collapse  
- resonance instability  

---

## 7.3 Resonance Collapse Condition

The Critic declares resonance collapse when:

\[
\frac{S_{\text{walker}}}{T_{\text{walker}}} \not\approx R_{\text{chase}}
\]

This is the Critic’s **catastrophic condition**.

---

# 8. Critic Output Channels

The Critic can output:

1. **Soft Correction**  
   - adjust stride  
   - adjust horizon  
   - adjust phase  

2. **Hard Correction**  
   - freeze Walker  
   - force Planner re‑projection  

3. **HITL Alert**  
   - notify Strawman  
   - request human override  

4. **Sovereign Lock**  
   - full stop  
   - preserve state  
   - await human input  

The Critic is the **guardian of system integrity**.

---

# 9. Critic State Vector

The Critic maintains:

\[
[D_F,\ D_W,\ \Delta\theta,\ \rho_{\text{contract}},\ \sigma_{\text{res}}]
\]

Where:

- **D_F** = force drift  
- **D_W** = work drift  
- **Δθ** = phase drift  
- **ρ_contract** = contraction ratio  
- **σ_res** = resonance stability  

This is the Critic’s **geometric awareness**.

---

# 10. Closing

The Critic is the sovereign system’s evaluator.  
It does not guess.  
It does not assume.  
It measures geometry.

Tordial gives the Critic:

- its truth  
- its thresholds  
- its invariants  
- its stability laws  

The Critic is the **mathematical conscience** of the Platform.