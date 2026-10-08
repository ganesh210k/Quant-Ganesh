# =============================================================================
# LESSON 5 - Making decisions: if / elif / else
# =============================================================================
# Run:  python 05_conditions.py
# =============================================================================


# -----------------------------------------------------------------------------
# 1. Booleans: True and False
# -----------------------------------------------------------------------------
# Comparisons produce a bool (True or False). Note the capital T and F.
print(5 > 3)       # True
print(5 < 3)       # False
print(5 == 5)      # True    == means "is equal to"   (one = is assignment!)
print(5 != 3)      # True    != means "is NOT equal to"
print(5 >= 5)      # True
print(5 <= 4)      # False


# -----------------------------------------------------------------------------
# 2. if statement - THE MOST IMPORTANT SYNTAX RULE IN PYTHON: INDENTATION
# -----------------------------------------------------------------------------
# Syntax:
#     if condition:            <- colon at the end is required
#         do_this              <- indented 4 spaces = "inside" the if
#         and_this
#     this_runs_always         <- back to the left = outside the if
#
# Python uses indentation (spaces at the start of a line) to know which lines
# belong together. Other languages use { }. Use 4 spaces, consistently.

temperature = 85

if temperature > 80:
    print("WARNING: component is hot!")
    print("Consider a heatsink.")
print("Temperature check done.")        # runs no matter what


# -----------------------------------------------------------------------------
# 3. if / else - two paths
# -----------------------------------------------------------------------------
battery_v = 3.4

if battery_v >= 3.6:
    print("Battery OK")
else:
    print("Battery LOW - recharge")


# -----------------------------------------------------------------------------
# 4. if / elif / else - many paths ("elif" = "else if")
# -----------------------------------------------------------------------------
# Python checks from top to bottom and runs ONLY the FIRST branch that is True.
pf = 0.82    # power factor

if pf >= 0.95:
    rating = "excellent"
elif pf >= 0.9:
    rating = "good"
elif pf >= 0.8:
    rating = "acceptable"
else:
    rating = "poor - needs correction"
print(f"Power factor {pf} is {rating}")     # -> acceptable


# -----------------------------------------------------------------------------
# 5. Combining conditions: and, or, not
# -----------------------------------------------------------------------------
v = 4.9
i = 0.3

if v > 4.75 and v < 5.25:       # both must be True
    print("Voltage within 5V ±5%")

if 4.75 < v < 5.25:              # Python allows this neat chained form too
    print("(same check, shorter)")

if v < 4.5 or i > 1.0:           # at least one must be True
    print("FAULT")
else:
    print("No fault")

overload = False
if not overload:                 # not flips True <-> False
    print("System running normally")


# -----------------------------------------------------------------------------
# 6. Nested if (an if inside an if) - each level indents 4 more spaces
# -----------------------------------------------------------------------------
power_on = True
v_out = 11.2
if power_on:
    if v_out < 11.5:
        print("Output under-voltage")
    else:
        print("Output OK")
else:
    print("Power is off")


# -----------------------------------------------------------------------------
# 7. One-line conditional expression
# -----------------------------------------------------------------------------
status = "ON" if power_on else "OFF"
print("Status:", status)


# -----------------------------------------------------------------------------
# TRY IT YOURSELF
# -----------------------------------------------------------------------------
# Resistor colour bands: write code that takes  digit = 3  and prints the
# colour: 0 black, 1 brown, 2 red, 3 orange, 4 yellow, else "other".
# Then change digit and re-run to test every branch.
