# =============================================================================
# LESSON 6 - Loops: repeating things
# =============================================================================
# Run:  python 06_loops.py
# =============================================================================


# -----------------------------------------------------------------------------
# 1. for loop with range()
# -----------------------------------------------------------------------------
# Syntax:
#     for variable in something:
#         indented code runs once per item
#
# range(5) produces 0, 1, 2, 3, 4   (5 numbers, starting at 0, NOT including 5)
for k in range(5):
    print("k =", k)

# range(start, stop)        -> start ... stop-1
# range(start, stop, step)  -> counts by step
print(list(range(1, 6)))         # [1, 2, 3, 4, 5]
print(list(range(0, 50, 10)))    # [0, 10, 20, 30, 40]
print(list(range(5, 0, -1)))     # [5, 4, 3, 2, 1]   counting down


# -----------------------------------------------------------------------------
# 2. Example: a table of current vs voltage for a 100 Ω resistor
# -----------------------------------------------------------------------------
r = 100
print(f"{'V':>4} {'I (mA)':>8}")         # table header
for v in range(0, 13, 3):                 # 0, 3, 6, 9, 12
    i_ma = v / r * 1000
    print(f"{v:>4} {i_ma:>8.1f}")


# -----------------------------------------------------------------------------
# 3. Looping over items directly (strings, lists ...)
# -----------------------------------------------------------------------------
for ch in "RLC":
    print("Component:", ch)

resistors = [100, 220, 470]          # a list (lesson 7)
for value in resistors:
    print(f"{value} Ω")


# -----------------------------------------------------------------------------
# 4. Accumulator pattern: build up a result inside a loop (VERY common)
# -----------------------------------------------------------------------------
total = 0                       # 1) start with an empty result BEFORE the loop
for value in resistors:
    total += value              # 2) update it each time round
print("Series total:", total)   # 3) use it AFTER the loop  -> 790

# Parallel resistance: 1/Rt = 1/R1 + 1/R2 + ...
inv_sum = 0
for value in resistors:
    inv_sum += 1 / value
print(f"Parallel total: {1 / inv_sum:.2f} Ω")    # -> 59.98 Ω


# -----------------------------------------------------------------------------
# 5. while loop: repeat AS LONG AS a condition is True
# -----------------------------------------------------------------------------
# Use while when you don't know in advance how many repeats you need.
# Example: a capacitor discharges 10% each step. How many steps until < 1 V?
v_cap = 10.0
steps = 0
while v_cap >= 1.0:
    v_cap = v_cap * 0.9
    steps += 1
print(f"Took {steps} steps, final voltage {v_cap:.3f} V")

# DANGER: if the condition never becomes False, the loop runs forever.
# Press Ctrl+C in the terminal to stop a stuck program.


# -----------------------------------------------------------------------------
# 6. break and continue
# -----------------------------------------------------------------------------
readings = [4.9, 5.0, 5.1, 7.8, 5.0]
for r_v in readings:
    if r_v > 6:
        print(f"Spike {r_v} V detected - stopping!")
        break                 # exit the loop immediately
    print("Reading OK:", r_v)

for n in range(6):
    if n % 2 == 0:
        continue              # skip the rest of THIS round, go to the next
    print("odd:", n)          # prints 1, 3, 5


# -----------------------------------------------------------------------------
# 7. enumerate(): get the position AND the item
# -----------------------------------------------------------------------------
for index, value in enumerate(resistors):
    print(f"R{index + 1} = {value} Ω")      # R1 = 100 Ω, R2 = 220 Ω ...


# -----------------------------------------------------------------------------
# 8. Nested loops: a loop inside a loop
# -----------------------------------------------------------------------------
for v in (5, 12):                # () makes a tuple - like a list (lesson 8)
    for r_val in (100, 1000):
        print(f"V={v:>2}, R={r_val:>4} -> I = {v / r_val * 1000:.1f} mA")


# -----------------------------------------------------------------------------
# TRY IT YOURSELF
# -----------------------------------------------------------------------------
# 1. Print the voltages of an RC charging curve for t = 0..5 time constants:
#        Vc = 5 * (1 - math.exp(-t))     (remember:  import math)
# 2. With a while loop, find the smallest n where 2**n > 1_000_000.
#    (Answer: 20)
