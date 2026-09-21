import numpy as np

A_elem = np.array([
    [ 6.0,  0.0,  0.0, -1.0, -1.0,  0.0],
    [12.0,  3.0,  0.0, -1.8,  0.0, -2.0],
    [ 6.0,  0.0,  2.0, -0.5, -2.0, -1.0],
    [ 0.0,  1.0,  0.0, -0.2,  0.0,  0.0]
])

c1 = np.array([1.0, 0.0, 0.0, 0.0, 0.0, 0.0])
c2 = np.array([0.0, 0.0, 0.0, 1.0, 0.0, 0.0])

A_full = np.vstack([A_elem, c1, c2])
B_full = np.array([0.0, 0.0, 0.0, 0.0, 1.0, 2.4])

x = np.linalg.solve(A_full, B_full)

labels = ["x1 (Glucose)", "x2 (NH3)", "x3 (O2)", "x4 (Biomass)", "x5 (CO2)", "x6 (H2O)"]

for label, val in zip(labels, x):
    print(f"{label}: {val:.2f}")

print(f"\nOxygen consumption (x3): {x[2]:.2f} moles O2/mol glucose")

