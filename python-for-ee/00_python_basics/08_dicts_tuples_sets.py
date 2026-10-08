# =============================================================================
# LESSON 8 - Dictionaries, tuples and sets
# =============================================================================
# Run:  python 08_dicts_tuples_sets.py
# =============================================================================


# -----------------------------------------------------------------------------
# 1. Dictionary (dict): look up a VALUE by a KEY  - written with { key: value }
# -----------------------------------------------------------------------------
# Think of a real dictionary: you look up a word (key) to get its meaning (value).
resistor = {
    "name": "R1",
    "value": 4700,
    "tolerance": 0.05,
    "package": "0805",
}

print(resistor["value"])          # 4700   - square brackets with the KEY
resistor["value"] = 10000         # change a value
resistor["power_w"] = 0.125       # add a new key
del resistor["package"]           # remove a key
print(resistor)

# Asking for a key that doesn't exist is an error (KeyError).
# .get() is safer: returns None (or a default you choose) instead.
print(resistor.get("colour"))             # None
print(resistor.get("colour", "unknown"))  # unknown
print("value" in resistor)                # True - checks the KEYS


# -----------------------------------------------------------------------------
# 2. Looping over a dictionary
# -----------------------------------------------------------------------------
colour_code = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4}

for colour in colour_code:                    # loops over KEYS
    print(colour)

for colour, digit in colour_code.items():     # keys AND values together
    print(f"{colour:>7} = {digit}")

print(list(colour_code.keys()))
print(list(colour_code.values()))

# Real use: decode a 3-band resistor: digit, digit, multiplier
bands = ["yellow", "black", "red"]                # 4, 0, ×10²
ohms = (colour_code[bands[0]] * 10 + colour_code[bands[1]]) * 10 ** colour_code[bands[2]]
print(f"{bands} = {ohms} Ω")                     # -> 4000 Ω


# -----------------------------------------------------------------------------
# 3. Tuple: like a list but CANNOT be changed  - written with ( )
# -----------------------------------------------------------------------------
# Use a tuple for a fixed group of values that belong together.
point = (3.3, 0.02)          # (voltage, current) operating point
v, i = point                 # "unpacking": split a tuple into variables
print(f"V = {v}, I = {i}")
# point[0] = 5               # would cause TypeError - tuples are fixed

# Functions often return tuples (lesson 9):
quotient, remainder = divmod(17, 5)
print(quotient, remainder)   # 3 2


# -----------------------------------------------------------------------------
# 4. Set: unordered collection with NO duplicates - written with { } (no colons)
# -----------------------------------------------------------------------------
used_parts = ["R1", "C1", "R1", "R2", "C1"]
unique = set(used_parts)
print(unique)                      # {'R1', 'R2', 'C1'}  (order may vary)
print(len(unique))                 # 3

stock = {"R1", "R2", "C1", "C2"}
needed = {"R1", "C1", "U1"}
print(needed - stock)              # {'U1'}  - needed but not in stock
print(needed & stock)              # items in both


# -----------------------------------------------------------------------------
# 5. A list of dictionaries - how real data usually looks
# -----------------------------------------------------------------------------
bom = [   # bill of materials
    {"ref": "R1", "qty": 4, "unit_price": 0.01},
    {"ref": "C1", "qty": 2, "unit_price": 0.05},
    {"ref": "U1", "qty": 1, "unit_price": 1.20},
]
total = 0
for item in bom:
    line_cost = item["qty"] * item["unit_price"]
    total += line_cost
    print(f"{item['ref']:<4} {item['qty']:>3} x {item['unit_price']:.2f} = {line_cost:.2f}")
print(f"BOM total: {total:.2f}")      # -> 1.34


# -----------------------------------------------------------------------------
# Quick summary
# -----------------------------------------------------------------------------
#   list   [1, 2, 3]        ordered, changeable, duplicates OK
#   tuple  (1, 2, 3)        ordered, NOT changeable
#   dict   {"a": 1}         key -> value lookup
#   set    {1, 2, 3}        no duplicates, no order


# -----------------------------------------------------------------------------
# TRY IT YOURSELF
# -----------------------------------------------------------------------------
# 1. Make a dict  prefixes = {"p": 1e-12, "n": 1e-9, "u": 1e-6, "m": 1e-3, "k": 1e3}
#    and use it to convert the text "47n" into 4.7e-08.
#    Hint: number = float(text[:-1]),  prefix = text[-1]
