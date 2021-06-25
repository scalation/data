
#install.packages("TSA")  #Unccomment and run this for the first time R is setup on your machine
library(forecast)
#library(TSA)
library(zoo)
library(Metrics)
library(stats)

zero_reference = 18317 #Difference between 1970-01-01 to 2020-02-25

ts_size = 376  # Number of Sample/Timesteps in entire time series 
tr_size = 222  # Number of Samples/Timesteps in Training set 236
te_size = 154  # Number of Samples/Timesteps in Training set 140
horizons = 14  # Number of days to forecast ahead in the future
kt = 1         # Retraining Frequency (No. of Samples)
rt = 0         # Total Number of Retrainings Occured
p = 4          # Non-seasonal Auto-Regressive Order
d = 1          # Non-seasonal Differencing/
q = 4          # Non-seasonal Moving Average Order
PP = 3         # Seasonal Auto-Regressive Order
DD = 1         # Seasonal Differencing
QQ = 1         # Seasonal Moving Average Order
s = 7          # Seasonal Period 

# Pull in the dataset from given URL
covid_data <- read.csv(file = "https://raw.githubusercontent.com/scalation/data/master/COVID/CLEANED_35_Updated.csv")

#Convert reponse column into "zoo" object
response_variable = covid_data$deathIncrease
response_variable = ifelse(covid_data$deathIncrease ==0, 1, covid_data$deathIncrease)

exog_variable = covid_data$hospitalizedCurrently
exog_variable = ifelse(covid_data$hospitalizedCurrently ==0, 1, covid_data$hospitalizedCurrently)

exog_variable = covid_data$hospitalizedIncrease
exog_variable = ifelse(covid_data$hospitalizedIncrease ==0, 1, covid_data$hospitalizedIncrease)



#@see: stackoverflow.com/questions/33714660/what-is-the-difference-the-zoo-object-and-ts-object-in-r
covid_ts <- zoo(response_variable, seq(as.Date("2020-01-13"), as.Date("2021-03-07"), by = "days"), frequency = 1)
exog_ts <- zoo(exog_variable, seq(as.Date("2020-01-13"), as.Date("2021-03-07"), by = "days"), frequency = 1)

#Build forecasting matrix to hold all rolling forecasts. Matrix Dimension: horizons by size of test set
forecast_matrix <- matrix(data = c(-1.2), nrow = horizons, ncol = te_size)

# Start rolling validation: run through entire test set 1 sample at a time
for (i in 1:te_size) {

    # Get training data: start=1+18317 from 1970-01-01 which is 2020-02-26 & end=221+18317+1 which is 2020-10-04(inclusive)
    # This also shifts the training window ahead by 1 sample at a time into the test set on every every iteration
    # For eg. For the next iteration: start=2+18317 from 1970-01-01 which is 2020-02-27 & end=221+18317+2 which is 2020-10-05(inclusive)
    # So we dropped the sample for 2020-02-26 from the training in 2nd iteration and included 1 from the test set. That's how we roll forward.
    #model_data <- as.ts(window(log(covid_ts), start = as.Date(i + zero_reference), end = as.Date(tr_size - 1 + zero_reference + i), frequency = 1))
    model_data <- window(log(covid_ts), start = as.Date(i + zero_reference), end = as.Date(tr_size - 1 + zero_reference + i), frequency = 1)
    exog_data <- window(log(exog_ts), start = as.Date(i + zero_reference), end = as.Date(tr_size - 1 + zero_reference + i), frequency = 1)
    # Retraining after kt samples
    if (i == 1) {
        arima_model <- Arima(y = model_data, order = c(p, d, q), seasonal = list(order = c(PP, DD, QQ), period = s), xreg=lag(exog_data, 14), method = "CSS")
    } else { 
        if ((i %% kt) == 0) { #if iteration mod retrain frequency is 0, then it is time to retrain the model with new training data
            rt = rt + 1
            arima_model <- Arima(y = model_data, order = c(p, d, q), seasonal = list(order = c(PP, DD, QQ), period = s), xreg=lag(exog_data, 14), method = "CSS")
        } else {
            # if not, then 
            # 1) use the new shifted data as the model data and 
            # 2) do not restimate the model parameters again: done by specifying the old model reference variable in "model" attribute of the function call
            arima_model <- Arima(y = model_data, xreg=lag(exog_data, 14), model = arima_model)
        }
    }
    # Once we have the model set: either with new data or with new data and retrained get next "horizon" number of forecasts.
    #future <- length(forecast(arima_model, xreg=lag(exog_data,14), h = horizons, level = 0))
    future <- forecast(arima_model, h = horizons, level = 0)
    # Get the single point forecast vector as forecast() function also returns high/max and low/min values
    forecasts <- future$mean
    # Start filling the forecast matrix 1 by 1 for "horizon" number of forecasts
    for (k in 1:horizons) {
      # future <- forecast(arima_model, xreg=lag(exog_data,k), h = k, level = 0)
      # forecasts <- future$mean
        if (k + i - 1 <= te_size) { # Condition to prevent overflow at the end of the test set;
            forecast_matrix[k, k+i-1] = forecasts[k]
        }
    }
}
# For first 14 days copy the values of the previous day as we cannot have h=2 forecast for first day of test set, h=3 forecast for the 2nd day of test set and so on;
for(i in 2:horizons){
  for(j in 1:i){
    forecast_matrix[i,j] = forecast_matrix[i-1,j]
  }
}
# Transpose the forecast matrix to be of dimension: te_size by horizons
forecast_matrix2 <- t(forecast_matrix)
forecast_matrix2 <- exp(forecast_matrix2)


# Get true values of the test data 
test_data <- window(covid_ts, start = as.Date((tr_size+1) + zero_reference), end = as.Date(ts_size + zero_reference), frequency = 1)

# Generate matrix to store smape scores for each horizon
smape_scores = matrix(data = NA, nrow = horizons, ncol = 1)

# Calculate the smape scores and store in the smape matrix, horizon by horizon.
for (i in 1:horizons) {
  smape_scores[i, 1] <- mean(abs((test_data - forecast_matrix2[, i]) / (test_data + forecast_matrix2[, i]))) * 200 #smape formula
  print(paste0("h=",i,",smape=",smape_scores[i,1]))
}

mean(smape_scores)
mean(c(17.87,15.40,17.30,18.6,18.8,19.6,19.2,19.4,22.1,24.6,24.9,25,25.1,25.3,25.40))


#In-sample Analysis

in_sample_data <- window(covid_ts, start = as.Date(1 + zero_reference), end = as.Date(376 + zero_reference), frequency = 1)
in_ts <- as.ts(in_sample_data)
in_sample_model <- Arima(y=in_sample_data, order = c(p,d,q), seasonal = list(order=c(PP,DD,QQ),period=s), method="CSS-ML")
length(in_sample_data)
summary(in_sample_model)
fitted_values <- in_ts - in_sample_model$residuals
length(fitted_values)
length(in_ts)
#in_sample_smape <- mean(abs((in_ts - fitted_values) / (in_ts + fitted_values))) * 200
#in_sample_smape
plot(fitted_values)
length(fitted_values)


sum = 0.0
e <- in_ts - fitted_values
cnt = 0
for(i in 1:length(in_ts)){
  denom <- abs(in_ts[i]) + abs(fitted_values[i])
  if(denom != 0){
    sum = sum + (abs(e[i]) / denom)
    cnt = cnt + 1
  }
}
print("In-Sample SMAPE:")
print(200 * sum/cnt)

