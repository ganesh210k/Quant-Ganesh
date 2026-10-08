"""
Lesson 01 - Python fundamentals through DC circuits
====================================================

Python concepts: functions, type hints, docstrings, f-strings, lists,
                 comprehensions, *args, exceptions, SI-prefix formatting.
EE concepts:     Ohm's law, series/parallel resistance, voltage & current
                 dividers, power dissipation, E-series standard values.

Run:  python lessons/01_basics_ohms_law.py
"""

import math


# ---------------------------------------------------------------------------
# 1. Functions with type hints and docstrings
# ---------------------------------------------------------------------------
def ohms_law(v: float | None = None, i: float | None = None, r: float | None = None) -> float:
    """Solve V = I*R for whichever argument is missing (pass exactly two)."""
    given = [x is not None for x in (v, i, r)]
    if sum(given) != 2:
        raise ValueError("Provide exactly two of v, i, r")
    if v is None:
        return i * r
    if i is None:
        return v / r
    return v / i


# ---------------------------------------------------------------------------
# 2. *args: accept any number of resistors
# ---------------------------------------------------------------------------
def series(*resistors: float) -> float:
    return sum(resistors)


def parallel(*resistors: float) -> float:
    if any(r == 0 for r in resistors):
        return 0.0  # a short circuit dominates
    return 1.0 / sum(1.0 / r for r in resistors)  # generator expression


def voltage_divider(vin: float, r_top: float, r_bottom: float) -> float:
    return vin * r_bottom / (r_top + r_bottom)


def current_divider(i_total: float, r_branch: float, *other_branches: float) -> float:
    """Current through r_branch when i_total splits across r_branch and others."""
    r_others = parallel(*other_branches)
    return i_total * r_others / (r_branch + r_others)


# ---------------------------------------------------------------------------
# 3. Engineering notation - every EE needs this helper
# ---------------------------------------------------------------------------
_PREFIXES = {-12: "p", -9: "n", -6: "µ", -3: "m", 0: "", 3: "k", 6: "M", 9: "G"}


def eng(value: float, unit: str = "", digits: int = 4) -> str:
    """Format 0.0047 -> '4.7 m' style engineering notation."""
    if value == 0:
        return f"0 {unit}"
    exp3 = int(math.floor(math.log10(abs(value)) / 3) * 3)
    exp3 = max(min(exp3, 9), -12)
    return f"{value / 10**exp3:.{digits}g} {_PREFIXES[exp3]}{unit}"


# ---------------------------------------------------------------------------
# 4. Lists & comprehensions: E12 standard resistor values
# ---------------------------------------------------------------------------
E12 = [1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]


def nearest_e12(r: float) -> float:
    """Snap an ideal resistance to the closest E12 value (log-distance)."""
    decade = 10 ** math.floor(math.log10(r))
    candidates = [v * decade for v in E12] + [10 * decade]
    return min(candidates, key=lambda c: abs(math.log10(c / r)))


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("== Ohm's law ==")
    print("I through 1k at 5V   :", eng(ohms_law(v=5, r=1e3), "A"))
    print("V across 220R @ 20mA :", eng(ohms_law(i=20e-3, r=220), "V"))

    print("\n== Networks ==")
    print("1k + 2.2k series     :", eng(series(1e3, 2.2e3), "Ω"))
    print("1k || 1k || 2k       :", eng(parallel(1e3, 1e3, 2e3), "Ω"))

    print("\n== Divider design: 12V -> 3.3V ADC input ==")
    r_top = 10e3
    r_bot_ideal = r_top * 3.3 / (12 - 3.3)
    r_bot = nearest_e12(r_bot_ideal)
    vout = voltage_divider(12, r_top, r_bot)
    print(f"ideal R_bottom = {eng(r_bot_ideal, 'Ω')}, E12 pick = {eng(r_bot, 'Ω')}, Vout = {eng(vout, 'V')}")

    print("\n== LED resistor sweep (list comprehension) ==")
    vsupply, vf, i_led = 5.0, 2.0, 15e-3
    r_needed = (vsupply - vf) / i_led
    print(f"Need {eng(r_needed, 'Ω')} -> use {eng(nearest_e12(r_needed), 'Ω')}")
    table = [(v, (v - vf) / i_led, (v - vf) * i_led) for v in (3.3, 5, 9, 12, 24)]
    print(f"{'Vsup':>6} {'R':>10} {'P_R':>10}")
    for v, r, p in table:
        print(f"{v:>6} {eng(r, 'Ω'):>10} {eng(p, 'W'):>10}")

    print("\n== Exceptions ==")
    try:
        ohms_law(v=1)
    except ValueError as err:
        print("Caught:", err)
