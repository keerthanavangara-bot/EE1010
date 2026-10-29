# V. Keerthana | October 29, 2026

import os, platform, subprocess
import matplotlib.pyplot as plt
import numpy as np

# Sampling parameters
Fs = 40  # Sampling frequency in Hz
Ts = 1 / Fs  # Sampling period in seconds
n = np.arange(10)  # First 10 sample indices (n = 0 to 9)
t_samples = n * Ts  # Discrete time points

# Continuous time array for smooth underlying curves
t_cont = np.linspace(0, 9 * Ts, 1000)

# Signals
# x1(t) = cos(20*pi*t) -> F1 = 10 Hz
# x2(t) = cos(100*pi*t) -> F2 = 50 Hz (Aliases to 50 - 40 = 10 Hz)
x1_cont = np.cos(20 * np.pi * t_cont)
x2_cont = np.cos(100 * np.pi * t_cont)

x1_discrete = np.cos(20 * np.pi * t_samples)
x2_discrete = np.cos(100 * np.pi * t_samples)

# Plotting
fig, ax = plt.subplots(figsize=(10, 5))

# Plot continuous signals
ax.plot(
    t_cont,
    x1_cont,
    'b--',
    alpha=0.6,
    label='$x_1(t) = \\cos(20\\pi t)$ (10 Hz)',
)
ax.plot(
    t_cont,
    x2_cont,
    'g:',
    alpha=0.6,
    label='$x_2(t) = \\cos(100\\pi t)$ (50 Hz)',
)

# Plot discrete samples
ax.stem(
    t_samples,
    x1_discrete,
    linefmt='r-',
    markerfmt='ro',
    basefmt='k-',
    label='Samples $x_1[n]$ & $x_2[n]$ ($F_s = 40$ Hz)',
)

ax.set_title(
    'Aliasing Analysis: $x_1(t)$ vs $x_2(t)$ at $F_s = 40$ Hz (First 10'
    ' Samples)',
    fontsize=12,
)
ax.set_xlabel('Time $t$ (seconds)')
ax.set_ylabel('Amplitude')
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper right')

# Save and auto-open
filename = 'aliasing_plot.png'
plt.tight_layout()
plt.savefig(filename, dpi=200, bbox_inches='tight')
plt.close()

cmd = (
    'termux-open'
    if 'TERMUX_VERSION' in os.environ
    else (
        'xdg-open'
        if platform.system() == 'Linux'
        else ('open' if platform.system() == 'Darwin' else None)
    )
)
if cmd:
  subprocess.run([cmd, filename])
else:
  os.startfile(filename)

