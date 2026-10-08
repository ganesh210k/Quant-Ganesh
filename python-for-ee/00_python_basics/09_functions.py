# =============================================================================
# LESSON 9 - Functions: write code once, use it many times
# =============================================================================
# Run:  python 09_functions.py
# =============================================================================


# -----------------------------------------------------------------------------
# 1. Defining and calling a function
# -----------------------------------------------------------------------------
# Syntax:
#     def function_name(parameter1, parameter2):     <- def, name, ( ), colon
#         indented body
#         return result                              <- send a value back
#
# Defining a function does NOT run it. It runs only when you CALL it.

def current(voltage, resistance):
    """Return the current through a resistor (Ohm's law)."""   # docstring
    return voltage / resistance

i1 = current(12, 100)        # call it: 12 goes into voltage, 100 into resistance
i2 = current(5, 220)
print(i1, i2)                # 0.12 0.022727272727272728


# -----------------------------------------------------------------------------
# 2. return vs print - a very common beginner confusion
# -----------------------------------------------------------------------------
def power_print(v, i):
    print(v * i)             # only SHOWS the value; gives nothing back

def power_return(v, i):
    return v * i             # GIVES the value back so you can use it

a = power_print(5, 2)        # prints 10 ...
print("a is", a)             # ... but a is None (nothing was returned)
b = power_return(5, 2)
print("b is", b)             # b is 10 - you can now use it in more maths
# Rule of thumb: functions should usually RETURN, and you print outside.


# -----------------------------------------------------------------------------
# 3. Default values for parameters
# -----------------------------------------------------------------------------
def led_resistor(v_supply, v_forward=2.0, i_ma=20):
    return (v_supply - v_forward) / (i_ma / 1000)

print(led_resistor(5))                    # uses defaults -> 150.0
print(led_resistor(5, 3.2))               # blue LED      -> 89.99999999999999 (≈90, float rounding)
print(led_resistor(5, i_ma=10))           # keyword argument: name it -> 300.0
print(led_resistor(v_supply=12, i_ma=15, v_forward=2.1))   # any order with names


# -----------------------------------------------------------------------------
# 4. Returning several values (as a tuple)
# -----------------------------------------------------------------------------
def divider(vin, r1, r2):
    vout = vin * r2 / (r1 + r2)
    i = vin / (r1 + r2)
    return vout, i                         # returns a tuple (vout, i)

vout, i = divider(12, 10_000, 3_300)       # unpack into two variables
print(f"Vout = {vout:.2f} V, I = {i * 1000:.3f} mA")


# -----------------------------------------------------------------------------
# 5. Functions calling functions
# -----------------------------------------------------------------------------
def series(resistors):
    return sum(resistors)

def parallel(resistors):
    return 1 / sum(1 / r for r in resistors)

def describe(resistors):
    print(f"{resistors}: series {series(resistors)} Ω, parallel {parallel(resistors):.1f} Ω")

describe([100, 100])           # series 200 Ω, parallel 50.0 Ω
describe([1000, 2200, 4700])


# -----------------------------------------------------------------------------
# 6. Scope: variables made inside a function stay inside
# -----------------------------------------------------------------------------
def demo():
    secret = 42                # "local" variable
    return secret

demo()
# print(secret)                # NameError: 'secret' only exists inside demo()


# -----------------------------------------------------------------------------
# 7. Type hints (optional, but you'll see them in the EE lessons)
# -----------------------------------------------------------------------------
# They describe what types the function expects/returns. Python does not
# enforce them; they're documentation that editors can check.
def capacitive_reactance(c: float, f: float) -> float:
    import math
    return 1 / (2 * math.pi * f * c)

print(f"Xc = {capacitive_reactance(1e-6, 50):.1f} Ω")    # -> 3183.1 Ω


# -----------------------------------------------------------------------------
# 8. lambda: a tiny one-line function without a name
# -----------------------------------------------------------------------------
square = lambda x: x ** 2
print(square(7))                               # 49
parts = [("R1", 470), ("R2", 100), ("R3", 220)]
print(sorted(parts, key=lambda p: p[1]))       # sort by value: R2, R3, R1


# -----------------------------------------------------------------------------
# TRY IT YOURSELF
# -----------------------------------------------------------------------------
# 1. Write  def watts_to_dbm(p):  that returns 10 * math.log10(p * 1000).
#    watts_to_dbm(1) should give 30.0
# 2. Write  def is_in_tolerance(measured, nominal, tol=0.05):  returning True
#    if measured is within ±tol of nominal.
