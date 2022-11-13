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
    return df.groupby(state_col)[col].transform(lambda x: x.rolling(window_size, 1).mean())
