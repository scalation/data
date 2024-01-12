def getmetrics(main_output: str, actual: np.array, forecasts: np.array) -> (float, float, float):
    """
    A function used for returning the MSE, MAE, sMAPE metrics.

    Arguments
    ----------
    main_output: str
        the name of the main output feature for evaluation
    actual: np.array
        the observed test set values aligned with the forecasts
    forecasts: np.array | List[floats]
        the output from a forecasting model, i.e. RandomWalk
           
    Returned Values
    ----------
    mse: float
    mae: float
    smape: float

    """
    return ('%.3f' %mse(actual, forecasts)), ('%.3f' %mae(actual, forecasts)), ('%.3f' %smape(actual, forecasts))
