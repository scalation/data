#install.packages("forecast")
library(forecast)

zero_reference = 18317 #Difference between 1970-01-01 to 2020-02-25

tr_size = 222
te_size = 154
horizons = 14
kt = 5

covid_data <- read.csv(file = "https://raw.githubusercontent.com/scalation/data/master/COVID/CLEANED_35_Updated.csv")

#Trying ts function from stats package - not working as expected
#covid_ts <- ts(covid_data$deathIncrease,start = as.Date("2020-02-26"),frequency = 365)
#covid_ts

# Trying zoo object for daily ts conversion - working as expected
covid_ts <- zoo(covid_data$deathIncrease, seq(as.Date("2020-01-13"), as.Date("2021-03-07"), by = "days"), frequency=1)
length(covid_ts)
forecast_matrix <- matrix(data = c(-1.2),nrow = horizons, ncol = te_size)
for(i in 1:te_size){
  model_data <- window(covid_ts, start = as.Date(i+zero_reference), end = as.Date(221+zero_reference+i),  frequency=1)
  arima_model <- Arima(y=model_data, order = c(1,0,0), seasonal = list(order=c(3,1,1),period=7), method="ML")
  future <- forecast(arima_model,h=horizons, level = 0)
  forecasts <- future$mean
  for (k in 1:horizons) {
    if(k+i-1 <= te_size){
      forecast_matrix[k, k+i-1] = forecasts[k]
    }
  }
}

for(i in 2:horizons){
  for(j in 1:i){
    forecast_matrix[i,j] = forecast_matrix[i-1,j]
  }
}

forecast_matrix <- t(forecast_matrix)
test_data <- window(covid_ts, start = as.Date(223+zero_reference), end = as.Date(376+zero_reference),  frequency=1)
smape_scores = matrix(data = NA, nrow = horizons, ncol = 1)
for (i in 1:horizons) {
  smape_scores[i, 1] <- mean(abs((test_data - forecast_matrix[, i]) / (test_data + forecast_matrix[, i]))) * 200
  print(paste0("h=",i,",smape=",smape_scores[i,1]))
}

#In-sample
in_sample_data <- window(covid_ts, start = as.Date(1 + zero_reference), end = as.Date(376 + zero_reference), frequency = 1)
in_ts <- as.ts(in_sample_data)
in_sample_model <- Arima(y=in_sample_data, order = c(4,0,2), seasonal = list(order=c(0,0,0),period=0), method="ML")
length(in_sample_data)
summary(in_sample_model)
fitted_values <- in_ts - in_sample_model$residuals
length(fitted_values)
length(in_ts)
in_sample_smape <- mean(abs((in_ts - fitted_values) / (in_ts + fitted_values))) * 200
in_sample_smape
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
print(200 * sum/cnt)

summary(in_sample_model)

for (i in 1:length(fitted_values)){
  print(fitted_values[i])
}

for (i in 1:length(in_ts)){
  print(in_ts[i])
}
