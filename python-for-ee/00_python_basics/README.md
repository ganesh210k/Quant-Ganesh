# Part 0: Python Basics (start here)

This part assumes you know no Python. Finish it before the EE lessons in `../lessons/`.

## Step 1: Install Python

1. Download **Python 3.12 or newer** from https://www.python.org/downloads/.
   - **On Windows:** in the first installer screen, tick **"Add python.exe to PATH"**.
2. Install an editor: **[VS Code](https://code.visualstudio.com/)**, plus its "Python" extension from Microsoft.
3. Open a terminal (in VS Code: *Terminal → New Terminal*) and check that Python works:
   ```
   python --version
   ```
   If that fails, try `python3 --version` (Mac and Linux) or `py --version` (Windows). Then use that word in place of `python` everywhere below.

## Step 2: Learn the two ways to run Python

**A) Interactive shell.** Use it to try one line at a time:
```
python
>>> 2 + 3
5
>>> v = 12
>>> v / 4
3.0
>>> exit()
```
The `>>>` is Python waiting for you. Don't type it yourself.

**B) Running a file.** This is how real programs run:
```
cd python-for-ee/00_python_basics
python 01_print_and_variables.py
```
`cd` means "change directory", which moves the terminal into that folder.

## Step 3: Work through the lessons in order

| File | You learn |
|------|-----------|
| `01_print_and_variables.py` | `print()`, comments, variables, f-strings |
| `02_numbers_and_math.py` | int/float, `+ - * / // % **`, `1e-6` notation, the `math` module |
| `03_strings.py` | text, indexing `[0]`, slicing `[1:3]`, string methods |
| `04_input_and_conversion.py` | `input()`, `int()` / `float()` / `str()` |
| `05_conditions.py` | `if` / `elif` / `else`, `and` / `or` / `not`, **indentation** |
| `06_loops.py` | `for`, `range()`, `while`, `break`, `continue` |
| `07_lists.py` | lists, `append`, list comprehensions, `zip` |
| `08_dicts_tuples_sets.py` | dictionaries, tuples, sets |
| `09_functions.py` | `def`, `return`, default and keyword arguments |
| `10_errors_and_debugging.py` | reading error messages, `try` / `except`, debugging tips |
| `11_modules_and_files.py` | `import`, reading and writing files, `if __name__ == "__main__"` |

**For each lesson:**
1. Open the file in your editor and **read every comment**. The expected output is written next to the code as `# -> ...`.
2. Run it. Check that what you see matches those comments.
3. **Change things** and predict the result before you run it again.
4. Do the **TRY IT YOURSELF** tasks at the bottom of the file.
5. Do the matching exercise in `practice.py`, then run `python practice.py` to check it.

When `practice.py` shows **13/13 ✅**, you're ready for `../lessons/01_basics_ohms_law.py`.

## Suggested pace (about 1 hour a day)

- **Days 1–2:** lessons 01–04
- **Days 3–4:** lessons 05–06. Loops and conditions are the core of programming, so take your time.
- **Days 5–6:** lessons 07–08
- **Day 7:** lesson 09. Functions matter most for the EE lessons.
- **Day 8:** lessons 10–11, then finish `practice.py`

Keep `CHEATSHEET.md` open while you work.
