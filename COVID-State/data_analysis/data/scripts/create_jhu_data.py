from datetime import datetime
import os
from pathlib import Path
import shutil
import subprocess

import pandas as pd
from tqdm import tqdm

def git(*args):
    return subprocess.check_call(['git'] + list(args))

def delete_folder(path):
    path = Path(path)
    if path.exists() and path.is_dir():
        shutil.rmtree(path)

def generate_csv_file(src="./temp", dest="../"):
    src = os.path.join(src, 'csse_covid_19_data/csse_covid_19_daily_reports_us')

    csv_files = os.listdir(src)
    columns = ["Date","Province_State","Confirmed", "Deaths","Recovered","Active","People_Tested","People_Hospitalized", "Testing_Rate", "Hospitalization_Rate", "Incident_Rate","Lat", "Long_", "UID", "ISO3", "FIPS"]

    dfs = []

    for f in tqdm(csv_files, total=len(csv_files)):
        if f == "README.md":
            continue

        df = pd.read_csv(os.path.join(src, f))
        df = df.drop(columns = ["Country_Region", "Last_Update"])
        df= df.fillna(0)
        df["Date"] = f.replace(".csv","")
        dfs.append(df)

    final_df = pd.concat(dfs)

    final_df['Date'] = pd.to_datetime(final_df['Date'], format='%m-%d-%Y')

    remove_states = set(['American Samoa', 'Diamond Princess', 'Grand Princess', 'Guam', 'Northern Mariana Islands', 'Recovered'])
    final_df = final_df[~final_df['Province_State'].isin(remove_states)]

    state_csv = pd.read_csv('./state_short_names.csv')
    final_df = pd.merge(final_df, state_csv, how='inner', left_on='Province_State', right_on='State')
    final_df = final_df.drop(columns=['Province_State', 'State'])
    final_df = final_df.rename(columns={'Code': 'State'})

    columns = list(final_df.columns.values)
    columns.insert(0, 'State')
    columns.pop()
    final_df = final_df[columns]
    
    final_df = final_df.sort_values(by=['State', 'Date'])
    final_df = final_df.set_index('Date')

    date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    final_df.to_csv(os.path.join(dest, f"jhu_{date}.csv"))

def download_data(temp_path='./temp', dest_path='../'):
    delete_folder(temp_path)
    os.makedirs(temp_path)

    git("clone", "https://github.com/CSSEGISandData/COVID-19.git", "--branch", "master", "--single-branch", "--depth", "1", temp_path)

    generate_csv_file(temp_path, dest_path)

    delete_folder(temp_path)

if __name__ == "__main__":
    download_data(temp_path='./temp', dest_path='../')
