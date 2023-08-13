import math

Yr=365*24*60*60
P_Pluto_Yr=248.348
P_Pluto_Sec=248.348*Yr
e_Pluto=0.25
theta_i=0
#h=1/1000

def theta_2_time_constant(P,e):
    time_constant=(P*(1-e**2)**1.5)/(2*math.pi)
    return time_constant

def theta_2_time_integrand(e,theta):
    time_integrand=(1-e*math.cos(theta))**(-2)
    return time_integrand

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
