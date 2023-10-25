import numpy as np
import pandas as pd

"""
metrics: 
    A module for evaulating the quality/goodness of fit
    Supports both symmetric and asymmetric metrics

Functions
----------
smape: 
    def smape(y: np.ndarray, y_pred: np.ndarray) -> float:
    
mae:
    def mae(y: np.ndarray, y_pred: np.ndarray) -> float:

sst:
    def sst(y: np.ndarray) - > float:

sse:
    def sse(y: np.ndarray, y_pred: np.ndarray) -> float:
    
r2:
    def r2(y: np.ndarray, y_pred: np.ndarray) -> float:

mse:
    def mse(y: np.ndarray, y_pred: np.ndarray) -> float:

rmse:
    def rmse(y: np.ndarray, y_pred: np.ndarray) -> float:

rae:
    def rae(y: np.ndarray, y_pred: np.ndarray) -> float:
"""

def smape(y: np.ndarray, y_pred: np.ndarray) -> float:
    """ 
    A function to calculate the symmetric mean absolute percentage error (sMAPE).

    Arguments
    ----------
    y: np.ndarray
        the response data
    y_pred: np.ndarray
        the predicted/forecasted outputs
        
    Returned Values
    ----------
    sMAPE : float

    """   
    return 200 * np.sum(np.abs(y-y_pred) / (np.abs(y) + np.abs(y_pred))) / len(y)

def mae(y: np.ndarray, y_pred: np.ndarray) -> float:
    """ 
    A function to calculate the mean absolute error (MAE).

    Arguments
    ----------
    y: np.ndarray
        the response data
    y_pred: np.ndarray
        the predicted/forecasted outputs
        
    Returned Values
    ----------
    MAE : float

    """   
    return np.sum(np.abs(y-y_pred))/len(y)

def sst(y: np.ndarray) -> float:
    """ 
    A function to calculate the sum of squares total (SST).

    Arguments
    ----------
    y: np.ndarray
        the response data
        
    Returned Values
    ----------
    SST : float
    """ 
    return np.sum((y-np.mean(y))**2)

def sse(y: np.ndarray, y_pred: np.ndarray) -> float:
    """ 
    A function to calculate the sum of squared errors (SSE).

    Arguments
    ----------
    y: np.ndarray
        the response data
    y_pred: np.ndarray
        the predicted/forecasted outputs
        
    Returned Values
    ----------
    SSE : float

    """   
    return np.sum((y-y_pred)**2)

def r2(y: np.ndarray, y_pred: np.ndarray) -> float:
    """ 
    A function to calculate R squared (r2).

    Arguments
    ----------
    y: np.ndarray
        the response data
    y_pred: np.ndarray
        the predicted/forecasted outputs
        
    Returned Values
    ----------
    r2 : float

    """   
    return 1-sse(y, y_pred)/sst(y)

def mse(y: np.ndarray, y_pred: np.ndarray) -> float:
    """ 
    A function to calculate mean squared error (MSE).

    Arguments
    ----------
    y: np.ndarray
        the response data
    y_pred: np.ndarray
        the predicted/forecasted outputs
        
    Returned Values
    ----------
    MSE : float

    """   
    return sse(y, y_pred)/len(y)

def rmse(y: np.ndarray, y_pred: np.ndarray) -> float:
    """ 
    A function to calculate root mean squared error (RMSE).

    Arguments
    ----------
    y: np.ndarray
        the response data
    y_pred: np.ndarray
        the predicted/forecasted outputs
        
    Returned Values
    ----------
    RMSE : float

    """   
    return np.sqrt(mse((y, y_pred)))

def rae(y: np.ndarray, y_pred: np.ndarray) -> float:
    """ 
    A function to calculate relative absolute error (RAE).

    Arguments
    ----------
    y: np.ndarray
        the response data
    y_pred: np.ndarray
        the predicted/forecasted outputs
        
    Returned Values
    ----------
    RAE : float

    """  
    y_mean = np.mean(y)
    squared_error_num = np.sum(np.abs(y - y_pred))
    squared_error_den = np.sum(np.abs(y - y_mean))
    rae_loss = squared_error_num / squared_error_den
    
    return rae_loss
