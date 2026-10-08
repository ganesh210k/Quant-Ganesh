# =============================================================================
# LESSON 7 - Lists: storing many values in one variable
# =============================================================================
# Run:  python 07_lists.py
# A list is an ordered collection written with square brackets [ ].
# =============================================================================


# -----------------------------------------------------------------------------
# 1. Creating and reading lists
# -----------------------------------------------------------------------------
readings = [4.98, 5.01, 5.03, 4.97, 5.00]     # voltages from a multimeter
parts = ["R1", "C1", "L1"]                    # lists can hold text too
empty = []                                    # an empty list

print(readings[0])        # 4.98   first item  (index starts at 0, like strings)
print(readings[-1])       # 5.0    last item
print(readings[1:3])      # [5.01, 5.03]   slicing works just like strings
print(len(readings))      # 5      number of items


# -----------------------------------------------------------------------------
# 2. Changing lists (unlike strings, lists CAN be changed in place)
# -----------------------------------------------------------------------------
parts[0] = "R2"           # replace an item
print(parts)              # ['R2', 'C1', 'L1']

parts.append("D1")        # add to the end
print(parts)              # ['R2', 'C1', 'L1', 'D1']

parts.insert(0, "U1")     # insert at position 0
parts.remove("L1")        # remove by value (the first match)
last = parts.pop()        # remove AND return the last item
print(parts, "| popped:", last)   # ['U1', 'R2', 'C1'] | popped: D1

print("C1" in parts)      # True   - is it in the list?


# -----------------------------------------------------------------------------
# 3. Useful functions on lists of numbers
# -----------------------------------------------------------------------------
print(sum(readings))                  # 24.990000000000002  (float surprise, lesson 2!)
print(max(readings), min(readings))   # 5.03 4.97
average = sum(readings) / len(readings)
print(f"Average = {average:.3f} V")   # -> 4.998 V

print(sorted(readings))       # new sorted list; original unchanged
readings.sort()               # sorts the list itself
readings.sort(reverse=True)   # largest first


# -----------------------------------------------------------------------------
# 4. Building a list with a loop
# -----------------------------------------------------------------------------
currents = []                 # start empty
for v in [1, 2, 3, 4, 5]:
    currents.append(v / 100)  # Ohm's law with R = 100
print(currents)               # [0.01, 0.02, 0.03, 0.04, 0.05]


# -----------------------------------------------------------------------------
# 5. List comprehension: the same thing in ONE line (very "Pythonic")
# -----------------------------------------------------------------------------
# Syntax:   [expression for item in collection]
currents = [v / 100 for v in [1, 2, 3, 4, 5]]
print(currents)               # same result as above

# With a filter:  [expression for item in collection if condition]
high = [x for x in [4.98, 5.01, 5.03, 4.97, 5.00] if x > 5.0]
print(high)                   # [5.01, 5.03]

squares = [n ** 2 for n in range(1, 6)]
print(squares)                # [1, 4, 9, 16, 25]


# -----------------------------------------------------------------------------
# 6. Looping over two lists together with zip()
# -----------------------------------------------------------------------------
voltages = [5, 12, 24]
resistances = [100, 470, 1000]
for v, r in zip(voltages, resistances):
    print(f"{v} V / {r} Ω = {v / r * 1000:.2f} mA")


# -----------------------------------------------------------------------------
# 7. Lists inside lists (like a table / matrix)
# -----------------------------------------------------------------------------
table = [
    [1, 2, 3],
    [4, 5, 6],
]
print(table[1][2])        # 6    row 1, column 2


# -----------------------------------------------------------------------------
# 8. A trap: copying a list
# -----------------------------------------------------------------------------
a = [1, 2, 3]
b = a            # b is NOT a copy - it's another name for the SAME list
b.append(4)
print(a)         # [1, 2, 3, 4]   a changed too!
c = a.copy()     # a real, independent copy
c.append(5)
print(a, c)      # [1, 2, 3, 4] [1, 2, 3, 4, 5]


# -----------------------------------------------------------------------------
# TRY IT YOURSELF
# -----------------------------------------------------------------------------
# readings = [3.31, 3.29, 3.35, 3.10, 3.30]
# 1. Print the average.
# 2. Using a list comprehension, make a list of readings outside 3.3 V ± 2%
#    (i.e. below 3.234 or above 3.366).   Answer: [3.1]
