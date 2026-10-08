# =============================================================================
# LESSON 11 - Modules (import) and working with files
# =============================================================================
# Run:  python 11_modules_and_files.py
# =============================================================================


# -----------------------------------------------------------------------------
# 1. import: use code someone else wrote
# -----------------------------------------------------------------------------
# A "module" is a Python file full of useful functions. Imports go at the TOP
# of a file in real programs (they are spread out here only for teaching).

import math                       # import the whole module, use math.xxx
print(math.sqrt(2))

from math import pi, sin          # import specific names, use them directly
print(sin(pi / 2))                # 1.0

import random as rnd              # import with a short nickname ("alias")
print(rnd.randint(1, 6))          # a random dice roll

# Python's "standard library" comes built in: math, random, statistics, csv,
# datetime, pathlib, json ...  Other packages (numpy, scipy, matplotlib) must
# be installed first with:   pip install numpy


# -----------------------------------------------------------------------------
# 2. A few handy standard-library modules
# -----------------------------------------------------------------------------
import statistics
samples = [4.98, 5.01, 5.03, 4.97, 5.00]
print("mean :", statistics.mean(samples))
print("stdev:", round(statistics.stdev(samples), 4))

from datetime import datetime
print("Now:", datetime.now().strftime("%Y-%m-%d %H:%M"))


# -----------------------------------------------------------------------------
# 3. Writing a text file
# -----------------------------------------------------------------------------
# open(filename, mode)   mode: "w" = write (overwrites!), "a" = append, "r" = read
# 'with' automatically closes the file when the indented block ends.

with open("measurements.txt", "w") as f:
    f.write("time_s,voltage_V\n")            # \n = end of line
    for t in range(5):
        v = 5 * (1 - math.exp(-t))           # an RC charging curve
        f.write(f"{t},{v:.4f}\n")
print("Wrote measurements.txt")


# -----------------------------------------------------------------------------
# 4. Reading a text file
# -----------------------------------------------------------------------------
with open("measurements.txt", "r") as f:
    lines = f.readlines()                    # list of lines (strings)

print("Header:", lines[0].strip())
voltages = []
for line in lines[1:]:                       # skip the header line
    t_text, v_text = line.strip().split(",")
    voltages.append(float(v_text))
print("Voltages read back:", voltages)
print("Max voltage:", max(voltages))


# -----------------------------------------------------------------------------
# 5. The csv module - the proper way for spreadsheet-like files
# -----------------------------------------------------------------------------
import csv

with open("measurements.txt", newline="") as f:
    reader = csv.DictReader(f)               # each row becomes a dict!
    for row in reader:
        print(f"t={row['time_s']} s  ->  {row['voltage_V']} V")


# -----------------------------------------------------------------------------
# 6. Making YOUR OWN module
# -----------------------------------------------------------------------------
# Any .py file is a module. If you save functions in  ee_tools.py  in the
# same folder, another file can do:
#
#     from ee_tools import parallel
#
# The special block below runs ONLY when you run this file directly, not
# when another file imports it. You'll see it in every EE lesson:

def main():
    print("Running as a program, not being imported.")

if __name__ == "__main__":
    main()

# Clean up the example file so it doesn't clutter your folder
import os
os.remove("measurements.txt")


# -----------------------------------------------------------------------------
# TRY IT YOURSELF
# -----------------------------------------------------------------------------
# 1. Write the numbers 1..10 and their squares to "squares.csv",
#    then read the file back and print the sum of the squares (385).
# 2. Create ee_tools.py with a function  parallel(r1, r2)  and import it
#    from a second file.
