# =============================================================================
# LESSON 4 - Getting input from the user & converting types
# =============================================================================
# Run:  python 04_input_and_conversion.py
# This program will WAIT for you to type answers and press Enter.
# =============================================================================


# -----------------------------------------------------------------------------
# 1. input() always gives you TEXT (a string)
# -----------------------------------------------------------------------------
name = input("What is your name? ")       # the text in brackets is the prompt
print(f"Welcome, {name}!")


# -----------------------------------------------------------------------------
# 2. Converting between types
# -----------------------------------------------------------------------------
#   int("12")      -> 12        text to whole number
#   float("3.3")   -> 3.3       text to decimal number
#   str(42)        -> "42"      number to text
#   int(3.9)       -> 3         float to int (chops off the decimals, no rounding)
#   float(5)       -> 5.0

# Common beginner bug: forgetting to convert.
#   v = input("Voltage: ")      # user types 10  -> v is the TEXT "10"
#   v * 2                        # gives "1010"  (text repeated!), not 20

v = float(input("Enter voltage in volts: "))     # convert immediately
r = float(input("Enter resistance in ohms: "))

i = v / r
p = v * i
print(f"Current = {i:.4f} A")
print(f"Power   = {p:.4f} W")

# If the user types something that isn't a number (like "abc"), float() fails
# with a ValueError. Lesson 10 shows how to handle that gracefully.


# -----------------------------------------------------------------------------
# TRY IT YOURSELF
# -----------------------------------------------------------------------------
# Write a mini "LED resistor calculator":
#   ask for supply voltage, LED forward voltage, and LED current in mA,
#   then print the resistor needed:  R = (Vs - Vf) / (I_mA / 1000)
#   Example: 5 V, 2 V, 15 mA  ->  200 Ω
