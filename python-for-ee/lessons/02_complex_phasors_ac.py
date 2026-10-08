"""
Lesson 02 - Complex numbers, phasors and AC circuits
=====================================================

Python concepts: built-in complex type (1j), cmath, tuples, dictionaries,
                 functions returning functions (closures).
EE concepts:     impedance of R/L/C, phasors, AC power (P, Q, S, pf),
                 power-factor correction, resonance.

Python uses `j` for the imaginary unit - exactly like electrical engineers.

Run:  python lessons/02_complex_phasors_ac.py
"""

import cmath
import math


def z_r(r: float) -> complex:
    return complex(r, 0)


def z_l(l: float, f: float) -> complex:
    return 1j * 2 * math.pi * f * l


def z_c(c: float, f: float) -> complex:
    return 1 / (1j * 2 * math.pi * f * c)


def zpar(*zs: complex) -> complex:
    return 1 / sum(1 / z for z in zs)


def phasor(mag: float, angle_deg: float) -> complex:
    """Build a phasor from polar form (magnitude, degrees)."""
    return cmath.rect(mag, math.radians(angle_deg))


def polar_str(z: complex, unit: str = "") -> str:
    mag, ang = cmath.polar(z)
    return f"{mag:.4g}{unit} ∠ {math.degrees(ang):+.2f}°"


def ac_power(v_rms: complex, i_rms: complex) -> dict:
    """Complex power S = V * conj(I). Returns a dictionary of quantities."""
    s = v_rms * i_rms.conjugate()
    return {
        "S": s,
        "P_W": s.real,
        "Q_var": s.imag,
        "|S|_VA": abs(s),
        "pf": s.real / abs(s) if abs(s) else 1.0,
        "lagging": s.imag > 0,
    }


def pf_correction_cap(p: float, pf_old: float, pf_new: float, v_rms: float, f: float) -> float:
    """Shunt capacitor needed to raise a lagging load's power factor."""
    q_old = p * math.tan(math.acos(pf_old))
    q_new = p * math.tan(math.acos(pf_new))
    q_c = q_old - q_new
    return q_c / (2 * math.pi * f * v_rms**2)


def make_series_rlc(r: float, l: float, c: float):
    """Closure: returns a function Z(f) for a fixed series RLC."""
    def impedance(f: float) -> complex:
        return z_r(r) + z_l(l, f) + z_c(c, f)
    return impedance


if __name__ == "__main__":
    f = 50.0  # use 60.0 in the Americas
    print("== Complex basics ==")
    z = 3 + 4j
    print("z =", z, "| |z| =", abs(z), "| angle =", math.degrees(cmath.phase(z)), "deg")

    print("\n== Inductive load on 230 V / 50 Hz ==")
    v = phasor(230, 0)
    z_load = z_r(10) + z_l(50e-3, f)
    i = v / z_load
    print("Z =", polar_str(z_load, " Ω"))
    print("I =", polar_str(i, " A"))
    pw = ac_power(v, i)
    print(f"P = {pw['P_W']:.1f} W, Q = {pw['Q_var']:.1f} var, |S| = {pw['|S|_VA']:.1f} VA, "
          f"pf = {pw['pf']:.3f} {'lagging' if pw['lagging'] else 'leading'}")

    c = pf_correction_cap(pw["P_W"], pw["pf"], 0.95, 230, f)
    print(f"Capacitor for pf 0.95: {c * 1e6:.1f} µF")
    z_new = zpar(z_load, z_c(c, f))
    print("Corrected pf:", f"{ac_power(v, v / z_new)['pf']:.3f}")

    print("\n== Series RLC resonance ==")
    R, L, C = 10, 10e-3, 1e-6
    Z = make_series_rlc(R, L, C)
    f0 = 1 / (2 * math.pi * math.sqrt(L * C))
    q = (1 / R) * math.sqrt(L / C)
    print(f"f0 = {f0:.1f} Hz, Q = {q:.2f}, bandwidth = {f0 / q:.1f} Hz")
    for ff in (f0 / 2, f0, 2 * f0):
        print(f"  f = {ff:8.1f} Hz -> Z = {polar_str(Z(ff), ' Ω')}")
