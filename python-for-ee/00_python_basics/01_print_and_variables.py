# =============================================================================
# LESSON 1 - print() and variables
# =============================================================================
# How to run this file (type in a terminal, inside the 00_python_basics folder):
#
#     python 01_print_and_variables.py
#
# (On some Macs/Linux you must type  python3  instead of  python.)
#
# Anything after a  #  is a COMMENT. Python ignores it. Comments are notes
# for humans. This whole block is comments, so Python skips it.
# =============================================================================


# -----------------------------------------------------------------------------
# 1. print() shows something on the screen
# -----------------------------------------------------------------------------
# print is a FUNCTION. You "call" a function by writing its name followed by
# round brackets ( ). Whatever you put inside the brackets is given to it.

print("Hello, engineer!")          # text must be inside quotes "..." or '...'
print(42)                          # numbers do NOT need quotes
print("Voltage:", 230, "V")        # commas separate items; print adds a space

print()                            # an empty print() prints a blank line


# -----------------------------------------------------------------------------
# 2. Variables: a NAME that stores a VALUE
# -----------------------------------------------------------------------------
# Syntax:      name = value
# The  =  sign means "store the value on the right into the name on the left".
# It is NOT "equals" like in maths. (Python checks equality with  ==  - lesson 5.)

voltage = 12          # store the number 12 under the name "voltage"
resistance = 4

current = voltage / resistance     # use variables in calculations
print("Current =", current, "A")   # -> Current = 3.0 A

# A variable can be changed later (that's why it's called a VARIABLE):
voltage = 24
print("New voltage:", voltage)     # -> New voltage: 24

# NOTE: 'current' did NOT update automatically. It still holds 3.0, because
# Python calculated it once, at the moment that line ran. Code runs top to bottom.
print("Current is still", current)  # -> Current is still 3.0


# -----------------------------------------------------------------------------
# 3. Rules for naming variables
# -----------------------------------------------------------------------------
# - letters, digits and underscore _ only
# - cannot START with a digit       (1st_value  is an error)
# - no spaces                        (my value   is an error)
# - case-sensitive                   (Voltage and voltage are DIFFERENT names)
# - convention in Python: lowercase_with_underscores  ("snake_case")

supply_voltage = 5.0      # good: clear and readable
r1 = 1000                 # fine: short names are OK when the meaning is obvious
x = 3                     # legal, but tells the reader nothing - avoid in real code


# -----------------------------------------------------------------------------
# 4. Several assignments at once (handy shortcuts)
# -----------------------------------------------------------------------------
r1, r2, r3 = 100, 220, 470          # three variables in one line
print(r1, r2, r3)                   # -> 100 220 470

a = b = 0                           # both a and b become 0


# -----------------------------------------------------------------------------
# 5. f-strings: the BEST way to print text mixed with values
# -----------------------------------------------------------------------------
# Put the letter  f  just before the opening quote. Then anything inside
# curly braces { } is calculated and inserted into the text.

name = "R1"
value = 4700
print(f"{name} is {value} ohms")             # -> R1 is 4700 ohms
print(f"Double is {value * 2} ohms")         # -> Double is 9400 ohms

# Control decimal places with  :.Nf   (N = number of decimals)
power = 2.3456789
print(f"Power = {power:.2f} W")              # -> Power = 2.35 W


# -----------------------------------------------------------------------------
# TRY IT YOURSELF (edit this file and run it again)
# -----------------------------------------------------------------------------
# 1. Make variables  v = 9  and  r = 330,  calculate  i = v / r,  and print
#    "Current is 0.0273 A" using an f-string with 4 decimals.
# 2. Delete the quotes around "Hello, engineer!" and run the file.
#    Read the error message - learning to read errors is a key skill!
#    Then put the quotes back.
