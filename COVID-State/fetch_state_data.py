import os
import pandas as pd
from datetime import datetime
now = datetime.now()

def create_strings_from_numbers(limit):
    months = []
    for i in range(1, limit):
      month = ""
      if i < 10:
       month = "0"
       month = month + f"{i}"
       months.append(month)
      else:
          month = f"{i}"
          months.append(month)

    return months
years = [2020,2021,2022]
months = create_strings_from_numbers(13)
dates = create_strings_from_numbers(32)

for year in years:
        for month in months:
            if year == str(now.year) and int(month) > int(now.month):
                break
            if year == 2020 and int(month) < 4:
                continue
            for date in dates:
                print(f"downloading - {year}-{month}-{date}")
                url = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/{month}-{date}-{year}.csv"
                try:
                    a = pd.read_csv(url)
                    a.to_csv(f"C:/Users/subas/PycharmProjects/covid19/raw/csse-jhu/{year}-{month}-{date}.csv")
                except:
                    print(f"did not download on date - {year}-{month}-{date}")

file_names = os.listdir(f"C:/Users/subas/PycharmProjects/covid19/raw/csse-jhu/")
columns = ["Date","Province_State","Confirmed", "Deaths","Recovered","Active","People_Tested","People_Hospitalized", "Testing_Rate", "Hospitalization_Rate", "Incident_Rate","Lat", "Long_", "UID", "ISO3", "FIPS"]
cumulative_df = pd.DataFrame(columns=columns)

for file in file_names:
        df = pd.read_csv(f"C:/Users/subas/PycharmProjects/covid19/raw/csse-jhu/{file}", index_col = 0)
        df = df.drop(columns = ["Country_Region", "Last_Update"])
        df= df.fillna(0)
        df["Date"] = file.replace(".csv","")
        cumulative_df = cumulative_df.append([df])

dt_string = now.strftime("%Y-%m-%d-%H-%M-%S")

cumulative_df = cumulative_df.fillna(0)
cumulative_df = cumulative_df.set_index("Date")
cumulative_df.to_csv(f"{dt_string}-State.csv")

