import math
import numpy as np
import matplotlib.pyplot as plt


P_Pluto = 248.348
e_Pluto = 0.25
theta_i = 0
theta_f = 2 * math.pi
t_i = 0
t_f = P_Pluto
N = 1000

def time_constant(P, e):
    time_constant = (P * (1 - e ** 2) ** 1.5) / (2 * math.pi)
    return time_constant

def theta_2_time_integrand(e, theta):
    time_integrand = (1 - e * math.cos(theta)) ** (-2)
    return time_integrand

def simpson(integrand, a, b, n):
    # calculating step size
    h = (b - a) / n
    
    # Finding sum
    integral_sum = integrand(a) + integrand(b)
    
    for i in range(1, n):
        k = a + i * h
        
        if i % 2 == 0:
            integral_sum += 2 * integrand(k)
        else:
            integral_sum += 4 * integrand(k)
    
    # Finding final integration value
    integral_sum *= h / 3

    return integral_sum

# Compute the time constant for Pluto
Pluto_time_constant = time_constant(P_Pluto, e_Pluto)

# Define the theta values
theta_values = np.linspace(theta_i, theta_f, N)

# Compute the integrand values using the theta_2_time_integrand function
integrand_values = theta_2_time_integrand(e_Pluto, theta_values)

# Find the time values
time_values = integrand_values * Pluto_time_constant

# Create a plot
plt.figure(figsize=(10, 6))

# Plot time_values on the x-axis and theta_values on the y-axis
plt.plot(time_values, theta_values, label='Angles')

# Add labels and a legend
plt.xlabel('Time')
plt.ylabel('Orbit Polar Angle')
plt.title('Angles vs. Time')
plt.legend()

# Show the plot
plt.show()
