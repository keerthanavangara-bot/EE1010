//Keerthana
// 29oct
import numpy as np
import matplotlib.pyplot as plt

# 1. Define the grid for x and y
x = np.linspace(-3, 3, 400)
y = np.linspace(-3, 3, 400)
X, Y = np.meshgrid(x, y)

# 2. Surface equation: z^2 = 2x^2 - y^2 => z = +sqrt(2x^2 - y^2)
Z_sq = 2 * X**2 - Y**2
Z = np.sqrt(np.maximum(0, Z_sq))
Z[Z_sq < 0] = np.nan  # Mask non-real values outside domain

# 3. Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the 3D surface
surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.75, edgecolor='none')

# 4. Highlight Point P = (1, 0, sqrt(2))
P_x, P_y, P_z = 1.0, 0.0, np.sqrt(2)
ax.scatter([P_x], [P_y], [P_z], color='red', s=100, label='Point $P(1, 0, \\sqrt{2})$', zorder=5)

# 5. Draw Unit Normal Vectors \hat{n} and -\hat{n} using quivers (arrows)
n_x = np.sqrt(6) / 3   # approx 0.816
n_y = 0.0
n_z = -np.sqrt(3) / 3  # approx -0.577

# Normal vector \hat{n}
ax.quiver(P_x, P_y, P_z, n_x, n_y, n_z,

