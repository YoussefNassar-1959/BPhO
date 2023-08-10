import matplotlib.pyplot as plt
import numpy as np

# Data for some major planets in the Solar System
# Format: (planet name, orbital semi-major axis in AU, orbital period in years)
solar_system_data = [
    ("Mercury", 0.39, 0.24),
    ("Venus", 0.72, 0.62),
    ("Earth", 1.00, 1.00),
    ("Mars", 1.52, 1.88),
    ("Jupiter", 5.20, 11.86),
    ("Saturn", 9.58, 29.46),
    ("Uranus", 19.22, 84.01),
    ("Neptune", 30.05, 164.79)
]

# Extract data for plotting
planet_names = [data[0] for data in solar_system_data]
semi_major_axis = np.array([data[1] for data in solar_system_data])
orbital_period = np.array([data[2] for data in solar_system_data])
plotted_semi_major_axis = semi_major_axis ** (3/2)

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(plotted_semi_major_axis, orbital_period, color='blue', marker='o')
plt.plot(plotted_semi_major_axis, orbital_period, color='red', linestyle='--', label='y = mx')
plt.title("Kepler's Third Law")
plt.xlabel("R^(3/2)")
plt.ylabel("T")
plt.legend()
plt.grid(True)
plt.show()

