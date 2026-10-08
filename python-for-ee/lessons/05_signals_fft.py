"""
Lesson 05 - Signals, sampling and the FFT
==========================================

Python concepts: np.fft.rfft, array slicing, boolean masks, windowing,
                 random number generation with a seeded Generator.
EE concepts:     sampling theorem, aliasing, spectrum of a distorted
                 waveform, RMS, Total Harmonic Distortion (THD).

Run:  python lessons/05_signals_fft.py   (plots saved to out/)
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent.parent / "out"
OUT.mkdir(exist_ok=True)


def rms(x: np.ndarray) -> float:
    return float(np.sqrt(np.mean(np.square(x))))


def spectrum(x: np.ndarray, fs: float, window: bool = True) -> tuple[np.ndarray, np.ndarray]:
    """Single-sided amplitude spectrum (peak amplitude per bin)."""
    n = len(x)
    w = np.hanning(n) if window else np.ones(n)
    X = np.fft.rfft(x * w)
    amp = 2 * np.abs(X) / np.sum(w)  # coherent-gain correction
    amp[0] /= 2                       # DC bin is not doubled
    return np.fft.rfftfreq(n, 1 / fs), amp


def thd(x: np.ndarray, fs: float, f0: float, n_harmonics: int = 10) -> float:
    """THD = sqrt(sum(V_h^2)) / V_1 using the peak bin near each harmonic."""
    f, amp = spectrum(x, fs)
    def peak_near(fh):
        mask = np.abs(f - fh) <= 2 * (f[1] - f[0])
        return amp[mask].max() if mask.any() else 0.0
    v1 = peak_near(f0)
    harmonics = [peak_near(k * f0) for k in range(2, n_harmonics + 1) if k * f0 < fs / 2]
    return float(np.sqrt(np.sum(np.square(harmonics))) / v1)


def alias_frequency(f_signal: float, fs: float) -> float:
    """Apparent frequency after sampling at fs."""
    return abs(f_signal - fs * round(f_signal / fs))


if __name__ == "__main__":
    rng = np.random.default_rng(42)
    fs, f0, dur = 10_000.0, 50.0, 0.2  # 10 periods of 50 Hz
    t = np.arange(0, dur, 1 / fs)

    # Mains voltage with 3rd/5th harmonics (typical of rectifier loads) + noise
    v = (325 * np.sin(2 * np.pi * f0 * t)
         + 30 * np.sin(2 * np.pi * 3 * f0 * t)
         + 15 * np.sin(2 * np.pi * 5 * f0 * t)
         + rng.normal(0, 2, t.size))

    print(f"RMS = {rms(v):.1f} V  (pure sine would be {325 / np.sqrt(2):.1f} V)")
    print(f"THD = {thd(v, fs, f0) * 100:.2f} %  (expected ≈ {np.hypot(30, 15) / 325 * 100:.2f} %)")

    f, amp = spectrum(v, fs)
    # Note: naively taking the 3 largest bins would return 45/50/55 Hz - the
    # window "leaks" the fundamental into neighbouring bins. Look at harmonics instead.
    for h in range(1, 8):
        k = np.argmin(np.abs(f - h * f0))
        print(f"  harmonic {h} ({f[k]:5.0f} Hz): {amp[k]:6.1f} V")

    print("\nAliasing: 9.2 kHz sampled at 10 kHz appears at",
          alias_frequency(9_200, 10_000), "Hz")

    fig, (a1, a2) = plt.subplots(2, 1, figsize=(8, 6))
    a1.plot(t * 1e3, v, lw=0.8); a1.set(xlabel="t [ms]", ylabel="V", title="Distorted mains")
    a2.stem(f[f < 1000], amp[f < 1000], basefmt=" ")
    a2.set(xlabel="f [Hz]", ylabel="|V| peak", title="Spectrum")
    for a in (a1, a2):
        a.grid(True, alpha=0.3)
    fig.tight_layout(); fig.savefig(OUT / "05_fft.png", dpi=120); plt.close(fig)
    print(f"Plot written to {OUT}")
