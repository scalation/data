from datetime import datetime
import os
from pathlib import Path
import shutil
import subprocess

import pandas as pd
from tqdm import tqdm

import sys
sys.path.append('../../')
from utils import get_rolling_average, get_common_data

cdc = pd.read_csv('../cdc_2022-11-18-05-12-04.csv')
jhu = pd.read_csv('../jhu_2022-11-18-05-14-54.csv')

cdc, jhu = get_common_data(cdc, jhu)

state = None
val = None
for i, row in jhu.iterrows():
    if state is None:
        state = row['State']
        cdc_row = cdc.loc[(cdc['Date'] == row['Date']) & (cdc['State'] == row['State'])]
        cdc_tot_deaths = cdc_row['tot_death'].item()
        val = cdc_tot_deaths
        jhu.loc[i, 'Deaths'] = cdc_tot_deaths
    else:
        if row['State'] == state:
            if row['Deaths'] < val:
                jhu.loc[i, 'Deaths'] = val
        else:
            state = row['State']
            cdc_row = cdc.loc[(cdc['Date'] == row['Date']) & (cdc['State'] == row['State'])]
            cdc_tot_deaths = cdc_row['tot_death'].item()
            val = cdc_tot_deaths
            jhu.loc[i, 'Deaths'] = cdc_tot_deaths

jhu['daily_deaths'] = jhu.groupby(['State'])['Deaths'].diff()
jhu = jhu.reset_index(drop=True)

jhu['rolling_deaths_3'] = get_rolling_average(jhu, 'daily_deaths', 3)
jhu['rolling_deaths_7'] = get_rolling_average(jhu, 'daily_deaths', 7)

jhu.to_csv(os.path.join('../', f"jhu_with_cdc.csv"), index=False)