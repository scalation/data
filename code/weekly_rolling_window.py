def weekly_rolling_window_df(df: pd.DataFrame, h: int = 4, model:str) -> pd.DataFrame:
      """
    A function used for displaying weekly predictions on a rolling window basis

    Arguments
    ----------
    df : pd.DataFrame
        the weekly forecasted data merged according to dates
    h : int
        the future horizons
    model : str
        the name of the model

    Returned Values
    ----------
    weekly : pd.DataFrame

    """

    df.set_index('date', inplace=True)
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
