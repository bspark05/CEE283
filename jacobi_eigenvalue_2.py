import numpy as np
def maxelem(a):

    n = len(a)
    amax = 0.0
    for i in range(n-1):
        for j in range(i+1,n):
            if abs(a[i,j]) >= amax:
                amax = abs(a[i,j])
                k = i
                l = j
    return amax,k,l

def rotate(a, p, k, l):

    n = len(a)
    aDiff = a[l,l] - a[k,k]
    if abs(a[k,l]) < abs(aDiff)*1.0e-36:
        t = a[k,l]/aDiff
    else:
        phi = aDiff/(2.0*a[k,l])
        t = 1.0/(abs(phi) + np.sqrt(phi**2 + 1.0))
        if phi < 0.0:
            t = -t
    c = 1.0/np.sqrt(t**2 + 1.0); s = t*c
    tau = s/(1.0 + c)
    temp = a[k,l]
    a[k,l] = 0.0
    a[k,k] = a[k,k] - t*temp
    a[l,l] = a[l,l] + t*temp
    # Case of i < k
    for i in range(k):
        temp = a[i,k]
        a[i,k] = temp - s*(a[i,l] + tau*temp)
        a[i,l] = a[i,l] + s*(temp - tau*a[i,l])
    # Case of k < i < l
    for i in range(k+1,l):
        temp = a[k,i]
        a[k,i] = temp - s*(a[i,l] + tau*a[k,i])
        a[i,l] = a[i,l] + s*(temp - tau*a[i,l])
    # Case of i > l
    for i in range(l+1,n):
        temp = a[k,i]
        a[k,i] = temp - s*(a[l,i] + tau*temp)
        a[l,i] = a[l,i] + s*(temp - tau*a[l,i])
    # Update transformation matrix
    for i in range(n):
        temp = p[i,k]
        p[i,k] = temp - s*(p[i,l] + tau*p[i,k])
        p[i,l] = p[i,l] + s*(temp - tau*p[i,l])
                             
                             
def jacobi_eig(a, tol=1.0e-9): # Jacobi method

    n = len(a)
    # Set limit on number of rotations
    nbrot_max = 5*(n**2)
    # Initialize transformation matrix
    p = np.identity(n)*1.0
    # Jacobi rotation loop
    for i in range(nbrot_max):
        amax, k, l = maxelem(a)
        if amax < tol:
            return np.diagonal(a),p
        rotate(a, p, k,l)

    print "Jacobi method did not converge"
    
    
    
    
    