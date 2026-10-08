"""
Lesson 08 - Control systems: DC motor speed control with PID
=============================================================

Python concepts: classes with state, discrete-time simulation loops,
                 scipy.signal.lti for poles/step response, dict of results.
EE concepts:     DC motor electrical + mechanical model, open-loop poles,
                 PID control, rise time / overshoot / settling metrics,
                 actuator saturation and anti-windup.

Run:  python lessons/08_control_systems.py   (plot saved to out/)
"""

from dataclasses import dataclass
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

OUT = Path(__file__).resolve().parent.parent / "out"
OUT.mkdir(exist_ok=True)


@dataclass
class DCMotor:
    R: float = 1.0      # armature resistance [Ω]
    L: float = 0.5      # armature inductance [H]
    K: float = 0.01     # torque / back-EMF constant [N·m/A] = [V·s/rad]
    J: float = 0.01     # rotor inertia [kg·m²]
    b: float = 0.1      # viscous friction [N·m·s]

    def tf(self) -> signal.lti:
        """speed / voltage = K / ((Js + b)(Ls + R) + K²)"""
        den = np.polymul([self.J, self.b], [self.L, self.R])
        den = np.polyadd(den, [self.K**2])
        return signal.lti([self.K], den)

    def step(self, state: np.ndarray, v: float, dt: float) -> np.ndarray:
        """One forward-Euler step. state = [current i, speed w]."""
        i, w = state
        di = (v - self.R * i - self.K * w) / self.L
        dw = (self.K * i - self.b * w) / self.J
        return np.array([i + di * dt, w + dw * dt])


class PID:
    def __init__(self, kp, ki, kd, dt, u_min=-np.inf, u_max=np.inf):
        self.kp, self.ki, self.kd, self.dt = kp, ki, kd, dt
        self.u_min, self.u_max = u_min, u_max
        self.integral = 0.0
        self.prev_meas = None

    def update(self, setpoint: float, measurement: float) -> float:
        err = setpoint - measurement
        # derivative on measurement avoids a "kick" when the setpoint steps
        d = 0.0 if self.prev_meas is None else -(measurement - self.prev_meas) / self.dt
        self.prev_meas = measurement
        u_unsat = self.kp * err + self.ki * (self.integral + err * self.dt) + self.kd * d
        u = float(np.clip(u_unsat, self.u_min, self.u_max))
        if u == u_unsat:                       # anti-windup: integrate only if not saturated
            self.integral += err * self.dt
        return u


def step_metrics(t: np.ndarray, y: np.ndarray, target: float) -> dict:
    final = y[-1]
    i10 = np.argmax(y >= 0.1 * target)
    i90 = np.argmax(y >= 0.9 * target)
    outside = np.where(np.abs(y - target) > 0.02 * abs(target))[0]
    return {
        "rise_time_s": t[i90] - t[i10],
        "overshoot_pct": max(0.0, (y.max() - target) / target * 100),
        "settling_time_s": t[outside[-1]] if outside.size else 0.0,
        "steady_state_error": target - final,
    }


def simulate(motor: DCMotor, pid: PID, setpoint: float, t_end: float, dt: float):
    n = int(t_end / dt)
    t = np.arange(n) * dt
    x = np.zeros(2)
    w, u = np.zeros(n), np.zeros(n)
    for k in range(n):
        u[k] = pid.update(setpoint, x[1])
        x = motor.step(x, u[k], dt)
        w[k] = x[1]
    return t, w, u


if __name__ == "__main__":
    motor = DCMotor()
    sys = motor.tf()
    print("Open-loop poles:", np.round(sys.poles, 3), "(all negative real parts -> stable)")
    t_ol, y_ol = signal.step(sys, T=np.linspace(0, 5, 1000))
    print(f"Open-loop: 1 V gives {y_ol[-1]:.4f} rad/s - far too slow & weak")

    dt, target = 1e-3, 1.0
    fig, (a1, a2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))
    for name, gains in {"P only": (100, 0, 0), "PI": (100, 200, 0), "PID": (100, 200, 10)}.items():
        t, w, u = simulate(motor, PID(*gains, dt=dt, u_min=-24, u_max=24), target, 3.0, dt)
        m = step_metrics(t, w, target)
        print(f"{name:7s} rise={m['rise_time_s']:.3f}s  OS={m['overshoot_pct']:5.1f}%  "
              f"settle={m['settling_time_s']:.3f}s  ess={m['steady_state_error']:+.4f}")
        a1.plot(t, w, label=name); a2.plot(t, u, label=name)
    a1.axhline(target, color="k", ls="--", lw=0.8)
    a1.set(ylabel="speed [rad/s]", title="DC motor speed control (24 V supply limit)")
    a2.set(xlabel="t [s]", ylabel="voltage [V]")
    for a in (a1, a2):
        a.grid(True, alpha=0.3); a.legend()
    fig.tight_layout(); fig.savefig(OUT / "08_pid.png", dpi=120); plt.close(fig)
    print(f"Plot written to {OUT}")
