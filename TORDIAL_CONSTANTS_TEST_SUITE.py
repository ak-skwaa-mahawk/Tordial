"""
TORDIAL_CONSTANTS_TEST_SUITE.py
Empirical & structural validation harness for Tordial operational constants.

Two Mile Solutions LLC | John B. Carroll
Status: Draft v0.9 — May 2026

This suite does three things:

1. Verifies the internal derivation structure of Tordial constants
   (Carroll Rings → φ_op, π₃D usage, chase ratio, contraction mapping).

2. Compares Tordial geometry (π₃D, φ_op) against standard blueprint geometry
   (flat π, standard φ) across a sweep of angles.

3. Provides hooks for plugging in real measurement data to fit π_eff and
   compare against π₃D (empirical extraction path).

Run directly:

    python TORDIAL_CONSTANTS_TEST_SUITE.py
"""

import math
from dataclasses import dataclass
from typing import List, Tuple, Dict, Callable


# ──────────────────────────────────────────────────────────────────────────────
#  Core Tordial constants & Carroll Rings engine
# ──────────────────────────────────────────────────────────────────────────────

@dataclass
class TordialConstants:
    # Blueprint constants
    flat_pi: float = math.pi
    phi: float = (1 + math.sqrt(5)) / 2

    # Gear shift (open‑chase residue)
    gear_shift: float = 1.04

    # Proposed operational constants
    phi_op: float = 1.65036       # Tordial φ (operational Fibonacci)
    pi_3d: float = 3.20442315     # Proposed 3D operational π
    pi_4d: float = 3.2672536      # Proposed 4D energetic π (exploratory)

    def ring_expansion(self) -> float:
        return self.phi * self.gear_shift

    def ring_settle(self) -> float:
        return (self.ring_expansion() + self.phi) / 2

    def chase_ratio(self) -> float:
        return self.pi_3d / self.phi_op


class CarrollRings:
    """
    Mirrors the structure of carroll_rings.py but in a test‑oriented form.
    """

    def __init__(self, consts: TordialConstants):
        self.c = consts

    def verify_derivation_chain(self, tol: float = 1e-5) -> bool:
        exp_val = self.c.ring_expansion()
        settle = self.c.ring_settle()

        assert abs(exp_val - self.c.phi * self.c.gear_shift) < tol, \
            f"Ring 1 expansion mismatch: {exp_val} vs φ*g"

        assert abs(settle - self.c.phi_op) < tol, \
            f"Ring 2 settle mismatch: {settle} vs φ_op={self.c.phi_op}"

        return True

    def contraction_step(self, x: float) -> float:
        """
        Ring 3 contraction mapping:
            x_{n+1} = (x + φ + φ_exp) / 3
        """
        phi = self.c.phi
        phi_exp = self.c.ring_expansion()
        return (x + phi + phi_exp) / 3

    def verify_contraction(self, x0: float = 1.0, steps: int = 10) -> Tuple[float, List[float]]:
        """
        Confirms that the mapping converges to φ_op and behaves as a contraction.
        Returns final value and the sequence.
        """
        seq = [x0]
        x = x0
        for _ in range(steps):
            x = self.contraction_step(x)
            seq.append(x)

        # Fixed point should be φ_op
        assert abs(x - self.c.phi_op) < 1e-4, \
            f"Contraction did not converge near φ_op: {x} vs {self.c.phi_op}"

        # Check contraction ratio ~ 1/3
        if len(seq) >= 3:
            num = abs(seq[-1] - self.c.phi_op)
            den = abs(seq[-2] - self.c.phi_op) or 1e-12
            ratio = num / den
            assert ratio < 0.5, f"Contraction ratio too large: {ratio} (expected ~1/3)"

        return x, seq


# ──────────────────────────────────────────────────────────────────────────────
#  Toroidal vs blueprint geometry comparison
# ──────────────────────────────────────────────────────────────────────────────

@dataclass
class AngleDriftResult:
    angle_deg: float
    theta_std: float
    theta_3d: float
    force_std: float
    force_3d: float
    work_std: float
    work_3d: float
    d_force: float
    d_work: float


def compute_angle_drift(consts: TordialConstants,
                        angle_deg: float) -> AngleDriftResult:
    theta_std = (consts.flat_pi * angle_deg) / 180.0
    theta_3d = (consts.pi_3d * angle_deg) / 180.0

    f_std = math.sin(theta_std)
    f_3d = math.sin(theta_3d)
    w_std = math.cos(theta_std)
    w_3d = math.cos(theta_3d)

    return AngleDriftResult(
        angle_deg=angle_deg,
        theta_std=theta_std,
        theta_3d=theta_3d,
        force_std=f_std,
        force_3d=f_3d,
        work_std=w_std,
        work_3d=w_3d,
        d_force=f_3d - f_std,
        d_work=w_3d - w_std,
    )


def sweep_angle_drift(consts: TordialConstants,
                      angles: List[float]) -> List[AngleDriftResult]:
    return [compute_angle_drift(consts, a) for a in angles]


# ──────────────────────────────────────────────────────────────────────────────
#  Empirical π extraction hook
# ──────────────────────────────────────────────────────────────────────────────

