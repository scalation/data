import pandas as pd
from datetime import datetime

def fetch_US_weeklydata(filename: str):
    """
    This function fetches weekly data for the USA from the provided CSV file.

    Arguments
    ----------
    filename: str
        the name of the input CSV file containing the data to be processed

    """
    #Reads the data from the input CSV file
    owid_df = pd.read_csv(filename)
    #Filters the data to include only records for the USA
    df = owid_df[owid_df["iso_code"] == "USA"]
    df.reset_index()
    #Fills any missing values in the DataFrame with zeros
    df = df.fillna(0)
    #Converts the 'date' column to a datetime type and sets it as the DataFrame index
    df.loc[:, 'date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    #Resamples the data to weekly intervals starting from Saturdays, summing the values for each week
    df_weekly = df[[
     'new_cases',
     'new_deaths',
     'reproduction_rate',
     'icu_patients',
     'hosp_patients',
     'new_tests',
     'positive_rate',
     'tests_per_case',
     'people_vaccinated',
     'people_fully_vaccinated',
     'total_boosters',
     'new_vaccinations',
     'excess_mortality_cumulative_absolute',
     'excess_mortality_cumulative',
     'excess_mortality',
     'excess_mortality_cumulative_per_million']].resample('W-SAT', closed='right', offset=pd.Timedelta(days=-2)).sum()

    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d-%H-%M-%S")
    #Saves the processed weekly data for the USA in a new CSV file
    df_weekly.to_csv(f"{dt_string}-OWID_weekly.csv")
