import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # or 'Qt5Agg'

# Create theta and phi grid
theta = np.linspace(0, np.pi, 200)
phi = np.linspace(0, 2*np.pi, 200)

theta, phi = np.meshgrid(theta, phi)

# Avoid division by zero
epsilon = 1e-10

# Radiation function (Group 4)
F = np.sin(2*np.pi*np.cos(theta)) / \
    (4*np.sin((np.pi/2)*np.cos(theta)) + epsilon)

# Normalize
F = np.abs(F)
F = F / np.max(F)

# Convert to Cartesian coordinates
X = F * np.sin(theta) * np.cos(phi)
Y = F * np.sin(theta) * np.sin(phi)
Z = F * np.cos(theta)

# Plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z)

# Labels
ax.set_title("3D Radiation Pattern (Uniform Linear Array - 4 Elements)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()
