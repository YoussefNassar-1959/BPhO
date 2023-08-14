import numpy as np
import matplotlib.pyplot as plt


pluto_a = 39.509
pluto_e = 0.25
neptune_a = 30.246
neptune_e = 0.01

pluto_P = (pluto_a ** 3) ** 0.5
neptune_P = (neptune_a ** 3) ** 0.5

years = 10*pluto_P
days_per_year = 365
time_step = years*365/1234  # days
total_steps = int(years * days_per_year / time_step)

pluto_x_positions = np.zeros(total_steps)
pluto_y_positions = np.zeros(total_steps)
neptune_x_positions = np.zeros(total_steps)
neptune_y_positions = np.zeros(total_steps)

pluto_theta = 0
neptune_theta = 0

lines_x = []
lines_y = []

for i in range(total_steps):
    pluto_theta_rad = np.deg2rad(pluto_theta)
    neptune_theta_rad = np.deg2rad(neptune_theta)

    pluto_r = (pluto_a * (1 - pluto_e ** 2)) / (1 + pluto_e * np.cos(pluto_theta_rad))
    neptune_r = (neptune_a * (1 - neptune_e ** 2)) / (1 + neptune_e * np.cos(neptune_theta_rad))

    pluto_x = pluto_r * np.cos(pluto_theta_rad)
    pluto_y = pluto_r * np.sin(pluto_theta_rad)
    neptune_x = neptune_r * np.cos(neptune_theta_rad)
    neptune_y = neptune_r * np.sin(neptune_theta_rad)

    pluto_x_positions[i] = pluto_x
    pluto_y_positions[i] = pluto_y
    neptune_x_positions[i] = neptune_x
    neptune_y_positions[i] = neptune_y

    lines_x.append([pluto_x, neptune_x])
    lines_y.append([pluto_y, neptune_y])

    pluto_theta += 360 * time_step / days_per_year
    neptune_theta += 360 * time_step / (days_per_year * (neptune_P / pluto_P))

plt.figure(figsize=(10, 6))
plt.plot(pluto_x_positions, pluto_y_positions, color='blue', label='Pluto')
plt.plot(neptune_x_positions, neptune_y_positions, color='red', label='Neptune')
for line_x, line_y in zip(lines_x, lines_y):
    plt.plot(line_x, line_y, color="black", linewidth=0.5, alpha=0.5)
plt.scatter([0], [0], color="orange", marker="o", label="Sun")
plt.xlabel("x position (AU)")
plt.ylabel("y position (AU)")
plt.title("Pluto-Neptune Spirograph")
plt.legend()
plt.grid(True)
plt.show()