def fit_pi_eff_from_measurements(
    angle_deg_series: List[float],
    force_meas: List[float],
    work_meas: List[float],
    pi_min: float = 3.0,
    pi_max: float = 3.3,
    steps: int = 2000,
) -> float:
    """
    Brute‑force 1D search for π_eff that best fits measured force/work data.

    This is intentionally simple and transparent; it can be replaced with
    gradient‑based or Bayesian methods later.

    Inputs:
        angle_deg_series: list of angles in degrees
        force_meas:       measured sin‑like component
        work_meas:        measured cos‑like component

    Returns:
        pi_eff_best: π that minimizes squared error vs measurements.
    """
    assert len(angle_deg_series) == len(force_meas) == len(work_meas), \
        "Measurement arrays must be same length."

    def error_for_pi(pi_eff: float) -> float:
        total = 0.0
        for d, f_m, w_m in zip(angle_deg_series, force_meas, work_meas):
            theta = (pi_eff * d) / 180.0
            f_pred = math.sin(theta)
            w_pred = math.cos(theta)
            total += (f_m - f_pred) ** 2 + (w_m - w_pred) ** 2
        return total

    best_pi = None
    best_err = float("inf")

    for i in range(steps + 1):
        pi_eff = pi_min + (pi_max - pi_min) * (i / steps)
        err = error_for_pi(pi_eff)
        if err < best_err:
            best_err = err
            best_pi = pi_eff

    return best_pi


# ──────────────────────────────────────────────────────────────────────────────
#  Pretty printing helpers
# ──────────────────────────────────────────────────────────────────────────────

def print_header(title: str):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80 + "\n")


def print_angle_drift_table(results: List[AngleDriftResult], consts: TordialConstants):
    print(f"Flat π  = {consts.flat_pi:.10f}")
    print(f"π_3D    = {consts.pi_3d:.10f}")
    print(f"φ       = {consts.phi:.10f}")
    print(f"φ_op    = {consts.phi_op:.5f}")
    print(f"Chase R = π_3D / φ_op = {consts.chase_ratio():.6f}\n")

    print(f"{'deg':>7} | {'θ_std':>9} | {'θ_3D':>9} | {'F_std':>9} | {'F_3D':>9} | {'ΔF':>9} | {'W_std':>9} | {'W_3D':>9} | {'ΔW':>9}")
    print("-" * 96)
    for r in results:
        print(
            f"{r.angle_deg:7.2f} | "
            f"{r.theta_std:9.5f} | {r.theta_3d:9.5f} | "
            f"{r.force_std:9.5f} | {r.force_3d:9.5f} | {r.d_force:9.5f} | "
            f"{r.work_std:9.5f}  | {r.work_3d:9.5f}  | {r.d_work:9.5f}"
        )
    print("")


# ──────────────────────────────────────────────────────────────────────────────
#  Test runner
# ──────────────────────────────────────────────────────────────────────────────

def run_structural_tests():
    print_header("TORDIAL STRUCTURAL TESTS — CARROLL RINGS & CONSTANTS")

    consts = TordialConstants()
    rings = CarrollRings(consts)

    # 1. Verify derivation chain
    print("1) Verifying Carroll Rings derivation chain (φ → φ_exp → φ_op)...")
    rings.verify_derivation_chain()
    print("   ✓ Derivation chain holds: φ_exp and φ_op match expected values.\n")

    # 2. Verify contraction mapping
    print("2) Verifying contraction mapping convergence to φ_op...")
    final_val, seq = rings.verify_contraction(x0=0.0, steps=12)
    print(f"   Final value: {final_val:.8f}")
    print(f"   φ_op       : {consts.phi_op:.8f}")
    print("   Sequence:")
    for i, v in enumerate(seq):
        print(f"     x[{i:02d}] = {v:.8f}")
    print("   ✓ Contraction converges to φ_op.\n")

    # 3. Print chase ratio
    print("3) Chase ratio (π_3D / φ_op):")
    print(f"   π_3D      = {consts.pi_3d:.10f}")
    print(f"   φ_op      = {consts.phi_op:.5f}")
    print(f"   R_chase   = {consts.chase_ratio():.10f}\n")


def run_geometry_comparison():
    print_header("TORDIAL GEOMETRY TESTS — TOROIDAL VS BLUEPRINT")

    consts = TordialConstants()
    angles = [0, 22.5, 45, 60, 79, 90, 120, 135, 142.5, 180]
    results = sweep_angle_drift(consts, angles)
    print_angle_drift_table(results, consts)


def run_demo_pi_fit():
    print_header("TORDIAL EMPIRICAL DEMO — π_eff FIT (SYNTHETIC DATA)")

    consts = TordialConstants()

    # Synthetic: assume the "true" system uses π_3D, then add small noise
    import random
    random.seed(42)

    angles = [i for i in range(0, 181, 15)]
    force_meas = []
    work_meas = []

    for d in angles:
        theta = (consts.pi_3d * d) / 180.0
        f = math.sin(theta) + random.gauss(0, 0.002)
        w = math.cos(theta) + random.gauss(0, 0.002)
        force_meas.append(f)
        work_meas.append(w)

    pi_eff = fit_pi_eff_from_measurements(
        angle_deg_series=angles,
        force_meas=force_meas,
        work_meas=work_meas,
        pi_min=3.0,
        pi_max=3.3,
        steps=1500,
    )

    print(f"True π_3D       : {consts.pi_3d:.10f}")
    print(f"Fitted π_eff    : {pi_eff:.10f}")
    print(f"Flat π (ref)    : {consts.flat_pi:.10f}")
    print("\nInterpretation:")
    print("  • If π_eff ≈ π_3D, the Tordial π is supported by the data model.")
    print("  • If π_eff ≈ flat π, the system behaves like a blueprint geometry.")
    print("  • Deviations suggest system‑specific drift or refinement of π_3D.\n")


# ──────────────────────────────────────────────────────────────────────────────
#  Main
# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    run_structural_tests()
    run_geometry_comparison()
    run_demo_pi_fit()