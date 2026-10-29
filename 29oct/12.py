import os, platform, subprocess
import matplotlib.pyplot as plt
import numpy as np

# 1. Parametric coordinates for full horizontal cone: 2x^2 = y^2 + z^2
# Let y = r*cos(theta), z = r*sin(theta), x = r / sqrt(2)
r = np.linspace(0, 3, 100)
theta = np.linspace(0, 2 * np.pi, 100)
R, THETA = np.meshgrid(r, theta)

X = R / np.sqrt(2)
Y = R * np.cos(THETA)
Z = R * np.sin(THETA)

# 2. Create 3D Plot
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot continuous full cone surface (matching classroom 'coolwarm' color map)
ax.plot_surface(X, Y, Z, cmap='coolwarm', alpha=0.8, edgecolor='none')

# 3. Point P = (1, 0, sqrt(2))
P = [1.0, 0.0, np.sqrt(2)]
ax.scatter(*P, color='black', s=90, label='Point $P(1, 0, \\sqrt{2})$', zorder=5)

# 4. Unit Normal Vectors \hat{n} and -\hat{n}
n = [np.sqrt(6) / 3, 0.0, -np.sqrt(3) / 3]
neg_n = [-x for x in n]

# Draw \hat{n} (Outward Normal - Red Arrow)
ax.quiver(
    *P,
    *n,
    color='red',
    length=1.2,
    linewidth=2.5,
    label='Unit Normal $\\hat{n}$',
)

# Draw -\hat{n} (Inward Normal - Orange Dashed Arrow)
ax.quiver(
    *P,
    *neg_n,
    color='orange',
    length=1.2,
    linewidth=2.5,
    linestyle='--',
    label='Unit Normal $-\\hat{n}$',
)

# 5. Styling & Labels
ax.set_title(
    'Surface $z^2 = 2x^2 - y^2$ and Normal Vectors at $P$',
    fontsize=12,
    pad=12,
)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.legend(loc='upper left')

# 6. Name and Date Watermark
fig.text(
    0.1,
    0.02,
    'Created by: V. Keerthana | Date: October 29, 2026',
    fontsize=9,
    fontweight='bold',
)

# 7. Save and Auto-Open
filename = 'surface_plot.png'
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

