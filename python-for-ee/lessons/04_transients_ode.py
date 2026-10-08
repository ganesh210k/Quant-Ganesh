"""
Lesson 04 - Transients: simulating RC and RLC circuits
=======================================================

Python concepts: np.linspace, vectorised math, scipy.integrate.solve_ivp,
                 matplotlib plotting, comparing numeric vs analytic results.
EE concepts:     RC charging (tau = RC), series RLC step response,
                 under/critically/over-damped behaviour.

Run:  python lessons/04_transients_ode.py   (plots saved to out/)
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # render to files; works without a display
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

OUT = Path(__file__).resolve().parent.parent / "out"
OUT.mkdir(exist_ok=True)


def rc_analytic(t: np.ndarray, vs: float, r: float, c: float) -> np.ndarray:
    return vs * (1 - np.exp(-t / (r * c)))


def rc_numeric(t: np.ndarray, vs: float, r: float, c: float) -> np.ndarray:
    # dVc/dt = (Vs - Vc) / (R C)
    sol = solve_ivp(lambda _t, v: (vs - v) / (r * c), (t[0], t[-1]), [0.0], t_eval=t, rtol=1e-8)
    return sol.y[0]


def rlc_step(t: np.ndarray, vs: float, r: float, l: float, c: float) -> tuple[np.ndarray, np.ndarray]:
    """Series RLC driven by a step. State x = [Vc, I]. Returns (Vc, I)."""
    def deriv(_t, x):
        vc, i = x
        return [i / c, (vs - r * i - vc) / l]
    sol = solve_ivp(deriv, (t[0], t[-1]), [0.0, 0.0], t_eval=t, max_step=(t[1] - t[0]))
    return sol.y[0], sol.y[1]


def damping(r: float, l: float, c: float) -> tuple[float, float, str]:
    alpha = r / (2 * l)
    w0 = 1 / np.sqrt(l * c)
    zeta = alpha / w0
    kind = "under-damped" if zeta < 1 else "critically damped" if np.isclose(zeta, 1) else "over-damped"
    return zeta, w0, kind


if __name__ == "__main__":
    # --- RC charging -------------------------------------------------------
    R, C, VS = 1e3, 1e-6, 5.0
    tau = R * C
    t = np.linspace(0, 5 * tau, 500)
    va, vn = rc_analytic(t, VS, R, C), rc_numeric(t, VS, R, C)
    print(f"tau = {tau * 1e3:.2f} ms; Vc(tau) = {rc_analytic(np.array([tau]), VS, R, C)[0]:.3f} V (63.2%)")
    print(f"max |numeric - analytic| = {np.max(np.abs(va - vn)):.2e} V")

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(t * 1e3, va, label="analytic")
    ax.plot(t * 1e3, vn, "--", label="solve_ivp")
    ax.axvline(tau * 1e3, color="gray", lw=0.8)
    ax.set(xlabel="t [ms]", ylabel="Vc [V]", title="RC charging")
    ax.grid(True, alpha=0.3); ax.legend()
    fig.tight_layout(); fig.savefig(OUT / "04_rc_charging.png", dpi=120); plt.close(fig)

    # --- RLC step response for 3 damping cases -----------------------------
    L, C = 10e-3, 1e-6
    t = np.linspace(0, 4e-3, 2000)
    fig, ax = plt.subplots(figsize=(7, 4))
    for R in (20, 2 * np.sqrt(L / C), 500):
        zeta, w0, kind = damping(R, L, C)
        vc, _ = rlc_step(t, 1.0, R, L, C)
        overshoot = (vc.max() - 1.0) * 100
        print(f"R = {R:7.1f} Ω  zeta = {zeta:5.2f}  {kind:18s} overshoot = {max(overshoot, 0):5.1f}%")
        ax.plot(t * 1e3, vc, label=f"R={R:.0f}Ω ({kind})")
    ax.set(xlabel="t [ms]", ylabel="Vc [V]", title="Series RLC step response")
    ax.grid(True, alpha=0.3); ax.legend()
    fig.tight_layout(); fig.savefig(OUT / "04_rlc_step.png", dpi=120); plt.close(fig)
    print(f"Plots written to {OUT}")
