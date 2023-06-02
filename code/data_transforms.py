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
def data_transform_std(df: pd.DataFrame, test_ratio: float = 0.7):
    
    """
    A function used for data transformation to make sure it's 
    in the sensitive active region of the activation function
    by substracting the mean and dividing by the standard deviation
    
    Required Imports
    ----------
    import pandas as pd

    Arguments
    ----------
    data : pd.DataFrame
        the input data
    test_ratio : int
        the fraction of data for testing purposes
        
    Returned Values
    ----------
    scalers : dict

    """ 
    scalers={}
    for i in range(0, len(df.columns)):
        scaler = StandardScaler()
        scaler.fit(df.iloc[0:round(test_ratio*df.shape[0]), i].values.reshape(-1, 1))
        rescaled = scaler.transform(df.iloc[:, i].values.reshape(-1, 1))
        scalers['scaler_' + df.columns[i]] = scaler
        df.iloc[:, i] = pd.DataFrame(rescaled)
    return scalers, df 

def data_transform_minmax(df: pd.DataFrame, test_ratio: float = 0.7, min_: float = 0, max_: float = 1):
    
    """
    A function used for data transformation to make sure it's 
    in the sensitive active region of the activation function
    by rescaling the data to be between min_ and max_
    
    Required Imports
    ----------
    import pandas as pd

    Arguments
    ----------
    data : pd.DataFrame
        the input data
    test_ratio : int
        the fraction of data for testing purposes
        
    Returned Values
    ----------
    scalers : dict

    """ 
    scalers={}
    for i in range(0, len(df.columns)):
        if (i == 0):
            continue
        scaler = MinMaxScaler(feature_range=(min_, max_))
        scaler.fit(df.iloc[0:round(test_ratio*df.shape[0]), i].values.reshape(-1, 1))
        rescaled = scaler.transform(df.iloc[:, i].values.reshape(-1, 1))
        scalers['scaler_' + df.columns[i]] = scaler
        df.iloc[:, i] = pd.DataFrame(rescaled)
    return scalers, df 
