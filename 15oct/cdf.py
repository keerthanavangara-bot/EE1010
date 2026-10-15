import numpy as np
import matplotlib.pyplot as plt
import os
import platform
import subprocess

# 1. Define CDF function pieces
def cdf(x):
    return np.piecewise(x, 
                        [x < 1, (x >= 1) & (x <= 4), x > 4], 
                        [0, lambda x: (x**3 - 1) / 63, 1])

x = np.linspace(0, 5, 500)
y = cdf(x)

# 2. Create the plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, label=r'$F(x) = \frac{x^3 - 1}{63}$', color='#2ca02c', linewidth=2.5)

# Formatting
plt.title('Cumulative Distribution Function $F(x)$', fontsize=14, fontweight='bold')
plt.xlabel('$x$', fontsize=12)
plt.ylabel('$F(x)$', fontsize=12)
plt.xlim(0, 5)
plt.ylim(-0.05, 1.15)
plt.axhline(0, color='black', linewidth=1, linestyle='--')
plt.axhline(1, color='gray', linewidth=1, linestyle=':', alpha=0.7, label='Max Probability = 1')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=11, loc='upper left')

# 3. Save as a PDF file
filename = 'cdf_graph.pdf'
plt.savefig(filename, bbox_inches='tight', dpi=300)
plt.close()
print(f"Saved {filename}. Opening viewer...")

# 4. Automatically trigger system viewer / app prompt
try:
    if platform.system() == 'Darwin':       # macOS
        subprocess.run(['open', filename])
    elif platform.system() == 'Windows':    # Windows
        os.startfile(filename)
    else:                                   # Linux / Termux / Android
        # Checks if running under Termux vs standard Linux desktop
        if 'TERMUX_VERSION' in os.environ or os.path.exists('/data/data/com.termux'):
            subprocess.run(['termux-open', filename])
        else:
            subprocess.run(['xdg-open', filename])
except Exception as e:
    print(f"Could not launch viewer automatically: {e}")

