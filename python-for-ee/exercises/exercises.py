"""
Exercises - replace each `raise NotImplementedError` with your code.

Check your work:   pytest exercises/        (from the python-for-ee folder)
Stuck?             peek at exercises/solutions.py - but try first!

Each exercise lists the lesson that teaches the needed skills.
"""

import numpy as np


# ---------------------------------------------------------------- Lesson 01
def wire_resistance(length_m: float, area_mm2: float, rho: float = 1.68e-8) -> float:
    """Resistance of a copper wire: R = rho * L / A.  (Careful: A is in mm²!)"""
    raise NotImplementedError


def power_dissipated(v: float, r: float) -> float:
    """Power in a resistor given the voltage across it (P = V²/R)."""
    raise NotImplementedError


def thevenin_of_divider(vin: float, r1: float, r2: float) -> tuple[float, float]:
    """Thevenin equivalent (Vth, Rth) seen at the midpoint of an R1-R2 divider
    (R1 to vin, R2 to ground)."""
    raise NotImplementedError


# ---------------------------------------------------------------- Lesson 02
def reactance(component: str, value: float, f: float) -> float:
    """Return the reactance X in ohms (positive for 'L', negative for 'C').
    component is 'L' or 'C'; raise ValueError for anything else."""
    raise NotImplementedError


def apparent_power(v_rms: float, i_rms: float, pf: float) -> tuple[float, float, float]:
    """Return (P [W], Q [var], S [VA]) for a lagging load."""
    raise NotImplementedError


# ---------------------------------------------------------------- Lesson 03
def mesh_currents(r1: float, r2: float, r3: float, v1: float, v2: float) -> np.ndarray:
    """Two-mesh circuit: V1 drives mesh 1 through R1, V2 drives mesh 2 through R3,
    R2 is shared between meshes. Both mesh currents clockwise, V2 *opposes* mesh 2
    (i.e. its KVL equation is  -R2*i1 + (R2+R3)*i2 = -v2).
    Return np.array([i1, i2]) using np.linalg.solve."""
    raise NotImplementedError


# ---------------------------------------------------------------- Lesson 04
def time_to_reach(fraction: float, r: float, c: float) -> float:
    """Time for a charging RC to reach `fraction` (0..1) of the final voltage."""
    raise NotImplementedError


# ---------------------------------------------------------------- Lesson 05
def dominant_frequency(x: np.ndarray, fs: float) -> float:
    """Frequency (Hz) of the largest non-DC peak in the spectrum of x."""
    raise NotImplementedError


def crest_factor(x: np.ndarray) -> float:
    """Peak / RMS. (A sine wave gives √2 ≈ 1.414.)"""
    raise NotImplementedError


# ---------------------------------------------------------------- Lesson 06
def rc_for_cutoff(fc: float, c: float) -> float:
    """Resistor value giving a first-order RC low-pass cutoff of fc."""
    raise NotImplementedError


def moving_average(x: np.ndarray, n: int) -> np.ndarray:
    """Simple FIR moving-average filter, output same length as x ('same' mode)."""
    raise NotImplementedError


# ---------------------------------------------------------------- Lesson 07
def line_current_delta(v_ll: float, z_phase: complex) -> float:
    """Magnitude of the LINE current for a balanced delta load with per-phase
    impedance z_phase connected to line-to-line voltage v_ll."""
    raise NotImplementedError


# ---------------------------------------------------------------- Lesson 08
def is_stable(den: list[float]) -> bool:
    """Continuous-time system is stable if all poles (roots of den) have
    strictly negative real parts."""
    raise NotImplementedError


# ---------------------------------------------------------------- Lesson 09
def linear_calibration(raw: np.ndarray, reference: np.ndarray) -> tuple[float, float]:
    """Fit reference = gain * raw + offset (least squares). Return (gain, offset)."""
    raise NotImplementedError
