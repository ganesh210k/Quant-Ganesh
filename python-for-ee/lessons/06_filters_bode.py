"""
Lesson 06 - Filters and Bode plots with scipy.signal
=====================================================

Python concepts: scipy.signal (TransferFunction, freqs, butter, sosfiltfilt),
                 log-spaced arrays, np.interp for crossing detection.
EE concepts:     first-order RC low-pass, -3 dB cutoff, Butterworth digital
                 filter design, zero-phase filtering of a noisy sensor signal.

Run:  python lessons/06_filters_bode.py   (plots saved to out/)
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

OUT = Path(__file__).resolve().parent.parent / "out"
OUT.mkdir(exist_ok=True)


def rc_lowpass_tf(r: float, c: float) -> signal.TransferFunction:
    """H(s) = 1 / (sRC + 1)"""
    return signal.TransferFunction([1], [r * c, 1])


def bode_data(tf: signal.TransferFunction, f: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    w, h = signal.freqs(tf.num, tf.den, worN=2 * np.pi * f)
    return 20 * np.log10(np.abs(h)), np.degrees(np.unwrap(np.angle(h)))


def cutoff_frequency(f: np.ndarray, mag_db: np.ndarray) -> float:
    """First frequency where gain drops to -3.01 dB (linear interpolation)."""
    below = np.where(mag_db <= mag_db[0] - 3.0103)[0]
    k = below[0]
    return float(np.interp(-3.0103 + mag_db[0], [mag_db[k], mag_db[k - 1]], [f[k], f[k - 1]]))


if __name__ == "__main__":
    # --- Analog RC filter --------------------------------------------------
    R, C = 1.6e3, 100e-9
    fc_theory = 1 / (2 * np.pi * R * C)
    f = np.logspace(1, 6, 2000)
    mag, ph = bode_data(rc_lowpass_tf(R, C), f)
    print(f"RC low-pass: fc theory = {fc_theory:.1f} Hz, measured = {cutoff_frequency(f, mag):.1f} Hz")
    print(f"Phase at fc = {np.interp(fc_theory, f, ph):.1f}° (expect -45°)")

    fig, (a1, a2) = plt.subplots(2, 1, sharex=True, figsize=(7, 6))
    a1.semilogx(f, mag); a1.set(ylabel="|H| [dB]", title="RC low-pass Bode plot")
    a2.semilogx(f, ph); a2.set(xlabel="f [Hz]", ylabel="phase [°]")
    for a in (a1, a2):
        a.axvline(fc_theory, color="gray", lw=0.8); a.grid(True, which="both", alpha=0.3)
    fig.tight_layout(); fig.savefig(OUT / "06_bode.png", dpi=120); plt.close(fig)

    # --- Digital Butterworth: clean a noisy sensor ------------------------
    rng = np.random.default_rng(0)
    fs = 2_000.0
    t = np.arange(0, 1, 1 / fs)
    clean = np.sin(2 * np.pi * 5 * t)                       # 5 Hz sensor signal
    noisy = clean + 0.4 * np.sin(2 * np.pi * 50 * t) + rng.normal(0, 0.3, t.size)
    sos = signal.butter(4, 15, btype="low", fs=fs, output="sos")  # SOS = numerically robust
    filtered = signal.sosfiltfilt(sos, noisy)                       # zero phase shift
    err_before = np.sqrt(np.mean((noisy - clean) ** 2))
    err_after = np.sqrt(np.mean((filtered - clean) ** 2))
    print(f"4th-order Butterworth @15 Hz: RMS error {err_before:.3f} -> {err_after:.3f}")

    fig, ax = plt.subplots(figsize=(8, 3.5))
    ax.plot(t, noisy, lw=0.5, alpha=0.6, label="noisy")
    ax.plot(t, filtered, lw=1.5, label="filtered")
    ax.plot(t, clean, "k--", lw=1, label="true")
    ax.set(xlabel="t [s]", title="Zero-phase Butterworth filtering"); ax.legend(); ax.grid(True, alpha=0.3)
    fig.tight_layout(); fig.savefig(OUT / "06_filtering.png", dpi=120); plt.close(fig)
    print(f"Plots written to {OUT}")
