import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

"""
data_transforms: 
    A module for transforming data

Functions
----------
data_transform_std: 
    def data_transform_std(df: pd.DataFrame, test_ratio: float = 0.7):
    
data_transform_minmax
    def data_transform_minmax(df: pd.DataFrame, test_ratio: float = 0.7, min_: float = 0, max_: float = 1):
"""
def data_transform_std(df: pd.DataFrame, train_size: float):
    
    """
    A function used for data transformation to make sure it's 
    in the sensitive active region of the activation function
    by substracting the mean and dividing by the standard deviation

    Arguments
    ----------
    data : pd.DataFrame
        the input data
    test_ratio : int
        the fraction of data for testing purposes
        
    Returned Values
    ----------
    scaled_mean_std : dict

    """ 
    scaled_mean_std={}
    for i in range(0, len(df.columns)):
        if (i == 0):
            continue
        scaled = StandardScaler()
        scaled.fit(df.iloc[0:train_size, i].values.reshape(-1, 1))
        transformed = scaled.transform(df.iloc[:, i].values.reshape(-1, 1))
        scaled_mean_std['scaled' + df.columns[i]] = scaled
        df.iloc[:, i] = pd.DataFrame(transformed)
    return scaled_mean_std, df 

def data_transform_minmax(df: pd.DataFrame, train_size: float, min_: float = 0, max_: float = 1):
    
    """
    A function used for data transformation to make sure it's 
    in the sensitive active region of the activation function
    by rescaling the data to be between min_ and max_

    Arguments
    ----------
    data : pd.DataFrame
        the input data
    test_ratio : int
        the fraction of data for testing purposes
        
    Returned Values
    ----------
    scaled_mean_std : dict

    """ 
    scalers={}
    for i in range(0, len(df.columns)):
        if (i == 0):
            continue
        scaler = MinMaxScaler(feature_range=(min_, max_))
        scaler.fit(df.iloc[0:train_size, i].values.reshape(-1, 1))
        rescaled = scaler.transform(df.iloc[:, i].values.reshape(-1, 1))
        scalers['scaler_' + df.columns[i]] = scaler
        df.iloc[:, i] = pd.DataFrame(rescaled)
    return scalers, df 
