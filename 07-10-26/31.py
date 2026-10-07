# Keerthana
# 7-10-26

import numpy as np
import matplotlib.pyplot as plt
import subprocess
import os

# Solve for a and b
a = 3*(1**2) + 2*1       # a = 5  (from differentiability)
b = 3 - a                # b = -2 (from continuity)

print(f"a = {a}")
print(f"b = {b}")

# Piecewise function
def f(x):
    return np.where(x < 1, a*x + b, x**3 + x**2 + 1)

# Build the graph
x = np.linspace(-2, 3, 500)
y = f(x)

plt.plot(x, y, label="f(x)", color="blue")
plt.axvline(1, color="gray", linestyle="--", label="x = 1")
plt.scatter([1], [3], color="red", zorder=5, label="junction (1, 3)")
plt.title("Piecewise f(x) - differentiable at x = 1")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
pdf_path = os.path.abspath("graph.pdf")
plt.savefig(pdf_path, format="pdf")
plt.close()

print(f"Saved: {pdf_path}")


subprocess.run(["xdg-open", pdf_path])   # Linux

