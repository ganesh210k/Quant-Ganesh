"""
Lesson 03 - NumPy linear algebra: solving circuits with nodal analysis
======================================================================

Python concepts: NumPy arrays, vectorisation, np.linalg.solve,
                 dataclasses, building a tiny netlist "language".
EE concepts:     Modified Nodal Analysis (MNA) - the algorithm inside SPICE.
                 G * x = b where x = [node voltages, voltage-source currents].

Run:  python lessons/03_numpy_nodal_analysis.py
"""

from dataclasses import dataclass

import numpy as np


@dataclass
class Resistor:
    name: str
    n1: int
    n2: int
    value: float


@dataclass
class VSource:
    name: str
    n_plus: int
    n_minus: int
    value: float


@dataclass
class ISource:
    """Current flows from n_from through the source into n_to."""
    name: str
    n_from: int
    n_to: int
    value: float


def solve_dc(elements: list, ground: int = 0) -> tuple[dict[int, float], dict[str, float]]:
    """Solve a linear DC circuit with MNA. Node 0 is ground."""
    node_fields = ("n1", "n2", "n_plus", "n_minus", "n_from", "n_to")
    nodes = sorted({getattr(e, f) for e in elements for f in node_fields if hasattr(e, f)} - {ground})
    idx = {n: k for k, n in enumerate(nodes)}
    vsrcs = [e for e in elements if isinstance(e, VSource)]
    n, m = len(nodes), len(vsrcs)

    A = np.zeros((n + m, n + m))
    b = np.zeros(n + m)

    for e in elements:
        if isinstance(e, Resistor):
            g = 1.0 / e.value
            for a in (e.n1, e.n2):
                if a != ground:
                    A[idx[a], idx[a]] += g
            if e.n1 != ground and e.n2 != ground:
                A[idx[e.n1], idx[e.n2]] -= g
                A[idx[e.n2], idx[e.n1]] -= g
        elif isinstance(e, ISource):
            if e.n_from != ground:
                b[idx[e.n_from]] -= e.value
            if e.n_to != ground:
                b[idx[e.n_to]] += e.value

    for k, vs in enumerate(vsrcs):
        row = n + k
        if vs.n_plus != ground:
            A[idx[vs.n_plus], row] += 1
            A[row, idx[vs.n_plus]] += 1
        if vs.n_minus != ground:
            A[idx[vs.n_minus], row] -= 1
            A[row, idx[vs.n_minus]] -= 1
        b[row] = vs.value

    x = np.linalg.solve(A, b)
    voltages = {node: float(x[idx[node]]) for node in nodes}
    voltages[ground] = 0.0
    # MNA current convention: positive = flowing into + terminal from the circuit.
    # Flip sign so the reported value is the current the source *delivers*.
    currents = {vs.name: float(-x[n + k]) for k, vs in enumerate(vsrcs)}
    return voltages, currents


if __name__ == "__main__":
    print("== NumPy warm-up ==")
    r = np.array([100, 220, 470, 1000])
    print("Currents at 5 V (vectorised):", 5 / r)
    print("Total parallel R:", 1 / np.sum(1 / r))

    print("\n== Wheatstone bridge ==")
    #      1 ---R1--- 2 ---R3--- 0
    #      |          |
    #      |          R5 (galvanometer)
    #      |          |
    #      1 ---R2--- 3 ---R4--- 0
    circuit = [
        VSource("V1", 1, 0, 10.0),
        Resistor("R1", 1, 2, 1000),
        Resistor("R2", 1, 3, 1000),
        Resistor("R3", 2, 0, 1000),
        Resistor("R4", 3, 0, 1200),
        Resistor("R5", 2, 3, 100),
    ]
    v, i = solve_dc(circuit)
    for node in sorted(v):
        print(f"  V({node}) = {v[node]:.4f} V")
    print(f"  Bridge imbalance V(2)-V(3) = {(v[2] - v[3]) * 1e3:.2f} mV")
    print(f"  Supply current = {i['V1'] * 1e3:.3f} mA")

    print("\n== Superposition check (V + I source) ==")
    ckt = [VSource("V1", 1, 0, 12), Resistor("R1", 1, 2, 4), Resistor("R2", 2, 0, 6), ISource("I1", 0, 2, 1.0)]
    v, _ = solve_dc(ckt)
    v_only, _ = solve_dc(ckt[:3])
    i_only, _ = solve_dc([VSource("V1", 1, 0, 0)] + ckt[1:])
    print(f"  V(2) full = {v[2]:.3f} V  =  {v_only[2]:.3f} (V only) + {i_only[2]:.3f} (I only)")
