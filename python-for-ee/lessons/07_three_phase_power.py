"""
Lesson 07 - Three-phase power systems
======================================

Python concepts: NumPy complex arrays, broadcasting, np.roll, @ (matmul),
                 small classes with @property.
EE concepts:     balanced/unbalanced Y loads, line vs phase quantities,
                 neutral current, symmetrical components (Fortescue).

Run:  python lessons/07_three_phase_power.py
"""

import numpy as np

a = np.exp(2j * np.pi / 3)               # the 120° rotation operator
A = np.array([[1, 1, 1],
              [1, a**2, a],
              [1, a, a**2]])              # abc = A @ [0, +, -]
A_INV = np.linalg.inv(A)


def balanced_phase_voltages(v_ll_rms: float) -> np.ndarray:
    """Phase (line-to-neutral) phasors Va, Vb, Vc for an abc sequence."""
    v_ph = v_ll_rms / np.sqrt(3)
    return v_ph * np.array([1, a**2, a])   # 0°, -120°, +120°


def sequence_components(abc: np.ndarray) -> np.ndarray:
    """Return [zero, positive, negative] sequence phasors."""
    return A_INV @ abc


class WyeLoad:
    """Grounded-wye load with per-phase impedances."""

    def __init__(self, za: complex, zb: complex, zc: complex):
        self.z = np.array([za, zb, zc], dtype=complex)

    def currents(self, v_phase: np.ndarray) -> np.ndarray:
        return v_phase / self.z               # element-wise (broadcasting)

    def power(self, v_phase: np.ndarray) -> complex:
        return complex(np.sum(v_phase * np.conj(self.currents(v_phase))))

    @property
    def is_balanced(self) -> bool:
        return bool(np.allclose(self.z, self.z[0]))


def fmt(z: complex) -> str:
    return f"{abs(z):8.2f} ∠ {np.degrees(np.angle(z)):+7.2f}°"


if __name__ == "__main__":
    V = balanced_phase_voltages(400)   # 400 V line-to-line (use 480 / 208 as needed)
    v_ll = V - np.roll(V, -1)          # Vab, Vbc, Vca in one line
    print("Phase voltages:", *map(fmt, V), sep="\n  ")
    print("Line voltages :", *map(fmt, v_ll), sep="\n  ")

    print("\n== Balanced load (motor-like, 8+6j Ω/phase) ==")
    load = WyeLoad(8 + 6j, 8 + 6j, 8 + 6j)
    I = load.currents(V)
    S = load.power(V)
    print("I:", *map(fmt, I))
    print(f"Neutral current |In| = {abs(I.sum()):.2e} A (≈0 when balanced)")
    print(f"P = {S.real / 1e3:.2f} kW, Q = {S.imag / 1e3:.2f} kvar, pf = {S.real / abs(S):.3f}")
    print(f"Check: √3·VLL·IL·pf = {np.sqrt(3) * 400 * abs(I[0]) * S.real / abs(S) / 1e3:.2f} kW")

    print("\n== Unbalanced load (one phase lightly loaded) ==")
    load2 = WyeLoad(8 + 6j, 8 + 6j, 30 + 0j)
    I2 = load2.currents(V)
    seq = sequence_components(I2)
    print(f"Neutral current |In| = {abs(I2.sum()):.2f} A")
    print(f"Sequence currents |I0|, |I1|, |I2| = {np.abs(seq).round(2)}")
    print(f"Current unbalance factor I2/I1 = {abs(seq[2]) / abs(seq[1]) * 100:.1f} %")
