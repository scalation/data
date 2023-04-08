## Introduction:  

This repository contains daily time series data of about three years from 1/03/2020 to 10/20/2022 about COVID-19 in the United States. All data is read from **Our World in Data** (https://covid.ourworldindata.org/data/owid-covid-data.csv). They switched from a daily to a weekly reporting schedule from 10/22/2022 (Sunday through Saturday), and so the data will be updated in a weekly format in this repository too. The meta-data for the data set is provided in the following:

## Meta-Data:  

### Confirmed cases
| Variable                         | Description                                                           |
|:---------------------------------|:----------------------------------------------------------------------|
| `total_cases`                    | Total confirmed cases of COVID-19                                     |
| `new_cases`                      | New confirmed cases of COVID-19                                       |
| `new_cases_smoothed`             | New confirmed cases of COVID-19 (7-day smoothed)                      |

### Confirmed deaths
| Variable                          | Description                                                             |
|:----------------------------------|:------------------------------------------------------------------------|
| `total_deaths`                    | Total deaths attributed to COVID-19                                     |
| `new_deaths`                      | New deaths attributed to COVID-19                                       |
| `new_deaths_smoothed`             | New deaths attributed to COVID-19 (7-day smoothed)                      |

### Hospital & ICU
| Variable                             | Description                                                                                                    |
|:-------------------------------------|:---------------------------------------------------------------------------------------------------------------|
| `icu_patients`                       | Number of COVID-19 patients in intensive care units (ICUs) on a given day                                      |
| `hosp_patients`                      | Number of COVID-19 patients in hospital on a given day                                                         |
| `weekly_hosp_admissions`             | Number of COVID-19 patients newly admitted to hospitals in a given week                                        |

### Reproduction rate
| Variable            | Description                                                                                                                                   |
|:--------------------|:----------------------------------------------------------------------------------------------------------------------------------------------|
| `reproduction_rate` | Real-time estimate of the effective reproduction rate (R) of COVID-19. See https://github.com/crondonm/TrackingR/tree/main/Estimates-Database |
### Tests & positivity
| Variable                          | Description                                                                                                                                                                                                                                                                                                          |
|:----------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `total_tests`                     | Total tests for COVID-19                                                                                                                                                                                                                                                                                             |
| `new_tests`                       | New tests for COVID-19 (only calculated for consecutive days)                                                                                                                                                                                                                                                        |
| `new_tests_smoothed`              | New tests for COVID-19 (7-day smoothed). For countries that don't report testing data on a daily basis, we assume that testing changed equally on a daily basis over any periods in which no data was reported. This produces a complete series of daily figures, which is then averaged over a rolling 7-day window |                                                                                                                                                                          
| `positive_rate`                   | The share of COVID-19 tests that are positive, given as a rolling 7-day average (this is the inverse of tests_per_case)                                                                                                                                                                                              |
| `tests_per_case`                  | Tests conducted per new confirmed case of COVID-19, given as a rolling 7-day average (this is the inverse of positive_rate)                                                                                                                                                                                          |

 ### Vaccinations
| Variable                                     | Description                                                                                                                                                                                                                                                                                                                                       |
|:---------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `total_vaccinations`                         | Total number of COVID-19 vaccination doses administered                                                                                                                                                                                                                                                                                           |
| `people_vaccinated`                          | Total number of people who received at least one vaccine dose                                                                                                                                                                                                                                                                                     |
| `people_fully_vaccinated`                    | Total number of people who received all doses prescribed by the vaccination protocol                                                                                                                                                                                                                                                              |
| `new_vaccinations`                           | New COVID-19 vaccination doses administered (only calculated for consecutive days)                                                                                                                                                                                                                                                                |
| `new_vaccinations_smoothed`                  | New COVID-19 vaccination doses administered (7-day smoothed). For countries that don't report vaccination data on a daily basis, we assume that vaccination changed equally on a daily basis over any periods in which no data was reported. This produces a complete series of daily figures, which is then averaged over a rolling 7-day window |
| `new_people_vaccinated_smoothed`             | Daily number of people receiving their first vaccine dose (7-day smoothed)                                                                                                                                                                                                                                                                        |
                                                                                                                                                                                                                                                                                                                                                                                                  
                                                                                                                                  
### Others
| Variable                         | Description                                                           |
|:---------------------------------|:----------------------------------------------------------------------|
| `date`                    | Date of observation                                    |
                     
