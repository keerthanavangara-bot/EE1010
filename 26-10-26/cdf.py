# Keerthana
# 26-10-26

# Python script for CDF, Inverse Transform Sampling, Numerical Probability Verification, and Plotting in Termux

import numpy as np
import matplotlib.pyplot as plt
import os
import subprocess
import shlex

# Create output directories for saving figures
os.makedirs('./figs/cdf', exist_ok=True)

# -------------------------------------------------------------
# Step 1: Generate Random Numbers using Inverse Transform Sampling
# -------------------------------------------------------------
# CDF: F(x) = (x^3 - 1) / 63  ==>  U = (x^3 - 1) / 63
# Inverse Function: x = (63*U + 1)^(1/3)
simlen = int(1e6) # 1 million samples
u = np.random.uniform(0, 1, simlen)
randvar = np.power(63.0 * u + 1.0, 1/3.0)

# -------------------------------------------------------------
# Step 2: Probability Verification P(2 <= x <= 3)
# -------------------------------------------------------------
# Theoretical Probability: F(3) - F(2) = (26/63) - (7/63) = 19/63
p_act = 19 / 63

# Simulated Probability: Counting samples in range [2, 3]
err_ind = np.nonzero((randvar >= 2) & (randvar <= 3))
p_sim = np.size(err_ind) / simlen

print("--- PROBABILITY VERIFICATION ---")
print(f"Theoretical P(2 <= x <= 3) : {p_act:.6f}")
print(f"Simulated P(2 <= x <= 3)   : {p_sim:.6f}")
print(f"Absolute Difference       : {abs(p_act - p_sim):.6f}\n")

# -------------------------------------------------------------
# Step 3: Compute Theoretical and Simulated CDF Plot Values
# -------------------------------------------------------------
x = np.linspace(0, 5, 50) # Points on the x-axis
err = []                  # Simulated CDF values list

for i in range(0, len(x)):
    err_ind = np.nonzero(randvar < x[i]) # Checking probability condition
    err_n = np.size(err_ind)             # Computing number of samples
    err.append(err_n / simlen)           # Empirical CDF value

# Theoretical CDF function
err_theo = np.zeros_like(x)
mask = (x >= 1) & (x <= 4)
err_theo[mask] = (np.power(x[mask], 3) - 1.0) / 63.0
err_theo[x > 4] = 1.0

# -------------------------------------------------------------
# Step 4: Plotting (Theoretical vs Simulated CDF & Probability Verification)
# -------------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.plot(x, err_theo, label='Theoretical CDF', color='black', linestyle='--', linewidth=2)
plt.plot(x, err, label='Simulated CDF', color='red', alpha=0.7)

# Verifying and highlighting specific probability points on the graph (F(2) and F(3))
f2_theo = (2**3 - 1) / 63
f3_theo = (3**3 - 1) / 63
plt.scatter([2, 3], [f2_theo, f3_theo], color=['blue', 'green'], s=80, zorder=5, label='Probability Check Points F(2), F(3)')

plt.grid(True)
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.title('CDF: Theoretical vs Simulated & Prob Verification')
plt.legend()

# Save plot to PDF
cdf_pdf_path = './figs/cdf/uni_cdf.pdf'
plt.savefig(cdf_pdf_path)
plt.close()

print(f"Plot saved successfully to {cdf_pdf_path}")

# Open PDF directly in Termux
subprocess.run(shlex.split(f"termux-open {cdf_pdf_path}"))

