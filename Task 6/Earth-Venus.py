import numpy as np
import matplotlib.pyplot as plt

earth_a = 1
earth_e = 0.02
venus_a = 0.723
venus_e = 0.01

earth_P = (earth_a ** 3) ** 0.5
venus_P = (venus_a ** 3) ** 0.5

years = 10*earth_P
days_per_year = 365
time_step = years*365/1234
total_steps = int(years * days_per_year / time_step)

earth_x_positions = np.zeros(total_steps)
earth_y_positions = np.zeros(total_steps)
venus_x_positions = np.zeros(total_steps)
venus_y_positions = np.zeros(total_steps)

earth_theta = 0
venus_theta = 0

lines_x = []
lines_y = []

for i in range(total_steps):
    earth_theta_rad = np.deg2rad(earth_theta)
    venus_theta_rad = np.deg2rad(venus_theta)

    earth_r = (earth_a * (1 - earth_e ** 2)) / (1 + earth_e * np.cos(earth_theta_rad))
    venus_r = (venus_a * (1 - venus_e ** 2)) / (1 + venus_e * np.cos(venus_theta_rad))

    earth_x = earth_r * np.cos(earth_theta_rad)
    earth_y = earth_r * np.sin(earth_theta_rad)
    venus_x = venus_r * np.cos(venus_theta_rad)
    venus_y = venus_r * np.sin(venus_theta_rad)

    earth_x_positions[i] = earth_x
    earth_y_positions[i] = earth_y
    venus_x_positions[i] = venus_x
    venus_y_positions[i] = venus_y

    lines_x.append([earth_x, venus_x])
    lines_y.append([earth_y, venus_y])

    earth_theta += 360 * time_step / days_per_year
    venus_theta += 360 * time_step / (days_per_year * (venus_P / earth_P))

plt.figure(figsize=(10, 6))
plt.plot(earth_x_positions, earth_y_positions, color='blue', label='Earth')
plt.plot(venus_x_positions, venus_y_positions, color='red', label='Venus')
for line_x, line_y in zip(lines_x, lines_y):
    plt.plot(line_x, line_y, color="black", linewidth=0.5, alpha=0.5)
plt.scatter([0], [0], color="orange", marker="o", label="Sun")
plt.xlabel("x position (AU)")
plt.ylabel("y position (AU)")
plt.title("Earth-Venus Spirograph")
plt.legend()
plt.grid(True)
plt.show()