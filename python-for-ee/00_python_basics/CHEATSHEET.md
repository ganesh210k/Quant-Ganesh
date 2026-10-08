# Python Syntax Cheat Sheet

## The 5 rules that cause most beginner errors

1. **Indentation matters.** Indent the code inside `if`, `for`, `while` and `def` by **4 spaces**.
2. **A colon `:`** goes at the end of every `if`, `elif`, `else`, `for`, `while`, `def` and `try` line.
3. **`=` stores a value; `==` compares two values.**
4. **Counting starts at 0.** `items[0]` is the first item.
5. **`input()` always returns text.** Wrap it in `float(...)` or `int(...)` to do maths with it.

## Basics
```python
# comment
print("text", 42)                 # show output
x = 5                             # variable
name = "R1"                       # string (text)
f"{name} = {x:.2f} Ω"             # f-string: insert values; .2f = 2 decimals
type(x)                           # what type is it?
```

## Numbers
```python
+  -  *  /        # / always gives a float
//                # floor division     7 // 2  -> 3
%                 # remainder          7 % 2   -> 1
**                # power              2 ** 3  -> 8
4.7e3             # 4700      100e-9 -> 0.0000001
x += 1            # x = x + 1   (also -=  *=  /=)
abs()  round(x, 2)  min()  max()  sum()
import math; math.sqrt(x); math.pi; math.log10(x); math.sin(x)
```

## Conversions
```python
int("12")   float("3.3")   str(42)   list("abc")   int(3.9) -> 3
```

## Strings
```python
s = "LM7805"
len(s)   s[0]   s[-1]   s[2:4]   s[-2:]
s.upper()  s.lower()  s.strip()  s.split(",")  s.replace("a", "b")
"78" in s       s.startswith("LM")
```

## Conditions
```python
if v > 5:
    print("high")
elif v > 3:
    print("medium")
else:
    print("low")

==  !=  <  >  <=  >=     and  or  not     3 < v < 5
result = "ON" if on else "OFF"
```

## Loops
```python
for i in range(5):          # 0,1,2,3,4
for i in range(2, 10, 2):   # 2,4,6,8
for item in my_list:
for i, item in enumerate(my_list):
for a, b in zip(list1, list2):
while condition:
break        # leave the loop
continue     # skip to the next round
```

## Lists  `[ ]`
```python
r = [100, 220, 470]
r[0]   r[-1]   r[1:]   len(r)
r.append(1000)   r.insert(0, 10)   r.remove(220)   r.pop()   r.sort()
sum(r)   max(r)   min(r)   sorted(r)   100 in r
[x * 2 for x in r]               # list comprehension
[x for x in r if x > 150]        # with filter
```

## Dictionaries `{key: value}`, tuples `( )` and sets `{ }`
```python
d = {"R": 100, "C": 1e-6}
d["R"]   d["L"] = 1e-3   d.get("X", 0)   "R" in d   del d["C"]
for key, value in d.items():

t = (3.3, 0.02);  v, i = t           # tuple + unpacking
s = {1, 2, 2, 3}                     # set -> {1, 2, 3}
```

## Functions
```python
def divider(vin, r1, r2=10_000):     # r2 has a default value
    """Docstring: what the function does."""
    return vin * r2 / (r1 + r2)

divider(12, 1000)                    # positional arguments
divider(12, r1=1000, r2=2000)        # keyword arguments
return a, b                          # return several values (a tuple)
lambda x: x ** 2                     # tiny one-line function
```

## Errors
```python
try:
    x = float(text)
except ValueError as err:
    print("bad input:", err)

raise ValueError("message")          # create your own error
assert x > 0, "x must be positive"
print(f"{x=}")                       # debug print -> x=5
```

## Files and modules
```python
import math
from math import pi
import numpy as np                   # after: pip install numpy

with open("data.txt", "w") as f:     # "w" write, "a" append, "r" read
    f.write("hello\n")
with open("data.txt") as f:
    for line in f:
        print(line.strip())

if __name__ == "__main__":           # runs only when this file is run directly
    main()
```

## Terminal commands
```
python file.py         run a file
python                 start the interactive shell (exit() to leave)
pip install numpy      install a package
cd folder              move into a folder      (cd .. goes up a level)
ls   (Mac/Linux)       list files      dir   (Windows)
Ctrl+C                 stop a running or stuck program
↑ arrow                repeat the previous command
```
