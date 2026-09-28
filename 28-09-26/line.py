import subprocess
import sys




import numpy as np
import matplotlib.pyplot as plt

def main():
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Define grids for Plane 1 and Plane 2
    x1_vals = np.linspace(-5, 5, 20)
    x2_vals = np.linspace(-5, 5, 20)
    X1, X2 = np.meshgrid(x1_vals, x2_vals)
    X3_plane1 = -X1 - X2

    x3_vals = np.linspace(-5, 5, 20)
    X2_p2, X3_p2 = np.meshgrid(x2_vals, x3_vals)
    X1_p2 = -2 * X3_p2

    # Plot the planes
    ax.plot_surface(X1, X2, X3_plane1, color='cyan', alpha=0.5, label='Plane 1')
    ax.plot_surface(X1_p2, X2_p2, X3_p2, color='orange', alpha=0.5, label='Plane 2')

    # Plot the line of intersection
    t = np.linspace(-5, 5, 100)
    ax.plot(-2 * t, t, t, color='red', linewidth=4, label='Line')

    # Graph labels
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_zlabel('X3')
    ax.set_title('Intersection of Two Planes')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

