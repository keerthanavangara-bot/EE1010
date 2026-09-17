import numpy as np
import matplotlib
matplotlib.use('pdf')                 # PDF backend, no display needed
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os

# ---------- take input ----------
k = float(input("Enter value of k: "))

# ---------- consistency check via ranks ----------
A  = np.array([[2.0, 3.0],
               [4.0, 6.0]])
B  = np.array([[6.0],
               [3.0*k]])
AB = np.hstack((A, B))

rA  = np.linalg.matrix_rank(A)
rAB = np.linalg.matrix_rank(AB)

# ---------- plot ----------
x  = np.linspace(-2, 8, 300)
y1 = (6 - 2*x) / 3.0          # 2x + 3y = 6
y2 = (3*k - 4*x) / 6.0        # 4x + 6y = 3k

fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(x, y1, lw=2.5, label='2x + 3y = 6')
ax.plot(x, y2, '--', lw=2.5, label=f'4x + 6y = {3*k:g}  (k = {k:g})')
ax.axhline(0, color='black', lw=0.6)
ax.axvline(0, color='black', lw=0.6)
ax.grid(True, alpha=0.3)
ax.set_xlim(-2, 8); ax.set_ylim(-2, 6)
ax.set_xlabel('x'); ax.set_ylabel('y')

# ---------- verdict ----------
if rA == rAB and rA < 2:
    verdict = "Infinitely many solutions (lines coincide)"
elif rA == rAB and rA == 2:
    verdict = "Unique solution"
else:
    verdict = "No solution (lines are parallel)"

ax.set_title(f"k = {k:g}  →  rank(A) = {rA}, rank([A|B]) = {rAB}\n{verdict}",
             fontsize=11)
ax.legend(loc='upper right')

# ---------- explanation text (placed below the plot) ----------
if k == 4:
    explanation = (
        "Explanation (k = 4):\n"
        "The second equation becomes  4x + 6y = 12,  i.e.  2x + 3y = 6.\n"
        "This is identical to the first equation, so the two lines coincide.\n"
        "rank(A) = rank([A|B]) = 1 < 2  →  infinitely many solutions."
    )
else:
    explanation = (
        f"Explanation (k = {k:g}):\n"
        f"The second equation becomes  4x + 6y = {3*k:g},  i.e.  2x + 3y = {3*k/2:g}.\n"
        f"But the first equation says  2x + 3y = 6.\n"
        f"Since  {3*k/2:g}  ≠  6,  the lines are parallel and never meet.\n"
        f"rank(A) = 1  ≠  rank([A|B]) = 2  →  no solution."
    )

fig.text(0.5, 0.01, explanation, ha='center', va='bottom',
         fontsize=9, family='monospace',
         bbox=dict(boxstyle='round', facecolor='#f0f0f0', edgecolor='gray'))

# ---------- save as PDF ----------
fname = f"plot_k_{k:g}.pdf"
fig.savefig(fname, bbox_inches='tight')
print(f"\nSaved: {fname}")
print(f"rank(A) = {rA}, rank([A|B]) = {rAB}")
print(f"Verdict : {verdict}\n")

# ---------- auto-open the PDF on Android (Termux) ----------
os.system(f"termux-open {fname}")
