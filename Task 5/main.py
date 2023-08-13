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
