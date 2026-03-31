# 2D_Radiation_Pattern_Group4.py
# Group 4: Uniform Linear Array of 4 Isotropic Elements (d = λ/2)
# F(θ) = sin(2π cos θ) / (4 sin(π cos θ / 2))
# This script generates:
#   1. Polar plot of normalized |F(θ)| (linear scale)
#   2. Rectangular plot of the same pattern in dB scale
# θ ranges from 0° to 180° (elevation plane)
# Normalized so maximum = 1 at θ = 90°

import numpy as np
import matplotlib.pyplot as plt

# -------------------------- COMPUTE NORMALIZED PATTERN --------------------------
theta_deg = np.linspace(0, 180, 2000)          # Fine grid, includes θ=90°
theta_rad = np.deg2rad(theta_deg)
cos_theta = np.cos(theta_rad)

# Raw array factor
num = np.sin(2 * np.pi * cos_theta)
den = 4 * np.sin((np.pi / 2) * cos_theta)

# Avoid division-by-zero at θ = 90° (limit is exactly 1)
F = np.zeros_like(num, dtype=float)
mask = np.abs(den) > 1e-10
F[mask] = num[mask] / den[mask]
F[~mask] = 1.0

# Radiation pattern uses magnitude (absolute value)
F_abs = np.abs(F)

# Normalize (max value should be exactly 1)
F_norm = F_abs / np.max(F_abs)

# -------------------------- 2D POLAR PLOT (LINEAR SCALE) --------------------------
fig1 = plt.figure(figsize=(8, 6))
ax1 = fig1.add_subplot(111, projection='polar')

# Plot with θ = 0° at the top (standard antenna convention: z-axis upward)
ax1.plot(theta_rad, F_norm, linewidth=2, color='blue')

ax1.set_title('Group 4 - Normalized 2D Radiation Pattern\nLinear Scale\n(Uniform 4-element array, d = λ/2)',
              fontsize=14, pad=20)
ax1.set_theta_zero_location('N')      # θ = 0° at North (top)
# Clockwise increase (standard elevation convention)
ax1.set_theta_direction(-1)
ax1.set_rlim(0, 1.05)
ax1.set_rlabel_position(90)
ax1.grid(True, linestyle='--', alpha=0.7)

# Optional: label main lobe direction
ax1.annotate('Main lobe (broadside)', xy=(np.pi/2, 1.0), xytext=(np.pi/2 + 0.3, 0.8),
             arrowprops=dict(facecolor='red', shrink=0.05), fontsize=10)
ax1.annotate('Major lobe\n(broadside, max)',
             xy=(np.pi/2, 1.0), xytext=(np.pi/2 + 0.4, 0.85),
             arrowprops=dict(facecolor='red', shrink=0.05, width=1),
             fontsize=10, ha='center', color='red', fontweight='bold')

# Nulls
ax1.annotate('Null', xy=(0, 0.02), xytext=(np.deg2rad(-25), 0.4),
             arrowprops=dict(arrowstyle='->', color='black'), fontsize=9, color='black')
ax1.annotate('Null', xy=(np.deg2rad(60), 0.02), xytext=(np.deg2rad(40), 0.35),
             arrowprops=dict(arrowstyle='->', color='black'), fontsize=9, color='black')
ax1.annotate('Null', xy=(np.deg2rad(120), 0.02), xytext=(np.deg2rad(140), 0.35),
             arrowprops=dict(arrowstyle='->', color='black'), fontsize=9, color='black')
ax1.annotate('Null', xy=(np.pi, 0.02), xytext=(np.deg2rad(205), 0.4),
             arrowprops=dict(arrowstyle='->', color='black'), fontsize=9, color='black')

# Side lobes
ax1.annotate('Side lobe\n(≈ –11.3 dB)',
             xy=(np.deg2rad(43), 0.28), xytext=(np.deg2rad(10), 0.55),
             arrowprops=dict(arrowstyle='->', color='orange'), fontsize=9, color='orange')
ax1.annotate('Side lobe\n(≈ –11.3 dB)',
             xy=(np.deg2rad(137), 0.28), xytext=(np.deg2rad(170), 0.55),
             arrowprops=dict(arrowstyle='->', color='orange'), fontsize=9, color='orange')

# Beamwidth indicator (curved arrow)
ax1.annotate('', xy=(np.deg2rad(77), 0.75), xytext=(np.deg2rad(103), 0.75),
             arrowprops=dict(arrowstyle='<->', color='green', lw=1.5))
ax1.text(np.deg2rad(90), 0.82, 'HPBW ≈ 26.3°',
         fontsize=10, color='green', ha='center')
plt.tight_layout()
plt.savefig('Group4_2D_Polar_Linear.png', dpi=300)
print("✅ 2D Polar Linear plot saved as 'Group4_2D_Polar_Linear.png'")

# -------------------------- 2D PATTERN IN dB (RECTANGULAR) --------------------------
F_db = 20 * np.log10(F_norm + 1e-12)

fig2 = plt.figure(figsize=(10, 6))
plt.plot(theta_deg, F_db, linewidth=2.5, color='red')

plt.title('Group 4 – Normalized Radiation Pattern in dB\n(Uniform 4-element array, d = λ/2)', fontsize=14)
plt.xlabel('θ (degrees)')
plt.ylabel('Magnitude (dB)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.ylim(-40, 5)
plt.xlim(0, 180)

# ====================== LABEL ALL REQUIRED FEATURES ======================
# Nulls
plt.axvline(0,   color='black', linestyle='--', alpha=0.8)
plt.axvline(60,  color='black', linestyle='--', alpha=0.8)
plt.axvline(120, color='black', linestyle='--', alpha=0.8)
plt.axvline(180, color='black', linestyle='--', alpha=0.8)
plt.text(5,   -35, 'Null', fontsize=10, color='black', rotation=90)
plt.text(55,  -35, 'Null', fontsize=10, color='black', rotation=90)
plt.text(115, -35, 'Null', fontsize=10, color='black', rotation=90)
plt.text(172, -35, 'Null', fontsize=10, color='black', rotation=90)

# Major lobe
plt.text(90, 2, 'Major lobe\n(broadside)', fontsize=11,
         color='red', ha='center', fontweight='bold')

# Side lobes
plt.text(43, -13, 'Side lobe\n(–11.3 dB)',
         fontsize=10, color='orange', ha='center')
plt.text(137, -13, 'Side lobe\n(–11.3 dB)',
         fontsize=10, color='orange', ha='center')

# Half-power beamwidth
plt.axhline(-3, color='green', linestyle='--', linewidth=1.5, label='–3 dB')
plt.axvline(76.8, color='green', linestyle=':', alpha=0.7)
plt.axvline(103.2, color='green', linestyle=':', alpha=0.7)
plt.annotate('HPBW ≈ 26.3°', xy=(90, -4), xytext=(90, -12),
             arrowprops=dict(arrowstyle='<->', color='green', lw=1.5),
             fontsize=11, color='green', ha='center')

plt.legend(loc='upper right')

plt.tight_layout()
plt.savefig('Group4_2D_dB.png', dpi=300)
print("✅ 2D dB plot saved as 'Group4_2D_dB.png'")

plt.show()
