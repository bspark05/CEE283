# CEE283 Project Library

----------

## Description
This library is written in Python and intended to conduct a Principal Component Regression (PCR) analysis.

## Requirements
numpy, xlrd

## CEE283 library modules
* CEE283.excel - File I/O based on the Microsoft Excel
* CEE283.jacobi_eigenvalue - Jacobi eigenvalue algorithm
* CEE283.statistics - Statistics for PCR analysis

## Function List 
### CEE283.excel.excelRead
CEE283.excel.**excelRead**(*filepath, sheetname*)
  : Read an excel file (.xlsx) and convert the cell values in a 2D list.

Parameters: | |
------|------
**filepath**|*string*
 | The path of a excel file including the file format
**sheetname**|*string*
 | The name of the worksheet of the excel file
 | |
**Returns:** | |
**excelList**|*list* 
 | A 2D list including all the cell values in the excel file

### CEE283.excel.excelToArray
CEE283.excel.**excelToArray**(*filepath, sheetname*)
  : Convert an excel list to numpy array format
  
Parameters: | |
------|------
**filepath**|*string*
 | The path of a excel file including the file format
**sheetname**|*string*
 | The name of the worksheet of the excel file
 | |
**Returns:** | |
**excelArray**|*numpy.ndarray* 
 | A multidimensional (n x m) array (where, n is the number of variables, m is the number of observations
 
### CEE283.jacobi_eigenvalue.maxelem
CEE283.jacobi_eigenvalue.**maxelem**(*matrix*)
: The maximum value and indices of the off-diagonal element in 2D array matrix

Parameters: | |
------|------
**matrix**|*numpy.ndarray*
 | A covariance matrix or correlation matrix to calculate the eigenvalues and corresponding eigenvectors
 | |
**Returns:** | |
**amax**|*numpy.float64* 
 | The maximum value
**ith**|*int* 
 | The row index of the maximum element
**jth**|*int* 
 | The column index of the maximum element

### CEE283.jacobi_eigenvalue.rotate
CEE283.jacobi_eigenvalue.**rotate**(*matrix, trans, ith, jth*)
: Rotate input matrix a in place to make a[k,l] = 0, and update the transformation matrix

Parameters: | |
------|------
**matrix**|*numpy.ndarray*
 | A covariance matrix or correlation matrix to calculate the eigenvalues and corresponding eigenvectors
**trans**|*numpy.ndarray*
 | A tranformation matrix
**ith**|*int*
 | The row index of the maximum element
**jth**|*int* 
 | The column index of the maximum element

### CEE283.jacobi_eigenvalue.jacobi_eig
CEE283.jacobi_eigenvalue.**jacobi_eig**(*matrix, tol=1.0e-9*)
: Implementation of Jacobi Method

Parameters: | |
------|------
**matrix**|*numpy.ndarray*
 | A covariance matrix or correlation matrix to calculate the eigenvalues and corresponding eigenvectors
**tol**|*float*
 | tolerence to determine the Jacobi roation loop
**Returns:** | |
**eig_val_cov**|*list* 
 | The eigenvalue list of the covariance matrix or correlation matrix
**eig_vec_cov**|*list*
 | The eigenvector list of the eigenvalues

### CEE283.statistics.coefficient
CEE283.statistics.**coefficient**(*eigenvectors, nComp*)

Parameters: | |
------|------
**eigenvectors**|*numpy.ndarray*
 | A set of eigenvectors of the covariance (or correlation) matrix
**nComp**|*int*
 | The number of principal components considered
 | |
**Returns:** | |
**coeffList**|*list* 
 | A list of the coefficients of the regression model in using the given number of principal components

### CEE283.statistics.yhat
CEE283.statistics.**yhat**(*eigenvectors, observations, nComp*)

Parameters: | |
------|------
**eigenvectors**|*numpy.ndarray*
 | A set of eigenvectors of the covariance (or correlation) matrix
**observations**|*numpy.ndarray*
 | A set of observations from the excel file (Note: the last column is the dependent variable)
**nComp**|*int*
 | The number of principal components considered
 | |
**Returns:** | |
**yhatList**|*list* 
 | A list of estimated y(dependent variable) values based on the regression model

### CEE283.statistics.corrVarPrinc
CEE283.statistics.**corrVarPrinc**(*eigenvectors, observations, nComp*)

Parameters: | |
------|------
**eigenvectors**|*numpy.ndarray*
 | A set of eigenvectors of the covariance (or correlation) matrix
**observations**|*numpy.ndarray*
 | A set of observations from the excel file (Note: the last column is the dependent variable)
**nComp**|*int*
 | The number of principal components considered
 | |
**Returns:** | |
**corrVarPrinc**|*numpy.ndarray* 
 | An array of correlation values between each independent variable and the given number of principal components

### CEE283.statistics.rSquared
CEE283.statistics.**rSquared**(*eigenvectors, observations, nComp*)

Parameters: | |
------|------
**eigenvectors**|*numpy.ndarray*
 | A set of eigenvectors of the covariance (or correlation) matrix
**observations**|*numpy.ndarray*
 | A set of observations from the excel file (Note: the last column is the dependent variable)
**nComp**|*int*
 | The number of principal components considered
 | |
**Returns:** | |
**rSquared**|*numpy.float64* 
 | The R-squared value of the model
