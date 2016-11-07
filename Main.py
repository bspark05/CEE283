'''
Created on Oct 8, 2016

@author: Administrator
'''
import FileIO.Excel as excel
import numpy as np
import jacobi_eigenvalue_2 as eig2

def excelToArray(filename, sheetname):
    varExcel = excel.excelRead(filename, sheetname)
    varList = []
    # first row is a field name
    for row in varExcel[1:]:
        rowList = []
        for value in row:
            rowList.append(float(value.value))
        varList.append(rowList)
    varArray = np.array(varList)
    # transpose the array
    varArrayTras = np.transpose(varArray)
    return varArrayTras
    

def coefficient(eigenvectors, nComp):
    #eigenvectors : eij where i = ith variable (i=1,2,...,p) / j = jth component (j=1,2,...,p)

    coeffList = []
    for comp in eigenvectors: # the first n components
        coeffList.append(np.sum(comp[:nComp]))
    return coeffList


def yhat(eigenvectors, observations, nComp):
    coeffiList = coefficient(eigenvectors, nComp)
    #observations : xij, where i = ith variable (i=1,2,...,p) / j = jth observation (j=1,2,...,n)
    #obser_T : xji
    obser_T = np.transpose(observations)
    
    yhatList = []
    for obser in obser_T:
        yhat = np.sum(obser[:-1]*coeffiList)
        yhatList.append(yhat)
    return yhatList


def corrVarPrinc(xArray, eig_vec, nComp):
    xArray_T = np.transpose(xArray)
    eig_vec_T = np.transpose(eig_vec)
    
    newXArray_T = []
    for obs in xArray_T:        
        indComp = 0
        princValue = []
        newObs=[]
        while indComp < nComp:
            princValue = np.append(princValue, sum(obs*eig_vec_T[indComp]))
            indComp +=1
            
        newObs = np.append(obs, princValue)
        newObsList = newObs.tolist()
        newXArray_T.append(newObsList)
    
    newXArray_T = np.asarray(newXArray_T)
    newXArray = np.transpose(newXArray_T)
    
    corr = np.corrcoef(newXArray)
    
    corrVarPrinc = corr[:-nComp, -nComp:]
    return corrVarPrinc
          
def rSquared(eig_vec, variables, nComp):
    yhatList = yhat(eig_vec_cov, variables, 3)
        
    rsArray_T = np.asarray([variables[-1], yhatList])
    ybar = np.mean(rsArray_T[0])
          
    SST = 0
    for y_i in rsArray_T[0]:
        SST += (y_i-ybar)**2
          
    SSRes = 0
    for y in rsArray_T:
        SSRes += (y[0]-y[1])**2
          
    rSquared = 1- SSRes/SST
    return rSquared


if __name__ == '__main__':
#     filename = "test.xlsx"
    filename = "variables11022016.xlsx"
      
    ## 1. Read Excel file and convert to list to array
    variables = excelToArray(filename, "variables11022016") #[variables][observations]
#     variables = excelToArray(filename, "Variables") 
    xArray = variables[:-1]
    yArray = variables[-1]
    
    ## 2. Computing the Covariance Matrix
    cov_mat = np.cov(xArray) #the last column is the dependent variable

    ## 2-1. Computing the Correlation Matrix
    corr_mat = np.corrcoef(xArray)
    
    ##3. Computing eigenvectors and corresponding eigenvalues
#     eig_val_cov, eig_vec_cov = np.linalg.eig(cov_mat)
    eig_val_cov, eig_vec_cov = eig2.jacobi_eig(cov_mat,tol = 1.0e-9)
    idx = eig_val_cov.argsort()[::-1]
    eig_val_cov = eig_val_cov[idx]
    eig_vec_cov = eig_vec_cov[:,idx]
    print eig_val_cov
    print eig_vec_cov

    ##4. Correlation table
    corrTable = corrVarPrinc(xArray, eig_vec_cov, 3)
    print corrTable


    #5. Computing the Regression Coefficients
    #eig_vec_cov : eij where i = ith variable (i=1,2,...,p) / j = jth component (j=1,2,...,p)    
       
    coeffiList = coefficient(eig_vec_cov, 3)
    print coeffiList


    ##6. Computing R-squared value   
    #eig_vec_cov : eij where i = ith variable (i=1,2,...,p) / j = jth component (j=1,2,...,p)
    #variables : xij, where i = ith variable (i=1,2,...,p) / j = jth observation (j=1,2,...,n)
    rSqaured = rSquared(eig_vec_cov, variables, 3)
    print rSqaured
 