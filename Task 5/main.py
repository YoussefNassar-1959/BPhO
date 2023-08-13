import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt


t = np.linspace(0.1, 800, 10000)
P = 248.348
theta0 = 0
ecc_pluto = 0.25
ecc_0 = 0
dtheta = 1 / 1000

def calculate_theta_eccentric(t, P, theta0, ecc):
    N = np.ceil(t[-1] / P)
    theta = np.arange(theta0, (2 * np.pi * N + theta0) + dtheta, dtheta)
    f = (1 - ecc * np.cos(theta)) ** (-2)
    
    L = len(theta)
    isodd = np.where(np.arange(1, L-1) % 2 == 1, 4, 2)
    c = np.concatenate(([1], isodd, [1]))
    
    tt = P * (1 - ecc ** 2) ** (3 / 2) * (1 / (2 * np.pi)) * dtheta * (1 / 3) * np.cumsum(c * f)
    
    theta_interp = interp1d(tt, theta, kind='cubic')
    return theta_interp
    
def calculate_theta_circular(t, P, theta0, ecc):
    N = np.ceil(t[-1] / P)
    theta = np.arange(theta0, (2 * np.pi * N + theta0) + dtheta, dtheta)
    f = (1 - ecc * np.cos(theta)) ** (-2)
    
    L = len(theta)
    isodd = np.where(np.arange(1, L-1) % 2 == 1, 4, 2)
    c = np.concatenate(([1], isodd, [1]))
    
    tt = P * (1 - ecc ** 2) ** (3 / 2) * (1 / (2 * np.pi)) * dtheta * (1 / 3) * np.cumsum(c * f)
    
    theta_interp = interp1d(tt, theta, kind='cubic')
    return theta_interp
    
theta1 = calculate_theta_eccentric(t, P, theta0, ecc_pluto)
theta2 = calculate_theta_circular(t, P, theta0, ecc_0)
eccentric_theta = theta1(t)
circular_theta= theta2(t)

plt.figure(figsize=(10, 6))
plt.plot(t, eccentric_theta, label='Eccentric')
plt.plot(t, circular_theta, label='Circular')
plt.xlabel('Year')
plt.ylabel('Rad')
plt.title('Angle vs. Time')
plt.legend()
plt.grid(True)
plt.show()
