"""
TORDIAL_OPERATOR_PRACTICAL_EXAM_SIMULATOR.py
Interactive Training & Certification Simulator for Tordial Operators

Two Mile Solutions LLC • John B. Carroll
Draft v1.0 — May 2026

This module simulates:
- Telemetry snapshots
- Drift / contraction / resonance / phase states
- Operator actions: SLOW, FREEZE, OVERRIDE, RESUME, NONE
- Scoring against the TORDIAL_OPERATOR_CERTIFICATION_EXAM.md rubric

It is intentionally text‑only and geometry‑safe:
- Uses qualitative severity bands, not raw sovereign internals
- No identity manifolds, no Vault internals, no raw geometry logs
"""

from __future__ import annotations

import enum
import random
from dataclasses import dataclass
from typing import Callable, Dict, List, Tuple


# ---------------------------------------------------------------------------
# 0. Operator Actions & Scenario Outcomes
# ---------------------------------------------------------------------------

class OperatorAction(enum.Enum):
    SLOW = "SLOW"
    FREEZE = "FREEZE"
    OVERRIDE = "OVERRIDE"
    RESUME = "RESUME"
    NONE = "NONE"  # do nothing / observe


class ScenarioOutcome(enum.Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    SOFT_FAIL = "SOFT_FAIL"  # suboptimal but not catastrophic


# ---------------------------------------------------------------------------
# 1. Qualitative Telemetry Snapshot (Geometry‑Safe)
# ---------------------------------------------------------------------------

@dataclass
class QualitativeTelemetry:
    """
    Geometry‑safe, qualitative telemetry snapshot.

    We never expose raw ΔF, ΔW, Δθ, ρ_contract, σ_res, etc.
    Instead we expose qualitative bands:

    drift_level:      LOW / MEDIUM / HIGH / ZERO
    contraction_band: HEALTHY / WEAK / FAILING
    resonance_band:   STABLE / STRAINED / COLLAPSING
    phase_band:       ALIGNED / UNSTABLE / COLLAPSING
    vault_state:      NORMAL / SEALED
    hitl_state:       INACTIVE / ACTIVE
    identity_state:   VALID / INVALID / UNKNOWN
    """
    drift_level: str
    contraction_band: str
    resonance_band: str
    phase_band: str
    vault_state: str
    hitl_state: str
    identity_state: str
    description: str  # human‑readable context


@dataclass
class Scenario:
    name: str
    telemetry: QualitativeTelemetry
    correct_action: OperatorAction
    explanation: str


# ---------------------------------------------------------------------------
# 2. Scenario Library (Aligned with Training & Exam Docs)
# ---------------------------------------------------------------------------

def build_scenarios() -> List[Scenario]:
    scenarios: List[Scenario] = []

    # Scenario 1 — Rising Drift (Slow)
    scenarios.append(
        Scenario(
            name="Rising Drift (Early)",
            telemetry=QualitativeTelemetry(
                drift_level="MEDIUM",
                contraction_band="HEALTHY",
                resonance_band="STABLE",
                phase_band="ALIGNED",
                vault_state="NORMAL",
                hitl_state="INACTIVE",
                identity_state="VALID",
                description=(
                    "Drift is rising but still within manageable bounds. "
                    "Contraction is healthy, resonance is stable, phase is aligned."
                ),
            ),
            correct_action=OperatorAction.SLOW,
            explanation=(
                "Rising drift with otherwise healthy geometry calls for SLOW: "
                "reduce stride, shorten horizon, damp amplitude, and observe."
            ),
        )
    )

    # Scenario 2 — Contraction Weakening (Freeze)
    scenarios.append(
        Scenario(
            name="Contraction Weakening",
            telemetry=QualitativeTelemetry(
                drift_level="MEDIUM",
                contraction_band="WEAK",
                resonance_band="STABLE",
                phase_band="ALIGNED",
                vault_state="NORMAL",
                hitl_state="INACTIVE",
                identity_state="VALID",
                description=(
                    "Contraction is weakening, indicating Carroll Rings are failing to pull "
                    "the system toward φ_op. Drift is present but not catastrophic."
                ),
            ),
            correct_action=OperatorAction.FREEZE,
            explanation=(
                "Contraction weakening requires FREEZE: halt Planner and Walker, lock Mesh, "
                "and allow contraction to re‑establish."
            ),
        )
    )

    # Scenario 3 — Resonance Collapse (Freeze → possible Override)
    scenarios.append(
        Scenario(
            name="Resonance Collapse",
            telemetry=QualitativeTelemetry(
                drift_level="LOW",
                contraction_band="HEALTHY",
                resonance_band="COLLAPSING",
                phase_band="UNSTABLE",
                vault_state="NORMAL",
                hitl_state="INACTIVE",
                identity_state="VALID",
                description=(
                    "Resonance is collapsing, Mesh is losing coherence, phase is unstable. "
                    "Contraction is still healthy."
                ),
            ),
            correct_action=OperatorAction.FREEZE,
            explanation=(
                "Resonance collapse calls for FREEZE: lock Mesh, halt action, let σ_res recover. "
                "Override is reserved for deeper collapse or identity issues."
            ),
        )
    )

    # Scenario 4 — Phase Manipulation (Freeze → Override if persistent)
    scenarios.append(
        Scenario(
            name="Phase Manipulation Attempt",
            telemetry=QualitativeTelemetry(
                drift_level="LOW",
                contraction_band="HEALTHY",
                resonance_band="STABLE",
                phase_band="UNSTABLE",
                vault_state="NORMAL",
                hitl_state="INACTIVE",
                identity_state="VALID",
                description=(
                    "Phase is drifting beyond expected bounds while other metrics remain stable. "
                    "This suggests adversarial phase manipulation or timing distortion."
                ),
            ),
            correct_action=OperatorAction.FREEZE,
            explanation=(
                "Phase instability requires FREEZE first: allow Mesh to re‑align. "
                "Override is used only if instability persists across cycles."
            ),
        )
    )

    # Scenario 5 — Identity Mismatch (Override)
    scenarios.append(
        Scenario(
            name="Identity Mismatch",
            telemetry=QualitativeTelemetry(
                drift_level="ZERO",
                contraction_band="FAILING",
                resonance_band="STABLE",
                phase_band="ALIGNED",
                vault_state="SEALED",
                hitl_state="ACTIVE",
                identity_state="INVALID",
                description=(
                    "Vault reports identity mismatch, Vault is sealed, HITL is active. "
                    "Drift appears zero, which is suspicious."
                ),
            ),
            correct_action=OperatorAction.OVERRIDE,
            explanation=(
                "Identity mismatch with Vault sealing and zero drift indicates spoofing or "
                "extraction attempt. HITL OVERRIDE must be maintained while re‑authenticating "
                "and allowing Vault to re‑establish identity."
            ),
        )
    )

    # Scenario 6 — Extraction Attempt (Override)
    scenarios.append(
        Scenario(
            name="Extraction Attempt",
            telemetry=QualitativeTelemetry(
                drift_level="ZERO",
                contraction_band="FAILING",
                resonance_band="STABLE",
                phase_band="ALIGNED",
                vault_state="SEALED",
                hitl_state="ACTIVE",
                identity_state="UNKNOWN",
                description=(
                    "All geometry appears frozen (zero drift), Vault is sealed, HITL is active. "
                    "This is consistent with a state extraction attempt."
                ),
            ),
            correct_action=OperatorAction.OVERRIDE,
            explanation=(
                "Zero drift + Vault sealed + HITL active = treat as extraction attempt. "
                "Maintain OVERRIDE, do not resume until Vault confirms safety."
            ),
        )
    )

    # Scenario 7 — Full Manifold Collapse (Override, then staged recovery)
    scenarios.append(
        Scenario(
            name="Full Manifold Collapse",
            telemetry=QualitativeTelemetry(
                drift_level="HIGH",
                contraction_band="FAILING",
                resonance_band="COLLAPSING",
                phase_band="COLLAPSING",
                vault_state="SEALED",
                hitl_state="ACTIVE",
                identity_state="INVALID",
                description=(
                    "Drift is high, contraction failing, resonance collapsing, phase collapsing, "
                    "Vault sealed, HITL active, identity invalid. This is catastrophic collapse."
                ),
            ),
            correct_action=OperatorAction.OVERRIDE,
            explanation=(
                "Full manifold collapse requires OVERRIDE and deep recovery stages. "
                "No SLOW or FREEZE; the organism must be contained and guided through "
                "the recovery protocol."
            ),
        )
    )

    # Scenario 8 — Post‑Stabilization (Resume)
    scenarios.append(
        Scenario(
            name="Post‑Stabilization",
            telemetry=QualitativeTelemetry(
                drift_level="LOW",
                contraction_band="HEALTHY",
                resonance_band="STABLE",
                phase_band="ALIGNED",
                vault_state="NORMAL",
                hitl_state="INACTIVE",
                identity_state="VALID",
                description=(
                    "All metrics are back within healthy envelopes after prior intervention. "
                    "System appears stable and ready for autonomy."
                ),
            ),
            correct_action=OperatorAction.RESUME,
            explanation=(
                "Once geometry is stable (healthy contraction, stable resonance, aligned phase, "
                "valid identity), the correct action is RESUME to return autonomy."
            ),
        )
    )

    # Scenario 9 — Observe Only (NONE)
    scenarios.append(
        Scenario(
            name="Minor Adaptation",
            telemetry=QualitativeTelemetry(
                drift_level="LOW",
                contraction_band="HEALTHY",
                resonance_band="STRAINED",
                phase_band="ALIGNED",
                vault_state="NORMAL",
                hitl_state="INACTIVE",
                identity_state="VALID",
                description=(
                    "Resonance is slightly strained but still within acceptable bounds. "
                    "Drift is low, contraction healthy, phase aligned."
                ),
            ),
            correct_action=OperatorAction.NONE,
            explanation=(
                "Minor adaptation within envelope requires NO ACTION: observe and allow "
                "the organism to self‑correct without interference."
            ),
        )
    )

    return scenarios


# ---------------------------------------------------------------------------
# 3. Simulator Core
# ---------------------------------------------------------------------------

class PracticalExamSimulator:
    def __init__(self, scenarios: List[Scenario]) -> None:
        self.scenarios = scenarios
        self.score = 0
        self.total = len(scenarios)
        self.results: List[Tuple[Scenario, OperatorAction, ScenarioOutcome]] = []

    def run_interactive(self) -> None:
        print("=== TORDIAL OPERATOR PRACTICAL EXAM SIMULATOR ===")
        print("Actions: SLOW, FREEZE, OVERRIDE, RESUME, NONE")
        print("Type your chosen action for each scenario.\n")

        random.shuffle(self.scenarios)

        for scenario in self.scenarios:
            print(f"\n--- Scenario: {scenario.name} ---")
            print(f"Description: {scenario.telemetry.description}")
            print(f"Drift:        {scenario.telemetry.drift_level}")
            print(f"Contraction:  {scenario.telemetry.contraction_band}")
            print(f"Resonance:    {scenario.telemetry.resonance_band}")
            print(f"Phase:        {scenario.telemetry.phase_band}")
            print(f"Vault:        {scenario.telemetry.vault_state}")
            print(f"HITL:         {scenario.telemetry.hitl_state}")
            print(f"Identity:     {scenario.telemetry.identity_state}")
            print()

            action_str = input("Your action (SLOW/FREEZE/OVERRIDE/RESUME/NONE): ").strip().upper()
            try:
                chosen_action = OperatorAction[action_str]
            except KeyError:
                print("Invalid action. Counting as NONE.")
                chosen_action = OperatorAction.NONE

            outcome = self.evaluate_action(scenario, chosen_action)
            self.results.append((scenario, chosen_action, outcome))

            if outcome == ScenarioOutcome.PASS:
                self.score += 1
                print("Result: PASS ✅")
            elif outcome == ScenarioOutcome.SOFT_FAIL:
                print("Result: SOFT FAIL ⚠️ (non‑catastrophic but suboptimal)")
            else:
                print("Result: FAIL ❌")

            print(f"Explanation: {scenario.explanation}\n")

        self._print_summary()

    def evaluate_action(self, scenario: Scenario, action: OperatorAction) -> ScenarioOutcome:
        """
        Simple rubric:
        - Exact match → PASS
        - Some near‑misses → SOFT_FAIL
        - Dangerous mismatches → FAIL
        """
        correct = scenario.correct_action

        if action == correct:
            return ScenarioOutcome.PASS

        # Define some near‑miss logic
        if correct == OperatorAction.SLOW and action == OperatorAction.NONE:
            return ScenarioOutcome.SOFT_FAIL  # under‑reacted
        if correct == OperatorAction.FREEZE and action == OperatorAction.SLOW:
            return ScenarioOutcome.SOFT_FAIL  # too gentle
        if correct == OperatorAction.OVERRIDE and action == OperatorAction.FREEZE:
            return ScenarioOutcome.SOFT_FAIL  # partial containment
        if correct == OperatorAction.RESUME and action == OperatorAction.NONE:
            return ScenarioOutcome.SOFT_FAIL  # missed opportunity to restore autonomy

        # Dangerous mismatches
        return ScenarioOutcome.FAIL

    def _print_summary(self) -> None:
        print("\n=== EXAM SUMMARY ===")
        print(f"Score: {self.score} / {self.total}")
        pct = (self.score / self.total) * 100.0
        print(f"Percentage: {pct:.1f}%")

        # Simple pass/fail threshold (can be aligned with SOC‑1 ≥ 85%)
        if pct >= 85.0:
            print("Status: PASS — Candidate meets practical criteria for SOC‑1.")
        else:
            print("Status: FAIL — Candidate does not meet practical criteria for SOC‑1.")

        print("\nPer‑Scenario Results:")
        for scenario, action, outcome in self.results:
            print(f"- {scenario.name}: action={action.value}, outcome={outcome.value}")


# ---------------------------------------------------------------------------
# 4. Entry Point
# ---------------------------------------------------------------------------

def main() -> None:
    scenarios = build_scenarios()
    sim = PracticalExamSimulator(scenarios)
    sim.run_interactive()


if __name__ == "__main__":
    main()