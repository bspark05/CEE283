
import excel as excel
import numpy as np
import jacobi_eigenvalue as eig
import statistics as stat

if __name__ == '__main__':
#     filename = "test.xlsx"
    filename = "variables11022016.xlsx"
      
    ## 1. Read excel file and convert to list to array
    variables = excel.excelToArray(filename, "variables11022016") #[variables][observations]
#     variables = excelToArray(filename, "Variables") 
    xArray = variables[:-1]
    yArray = variables[-1]
    
    ## 2. Computing the Covariance Matrix
    cov_mat = np.cov(xArray) #the last column is the dependent variable

    ## 2-1. Computing the Correlation Matrix
    corr_mat = np.corrcoef(xArray)
    
    ##3. Computing eigenvectors and corresponding eigenvalues
#     eig_val_cov, eig_vec_cov = np.linalg.eig(cov_mat)
    [eig_val_cov, eig_vec_cov] = eig.jacobi_eig(cov_mat,tol = 1.0e-9)
    
    print eig_val_cov
    print eig_vec_cov

    ##4. Correlation table
    corrTable = stat.corrVarPrinc(xArray, eig_vec_cov, 3)
#     print corrTable


    #5. Computing the Regression Coefficients
    #eig_vec_cov : eij where i = ith variable (i=1,2,...,p) / j = jth component (j=1,2,...,p)    
       
    coeffiList = stat.coefficient(eig_vec_cov, 3)
#     print coeffiList


    ##6. Computing R-squared value   
    #eig_vec_cov : eij where i = ith variable (i=1,2,...,p) / j = jth component (j=1,2,...,p)
    #variables : xij, where i = ith variable (i=1,2,...,p) / j = jth observation (j=1,2,...,n)
    rSqaured = stat.rSquared(eig_vec_cov, variables, 3)
#     print rSqaured
 