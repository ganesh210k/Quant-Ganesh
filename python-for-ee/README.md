# Python for Electrical Engineers

This is a hands-on course. Each lesson teaches Python by solving real EE problems, and every lesson is a runnable script.

## Setup (one time)

```bash
cd python-for-ee
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## How to study (the method matters more than the material)

1. **Read** a lesson top to bottom, then **run** it: `python lessons/01_basics_ohms_law.py`
2. **Break it on purpose.** Change values, delete a line, and predict the output *before* you run it.
3. **Do the matching exercises** in `exercises/exercises.py`, then grade yourself:
   ```bash
   pytest exercises/ -v
   ```
4. **Rebuild the lesson from memory** in a blank file a few days later. Treat this step as required: it is what makes the skill stick.
5. **Extend it** with one idea from the "Level up" column below.

## Curriculum

| # | Lesson | Python skills | EE topic | Level up |
|---|--------|---------------|----------|----------|
| 01 | `01_basics_ohms_law.py` | functions, type hints, `*args`, comprehensions, exceptions, f-strings | Ohm's law, dividers, E12 values | Add E24/E96 series and pick the best resistor *pair* for a divider ratio |
| 02 | `02_complex_phasors_ac.py` | `complex`, `cmath`, dicts, closures | Impedance, phasors, P/Q/S, PF correction, resonance | Plot \|Z(f)\| for the RLC across 10 Hz–100 kHz |
| 03 | `03_numpy_nodal_analysis.py` | NumPy, `np.linalg.solve`, dataclasses | Modified Nodal Analysis (how SPICE works) | Add a VCVS (op-amp) element and solve an inverting amplifier |
| 04 | `04_transients_ode.py` | `solve_ivp`, matplotlib | RC and RLC transients, damping | Add a diode and simulate a half-wave rectifier with a smoothing capacitor |
| 05 | `05_signals_fft.py` | FFT, windowing, boolean masks | Sampling, aliasing, harmonics, THD | Compute THD of a square wave and compare with theory (48.3 %) |
| 06 | `06_filters_bode.py` | `scipy.signal`, log arrays | Bode plots, Butterworth filters | Design a 50/60 Hz notch filter with `signal.iirnotch` |
| 07 | `07_three_phase_power.py` | complex arrays, broadcasting, `@`, classes | 3-phase Y loads, neutral current, symmetrical components | Add delta loads and Y↔Δ conversion |
| 08 | `08_control_systems.py` | stateful classes, simulation loops | DC motor model, PID, anti-windup | Auto-tune the PID gains with `scipy.optimize.minimize` on ITAE |
| 09 | `09_data_from_instruments.py` | CSV, `curve_fit`, `polyfit`, pathlib | Extracting C and diode parameters from measurements | Read a real scope CSV export from your lab |

Plots and CSVs go to `out/`.

## A 6-week plan (about 1 hour a day)

- **Week 1:** Lessons 01–02. Learn core Python thoroughly before moving on. Use [Python's official tutorial](https://docs.python.org/3/tutorial/), sections 3–5 and 9, alongside them.
- **Week 2:** Lesson 03. Learn NumPy well, because every later lesson builds on it.
- **Week 3:** Lessons 04–05.
- **Week 4:** Lessons 06–07.
- **Week 5:** Lessons 08–09.
- **Week 6:** Capstone project (pick one):
  - A **mini-SPICE** that parses a text netlist (`R1 1 2 1k`) and runs DC and AC analysis, built by extending lesson 03 with lesson 02's impedances
  - A **power-quality analyser** that reads a CSV of voltage and current samples and reports RMS, PF, THD and harmonics up to the 25th
  - A **battery model** with an equivalent-circuit model (R0 + RC pairs) that you fit to a discharge curve with `curve_fit`
  - **Instrument automation**: drive a real DMM or scope with `pyvisa` and log the readings to CSV

## Habits that make you "very good" rather than just able to get by

- **Vectorise.** If you write `for i in range(len(x))` over numbers, ask whether NumPy can do it in one line.
- **Test your physics.** Write a `pytest` check for every formula against a hand calculation or a known limit, such as Vc(τ) = 63.2 % or In = 0 when the load is balanced.
- **Always carry units.** Put them in variable names (`r_ohm`, `t_ms`) or use the `pint` library.
- **Validate numerics against analytics.** Lesson 04 does this with `solve_ivp` against the closed form. Make it a reflex.
- **Read other people's code.** `scipy.signal` and [`python-control`](https://python-control.readthedocs.io/), and later [`PySpice`](https://pyspice.fabrice-salvaire.fr/), [`pandapower`](https://www.pandapower.org/) for power systems and `scikit-rf` for RF.
- **Use git** for every project, even small ones.

## Next libraries by specialty

| Area | Libraries |
|------|-----------|
| Power systems | `pandapower`, `pypsa` |
| Controls | `python-control`, `slycot` |
| Signal processing / comms | `scipy.signal`, `commpy` |
| RF / microwave | `scikit-rf` |
| Circuits | `PySpice`, `lcapy` (symbolic) |
| Embedded / hardware | `pyserial`, `pyvisa`, MicroPython |
| Symbolic math | `sympy`, for deriving transfer functions by hand-style algebra |
| Data | `pandas`, Jupyter notebooks |
