import pandas as pd
from datetime import datetime
owid_df = pd.read_csv("owid-covid-data.csv")
us_df = owid_df[owid_df["iso_code"] == "USA"]
us_df.reset_index()

# fetch data till today
# now = datetime.now()
# dt_string = now.strftime("%Y-%m-%d-%H-%M-%S")
# us_df = us_df.fillna(0)
# us_df.to_csv(f"{dt_string}-OWID.csv")

# filter data till a given date
us_df.loc[:, 'date'] = pd.to_datetime(us_df['date']) 
date_cutoff = pd.to_datetime('2022-10-20')
dt_string = date_cutoff.strftime("%Y-%m-%d")
df_till_cutoff = us_df.loc[us_df['date'] <= date_cutoff]
df_till_cutoff = df_till_cutoff.fillna(0)
df_till_cutoff.to_csv(f"OWID_daily_till_{dt_string}.csv")
