# =============================================================================
# LESSON 2 - Numbers and maths
# =============================================================================
# Run:  python 02_numbers_and_math.py
# =============================================================================


# -----------------------------------------------------------------------------
# 1. Two kinds of numbers
# -----------------------------------------------------------------------------
# int   = whole number          e.g. 5, -3, 1000
# float = number with a decimal e.g. 3.3, 0.001, -2.0

n_resistors = 4        # int
vcc = 3.3              # float

# type() tells you what kind of value something is
print(type(n_resistors))   # -> <class 'int'>
print(type(vcc))           # -> <class 'float'>


# -----------------------------------------------------------------------------
# 2. Arithmetic operators
# -----------------------------------------------------------------------------
print(7 + 2)     # 9     addition
print(7 - 2)     # 5     subtraction
print(7 * 2)     # 14    multiplication
print(7 / 2)     # 3.5   division  (ALWAYS gives a float)
print(7 // 2)    # 3     floor division (drops the decimal part)
print(7 % 2)     # 1     remainder ("modulo") - 7 = 2*3 + 1
print(7 ** 2)    # 49    power  (NOT ^ like on a calculator!)

# Order of operations is the same as maths: brackets, powers, * /, + -
print(2 + 3 * 4)        # -> 14
print((2 + 3) * 4)      # -> 20


# -----------------------------------------------------------------------------
# 3. Scientific notation - you will use this ALL the time in EE
# -----------------------------------------------------------------------------
# 4.7e3 means 4.7 × 10³ ;  100e-9 means 100 × 10⁻⁹
r = 4.7e3          # 4.7 kΩ
c = 100e-9         # 100 nF
tau = r * c        # time constant
print("tau =", tau, "seconds")       # -> tau = 0.00047 seconds
print(f"tau = {tau * 1000} ms")      # -> tau = 0.47 ms

# Underscores make big numbers readable (Python ignores them):
sample_rate = 44_100


# -----------------------------------------------------------------------------
# 4. Shortcut operators: update a variable using its own value
# -----------------------------------------------------------------------------
total_r = 0
total_r += 100      # same as  total_r = total_r + 100
total_r += 220
print(total_r)      # -> 320
total_r *= 2        # same as  total_r = total_r * 2   (also -=  /= )
print(total_r)      # -> 640


# -----------------------------------------------------------------------------
# 5. Built-in maths functions
# -----------------------------------------------------------------------------
print(abs(-5))             # 5      absolute value
print(round(3.14159, 2))   # 3.14   round to 2 decimals
print(max(3, 9, 2))        # 9
print(min(3, 9, 2))        # 2

# For sqrt, sin, pi, log ... we IMPORT the "math" module (more in lesson 11)
import math

print(math.sqrt(16))       # 4.0
print(math.pi)             # 3.141592653589793
print(math.log10(1000))    # 3.0

# Example: resonant frequency of an LC circuit  f = 1 / (2π√(LC))
L = 10e-3
C = 1e-6
f0 = 1 / (2 * math.pi * math.sqrt(L * C))
print(f"Resonant frequency = {f0:.1f} Hz")    # -> 1591.5 Hz


# -----------------------------------------------------------------------------
# 6. A float surprise every programmer must know
# -----------------------------------------------------------------------------
print(0.1 + 0.2)          # -> 0.30000000000000004  (!)
# Computers store decimals in binary, so tiny errors appear. This is normal.
# Never compare floats with == ; check if they are CLOSE instead:
print(math.isclose(0.1 + 0.2, 0.3))   # -> True


# -----------------------------------------------------------------------------
# TRY IT YOURSELF
# -----------------------------------------------------------------------------
# 1. Power in a resistor: P = I² × R. With I = 0.02 A and R = 220 Ω, print P.
#    (Answer: 0.088 W)
# 2. How many full 4.7 kΩ resistors fit in 50 kΩ, and what's left over?
#    Hint: use  //  and  %   on 50000 and 4700.
