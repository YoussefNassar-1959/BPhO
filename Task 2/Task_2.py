import numpy as np
import matplotlib.pyplot as plt

# Semi-major axes in AU
semi_major_axes = {
    #"Mercury": 0.39,
    #"Venus": 0.72,
    #"Earth": 1.0,
    #"Mars": 1.52, 
    "Jupiter": 5.2,
    "Saturn": 9.58,
    "Uranus": 19.22,
    "Neptune": 30.05
}

# Eccentricities
eccentricities = {
    #"Mercury": 0.205,
    #"Venus": 0.007,
    #"Earth": 0.017,
    #"Mars": 0.094,
    "Jupiter": 0.049,
    "Saturn": 0.056,
    "Uranus": 0.046,
    "Neptune": 0.010
}

# Angle values
theta = np.linspace(0, 2 * np.pi, 1000)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Plot inner planet orbits
for planet in semi_major_axes:
    a = semi_major_axes[planet]
    e = eccentricities[planet]
    r = a * (1 - e ** 2) / (1 + e * np.cos(theta))
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    ax.plot(x, y, label=planet)


# Plot the yellow dot at (0, 0)
ax.plot(0, 0, 'yo', label='Sun')


# Set equal aspect ratio
ax.set_aspect('equal', adjustable='box')

# Add labels and legend
ax.set_title("Outer Planet Orbits")
ax.set_xlabel("X (AU)")
ax.set_ylabel("Y (AU)")
ax.legend()

# Show the plot
plt.show()