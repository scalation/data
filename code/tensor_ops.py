import pandas as pd

"""
tensor_ops: 
    A module for handling tensors.

Functions
----------
make_3d_tensors: 
    def make_3d_tensors(df: pd.DataFrame, lags: int = 1, h: int = 1):  
"""
def make_3d_tensors(df: pd.DataFrame, lags: int = 1, h: int = 1) -> (np.ndarray, np.ndarray):  
    """
    Let the number of lags of your model be p and let the number for 
    forecasting horions be h.
    A function used for converting time × variables T-by-n matrix to
    two tensors: 
        x is a (T-p-h+1)-by-p-by-n tensor
        y is a (T-p-h+1)-by-h-by-n tensor.

    Arguments
    ----------
    data : pd.DataFrame
        the input data
    lags: int
        the past lagged values
    h: int
        the future horizons
        
    Returned Values
    ----------
    x: numpy.ndarray
    y: numpy.ndarray    
    """ 
    data = df.values
    x = np.zeros((data.shape[0] - lags - h + 1, lags, df.shape[1]))
    y = np.zeros((data.shape[0] - lags - h + 1, h, df.shape[1]))
    for t in range(0, data.shape[0] - lags - h + 1):
        past_lags = data[t:t + lags, :]
        future_h = data[t + lags:t + lags + h, :]
        x[t, :, :] = past_lags
        y[t, :, :] = future_h
    return x, y
