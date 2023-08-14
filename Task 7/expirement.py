import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Orbital parameters for the planets in the solar system (in AU)
orbital_parameters = {
    "Mercury": {"a": 0.39, "e": 0.206, "T": 0.241, "beta": 7.0},
    "Venus": {"a": 0.72, "e": 0.007, "T": 0.615, "beta": 3.4},
    "Earth": {"a": 1.0, "e": 0.017, "T": 1.0, "beta": 0.0},
    "Mars": {"a": 1.52, "e": 0.093, "T": 1.881, "beta": 1.9},
    "Jupiter": {"a": 5.20, "e": 0.049, "T": 11.86, "beta": 1.3},
    "Saturn": {"a": 9.58, "e": 0.056, "T": 29.46, "beta": 2.5},
    "Uranus": {"a": 19.22, "e": 0.046, "T": 84.01, "beta": 0.8},
    "Neptune": {"a": 30.05, "e": 0.010, "T": 164.8, "beta": 1.8},
    "Pluto": {"a": 39.48, "e": 0.248, "T": 248.1, "beta": 17.2}
}

# Create a dictionary to store planet orbit points
planet_orbits = {}

# Generate orbit points for each planet
num_points = 100  # Number of points along the orbit
theta = np.linspace(0, 2 * np.pi, num_points)
for planet, params in orbital_parameters.items():
    a = params["a"]
    e = params["e"]
    T = params["T"]
    beta = params["beta"]

    r = a * (1 - e ** 2) / (1 + e * np.cos(theta))
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    z = np.zeros_like(x)

    rotation_matrix = np.array([[np.cos(np.radians(beta)), 0, np.sin(np.radians(beta))],
                                [0, 1, 0],
                                [-np.sin(np.radians(beta)), 0, np.cos(np.radians(beta))]])
    orbit_points = np.dot(rotation_matrix, np.array([x, y, z]))
    planet_orbits[planet] = orbit_points

# Shifting all orbits to be centered around Earth's orbit
earth_orbit = planet_orbits["Earth"]
for planet, orbit_points in planet_orbits.items():
    planet_orbits[planet] = orbit_points - earth_orbit

# Create the figure and 3D axis
fig = plt.figure(figsize=(800, 600))
ax = fig.add_subplot(111, projection='3d')

# Find the maximum absolute values for setting plot limits
max_val = 0
for orbit_points in planet_orbits.values():
    max_val = max(max_val, np.max(np.abs(orbit_points)))

# Set plot limits based on the maximum absolute values
ax.set_xlim([-max_val, max_val])
ax.set_ylim([-max_val, max_val])
ax.set_zlim([-max_val, max_val])

# Plot the orbit animations for each planet
lines = {}
for planet, orbit_points in planet_orbits.items():
    line, = ax.plot([], [], [], label=planet)
    lines[planet] = line


def init():
    for line in lines.values():
        line.set_data([], [])
        line.set_3d_properties([])
    return [lines[planet] for planet in lines]


def animate(i):
    for planet, line in lines.items():
        orbit_points = planet_orbits[planet]
        line.set_data(orbit_points[0, :i], orbit_points[1, :i])
        line.set_3d_properties(orbit_points[2, :i])
    return [lines[planet] for planet in lines]


# Set animation parameters
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=num_points, interval=50, blit=True)

# Add legend
ax.legend()

plt.show()