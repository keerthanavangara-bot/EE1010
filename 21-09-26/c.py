import numpy as np
import matplotlib.pyplot as plt
import os
import subprocess
import platform

a = 0.0
b = 2.0
print(f"a = {a}, b = {b}")
print(f"a + b = {a + b}  -> Option (C)")

x_pos = np.linspace(0, 2*np.pi, 500)
x_neg = np.linspace(-2*np.pi, 0, 500)

y_pos = np.sin(2 * x_pos)
y_neg = a + b * x_neg

plt.figure(figsize=(9, 5))
plt.plot(x_neg, y_neg, color='blue', linewidth=2,
         label=r'$f(x)=2x\ \ (x\leq 0)$')
plt.plot(x_pos, y_pos, color='red', linewidth=2,
         label=r'$f(x)=\sin(2x)\ \ (x>0)$')

plt.plot(0, 0, 'ko', markersize=8)
plt.axvline(0, color='gray', linestyle=':', alpha=0.7)
plt.axhline(0, color='gray', linestyle=':', alpha=0.7)

plt.title(r'Q46: $f(x)$ differentiable at $x=0$ with $a=0,\ b=2$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

pdf_path = os.path.abspath('q46_solution.pdf')
plt.savefig(pdf_path, format='pdf')
plt.close()
print(f"Plot saved: {pdf_path}")

if platform.system() == 'Windows':
    os.startfile(pdf_path)
elif platform.system() == 'Darwin':
    subprocess.call(['open', pdf_path])
else:
    subprocess.call(['xdg-open', pdf_path])
