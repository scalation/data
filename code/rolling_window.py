import pandas as pd
"""
rolling_window: 
    A module for displaying daily and weekly predictions from a dataframe on a rolling window basis 

Functions
----------
daily_rolling_window: 
    def daily_rolling_window(model:str,df: pd.DataFrame, h: int = 14, date:str='date'):
    
weekly_rolling_window:
    def weekly_rolling_window(model:str,df: pd.DataFrame, h: int = 4, date:str='date'):
"""
def daily_rolling_window(model:str,df: pd.DataFrame, h: int = 14, date:str='date') -> pd.DataFrame:
    """
    A function used for displaying 14-days ahead predictions on a rolling window basis

    Arguments
    ----------
    df: pd.DataFrame
        the daily forecasted data merged according to the dates
    h: int
        the future horizons
    model: str
        the name of the model
    date: str
        the date column name in the dataframe

    Returned Values
    ----------
    daily: pd.DataFrame

    """
    df.set_index(date, inplace=True)
    start = 0
    end = h
    daily_pred = []
    window = 0
    for i in range(len(df.columns)-h):
        forecast_matrix_temp = df.iloc[start:end]
        date = forecast_matrix_temp.tail(1).index.item()
        l_row = forecast_matrix_temp.tail(1)
        daily_pred.append([date,l_row.iloc[0][window],l_row.iloc[0][window+1],l_row.iloc[0][window+2],l_row.iloc[0][window+3],
                           l_row.iloc[0][window+4],l_row.iloc[0][window+5],l_row.iloc[0][window+6],l_row.iloc[0][window+7],
                           l_row.iloc[0][window+8],l_row.iloc[0][window+9],l_row.iloc[0][window+10],l_row.iloc[0][window+11],
                           l_row.iloc[0][window+12],l_row.iloc[0][window+13]])
        window = window + 1
        start = end
        end = end+1
    daily_predictions = pd.DataFrame(daily_pred, columns=[ 'Date',str('day14_'+model),str('day13_'+model),str('day12_'+model),str('day11_'+model)
                                                            ,str('day10_'+model),str('day9_'+model),str('day8_'+model),str('day7_'+model)
                                                            ,str('day6_'+model),str('day5_'+model),str('day4_'+model),str('day3_'+model),
                                                             str('day2_'+model),str('day1_'+model)])
    daily_predictions['Date'] = pd.to_datetime(daily_predictions['Date'])
    daily = daily_predictions
    return daily

def weekly_rolling_window(model:str,df: pd.DataFrame, h: int = 4, date:str='date') -> pd.DataFrame:
    """
    A function used for displaying 4 weeks ahead predictions on a rolling window basis

    Arguments
    ----------
    df: pd.DataFrame
        the weekly forecasted data merged according to the dates
    h: int
        the future horizons
    model: str
        the name of the model

    Returned Values
    ----------
    weekly: pd.DataFrame

    """
    df.set_index(date, inplace=True)
    start = 0
    end = h
    weekly_pred = []
    window = 0
    for i in range(len(df.columns)-h):
        forecast_matrix_temp = df.iloc[start:end]
        date = forecast_matrix_temp.tail(1).index.item()
        l_row = forecast_matrix_temp.tail(1)
        weekly_pred.append([date,l_row.iloc[0][window],l_row.iloc[0][window+1],l_row.iloc[0][window+2],l_row.iloc[0][window+3]])
        window = window + 1
        start = end
        end = end+1
    weekly_predictions = pd.DataFrame(weekly_pred, columns=[ 'Date',str('week4_'+model),str('week3_'+model),
                                                                  str('week2_'+model),
                                                                  str('week1_'+model)])
    weekly_predictions['Date'] = pd.to_datetime(weekly_predictions['Date'])
    weekly = weekly_predictions
    return weekly
