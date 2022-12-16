CALL gds.beta.graphSage.train(
'complete_graph',
{
modelName: 'multiLabelModelAll',
featureProperties: ['elevation', 'population', 'Active', 'Case_Fatality_Ratio', 'Confirmed', 'Deaths', 'Hospitalization_Rate', 'Incident_Rate', 'Mortality_Rate', 'People_Hospitalized', 'People_Tested', 'Recovered', 'Testing_Rate', 'Total_Test_Results', 'daily_deaths', 'grocery_and_pharmacy_percent_change_from_baseline', 'parks_percent_change_from_baseline', 'residential_percent_change_from_baseline', 'transit_stations_percent_change_from_baseline', 'workplaces_percent_change_from_baseline'
],
projectedFeatureDimension: 16,
batchSize: 64,
searchDepth: 10,
activationFunction: "RELU",
epochs: 100,
learningRate: 0.005
}
)
;
CALL gds.beta.graphSage.write(
  'complete_graph',
  {
    writeProperty: 'embedding',
    modelName: 'multiLabelModelAll'
  }
)