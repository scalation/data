import sklearn.model_selection as sk
import numpy as np

"""
data_splitting: 
    A module for splitting data.

Functions
----------
train_test_split: 
    def train_test_split(x: np.ndarray, y: np.ndarray, test_ratio: float = 0.25) -> (np.ndarray, np.ndarray, np.ndarray, np.ndarray):
"""

def train_test_split(x: np.ndarray, y: np.ndarray, test_ratio: float = 0.25) -> (np.ndarray, np.ndarray, np.ndarray, np.ndarray):
    
    """ 
    A function used for splitting the data into fixed train and test sets.
    Usually, for time series, it is better to use a rolling window.
    For the train/test split, we use the default split ratio by scikit-learn 
    set to 0.25.

    Arguments
    ----------
    x : pd.DataFrame
        past lagged data
        
    y : pd.DataFrame
        future horizons
        
    test_ratio : int
        the fraction of data for testing purposes
        
    Returned Values
    ----------
    x_train : numpy.ndarray
    x_test : numpy.ndarray
    y_train : numpy.ndarray
    y_test : numpy.ndarray
    
    """ 
    x_train, x_test, y_train, y_test = sk.train_test_split(x, y, test_size = test_ratio, 
                                                           random_state = 42, shuffle = False)
    return x_train, x_test, y_train, y_test
