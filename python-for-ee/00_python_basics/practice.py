# =============================================================================
# PRACTICE - fill in each function, then run:   python practice.py
# =============================================================================
# Each function currently contains  pass  (which means "do nothing").
# Replace  pass  with your code. The checker at the bottom tells you which
# answers are right (✅) and which still need work (❌).
#
# Do them in order - each one matches a lesson number.
# Stuck for more than 15 minutes? Look in practice_solutions.py.
# =============================================================================


# ---- Lesson 1-2: variables and maths ---------------------------------------
def ohms_law_current(v, r):
    """Return the current I = V / R."""
    pass


def power(v, i):
    """Return the power P = V * I."""
    pass


# ---- Lesson 3: strings -----------------------------------------------------
def format_reading(value, unit):
    """Return text like  '3.30 V'  - value with exactly 2 decimals, a space, then unit.
    format_reading(3.3, "V")  ->  "3.30 V"
    """
    pass


def regulator_voltage(part_number):
    """78xx regulators: the last two characters are the voltage.
    regulator_voltage("LM7812")  ->  12   (an int, not text!)
    """
    pass


# ---- Lesson 5: conditions --------------------------------------------------
def battery_status(volts):
    """Return "FULL" if volts >= 4.1, "OK" if volts >= 3.5, otherwise "LOW"."""
    pass


# ---- Lesson 6: loops -------------------------------------------------------
def series_resistance(resistors):
    """Return the sum of a list of resistances, USING A for LOOP (not sum())."""
    pass


def count_over_limit(readings, limit):
    """Return how many readings are strictly greater than limit."""
    pass


# ---- Lesson 7: lists -------------------------------------------------------
def to_milliamps(currents_a):
    """Convert a list of amps to a list of milliamps (multiply each by 1000).
    Try a list comprehension!
    """
    pass


def average(values):
    """Return the mean of a list of numbers."""
    pass


# ---- Lesson 8: dictionaries ------------------------------------------------
def colour_to_digit(colour):
    """Resistor colour code: black 0, brown 1, red 2, orange 3, yellow 4,
    green 5, blue 6, violet 7, grey 8, white 9.  Use a dictionary.
    colour_to_digit("red") -> 2
    """
    pass


# ---- Lesson 9: functions ---------------------------------------------------
def parallel_resistance(r1, r2):
    """Return R1 || R2 = (R1 * R2) / (R1 + R2)."""
    pass


def voltage_divider(vin, r1, r2=10_000):
    """Return Vout = Vin * R2 / (R1 + R2). Note r2 has a default of 10 kΩ."""
    pass


# ---- Lesson 10: errors -----------------------------------------------------
def safe_float(text):
    """Convert text to a float. If it isn't a valid number, return None
    instead of crashing.   safe_float("3.3") -> 3.3    safe_float("abc") -> None
    """
    pass


# =============================================================================
# CHECKER - don't edit below this line
# =============================================================================
def _check():
    import math

    def close(a, b):
        return isinstance(a, (int, float)) and math.isclose(a, b, rel_tol=1e-6)

    tests = [
        ("ohms_law_current", lambda: close(ohms_law_current(12, 4), 3.0)),
        ("power",            lambda: close(power(5, 0.5), 2.5)),
        ("format_reading",   lambda: format_reading(3.3, "V") == "3.30 V"
                                     and format_reading(0.125, "A") == "0.12 A"),
        ("regulator_voltage", lambda: regulator_voltage("LM7812") == 12
                                      and regulator_voltage("7805") == 5),
        ("battery_status",   lambda: [battery_status(v) for v in (4.2, 4.1, 3.7, 3.5, 3.2)]
                                     == ["FULL", "FULL", "OK", "OK", "LOW"]),
        ("series_resistance", lambda: close(series_resistance([100, 220, 470]), 790)
                                      and series_resistance([]) == 0),
        ("count_over_limit", lambda: count_over_limit([4.9, 5.2, 5.0, 5.3], 5.0) == 2),
        ("to_milliamps",     lambda: to_milliamps([0.001, 0.02, 1]) == [1.0, 20.0, 1000]),
        ("average",          lambda: close(average([1, 2, 3, 4]), 2.5)),
        ("colour_to_digit",  lambda: [colour_to_digit(c) for c in ("black", "red", "violet", "white")]
                                     == [0, 2, 7, 9]),
        ("parallel_resistance", lambda: close(parallel_resistance(100, 100), 50)),
        ("voltage_divider",  lambda: close(voltage_divider(12, 10_000), 6)
                                     and close(voltage_divider(10, 1000, 4000), 8)),
        ("safe_float",       lambda: safe_float("3.3") == 3.3 and safe_float("abc") is None),
    ]

    passed = 0
    for name, test in tests:
        try:
            ok = bool(test())
        except Exception as err:          # show the error instead of crashing
            ok = False
            name += f"   ({type(err).__name__}: {err})"
        print(("✅ " if ok else "❌ ") + name)
        passed += ok
    print(f"\n{passed}/{len(tests)} passed" + ("  🎉 Ready for the EE lessons!" if passed == len(tests) else ""))


if __name__ == "__main__":
    _check()
