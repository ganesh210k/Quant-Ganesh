# =============================================================================
# LESSON 3 - Strings (text)
# =============================================================================
# Run:  python 03_strings.py
# A "string" (type str) is text. Write it inside quotes: "..." or '...'
# =============================================================================


part = "LM7805 voltage regulator"

# -----------------------------------------------------------------------------
# 1. Basic operations
# -----------------------------------------------------------------------------
print(len(part))              # 24   number of characters (spaces count!)
print(part.upper())           # LM7805 VOLTAGE REGULATOR
print(part.lower())           # lm7805 voltage regulator
print("Part: " + part)        # +  joins strings together ("concatenation")
print("-" * 20)               # *  repeats a string: --------------------

# Joining text and a number with + is an ERROR:
#   print("R = " + 100)        -> TypeError
# Convert the number to text first with str(), or (better) use an f-string:
print("R = " + str(100))
print(f"R = {100}")


# -----------------------------------------------------------------------------
# 2. Indexing: get one character by position
# -----------------------------------------------------------------------------
# IMPORTANT: Python counts from 0, not 1!
#
#    L  M  7  8  0  5
#    0  1  2  3  4  5      <- positive index
#   -6 -5 -4 -3 -2 -1      <- negative index (counts from the end)

code = "LM7805"
print(code[0])        # L    first character
print(code[2])        # 7
print(code[-1])       # 5    last character


# -----------------------------------------------------------------------------
# 3. Slicing: get a piece   text[start:stop]   (stop is NOT included)
# -----------------------------------------------------------------------------
print(code[0:2])      # LM       positions 0 and 1
print(code[2:])       # 7805     from position 2 to the end
print(code[-2:])      # 05       last two characters
print(code[:4])       # LM78     from the start up to (not including) 4

# Real use: the last 2 digits of a 78xx regulator are its output voltage
output_v = int(code[-2:])         # int() turns the text "05" into number 5
print(f"{code} gives {output_v} V")   # -> LM7805 gives 5 V


# -----------------------------------------------------------------------------
# 4. Useful string methods
# -----------------------------------------------------------------------------
# A "method" is a function that belongs to a value: value.method()
reading = "   12.6 V  "
print(reading.strip())                  # "12.6 V"  removes spaces at both ends
print("12.6 V".replace(" V", ""))       # "12.6"
print("R1,R2,R3".split(","))            # ['R1', 'R2', 'R3']  -> a list (lesson 7)
print("V" in "12.6 V")                  # True   - does it contain "V"?
print("12.6 V".startswith("12"))        # True
print("12.6 V".endswith("A"))           # False

# Strings cannot be changed in place. Methods RETURN a new string:
s = "volt"
s.upper()          # result is thrown away!
print(s)           # still "volt"
s = s.upper()      # store the result to keep it
print(s)           # "VOLT"


# -----------------------------------------------------------------------------
# 5. Special characters and multi-line strings
# -----------------------------------------------------------------------------
print("Line 1\nLine 2")          # \n  = new line
print("Col1\tCol2")              # \t  = tab
print("Ω, µ, °, ± all work")     # Unicode symbols are fine
spec = """This is a
multi-line string,
using three quotes."""
print(spec)


# -----------------------------------------------------------------------------
# 6. f-string formatting tricks
# -----------------------------------------------------------------------------
v = 3.14159
print(f"{v:.2f}")        # 3.14       2 decimal places
print(f"{0.00047:.2e}")  # 4.70e-04   scientific notation
print(f"{0.25:.0%}")     # 25%        percentage
print(f"[{'R1':>6}]")    # [    R1]   right-align in 6 characters
print(f"[{'R1':<6}]")    # [R1    ]   left-align
print(f"{1234567:,}")    # 1,234,567  thousands separator


# -----------------------------------------------------------------------------
# TRY IT YOURSELF
# -----------------------------------------------------------------------------
# 1. Given  label = "R12=4700"  use .split("=") to get the name and the value,
#    convert the value to an int, and print "R12 is 4.7 kΩ".
# 2. Print the 3rd character of "LM317".  (Answer: 3)
