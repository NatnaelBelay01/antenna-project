import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
theta = np.linspace(0, np.pi, 1000)

# Avoid division by zero
epsilon = 1e-10
F = np.sin(2*np.pi*np.cos(theta)) / \
    (4*np.sin((np.pi/2)*np.cos(theta)) + epsilon)

# Normalize
F = np.abs(F)
F = F / np.max(F)

# Convert to dB
F_dB = 20 * np.log10(F + epsilon)

# Polar Plot (Linear)
plt.figure()
ax = plt.subplot(111, polar=True)
ax.plot(theta, F)
ax.set_title("Radiation Pattern (Linear)")
plt.show()

# Polar Plot (dB)
plt.figure()
ax = plt.subplot(111, polar=True)
ax.plot(theta, F_dB)
ax.set_title("Radiation Pattern (dB)")
plt.show()
