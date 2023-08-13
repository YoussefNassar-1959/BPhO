import numpy as np
from scipy.interpolate import interp1d
t = np.linspace(0, 800, 10000)  # Replace with your actual time values
P = 248.348
theta0 = 0
ecc = 0.25
dtheta = 1 / 1000

def calculate_theta_interp(t, P, theta0, ecc):
    N = np.ceil(t[-1] / P)
    theta = np.arange(theta0, (2 * np.pi * N + theta0) + dtheta, dtheta)
    f = (1 - ecc * np.cos(theta)) ** (-2)
    
    L = len(theta)
    isodd = np.where(np.arange(1, L-1) % 2 == 1, 4, 2)
    c = np.concatenate(([1], isodd, [1]))
    
    tt = P * (1 - ecc ** 2) ** (3 / 2) * (1 / (2 * np.pi)) * dtheta * (1 / 3) * np.cumsum(c * f)
    
    theta_interp = interp1d(tt, theta, kind='spline')
    return theta_interp

# Calculate theta_interp using the function
theta_interp = calculate_theta_interp(t, P, theta0, ecc)

# Interpolate theta values at specific times 't'
interpolated_theta = theta_interp(t)

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(t, interpolated_theta, label='Interpolated Theta')
plt.xlabel('Time')
plt.ylabel('Interpolated Theta')
plt.title('Interpolated Theta vs. Time')
plt.legend()
plt.grid(True)
plt.show()
