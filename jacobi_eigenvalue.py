import numpy as np
def maxelem(matrix):
    #Return (amax, ith, jth), the value and indices of the off-diagonal element in 2D array matrix
    n = len(matrix)
    amax = 0.0
    for i in range(n-1):
        for j in range(i+1,n):
            if abs(matrix[i,j]) >= amax:
                amax = abs(matrix[i,j])
                ith = i
                jth = j
    return amax,ith,jth

def rotate(matrix, trans, ith, jth):
    #Rotate input matrix matrix in place to make matrix[ith,jth] = 0, and update the transformation matrix trans

    n = len(matrix)
    aDiff = matrix[jth,jth] - matrix[ith,ith]
    if abs(matrix[ith,jth]) < abs(aDiff)*1.0e-36:
        t = matrix[ith,jth]/aDiff
    else:
        phi = aDiff/(2.0*matrix[ith,jth])
        t = 1.0/(abs(phi) + np.sqrt(phi**2 + 1.0))
        if phi < 0.0:
            t = -t
    c = 1.0/np.sqrt(t**2 + 1.0); s = t*c
    tau = s/(1.0 + c)
    temp = matrix[ith,jth]
    matrix[ith,jth] = 0.0
    matrix[ith,ith] = matrix[ith,ith] - t*temp
    matrix[jth,jth] = matrix[jth,jth] + t*temp
    # Case of i < ith
    for i in range(ith):
        temp = matrix[i,ith]
        matrix[i,ith] = temp - s*(matrix[i,jth] + tau*temp)
        matrix[i,jth] = matrix[i,jth] + s*(temp - tau*matrix[i,jth])
    # Case of ith < i < jth
    for i in range(ith+1,jth):
        temp = matrix[ith,i]
        matrix[ith,i] = temp - s*(matrix[i,jth] + tau*matrix[ith,i])
        matrix[i,jth] = matrix[i,jth] + s*(temp - tau*matrix[i,jth])
    # Case of i > jth
    for i in range(jth+1,n):
        temp = matrix[ith,i]
        matrix[ith,i] = temp - s*(matrix[jth,i] + tau*temp)
        matrix[jth,i] = matrix[jth,i] + s*(temp - tau*matrix[jth,i])
    # Update transformation matrix
    for i in range(n):
        temp = trans[i,ith]
        trans[i,ith] = temp - s*(trans[i,jth] + tau*trans[i,ith])
        trans[i,jth] = trans[i,jth] + s*(temp - tau*trans[i,jth])
                             
                             
def jacobi_eig(matrix, tol=1.0e-9): # Jacobi method
    
    n = len(matrix)
    # Set limit on number of rotations
    nbrot_max = 5*(n**2)
    # Initialize transformation matrix
    trans = np.identity(n)*1.0
    # Jacobi rotation loop
    for i in range(nbrot_max):
        amax, ith, jth = maxelem(matrix)
        if amax < tol:
            [eig_val_cov, eig_vec_cov] = np.diagonal(matrix),trans
            idx = eig_val_cov.argsort()[::-1]
            eig_val_cov = eig_val_cov[idx]
            eig_vec_cov = eig_vec_cov[:,idx] 
            return [eig_val_cov, eig_vec_cov]
        rotate(matrix, trans, ith,jth)

    print "Jacobi method did not converge"
    
    
    
    
    