"""
Auto-grader for exercises.py.

    pytest exercises/ -v                      # grade YOUR answers
    EE_SOLUTIONS=1 pytest exercises/ -v       # sanity-check the reference solutions
"""

import importlib
import os
import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).parent))
ex = importlib.import_module("solutions" if os.environ.get("EE_SOLUTIONS") else "exercises")


def test_wire_resistance():
    # 100 m of 1.5 mm² copper ≈ 1.12 Ω
    assert ex.wire_resistance(100, 1.5) == pytest.approx(1.12, rel=1e-3)


def test_power_dissipated():
    assert ex.power_dissipated(12, 100) == pytest.approx(1.44)


def test_thevenin_of_divider():
    vth, rth = ex.thevenin_of_divider(10, 1e3, 1e3)
    assert vth == pytest.approx(5)
    assert rth == pytest.approx(500)


def test_reactance():
    assert ex.reactance("L", 10e-3, 50) == pytest.approx(3.1416, rel=1e-4)
    assert ex.reactance("C", 100e-6, 50) == pytest.approx(-31.831, rel=1e-4)
    with pytest.raises(ValueError):
        ex.reactance("R", 1, 50)


def test_apparent_power():
    p, q, s = ex.apparent_power(230, 10, 0.8)
    assert (p, q, s) == pytest.approx((1840, 1380, 2300))


def test_mesh_currents():
    i = ex.mesh_currents(2, 4, 6, 20, 10)
    # verify KVL directly rather than hard-coding the answer
    assert (2 + 4) * i[0] - 4 * i[1] == pytest.approx(20)
    assert -4 * i[0] + (4 + 6) * i[1] == pytest.approx(-10)


def test_time_to_reach():
    tau = 1e3 * 1e-6
    assert ex.time_to_reach(1 - np.exp(-1), 1e3, 1e-6) == pytest.approx(tau)
    assert ex.time_to_reach(0.99, 1e3, 1e-6) == pytest.approx(4.605e-3, rel=1e-3)


def test_dominant_frequency():
    fs = 1000
    t = np.arange(0, 1, 1 / fs)
    x = 2 + np.sin(2 * np.pi * 60 * t) + 0.3 * np.sin(2 * np.pi * 180 * t)
    assert ex.dominant_frequency(x, fs) == pytest.approx(60)


def test_crest_factor():
    t = np.linspace(0, 1, 10_000, endpoint=False)
    assert ex.crest_factor(np.sin(2 * np.pi * 5 * t)) == pytest.approx(np.sqrt(2), rel=1e-3)
    assert ex.crest_factor(np.sign(np.sin(2 * np.pi * 5 * t) + 1e-12)) == pytest.approx(1.0, rel=1e-3)


def test_rc_for_cutoff():
    assert ex.rc_for_cutoff(1000, 100e-9) == pytest.approx(1591.5, rel=1e-4)


def test_moving_average():
    x = np.ones(20)
    y = ex.moving_average(x, 5)
    assert y.shape == x.shape
    assert y[10] == pytest.approx(1.0)


def test_line_current_delta():
    assert ex.line_current_delta(400, 30 + 40j) == pytest.approx(13.856, rel=1e-4)


def test_is_stable():
    assert ex.is_stable([1, 3, 2]) is True       # poles -1, -2
    assert ex.is_stable([1, -1, 2]) is False     # RHP poles
    assert ex.is_stable([1, 0, 4]) is False      # marginal (on jω axis)


def test_linear_calibration():
    raw = np.array([0, 1000, 2000, 3000, 4095])
    ref = 0.0008 * raw + 0.05
    gain, offset = ex.linear_calibration(raw, ref)
    assert gain == pytest.approx(0.0008)
    assert offset == pytest.approx(0.05)
