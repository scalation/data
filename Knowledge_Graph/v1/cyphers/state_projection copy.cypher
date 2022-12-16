CALL gds.graph.project(
'complete_graph',
{
State: {
label: 'State',
properties: {
elevation:{
property: 'elevation',
defaultValue: 0
},
population:{
property: 'population',
defaultValue: 0
}
}
},

Reports:{
label:'Reports',
properties: {
Active:{
property: 'Active',
defaultValue: 0
},
Case_Fatality_Ratio:{
property: 'Case_Fatality_Ratio',
defaultValue: 0
},
Confirmed:{
property: 'Confirmed',
defaultValue: 0
},
Deaths:{
property: 'Deaths',
defaultValue: 0
},
Hospitalization_Rate:{
property: 'Hospitalization_Rate',
defaultValue: 0
},
Incident_Rate:{
property: 'Incident_Rate',
defaultValue: 0
},
Mortality_Rate:{
property: 'Mortality_Rate',
defaultValue: 0
},
People_Hospitalized:{
property: 'People_Hospitalized',
defaultValue: 0
},
People_Tested:{
property: 'People_Tested',
defaultValue: 0
},
Recovered:{
property: 'Recovered',
defaultValue: 0
},
Testing_Rate:{
property: 'Testing_Rate',
defaultValue: 0
},
Total_Test_Results:{
property: 'Total_Test_Results',
defaultValue: 0
},
daily_deaths:{
property: 'daily_deaths',
defaultValue: 0
}
}
},

Mobility:{
label:'Mobility',
properties: {
grocery_and_pharmacy_percent_change_from_baseline:{
property: 'grocery_and_pharmacy_percent_change_from_baseline',
defaultValue: 0
},
parks_percent_change_from_baseline:{
property: 'parks_percent_change_from_baseline',
defaultValue: 0
},
residential_percent_change_from_baseline:{
property: 'residential_percent_change_from_baseline',
defaultValue: 0
},
transit_stations_percent_change_from_baseline:{
property: 'transit_stations_percent_change_from_baseline',
defaultValue: 0
},
workplaces_percent_change_from_baseline:{
property: 'workplaces_percent_change_from_baseline',
defaultValue: 0
}
}
},

SocialCharacteristics:{
label:'SocialCharacteristics'
},

Education: {
label:'Education',
properties: {
associateDegreePct: {
property: 'associatesDegreePct',
defaultValue: 0
},
bachelorsDegreeOrHigherPct: {
property: 'bachelorsDegreeOrHigherPct',
defaultValue: 0
},
bachelorsDegreePct: {
property: 'bachelorsDegreePct',
defaultValue: 0
},
grade9thTo12thNoDiplomaPct: {
property: 'grade9thTo12thNoDiplomaPct',
defaultValue: 0
},
graduateOrProfessionalDegreePct: {
property: 'graduateOrProfessionalDegreePct',
defaultValue: 0.0
},
highSchoolGraduateOrHigherPct:{
property: 'highSchoolGraduateOrHigherPct',
defaultValue: 0
},
highSchoolGraduatePct:{
property: 'highSchoolGraduatePct',
defaultValue: 0
},
lessThan9thGradePct:{
property: 'lessThan9thGradePct',
defaultValue: 0
},
someCollegeNoDegreePct:{
property: 'someCollegeNoDegreePct',
defaultValue: 0
}
}
},

Computers:{
Label: 'Computers',
Properties: {
withBroadbandInternetPct: {
property: 'withBroadbandInternetPct',
defaultValue: 0
},
withComputerPct: {
property: 'withComputerPct',
defaultValue: 0
}
}
},

Demographics:{
Label: 'Demographics',
Properties: {
age0_4: {
property: 'age0_4',
defaultValue: 0
},
age10_14: {
property: 'age10_14',
defaultValue: 0
},
age15_19: {
property: 'age15_19',
defaultValue: 0
},
age20_24: {
property: 'age20_24',
defaultValue: 0
},
age25_34: {
property: 'age25_34',
defaultValue: 0
},
age35_44: {
property: 'age35_44',
defaultValue: 0
},
age45_54: {
property: 'age45_54',
defaultValue: 0
},
age55_59: {
property: 'age55_59',
defaultValue: 0
},
age5_9: {
property: 'age5_9',
defaultValue: 0
},
age60_64: {
property: 'age60_64',
defaultValue: 0
},
age65_74: {
property: 'age65_74',
defaultValue: 0
},
age75_84: {
property: 'age75_84',
defaultValue: 0
},
age85_: {
property: 'age85_',
defaultValue: 0
},
americanIndianAndAlaskaNative: {
property: 'americanIndianAndAlaskaNative',
defaultValue: 0
},
asian: {
property: 'asian',
defaultValue: 0
},
blackOrAfricanAmerican: {
property: 'blackOrAfricanAmerican',
defaultValue: 0
},
female: {
property: 'female',
defaultValue: 0
},
hispanicOrLatino: {
property: 'hispanicOrLatino',
defaultValue: 0
},
male: {
property: 'male',
defaultValue: 0
},
nativeHawaiianAndOtherPacificIslander: {
property: 'nativeHawaiianAndOtherPacificIslander',
defaultValue: 0
},
notHispanicOrLatino: {
property: 'notHispanicOrLatino',
defaultValue: 0
},
otherRace: {
property: 'otherRace',
defaultValue: 0
},
totalPopulation: {
property: 'totalPopulation',
defaultValue: 0
},
twoOrMoreRaces: {
property: 'twoOrMoreRaces',
defaultValue: 0
},
white: {
property: 'white',
defaultValue: 0
}
}
},

Economics:{
Label: 'Economics'
},

Commuting:{
Label: 'Commuting',
Properties: {
carpooledToWorkInCarTruckOrVanPct: {
property: 'carpooledToWorkInCarTruckOrVanPct',
defaultValue: 0
},
droveAloneToWorkInCarTruckOrVanPct: {
property: 'droveAloneToWorkInCarTruckOrVanPct',
defaultValue: 0
},
otherMeansOfCommutingToWorkPct: {
property: 'otherMeansOfCommutingToWorkPct',
defaultValue: 0
},
publicTransportToWorkPct: {
property: 'publicTransportToWorkPct',
defaultValue: 0
},
walkedToWorkPct: {
property: 'walkedToWorkPct',
defaultValue: 0
},
workedAtHomePct: {
property: 'workedAtHomePct',
defaultValue: 0
}
}
},

Occupation:{
Label: 'Occupation',
Properties: {
civilianEmployedPopulation16YearsAndOver: {
property: 'civilianEmployedPopulation16YearsAndOver',
defaultValue: 0
},
managementBusinessScienceAndArtsOccupations: {
property: 'managementBusinessScienceAndArtsOccupations',
defaultValue: 0
},
managementBusinessScienceAndArtsOccupationsPct: {
property: 'managementBusinessScienceAndArtsOccupationsPct',
defaultValue: 0
},
naturalResourcesConstructionAndMaintenanceOccupations: {
property: 'naturalResourcesConstructionAndMaintenanceOccupations',
defaultValue: 0
},
naturalResourcesConstructionAndMaintenanceOccupationsPct: {
property: 'naturalResourcesConstructionAndMaintenanceOccupationsPct',
defaultValue: 0
},
productionTransportationAndMaterialMovingOccupations: {
property: 'productionTransportationAndMaterialMovingOccupations',
defaultValue: 0
},
productionTransportationAndMaterialMovingOccupationsPct: {
property: 'productionTransportationAndMaterialMovingOccupationsPct',
defaultValue: 0
},
salesAndOfficeOccupations: {
property: 'salesAndOfficeOccupations',
defaultValue: 0
},
salesAndOfficeOccupationsPct: {
property: 'salesAndOfficeOccupationsPct',
defaultValue: 0
},
serviceOccupations: {
property: 'serviceOccupations',
defaultValue: 0
},
serviceOccupationsPct: {
property: 'serviceOccupationsPct',
defaultValue: 0
}
}
},

Employment:{
Label: 'Employment',
Properties: {
population16YearsAndOverInArmedForcesPct: {
property: 'population16YearsAndOverInArmedForcesPct',
defaultValue: 0
},
population16YearsAndOverInCivilianLaborForcePct: {
property: 'population16YearsAndOverInCivilianLaborForcePct',
defaultValue: 0
},
population16YearsAndOverInLaborForcePct: {
property: 'population16YearsAndOverInLaborForcePct',
defaultValue: 0
},
population16YearsAndOverNotInLaborForcePct: {
property: 'population16YearsAndOverNotInLaborForcePct',
defaultValue: 0
}
}
},

HealthInsurance:{
Label: 'HealthInsurance',
Properties: {
noHealthInsuranceCoveragePct: {
property: 'noHealthInsuranceCoveragePct',
defaultValue: 0
},
withHealthInsuranceCoveragePct: {
property: 'withHealthInsuranceCoveragePct',
defaultValue: 0
},
withPrivateHealthInsurancePct: {
property: 'withPrivateHealthInsurancePct',
defaultValue: 0
},
withPublicCoveragePct: {
property: 'withPublicCoveragePct',
defaultValue: 0
}
}
},

Income:{
Label: 'Income',
Properties: {
householdIncome100000To149999USDPct: {
property: 'householdIncome100000To149999USDPct',
defaultValue: 0
},
householdIncome10000To14999USDPct: {
property: 'householdIncome10000To14999USDPct',
defaultValue: 0
},
householdIncome150000To199999USDPct: {
property: 'householdIncome150000To199999USDPct',
defaultValue: 0
},
householdIncome15000To24999USDPct: {
property: 'householdIncome15000To24999USDPct',
defaultValue: 0
},
householdIncome25000To34999USDPct: {
property: 'householdIncome25000To34999USDPct',
defaultValue: 0
},
householdIncome35000To49999USDPct: {
property: 'householdIncome35000To49999USDPct',
defaultValue: 0
},
householdIncome50000To74999USDPct: {
property: 'householdIncome50000To74999USDPct',
defaultValue: 0
},
householdIncome75000To99999USDPct: {
property: 'householdIncome75000To99999USDPct',
defaultValue: 0
},
householdIncomeLessThan10000USDPct: {
property: 'householdIncomeLessThan10000USDPct',
defaultValue: 0
},
householdIncomeMoreThan200000USDPct: {
property: 'householdIncomeMoreThan200000USDPct',
defaultValue: 0
}
}
}
},
{
HAS_COMMUTING: {
type: 'HAS_COMMUTING',
orientation: 'UNDIRECTED'
},
HAS_COMPUTERS: {
type: 'HAS_COMPUTERS',
orientation: 'UNDIRECTED'
},
HAS_DEMOGRAPHICS: {
type: 'HAS_DEMOGRAPHICS',
orientation: 'UNDIRECTED'
},
HAS_ECONOMICS: {
type: 'HAS_ECONOMICS',
orientation: 'UNDIRECTED'
},
HAS_EDUCATION: {
type: 'HAS_EDUCATION',
orientation: 'UNDIRECTED'
},
HAS_EMPLOYMENT: {
type: 'HAS_EMPLOYMENT',
orientation: 'UNDIRECTED'
},
HAS_HEALTH_INSURANCE: {
type: 'HAS_HEALTH_INSURANCE',
orientation: 'UNDIRECTED'
},
HAS_INCOME: {
type: 'HAS_INCOME',
orientation: 'UNDIRECTED'
},
HAS_MOBILITY: {
type: 'HAS_MOBILITY',
orientation: 'UNDIRECTED'
},
HAS_OCCUPATION: {
type: 'HAS_OCCUPATION',
orientation: 'UNDIRECTED'
},
HAS_SOCIAL_CHARACTERISTICS: {
type: 'HAS_SOCIAL_CHARACTERISTICS',
orientation: 'UNDIRECTED'
},
IS_IN: {
type: 'IN',
orientation: 'UNDIRECTED'
},
PATH: {
type: 'PATH',
properties: {
distance: { 
property: 'distance',
defaultValue: 0
}
},
orientation: 'UNDIRECTED'
},
REPORTED_IN: {
type: 'REPORTED_IN',
orientation: 'UNDIRECTED'
}
})