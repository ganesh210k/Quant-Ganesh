"""Reference solutions. Try exercises.py on your own first!"""

import numpy as np


def wire_resistance(length_m, area_mm2, rho=1.68e-8):
    return rho * length_m / (area_mm2 * 1e-6)


def power_dissipated(v, r):
    return v**2 / r


def thevenin_of_divider(vin, r1, r2):
    return vin * r2 / (r1 + r2), r1 * r2 / (r1 + r2)


def reactance(component, value, f):
    w = 2 * np.pi * f
    if component == "L":
        return w * value
    if component == "C":
        return -1 / (w * value)
    raise ValueError(f"unknown component {component!r}")


def apparent_power(v_rms, i_rms, pf):
    s = v_rms * i_rms
    p = s * pf
    q = s * np.sqrt(1 - pf**2)
    return p, q, s


def mesh_currents(r1, r2, r3, v1, v2):
    A = np.array([[r1 + r2, -r2], [-r2, r2 + r3]])
    b = np.array([v1, -v2])
    return np.linalg.solve(A, b)


def time_to_reach(fraction, r, c):
    return -r * c * np.log(1 - fraction)


def dominant_frequency(x, fs):
    X = np.abs(np.fft.rfft(x - np.mean(x)))
    f = np.fft.rfftfreq(len(x), 1 / fs)
    return float(f[np.argmax(X)])


def crest_factor(x):
    return float(np.max(np.abs(x)) / np.sqrt(np.mean(x**2)))


def rc_for_cutoff(fc, c):
    return 1 / (2 * np.pi * fc * c)


def moving_average(x, n):
    return np.convolve(x, np.ones(n) / n, mode="same")


def line_current_delta(v_ll, z_phase):
    return np.sqrt(3) * v_ll / abs(z_phase)


def is_stable(den):
    return bool(np.all(np.real(np.roots(den)) < 0))


def linear_calibration(raw, reference):
    gain, offset = np.polyfit(raw, reference, 1)
    return float(gain), float(offset)
