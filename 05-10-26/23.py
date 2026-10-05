import os
import platform
import subprocess
import matplotlib.pyplot as plt
import numpy as np

# Test values of k corresponding to the three conditions
conditions = [
    ("No Solution (k = 1)", 1),
    ("Unique Solution (k = 0)", 0),
    ("Infinite Solutions (k = -1)", -1),
]

fig, axes = plt.subplots(1, 3, figsize=(18, 6))
x = np.linspace(-6, 6, 400)

for i, (title, k_val) in enumerate(conditions):
  ax = axes[i]

  # Setup coefficient matrix A and constant vector b
  A = np.array([[1.0, float(k_val)], [float(k_val), 1.0]])
  b = np.array([[1.0], [-1.0]])

  # Augmented matrix [A | b]
  aug_mat = np.hstack((A, b))

  # Apply row operation logic: R2 = R2 - k * R1 (Row Echelon Form)
  aug_mat[1, :] = aug_mat[1, :] - k_val * aug_mat[0, :]

  # Extract ranks for verification
  rank_coef = np.linalg.matrix_rank(aug_mat[:, :2])
  rank_aug = np.linalg.matrix_rank(aug_mat)

  # Determine solution status
  if rank_coef < rank_aug:
    status = "No Solution"
  elif rank_coef == rank_aug and rank_coef < 2:
    status = "Infinite Solutions"
  else:
    status = "Unique Solution"

  # Plotting the lines
  if k_val == 0:
    ax.axvline(x=1, color="blue", label="x = 1", linewidth=2)
    ax.axhline(y=-1, color="red", linestyle="--", label="y = -1", linewidth=2)
  else:
    y1 = (1 - x) / k_val
    y2 = -1 - k_val * x
    ax.plot(x, y1, label=f"x + {k_val}y = 1", color="blue", linewidth=2)
    ax.plot(
        x,
        y2,
        label=f"{k_val}x + y = -1",
        color="red",
        linestyle="--",
        linewidth=2,
    )

  # Text box displaying row echelon form and rank details on the graph
  matrix_str = (
      f"Row Echelon Form:\n{np.array2string(aug_mat, precision=2)}\nRank(A) ="
      f" {rank_coef}, Rank([A|b]) = {rank_aug}\nStatus: {status}"
  )
  ax.text(
      0.05,
      0.05,
      matrix_str,
      transform=ax.transAxes,
      fontsize=9,
      verticalalignment="bottom",
      bbox=dict(boxstyle="round", facecolor="white", alpha=0.8),
  )

  ax.set_title(title, fontsize=12, fontweight="bold")
  ax.set_xlabel("x")
  ax.set_ylabel("y")
  ax.axhline(0, color="black", linewidth=0.8, alpha=0.7)
  ax.axvline(0, color="black", linewidth=0.8, alpha=0.7)
  ax.grid(True, linestyle=":", alpha=0.6)
  ax.legend(loc="upper right")
  ax.set_xlim(-5, 5)
  ax.set_ylim(-5, 5)

plt.tight_layout()

# Save as PDF
pdf_filename = "linear_systems_analysis.pdf"
plt.savefig(pdf_filename, format="pdf", bbox_inches="tight")
plt.close()
print(f"PDF successfully generated and saved as '{pdf_filename}'")

# Automatically open the PDF file popup via the system viewer
current_os = platform.system()
try:
  if current_os == "Windows":
    os.startfile(pdf_filename)
  elif current_os == "Darwin":  # macOS
    subprocess.run(["open", pdf_filename])
  else:  # Linux
    subprocess.run(["xdg-open", pdf_filename])
except Exception as e:
  print(f"Could not open automatically: {e}")

