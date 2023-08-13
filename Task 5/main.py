import math
import numpy as np

P_Pluto=248.348
e_Pluto=0.25
theta_i=0
theta_f=2*math.pi
t_i=0
t_f=P_Pluto
N=1000
Pluto_time_constant=theta_constant(P_Pluto,e_Pluto)
theta_values = np.linspace(theta_i, theta_f, N)
time_values = np.linespace(t_i,t_f,N)
integrand_values = integrand(theta_values)
cumulative_sum_values = simpson(integrand, theta_i, theta_f, N)

def time_constant(P,e):
    time_constant=(P*(1-e**2)**1.5)/(2*math.pi)
    return time_constant

def theta_2_time_integrand(e,theta):
    time_integrand=(1-e*math.cos(theta))**(-2)
    return time_integrand

# def time_2_theta(constant,P,e,t):
#    theta=-constant(P,e)/(4*y)+0.5
#    return theta

def simpson(integrand,a,b,n):
    # calculating step size
    h = (b - a) / n
    
    # Finding sum 
    int = integrand(a) + integrand(b)
    
    for i in range(1,n):
        k = a + i*h
        
        if i%2 == 0:
            int += 2 * integrand(k)
        else:
            int += 4 * integrand(k)
    
    # Finding final integration value
    int = int * h/3

    return int
