import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
from typing import Callable

def forecast_SARIMAX(window: int, n_train: int, p: int, d: int, q: int, ps: int, ds: int, qs: int, m: int, 
                     x: list[str], y: str, h_max: int, transf: Callable[[float], float], itransf: Callable[[float], float] )-> pd.DataFrame:
    
    """
    This function uses the SARIMAX model from statsmodels. It predicts 'y' by using 'x' as exogenous variables. 
    For each exogenous variable, the function takes 1 lag at a distance of 'h' time units.
    It forecasts 'h_max' time steps in future.

    Arguments
    ----------
    window : int
        window number
    n_train : int
        the size of training set
    p : int
        the value for auto regression order
    d : int
        the value for differencing 
    q : int
        the value for moving average order
    ps : int
        the value for seasonal auto regression order
    ds : int
        the value for seasonal differencing 
    qs : int
        the value for seasonal moving average order
    m : int
        the number of time steps for a single seasonal period
    x : list[str]
        the list of exogenous variables
    y : str
        the forecasted variable
    h_max : int
        the maximum number of forecasted horizons
    transf: Callable[[float], float]
        the definition for transformation
    itransf: Callable[[float], float]
        the definition for inverse transformation

    Returned Values
    ----------
    forecast_f : pd.DataFrame
      DataFrame containing the forecasted variable for 'h_max' horizons.

    """

    df_US = pd.read_csv('OWID_weekly.csv')
    df_US.index = pd.to_datetime(df_US['date'])
    date = df_US['date']
    date_list = date.tolist()
    df_US = df_US.drop(columns=['date'])
    
    #Apply transformation
    df_US_transf = pd.DataFrame()
    for col in df_US.columns:
        df_US_transf[col] = df_US[col].apply(lambda x: transf(x))


    #List of exogenous variables
    total_features = ['icu_patients', 'hosp_patients','positive_rate','new_cases','new_tests' , 'people_vaccinated', 'people_fully_vaccinated']

    df_y = df_US_transf[y]
    df_x = df_US_transf[total_features]
    value = np.empty(h_max)
    index = list()
    #Predicting weeks in future according to the horizon (h) 
    for h in range(1,h_max+1):

    #Shifting exogenous variables according to the horizon (h)   
        x_lagged_variables = df_x.shift(h).bfill()
        exog_variables = x_lagged_variables[x]

        # Its a moving window that starts from the window value till the train size plus the 'h' time steps in future
        df_window = df_y[int(window-1):int(window-1+n_train+h)]

        i = h-1

        #Defining train and test data
        col_train = df_y.loc[df_window.index][0:n_train]
        exo_train = exog_variables.loc[df_window.index][0:n_train]
        exo_test = exog_variables.loc[df_window.index][n_train:]

        #Model definition for prediction
        model = SARIMAX(col_train, exog=exo_train, order=(p,d,q), seasonal_order=(ps,ds,qs,m), enforce_stationarity=False, enforce_invertibility=False)
        model_fit = model.fit(disp=False)
        forecast = model_fit.predict(len(col_train), len(col_train)+i, exog=exo_test)

        #Inverse transformation
        forecast = itransf(forecast)
        forecast_f = forecast.to_frame()

        #For each horizon, the function selectively uses values that have a lag/shift equal to the specific horizon
        if h == 1:
            df1 = forecast_f.rename(columns= {0: y})
            value[i] = df1[y].iloc[i]
            index.append(date_list[n_train+window-1])            

        else:
            df2 = forecast_f.rename(columns= {'predicted_mean': y})
            value[i] = df2[y].iloc[i]
            index.append(date_list[n_train+window-2+h])
            
    data = {'index': index, y: value}
    forecast_f = pd.DataFrame(data)
    forecast_f['index'] = pd.to_datetime(forecast_f['index'])

    # Set the 'index' column as the DataFrame's index
    forecast_f.set_index('index', inplace=True)
    
    return forecast_f
