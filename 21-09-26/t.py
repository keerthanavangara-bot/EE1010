import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import subprocess
import platform

# Parameters
tau = 40.0          # time constant (seconds)
V = 1.0             # step amplitude (normalized)

# Time vector
t = np.linspace(0, 200, 2000)

# First-order step response: Vout(t) = V * (1 - exp(-t/tau))
Vout = V * (1 - np.exp(-t / tau))

# Analytical time to reach 95% of steady state
t_95_exact = tau * np.log(20)   # ln(20) ≈ 2.9957
V_95 = 0.95 * V

print(f"Analytical time to 95%: {t_95_exact:.2f} seconds")
print(f"Rounded to nearest integer: {round(t_95_exact)} seconds")

# Numerical check from the array
idx = np.argmin(np.abs(Vout - V_95))
t_95_num = t[idx]
print(f"Numerical time from array: {t_95_num:.2f} seconds")

# Plot
plt.figure(figsize=(9, 5))
plt.plot(t, Vout, label=r'$V_{out}(t) = V(1 - e^{-t/\tau})$', linewidth=2)
plt.axhline(y=V_95, color='red', linestyle='--', label='95% of steady state')
plt.axvline(x=t_95_exact, color='green', linestyle='--', label=f't = {t_95_exact:.2f} s')
plt.plot(t_95_exact, V_95, 'ro', markersize=8)

plt.xlabel('Time (s)')
plt.ylabel('Output Voltage (V)')
plt.title(f'First-Order Step Response (τ = {tau} s)')
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

# Save the plot as a PDF
pdf_path = os.path.abspath('first_order_response.pdf')
plt.savefig(pdf_path, format='pdf')
plt.close()
print(f"Plot saved as '{pdf_path}'")

# Automatically open the PDF in the default viewer
if platform.system() == 'Windows':
    os.startfile(pdf_path)
elif platform.system() == 'Darwin':          # macOS
    subprocess.call(['open', pdf_path])
else:                                        # Linux
    subprocess.call(['xdg-open', pdf_path])
