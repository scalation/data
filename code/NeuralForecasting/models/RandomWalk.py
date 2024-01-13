import numpy as np
from typing import List, Union
from data.data_loading import load_data, plot_train_test
from data.data_transforms import data_transform_std
from data.data_splitting import train_test_split
from utils.metrics import mse, mae, smape
from utils.getmetrics import getmetrics

def RandomWalk(file_name: str, training_ratio: float, horizon: int, main_output: str, normalization: bool) -> (int, float, float, float):
    """
    A function used for producing forecasts based on the Random Walk model that simply projects a current value into the future (yhat[t] = y[t-h]).
    
    Arguments
    ----------
    file_name: str
        the file path for csv data file.
    training_ratio: float
        the training ratio used for splitting the dataset into train and test
    horizon: int
        how many time steps ahead to make the forecasts
    main_output: str
        the main output column/feature, e.g. '% WEIGHTED ILI'
    normalization: bool
        specifies whether the data is normalized or original
        
    Returned Values
    ----------
    mse: float
    mae: float
    smape: float

    """
    
    data = load_data(file_name, main_output = main_output)
    train_size = int(training_ratio*len(data))
    if normalization:
        scaled_mean_std, data = data_transform_std(data, train_size)

    train_data, val_data, test_data = train_test_split(data)    # No validation data for Random Walk.   
    train_data_MO = train_data[[main_output]]                   # Train set for main output column.
    test_data_MO = test_data[[main_output]]                     # Test set for main output column.
    actual = data[[main_output]]                                # Actual complete dataset for main output.
    forecasts = []
    for i in range(len(test_data_MO) - horizon):
        forecasts.append(actual.iloc[train_size + i - 1,:])     # For Random Walk, start with the last value from the training set.

    actual = actual[train_size + horizon:]                      # Aligning actual with forecasts so both have the same length.
    actual = np.array(actual)                                   # Convert actual a numpy array

    plot_train_test(data, main_output, train_size, train_data_MO, test_data_MO, forecasts)
    mse, mae, smape = getmetrics(actual, forecasts)
    
    return len(actual), mse, mae, smape
