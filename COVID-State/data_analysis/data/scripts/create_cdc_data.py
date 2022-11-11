from datetime import datetime
import os
from urllib.request import urlretrieve

import requests
import pandas as pd

def delete_file(path):
    if os.path.exists(path):
        os.remove(path)

def download_data(dest_path='../'):
    temp_file = 'temp.csv'
    delete_file(temp_file)

    urlretrieve('https://data.cdc.gov/api/views/9mfq-cb36/rows.csv?accessType=DOWNLOAD', 'temp.csv')

    df = pd.read_csv(temp_file)
    df = df.rename(columns={'submission_date': 'Date', 'state': 'State'})
    
    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

    remove_states = set(['AS', 'RMI', 'NYC', 'GU', 'MP', 'FSM', 'PW'])
    df = df[~df['State'].isin(remove_states)]

    df = df.sort_values(by=['State', 'Date'])
    df = df.set_index('Date')

    date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    df.to_csv(os.path.join(dest_path, f"cdc_{date}.csv"))

    delete_file(temp_file)

if __name__ == "__main__":
    download_data(dest_path='../')
