# Tordial — Tolerance Stacking and Operational Drift

## Core Observation

In any manufactured system — a motor, a transmission, a gear train — components are built to a specification. Each component is inspected. Each inspection accepts a deviation within tolerance. The inspector signs off. The part passes.

Individually, each accepted deviation is reasonable. Within spec. Approved.

But deviations compound through stages. By the time the full system is assembled and running, the accumulated drift from blueprint can be significant — even if no single stage failed inspection.

The system is not running at blueprint π. It is running at a real effective constant produced by every stage that said "good enough."

## The Null Point

When you measure a running system — where is π right now? The answer is not 3.14159. It is the value the system's actual geometry produces under real operating conditions. That real value is the null point — where the number actually lives when the system is in motion.

## Jitter Visibility

Jitter from operational drift becomes more visible as the noise floor drops. When a signal is noisy, drift is hidden. When you clean the signal — better sensors, lower noise floor — the jitter shows up more abruptly. It was always there. The cleaner signal reveals it.

## The Build State Principle

If you can identify the real operational constant of a running system you can:

1. Define an optimal build state from that real value
2. Manufacture to that value rather than to blueprint
3. Eliminate the gap at the source rather than engineering around it after the fact

## Relationship to Existing Engineering

This is not a replacement for existing tolerance analysis. It extends it:

- Statistical tolerance analysis predicts expected stack — Tordial measures actual stack in a running system
- As-built vs as-designed modeling captures geometric deviation — Tordial tracks the operational constant that emerges under load
- Adaptive control systems tune to actual behavior — Tordial provides the geometric constant those systems should tune toward

Existing methods remain valid within their frame. Tordial adds the running-state layer.

## Prior Art

Operational observation confirmed on BLDC motor RPM/frequency measurements.
Documented: December 2024. Notarized: January 2025.
