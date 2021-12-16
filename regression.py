import wbdata
import datetime
import os
import numpy as np
import pandas as pd
import statsmodels.api as sm
import test_input

os.chdir('C:/Users/CKIRAC15')

test_input.test('gdp_per_capita.csv')

df=pd.read_csv('gdp_per_capita.csv')

def Regression(df,outcome_variable):
    df=df.dropna()
    y_dataframe = df[outcome_variable] # GDP per capita in my case
    X_dataframe = df.iloc[:, 3:] # my covariates are starting from column 4 so..
    y=y_dataframe.to_numpy()
    X=X_dataframe.to_numpy()
    k=np.shape(X)[1] # number of covariates
    n=np.shape(X)[0] #number of observations
    b = np.ones(X.shape[0]) # column of ones 
    X=np.c_[b,X]  # concatenate column of ones 
    X_transpose=X.transpose()      
    XIX=np.dot(X_transpose,X)   #matrix multiplication using numpy
    inverse_of_XIX=np.linalg.inv(XIX)    #inverse of matrix numpy
    XIy=np.matmul(X_transpose,y)  ##matrix multiplication using numpy
    B=np.matmul(inverse_of_XIX,XIy) # coefficients of linear regression
    predicted_y=np.matmul(X,B) #predictions
    errors=y-predicted_y     #errors
    error_trans=errors.transpose()   # transpose of errors
    eIe=np.matmul(errors,error_trans)/(n-k-1)    #sigma square of residuals
    varianceXIX=eIe*inverse_of_XIX   #variance - covariance matrix of coefficients
    diagonal=np.diag(varianceXIX)         # the diagonal has variances
    diagonal=diagonal**(1/2)              #square root the variances to get errors
    
    Covariates=['Constant']                           #Covariate column names 
    for count in range(len(X_dataframe.columns)):       #Covariate column names 
        Covariates.append(X_dataframe.columns[count]) #Covariate column names 
    Covariates=np.array(Covariates)
    mod = sm.OLS(y, X)   #checking the results with statsmodels module
    res = mod.fit()     #checking the results with statsmodels module
    interval=res.conf_int(0.05) #%95 intervals of the coefficients
    min_interval=[]
    for count in range(len(X_dataframe.columns)+1):
        min_interval.append(interval[count][0])
    max_interval=[]
    for count in range(len(X_dataframe.columns)+1):
        max_interval.append(interval[count][1])
    Results=pd.DataFrame()
    Results['Covariates'] = Covariates.tolist()
    Results['Coefficients'] = B.tolist()
    Results['StandardErrors'] = diagonal.tolist()
    Results['Interval_Min'] = min_interval  # from statsmodels
    Results['Interval_Max'] = max_interval  # from statsmodels
    #return Covariates,B,diagonal,interval
    return Results, res.summary() #1st output has my own results, 2nd has statsmodels results

Results, imported_module_results=Regression(df,'GDP_PER_CAPITA') #1st output has my own results, 2nd has statsmodels results
