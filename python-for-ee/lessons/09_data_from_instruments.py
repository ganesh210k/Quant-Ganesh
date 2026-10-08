"""
Lesson 09 - Working with measurement data (CSV, curve fitting, reports)
=======================================================================

Python concepts: csv module & np.genfromtxt, pathlib, scipy.optimize.curve_fit,
                 np.polyfit, writing tidy reports, context managers (`with`).
EE concepts:     logging oscilloscope / DMM data, extracting component values
                 from measurements (capacitor discharge -> C, diode I-V ->
                 Shockley parameters), uncertainty from the covariance matrix.

This is what most practising engineers use Python for day-to-day.

Run:  python lessons/09_data_from_instruments.py   (CSV + plot saved to out/)
"""

import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

OUT = Path(__file__).resolve().parent.parent / "out"
OUT.mkdir(exist_ok=True)


def write_fake_scope_capture(path: Path, r: float, c_true: float, v0: float, seed: int = 1) -> None:
    """Simulate an oscilloscope CSV export of an RC discharge."""
    rng = np.random.default_rng(seed)
    t = np.linspace(0, 5 * r * c_true, 400)
    v = v0 * np.exp(-t / (r * c_true)) + rng.normal(0, 0.02, t.size)
    with path.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["time_s", "voltage_V"])
        w.writerows(zip(t, v))


def load_csv(path: Path) -> tuple[np.ndarray, np.ndarray]:
    data = np.genfromtxt(path, delimiter=",", names=True)
    return data["time_s"], data["voltage_V"]


def fit_discharge(t: np.ndarray, v: np.ndarray, r: float) -> tuple[float, float]:
    """Fit V = V0 exp(-t/RC) + offset. Returns (C, 1-sigma uncertainty of C)."""
    model = lambda t, v0, tau, off: v0 * np.exp(-t / tau) + off
    p0 = [v.max(), t[-1] / 5, 0.0]                    # good initial guesses matter
    popt, pcov = curve_fit(model, t, v, p0=p0)
    tau, tau_sigma = popt[1], np.sqrt(pcov[1, 1])
    return tau / r, tau_sigma / r


def fit_diode(v: np.ndarray, i: np.ndarray, vt: float = 0.02585) -> tuple[float, float]:
    """Shockley: ln(I) = ln(Is) + V/(n Vt) -> linear fit. Returns (Is, n)."""
    slope, intercept = np.polyfit(v, np.log(i), 1)
    return float(np.exp(intercept)), float(1 / (slope * vt))


if __name__ == "__main__":
    # --- Capacitor value from a scope capture ----------------------------
    csv_path = OUT / "09_scope_capture.csv"
    R = 10e3
    write_fake_scope_capture(csv_path, R, c_true=4.7e-6, v0=5.0)
    t, v = load_csv(csv_path)
    c, c_sig = fit_discharge(t, v, R)
    print(f"Loaded {t.size} samples from {csv_path.name}")
    print(f"Fitted C = {c * 1e6:.3f} ± {c_sig * 1e6:.3f} µF (true 4.700 µF)")

    # --- Diode parameters from a curve-tracer sweep ------------------------
    rng = np.random.default_rng(7)
    vd = np.linspace(0.45, 0.70, 30)
    i_true = 2e-9 * (np.exp(vd / (1.8 * 0.02585)) - 1)
    i_meas = i_true * (1 + rng.normal(0, 0.03, vd.size))
    Is, n = fit_diode(vd, i_meas)
    print(f"Diode fit: Is = {Is:.2e} A (true 2e-9), n = {n:.2f} (true 1.8)")

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4))
    a1.plot(t * 1e3, v, ".", ms=2, label="measured")
    a1.plot(t * 1e3, 5 * np.exp(-t / (R * c)), "r", label=f"fit C={c * 1e6:.2f} µF")
    a1.set(xlabel="t [ms]", ylabel="V", title="RC discharge"); a1.legend()
    a2.semilogy(vd, i_meas, "o", ms=3, label="measured")
    a2.semilogy(vd, Is * (np.exp(vd / (n * 0.02585)) - 1), label=f"fit n={n:.2f}")
    a2.set(xlabel="Vd [V]", ylabel="Id [A]", title="Diode I-V"); a2.legend()
    for a in (a1, a2):
        a.grid(True, which="both", alpha=0.3)
    fig.tight_layout(); fig.savefig(OUT / "09_fits.png", dpi=120); plt.close(fig)
    print(f"Plot written to {OUT}")
