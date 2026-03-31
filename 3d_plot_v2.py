# 3D_Radiation_Pattern_Group4.py
# Group 4: Uniform Linear Array of 4 Isotropic Elements (d = λ/2)
# Same F(θ) as above
# 3D surface plot assuming rotational symmetry about z-axis
# Radius r = normalized |F(θ)|

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# -------------------------- COMPUTE NORMALIZED PATTERN --------------------------
theta_deg_1d = np.linspace(0, 180, 200)
phi_deg_1d = np.linspace(0, 360, 200)

theta_deg, phi_deg = np.meshgrid(theta_deg_1d, phi_deg_1d)
theta_rad = np.deg2rad(theta_deg)
phi_rad = np.deg2rad(phi_deg)

cos_theta = np.cos(theta_rad)

# Raw array factor (vectorized)
num = np.sin(2 * np.pi * cos_theta)
den = 4 * np.sin((np.pi / 2) * cos_theta)

F = np.zeros_like(num, dtype=float)
mask = np.abs(den) > 1e-10
F[mask] = num[mask] / den[mask]
F[~mask] = 1.0

F_abs = np.abs(F)
F_norm = F_abs / np.max(F_abs)          # r = normalized pattern

# -------------------------- CONVERT TO CARTESIAN COORDINATES --------------------------
r = F_norm

x = r * np.sin(theta_rad) * np.cos(phi_rad)
y = r * np.sin(theta_rad) * np.sin(phi_rad)
z = r * np.cos(theta_rad)

# -------------------------- 3D SURFACE PLOT --------------------------
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(x, y, z, cmap='viridis',
                       alpha=0.85, linewidth=0, antialiased=True)

ax.set_title('Group 4 - 3D Radiation Pattern\nUniform Linear Array of 4 Isotropic Elements (d = λ/2)\nRotational symmetry about z-axis',
             fontsize=14, pad=20)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Equal aspect ratio (approximate)
ax.set_box_aspect([1, 1, 1])

# View angle for best visualization
ax.view_init(elev=20, azim=30)

# Colorbar
fig.colorbar(surf, ax=ax, shrink=0.6, aspect=10, label='Normalized |F(θ)|')

plt.tight_layout()
plt.savefig('Group4_3D_Surface.png', dpi=300)
print("✅ 3D surface plot saved as 'Group4_3D_Surface.png'")

plt.show()
