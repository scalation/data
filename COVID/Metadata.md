## Introduction:  

This repository contains daily time series data about COVID-19 in the United States. All data is read in from the daily case report, collected and maintained by **The COVID Tracking Project**. The meta-data for the data set is provided in the following.  

## Meta-Data:  

 

| Column                       | Description                                                                                        |
|------------------------------|----------------------------------------------------------------------------------------------------|
| date                         | The current date starting with 1/13/2020 to 2/6/2021                                              |
| death                        | The cumulative number of deaths                                                                    |
| deathIncrease                | The number of new deaths on the given date                                                         |
| inIcuCumulative              | The cumulative number of patients in ICU                                                           |
| inIcuCurrently               | The number of net total patients in ICU on the given date                                          |
| hospitalizedIncrease         | The number of new hospitalizations on the given date                                               |
| hospitalizedIncrease_alt*    | The number of new hospitalizations on the given date between 0.005 and 0.995 percentiles           |
| hospitalizedCurrently        | The number of net total hospitalizations on the given date                                         |
| hospitalizedCumulative       | The cumulative number of hospitalizations                                                          |
| negative                     | The cumulative number of negative test results                                                     |
| negativeIncrease             | The number of new negative test results on the given date                                          |
| onVentilatorCumulative       | The cumulative number of patients on ventilator                                                    |
| onVentilatorCurrently        | The number of net total patients on ventilator on the given date                                   |
| positive                     | The cumulative number of positive test results                                                     |
| positiveIncrease             | The number of new positive test results on the given date                                          |
| states                       | The number of states reporting COVID-19 cases on the given date                                    |
| totalTestResults             | The cumulative number of total test results                                                        |
| totalTestResultsIncrease     | The number of total test results on the given date                                                 |
<!---| recovered                    | The cumulative number of recovered cases                                                           |-->

<!---\*The values on dates 5/26/2020, 6/4/2020, 10/6/2020 and 10/23/2020 were imputed by the average values of before and after the dates.  -->

## CLEANED_30.csv
Data is preprocessed for smoothing the outliers that lie 3 standard deviations away from the rolling mean. 
The rolling mean is the 6 time points local average such that we consider 3 time-points before and after the current point.
Observations within 3 standard deviations are left unchanged while the observations which are considered as outliers are replaced by the Kalman Smoothing using a Local Level Model.

## CLEANED_35.csv
Similar to the above cleaned data, expect 3.5 standar deviations is used as a threshold instead of 3 standard deviations.

## Eliminating early samples
We eliminate the first 44 day records and feed our models time-series data starting February 26, 2020 when the first deaths due to COVID-19 in the United States were recorded.
After eliminating the first 44 days, the new size of the time-series is 347 days.

<!---## CLEANED_USCOVID_KF
Four values of deathIncrease, 24 values of hospitalizedIncrease, 0 values of hospitalizedCurrently, 19 values of negativeIncrease, 6 values of positiveIncrease, and 0 values of recovered are treated as missing values. The missing values are replaced by using Kalman smoothing. -->

<!---## USCOVID_BY_STATE
The COVID-19 dataset expands upon USCOVID.CSV by splitting the data from the first one into counts for each state.-->

## USNPI
This dataset provides the U.S. Covid-19 Government Response Tracker.  
Most indicators are recorded on an ordinal scale that represents the level of strictness of the policy. Four of the indicators (E3, E4, H4 and H5) are recorded as a US dollar value of fiscal spending.  
This [cookbook](https://github.com/OxCGRT/covid-policy-tracker/blob/master/documentation/codebook.md) provides more information about each column.
