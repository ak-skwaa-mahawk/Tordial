"""
TORDIAL_MANIFOLD_DIAGNOSTICS_SUITE.py
Runtime Geometry Inspection & Diagnostics for the Tordial Sovereign Manifold
Two Mile Solutions LLC • John B. Carroll
Draft v1.0 — May 2026
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto
from math import sin, cos, radians, sqrt
from typing import Iterable, List, Tuple, Optional, Dict


# ---------------------------------------------------------------------------
# 0. Tordial Operational Constants
# ---------------------------------------------------------------------------

PHI_BLUEPRINT: float = 1.61803398875          # classical φ (for reference only)
PHI_EXPANSION_FACTOR: float = 1.04            # Carroll Rings expansion factor

PHI_OP: float = 1.65036                       # operational Fibonacci (running state)
PI_3D: float = 3.20442315                     # running‑state π (toroidal)
PI_FLAT: float = 3.141592653589793            # flat π (reference)

CHASE_RATIO: float = PI_3D / PHI_OP           # π₃D / φ_op
MESH_BASE_FREQ_HZ: float = 79.0               # resonance mesh base frequency

# Default tolerances (can be tuned per deployment)
DEFAULT_DRIFT_EPS: float = 1e-3
DEFAULT_PHASE_LIMIT_RAD: float = 0.05
DEFAULT_CONTRACTION_LIMIT: float = 0.5
DEFAULT_RESONANCE_TOL: float = 0.05


# ---------------------------------------------------------------------------
# 1. Core Data Structures
# ---------------------------------------------------------------------------

@dataclass
class DriftSignature:
    """Toroidal drift signature (ΔF, ΔW, Δθ)."""
    delta_F: float
    delta_W: float
    delta_theta: float  # radians


@dataclass
class ContractionMetrics:
    """Contraction behavior around φ_op."""
    rho_contract: float  # contraction ratio
    x_prev: float
    x_next: float


@dataclass
class ResonanceMetrics:
    """Resonance stability metrics."""
    amplitude: float
    phase: float          # radians
    frequency: float      # Hz
    sigma_res: float      # dimensionless stability score


@dataclass
class ManifoldStateVector:
    """
    Full geometric state vector of the sovereign manifold at a given instant.
    Mirrors the spec across the docs.
    """
    amplitude: float
    phase: float
    frequency: float
    stride: float
    horizon: float
    drift: DriftSignature
    contraction: ContractionMetrics
    resonance: ResonanceMetrics
    override_lambda: float  # λ_override (0 = none, 1 = full override)


class SeverityLevel(Enum):
    GREEN = auto()
    YELLOW = auto()
    ORANGE = auto()
    RED = auto()


@dataclass
class StabilityAssessment:
    """Aggregated stability assessment for the current manifold state."""
    drift_severity: SeverityLevel
    phase_severity: SeverityLevel
    contraction_severity: SeverityLevel
    resonance_severity: SeverityLevel
    overall_severity: SeverityLevel
    notes: List[str]


# ---------------------------------------------------------------------------
# 2. Tordial Geometry Primitives
# ---------------------------------------------------------------------------

def deg_to_rad_3d(deg: float) -> float:
    """
    Convert degrees to radians using π₃D (running‑state π).
    θ_3D = π₃D * deg / 180
    """
    return PI_3D * deg / 180.0


def deg_to_rad_flat(deg: float) -> float:
    """
    Convert degrees to radians using flat π (reference).
    θ_std = π_flat * deg / 180
    """
    return PI_FLAT * deg / 180.0


def compute_drift_from_angle_deg(deg: float) -> DriftSignature:
    """
    Compute toroidal drift signature (ΔF, ΔW, Δθ) for a given angle in degrees.
    F = sin(θ), W = cos(θ)
    3D uses π₃D, std uses flat π.
    """
    theta_3d = deg_to_rad_3d(deg)
    theta_std = deg_to_rad_flat(deg)

    F_3d = sin(theta_3d)
    W_3d = cos(theta_3d)

    F_std = sin(theta_std)
    W_std = cos(theta_std)

    delta_F = F_3d - F_std
    delta_W = W_3d - W_std
    delta_theta = theta_3d - theta_std

    return DriftSignature(delta_F=delta_F, delta_W=delta_W, delta_theta=delta_theta)


def carroll_expansion_phi(phi_blueprint: float = PHI_BLUEPRINT,
                          expansion_factor: float = PHI_EXPANSION_FACTOR) -> float:
    """φ_exp = φ * 1.04 (Carroll Rings expansion)."""
    return phi_blueprint * expansion_factor


def carroll_phi_op(phi_blueprint: float = PHI_BLUEPRINT,
                   expansion_factor: float = PHI_EXPANSION_FACTOR) -> float:
    """
    φ_op = (φ + φ_exp) / 2
    Operational midpoint between blueprint φ and expanded φ.
    """
    phi_exp = carroll_expansion_phi(phi_blueprint, expansion_factor)
    return (phi_blueprint + phi_exp) / 2.0


def contraction_step(x_n: float,
                     phi_blueprint: float = PHI_BLUEPRINT,
                     expansion_factor: float = PHI_EXPANSION_FACTOR) -> float:
    """
    x_{n+1} = (x_n + φ + φ_exp) / 3
    Carroll Rings contraction map.
    """
    phi_exp = carroll_expansion_phi(phi_blueprint, expansion_factor)
    return (x_n + phi_blueprint + phi_exp) / 3.0


def contraction_metrics(x_n: float,
                        phi_op: float = PHI_OP,
                        phi_blueprint: float = PHI_BLUEPRINT,
                        expansion_factor: float = PHI_EXPANSION_FACTOR) -> ContractionMetrics:
    """
    Compute contraction ratio ρ_contract around φ_op.
    ρ_contract = |x_{n+1} - φ_op| / |x_n - φ_op|
    """
    x_next = contraction_step(x_n, phi_blueprint, expansion_factor)
    num = abs(x_next - phi_op)
    den = abs(x_n - phi_op) if abs(x_n - phi_op) > 0 else 1e-12
    rho = num / den
    return ContractionMetrics(rho_contract=rho, x_prev=x_n, x_next=x_next)


# ---------------------------------------------------------------------------
# 3. Resonance & Mesh Diagnostics
# ---------------------------------------------------------------------------

def mesh_timestep(phi_op: float = PHI_OP,
                  base_freq_hz: float = MESH_BASE_FREQ_HZ) -> float:
    """
    T_mesh = (1 / 79) * φ_op
    Living timestep of the resonance mesh.
    """
    return (1.0 / base_freq_hz) * phi_op


def mesh_phase(phi_op: float = PHI_OP,
               base_freq_hz: float = MESH_BASE_FREQ_HZ) -> float:
    """
    θ_mesh = (79° * π₃D) / 180
    Phase reference for the mesh.
    """
    return deg_to_rad_3d(base_freq_hz)  # using 79° as in the spec


def resonance_metrics_from_state(amplitude: float,
                                 phase_rad: float,
                                 frequency_hz: float,
                                 phi_op: float = PHI_OP,
                                 chase_ratio: float = CHASE_RATIO) -> ResonanceMetrics:
    """
    Compute resonance stability σ_res as a simple deviation from the chase ratio.
    σ_res ~ 1 - normalized deviation.
    """
    # Effective velocity proxy: v = A * f
    v = amplitude * frequency_hz
    target_v = chase_ratio  # using chase ratio as target invariant
    dev = abs(v - target_v)
    # Normalize with a soft scale to keep σ_res in [0, 1]
    scale = abs(target_v) + 1e-9
    sigma_res = max(0.0, 1.0 - dev / scale)
    return ResonanceMetrics(
        amplitude=amplitude,
        phase=phase_rad,
        frequency=frequency_hz,
        sigma_res=sigma_res,
    )


# ---------------------------------------------------------------------------
# 4. Stability Assessment
# ---------------------------------------------------------------------------

def _severity_from_value(value: float,
                         thresholds: Tuple[float, float, float]) -> SeverityLevel:
    """
    Map a scalar value to a severity level given three thresholds:
    (ε1, ε2, ε3) → Green, Yellow, Orange, Red.
    """
    eps1, eps2, eps3 = thresholds
    if value < eps1:
        return SeverityLevel.GREEN
    if value < eps2:
        return SeverityLevel.YELLOW
    if value < eps3:
        return SeverityLevel.ORANGE
    return SeverityLevel.RED


def assess_stability(state: ManifoldStateVector,
                     drift_eps: float = DEFAULT_DRIFT_EPS,
                     phase_limit: float = DEFAULT_PHASE_LIMIT_RAD,
                     contraction_limit: float = DEFAULT_CONTRACTION_LIMIT,
                     resonance_tol: float = DEFAULT_RESONANCE_TOL) -> StabilityAssessment:
    """
    Assess stability of the current manifold state using Tordial‑aligned thresholds.
    """
    notes: List[str] = []

    # Drift magnitude
    drift_mag = sqrt(
        state.drift.delta_F ** 2 +
        state.drift.delta_W ** 2 +
        state.drift.delta_theta ** 2
    )
    drift_sev = _severity_from_value(
        drift_mag,
        (drift_eps, 5 * drift_eps, 20 * drift_eps)
    )
    if drift_sev != SeverityLevel.GREEN:
        notes.append(f"Drift magnitude elevated: {drift_mag:.4e}")

    # Phase deviation
    phase_dev = abs(state.drift.delta_theta)
    phase_sev = _severity_from_value(
        phase_dev,
        (phase_limit * 0.25, phase_limit * 0.75, phase_limit)
    )
    if phase_sev != SeverityLevel.GREEN:
        notes.append(f"Phase deviation elevated: {phase_dev:.4e} rad")

    # Contraction
    rho = state.contraction.rho_contract
    contraction_sev = _severity_from_value(
        rho,
        (contraction_limit * 0.5, contraction_limit, 0.75)
    )
    if contraction_sev != SeverityLevel.GREEN:
        notes.append(f"Contraction ratio elevated: ρ={rho:.4f}")

    # Resonance
    res_dev = abs(1.0 - state.resonance.sigma_res)
    resonance_sev = _severity_from_value(
        res_dev,
        (resonance_tol * 0.5, resonance_tol, 2 * resonance_tol)
    )
    if resonance_sev != SeverityLevel.GREEN:
        notes.append(f"Resonance stability degraded: σ_res={state.resonance.sigma_res:.4f}")

    # Overall severity = max of all
    overall = max(drift_sev, phase_sev, contraction_sev, resonance_sev, key=lambda s: s.value)

    return StabilityAssessment(
        drift_severity=drift_sev,
        phase_severity=phase_sev,
        contraction_severity=contraction_sev,
        resonance_severity=resonance_sev,
        overall_severity=overall,
        notes=notes,
    )


# ---------------------------------------------------------------------------
# 5. Manifold State Construction Helpers
# ---------------------------------------------------------------------------

def build_manifold_state_from_telemetry(
    *,
    angle_deg: float,
    stride: float,
    horizon: float,
    amplitude: float,
    frequency_hz: float = MESH_BASE_FREQ_HZ,
    phi_op: float = PHI_OP,
) -> ManifoldStateVector:
    """
    Construct a ManifoldStateVector from basic telemetry:
    - angle_deg: current system angle (deg)
    - stride: Walker stride
    - horizon: Planner horizon
    - amplitude: Mesh amplitude
    - frequency_hz: Mesh frequency (default 79 Hz)
    """
    drift = compute_drift_from_angle_deg(angle_deg)
    contraction = contraction_metrics(x_n=stride, phi_op=phi_op)
    phase_mesh = mesh_phase(phi_op=phi_op, base_freq_hz=frequency_hz)
    resonance = resonance_metrics_from_state(
        amplitude=amplitude,
        phase_rad=phase_mesh,
        frequency_hz=frequency_hz,
        phi_op=phi_op,
        chase_ratio=CHASE_RATIO,
    )

    return ManifoldStateVector(
        amplitude=amplitude,
        phase=phase_mesh,
        frequency=frequency_hz,
        stride=stride,
        horizon=horizon,
        drift=drift,
        contraction=contraction,
        resonance=resonance,
        override_lambda=0.0,
    )


# ---------------------------------------------------------------------------
# 6. Diagnostics API
# ---------------------------------------------------------------------------

def diagnose_manifold_state(
    state: ManifoldStateVector,
    *,
    drift_eps: float = DEFAULT_DRIFT_EPS,
    phase_limit: float = DEFAULT_PHASE_LIMIT_RAD,
    contraction_limit: float = DEFAULT_CONTRACTION_LIMIT,
    resonance_tol: float = DEFAULT_RESONANCE_TOL,
) -> Dict[str, object]:
    """
    High‑level diagnostic entry point.
    Returns a structured dict suitable for logging, UI, or Vault ingestion.
    """
    assessment = assess_stability(
        state,
        drift_eps=drift_eps,
        phase_limit=phase_limit,
        contraction_limit=contraction_limit,
        resonance_tol=resonance_tol,
    )

    return {
        "state": state,
        "assessment": assessment,
        "summary": {
            "overall_severity": assessment.overall_severity.name,
            "drift_severity": assessment.drift_severity.name,
            "phase_severity": assessment.phase_severity.name,
            "contraction_severity": assessment.contraction_severity.name,
            "resonance_severity": assessment.resonance_severity.name,
        },
        "notes": assessment.notes,
    }


# ---------------------------------------------------------------------------
# 7. CLI / Quick‑Look Utility
# ---------------------------------------------------------------------------

def _severity_color(sev: SeverityLevel) -> str:
    """Simple text color mapping for quick CLI inspection."""
    if sev == SeverityLevel.GREEN:
        return "GREEN"
    if sev == SeverityLevel.YELLOW:
        return "YELLOW"
    if sev == SeverityLevel.ORANGE:
        return "ORANGE"
    return "RED"


def quick_inspect(
    angle_deg: float,
    stride: float,
    horizon: float,
    amplitude: float,
    frequency_hz: float = MESH_BASE_FREQ_HZ,
) -> None:
    """
    Quick CLI‑style inspection of the manifold state for a single sample.
    """
    state = build_manifold_state_from_telemetry(
        angle_deg=angle_deg,
        stride=stride,
        horizon=horizon,
        amplitude=amplitude,
        frequency_hz=frequency_hz,
    )
    diag = diagnose_manifold_state(state)

    assessment: StabilityAssessment = diag["assessment"]  # type: ignore

    print("=== TORDIAL MANIFOLD DIAGNOSTICS ===")
    print(f"Angle (deg): {angle_deg:.3f}")
    print(f"Stride:      {state.stride:.6f}")
    print(f"Horizon:     {state.horizon:.6f}")
    print(f"Amplitude:   {state.amplitude:.6f}")
    print(f"Frequency:   {state.frequency:.3f} Hz")
    print()
    print(f"ΔF:          {state.drift.delta_F:.6e}")
    print(f"ΔW:          {state.drift.delta_W:.6e}")
    print(f"Δθ:          {state.drift.delta_theta:.6e} rad")
    print(f"ρ_contract:  {state.contraction.rho_contract:.6f}")
    print(f"σ_res:       {state.resonance.sigma_res:.6f}")
    print()
    print("Severity:")
    print(f"  Drift:       {_severity_color(assessment.drift_severity)}")
    print(f"  Phase:       {_severity_color(assessment.phase_severity)}")
    print(f"  Contraction: {_severity_color(assessment.contraction_severity)}")
    print(f"  Resonance:   {_severity_color(assessment.resonance_severity)}")
    print(f"  Overall:     {_severity_color(assessment.overall_severity)}")
    if assessment.notes:
        print("\nNotes:")
        for n in assessment.notes:
            print(f"  - {n}")
    print("====================================")


if __name__ == "__main__":
    # Example quick‑look run; tweak values to see severity transitions.
    quick_inspect(
        angle_deg=79.0,
        stride=1.0,
        horizon=1.0 * PHI_OP,
        amplitude=PHI_OP,
        frequency_hz=MESH_BASE_FREQ_HZ,
    )