
import numpy as np

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
    yhatList = yhat(eig_vec, variables, 3)
        
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