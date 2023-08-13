import math
import numpy as np

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

# Define the time values
time_values = np.linspace(t_i, t_f, N)

# Compute the integrand values using the theta_2_time_integrand function
integrand_values = theta_2_time_integrand(e_Pluto, theta_values)

# Compute the cumulative sum values using the simpson function
cumulative_sum_values = simpson(theta_2_time_integrand, theta_i, theta_f, N)

# Optional: If you want to convert the cumulative_sum_values to time units using the Pluto_time_constant
cumulative_sum_time_values = cumulative_sum_values * Pluto_time_constant
