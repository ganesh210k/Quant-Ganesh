# =============================================================================
# LESSON 10 - Errors, reading tracebacks, and debugging
# =============================================================================
# Run:  python 10_errors_and_debugging.py
# Errors are NORMAL. Professionals see them all day. The skill is reading them.
# =============================================================================


# -----------------------------------------------------------------------------
# 1. How to read an error message ("traceback")
# -----------------------------------------------------------------------------
# Example of what Python prints when something goes wrong:
#
#   Traceback (most recent call last):
#     File "circuit.py", line 7, in <module>        <- WHERE: file and line
#       i = v / r                                   <- the line that failed
#           ~~^~~
#   ZeroDivisionError: division by zero             <- WHAT went wrong
#
# READ FROM THE BOTTOM UP: the last line tells you the error type and message;
# the lines above show which line of your code caused it.


# -----------------------------------------------------------------------------
# 2. The errors you'll meet most often
# -----------------------------------------------------------------------------
# SyntaxError       - code is not valid Python: missing colon, bracket, quote
#                       if x > 3          <- missing ':'
# IndentationError  - spaces at the start of lines don't line up
# NameError         - you used a name that doesn't exist (often a typo)
#                       print(voltge)
# TypeError         - wrong type for the operation
#                       "R = " + 100
# ValueError        - right type, bad value
#                       float("abc")
# ZeroDivisionError - divided by zero
# IndexError        - list position doesn't exist
#                       [1, 2, 3][5]
# KeyError          - dictionary key doesn't exist
# ModuleNotFoundError - import of something not installed  ->  pip install it


# -----------------------------------------------------------------------------
# 3. Handling errors with try / except
# -----------------------------------------------------------------------------
# Syntax:
#     try:
#         code that might fail
#     except SomeError:
#         what to do if it fails

def safe_current(v, r):
    try:
        return v / r
    except ZeroDivisionError:
        print("  Warning: R = 0 is a short circuit!")
        return float("inf")       # "infinity"

print(safe_current(5, 100))
print(safe_current(5, 0))


# Converting user text safely:
for text in ["3.3", "abc", "12"]:
    try:
        value = float(text)
        print(f"  '{text}' -> {value}")
    except ValueError:
        print(f"  '{text}' is not a number, skipping")


# -----------------------------------------------------------------------------
# 4. Raising your own errors to catch bad input early
# -----------------------------------------------------------------------------
def resistor_power(i, r):
    if r < 0:
        raise ValueError(f"Resistance cannot be negative (got {r})")
    return i ** 2 * r

try:
    resistor_power(0.1, -10)
except ValueError as err:          # 'as err' gives you the error message
    print("  Caught:", err)


# -----------------------------------------------------------------------------
# 5. Debugging techniques
# -----------------------------------------------------------------------------
# a) PRINT DEBUGGING - print values to see what's really happening.
#    The f"{name=}" trick prints both the name and the value:
v_in, r1, r2 = 12, 10_000, 4_700
v_out = v_in * r2 / (r1 + r2)
print(f"{v_out=}")                 # -> v_out=3.836734693877551

# b) assert - stop immediately if something you believe is True isn't
assert 0 < v_out < v_in, "divider output must be between 0 and Vin"

# c) Check types when confused:   print(type(x))

# d) Use the interactive Python shell: type  python  in a terminal and try
#    lines one at a time. Type  exit()  to leave.

# e) breakpoint() - put this line in your code; the program pauses there and
#    lets you inspect variables. Type  p variable_name  to print, c to continue.

# f) Read the error, google the LAST line of it. Someone has had it before.

print("Lesson 10 finished without crashing!")


# -----------------------------------------------------------------------------
# TRY IT YOURSELF
# -----------------------------------------------------------------------------
# Each line below has ONE bug. Uncomment one at a time, run, read the error,
# fix it.
#
# print("Voltage is: " + 5)
# if 3 > 2
#     print("yes")
# values = [1, 2, 3]; print(values[3])
# Resistance = 100; print(resistance)
