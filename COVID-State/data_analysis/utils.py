import numpy as np
import pandas as pd

def print_start_end_dates(cdc, jhu):
    def f(df, name):
        print(f"{name} start date = {min(df['Date'])}")
        print(f"{name} end date = {max(df['Date'])}")
        
    
    f(cdc, 'CDC')
    f(jhu, 'JHU')

def print_avg_rows_per_state(cdc, jhu):
    def f(df, name):
        avg = df.shape[0] / df['State'].nunique()
        print(f"{name} avg rows per state = {avg}")

    f(cdc, 'CDC')
    f(jhu, 'JHU')

def print_stats(cdc, jhu):
    print_start_end_dates(cdc, jhu)
    print()
    print_avg_rows_per_state(cdc, jhu)

def get_common_data(cdc, jhu):
    def f(df1, df2):
        unique_indexes = set(df2['Date'].values)
        new_df1 = df1[df1['Date'].isin(unique_indexes)]
        new_df1 = new_df1.sort_values(by=['State', 'Date'])
        new_df1 = new_df1.reset_index(drop=True)
        return new_df1

    new_cdc = f(cdc, jhu)
    new_jhu = f(jhu, cdc)
    return new_cdc, new_jhu

def get_rolling_average(df, col, window_size, state_col='State'):
    curr_state = ''
    rolling_sum = 0
    rolling_length = 0
    avg = []

    for i, row in df.iterrows():
        state = row[state_col]
        if state != curr_state:
            curr_state = state
            rolling_sum = row[col]
            
            if np.isnan(rolling_sum):
                curr_state = ''
            else:
                rolling_length = 1
            avg.append(None)
        else:
            if rolling_length <= window_size:
                rolling_sum += row[col]
                rolling_length += 1
                
                if rolling_length < window_size:
                    avg.append(None)
                else:
                    avg.append(rolling_sum / window_size)
            else:
                rolling_sum += row[col] - df[col][i-window_size]
                avg.append(rolling_sum / window_size)
    
    return avg

def get_state_dfs(cdc, jhu, cdc_state_col='State', jhu_state_col='State'):
    states = list(cdc[cdc_state_col].unique())
    dfs = []
    
    for state in states:
        cdc_state = cdc[cdc[cdc_state_col] == state]
        jhu_state = jhu[jhu[jhu_state_col] == state]
        dfs.append((state, cdc_state, jhu_state))
    
    return dfs

def get_diff_list(cdc, cdc_col, jhu, jhu_col, start_ind=0, cdc_date_col='Date'):
    diff = list(cdc[cdc_col] - jhu[jhu_col])
    diff = diff[start_ind:]

    dates = list(cdc[cdc_date_col])
    dates = dates[start_ind:]

    df = pd.DataFrame(list(zip(dates, diff)), columns=['Date', 'Diff'])
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
    return df
