import numpy as np
import matplotlib.pyplot as plt

# Orbital parameters (semi-major axis, eccentricity)
orbital_params = {
    "Sun": (0, 0),  # Treat the Sun as a planet
    "Mercury": (0.387, 0.21),
    "Venus": (0.723, 0.01),
    "Earth": (1, 0.02),
    "Mars": (1.523, 0.09),
}

# Calculate periods based on Kepler's third law
orbital_periods = {planet: (a ** 3) ** 0.5 for planet, (a, _) in orbital_params.items()}

years = 20 * orbital_periods["Earth"]
days_per_year = 365
time_step = years * days_per_year / 1234
total_steps = int(years * days_per_year / time_step)

planet_positions = {planet: np.zeros((total_steps, 2)) for planet in orbital_params.keys()}
planet_thetas = {planet: 0 for planet in orbital_params.keys()}

for i in range(total_steps):
    for planet, (a, e) in orbital_params.items():
        if planet == "Sun":
            # Adjust the Sun's position relative to Earth
            planet_positions[planet][i, :] = planet_positions["Earth"][i, :]
        else:
            theta_rad = np.deg2rad(planet_thetas[planet])
            r = (a * (1 - e ** 2)) / (1 + e * np.cos(theta_rad))
            x = r * np.cos(theta_rad)
            y = r * np.sin(theta_rad)
            planet_positions[planet][i, :] = x, y
            planet_thetas[planet] += 360 * time_step / days_per_year * (1 / (orbital_periods[planet] / orbital_periods["Earth"]))

# Calculate relative positions of planets and the Sun
relative_positions = {planet: positions - planet_positions["Earth"] for planet, positions in planet_positions.items()}

# Plotting
plt.figure(figsize=(10, 6))
colors = ['yellow', 'gray', 'orange', 'blue', 'red', 'green', 'goldenrod']
for i, planet in enumerate(relative_positions.keys()):
    plt.plot(relative_positions[planet][:, 0], relative_positions[planet][:, 1], color=colors[i], label=planet)

plt.scatter([0], [0], color="black", marker="o", label="Earth")

plt.xlabel("x position relative to Earth (AU)")
plt.ylabel("y position relative to Earth (AU)")
plt.title("Planetary Orbits Relative to Earth")
plt.legend()
plt.grid(True)
plt.axis('equal')  # Set the x-y ratio to 1:1

# Set x and y axis limits to 2.5 AU
plt.xlim(-2.5, 2.5)
plt.ylim(-2.5, 2.5)

plt.show()

