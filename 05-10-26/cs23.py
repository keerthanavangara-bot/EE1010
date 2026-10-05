import os
import platform
import subprocess
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

k = sp.Symbol('k', real=True)
A_sym = sp.Matrix([
    [1, k, 1],
    [k, 1, -1]
])
A_sym[1, :] = A_sym[1, :] - k * A_sym[0, :]
print("Symbolic Row Echelon Form:")
sp.pprint(A_sym)
print("\nCondition for non-unique solution: 1 - k^2 = 0 => k = 1 or k = -1\n")

test_cases = [2.0, 1.0, -1.0]

for val in test_cases:
    print(f"--- Testing k = {val} ---")
    A = np.array([[1.0, val], [val, 1.0]])
    b = np.array([[1.0], [-1.0]])
    aug = np.hstack((A, b))
    
    aug[1, :] = aug[1, :] - val * aug[0, :]
    print("Row Reduction Matrix (Echelon Form):")
    print(np.round(aug, 4))
    
    rc = np.linalg.matrix_rank(aug[:, :2])
    ra = np.linalg.matrix_rank(aug)
    
    print(f"Rank of A: {rc}")
    print(f"Rank of Augmented Matrix: {ra}")
    
    if rc < ra:
        print("Conclusion: No Solution\n")
    elif rc == ra and rc < 2:
        print("Conclusion: Infinitely Many Solutions\n")
    else:
        print("Conclusion: Unique Solution\n")

try:
    user_k = float(input("Enter value for k (No Solution: k=1, Infinitely Many: k=-1, Unique: k != ±1): "))
except ValueError:
    user_k = 0.0

A_u = np.array([[1.0, user_k], [user_k, 1.0]])
b_u = np.array([[1.0], [-1.0]])
aug_u = np.hstack((A_u, b_u))
aug_u[1, :] = aug_u[1, :] - user_k * aug_u[0, :]

rc_u = np.linalg.matrix_rank(aug_u[:, :2])
ra_u = np.linalg.matrix_rank(aug_u)

if rc_u < ra_u:
    status_u = "No Solution"
elif rc_u == ra_u and rc_u < 2:
    status_u = "Infinitely Many Solutions"
else:
    status_u = "Unique Solution"

fig, ax = plt.subplots(figsize=(8, 6))
x = np.linspace(-6, 6, 400)

if user_k == 0:
    ax.axvline(x=1, color='blue', label='x = 1', linewidth=2)
    ax.axhline(y=-1, color='red', linestyle='--', label='y = -1', linewidth=2)
else:
    ax.plot(x, (1 - x) / user_k, label=f'x + {user_k}y = 1', color='blue', linewidth=2)
    ax.plot(x, -1 - user_k * x, label=f'{user_k}x + y = -1', color='red', linestyle='--')

txt = f"k = {user_k}\nEchelon:\n{np.array2string(aug_u, precision=2)}\nRank(A) = {rc_u}, Rank([A|b]) = {ra_u}\n{status_u}"
ax.text(0.05, 0.05, txt, transform=ax.transAxes, fontsize=10, bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
ax.set_title(f"Graph for k = {user_k} ({status_u})")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right')

plt.tight_layout()
pdf_file = f"linear_system_k_{user_k}.pdf"
plt.savefig(pdf_file, format="pdf", bbox_inches="tight")
plt.close()

print(f"\nSaved graph to '{pdf_file}' and launching viewer...")
os_sys = platform.system()
if os_sys == "Windows":
    os.startfile(pdf_file)
elif os_sys == "Darwin":
    subprocess.run(["open", pdf_file])
else:
    subprocess.run(["xdg-open", pdf_file])

