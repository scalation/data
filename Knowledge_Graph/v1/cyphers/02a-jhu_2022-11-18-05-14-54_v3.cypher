:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS 
FROM 'FILE:///02a-jhu_2022-11-18-05-14-54_v3.csv' AS row 
MERGE (c:Reports{id: 'Reports' + row.Date + '-' + row.FIPS})
SET c.name = 'Reports' + row.Date, c.date = date(row.Date), 
c.Confirmed = COALESCE(toInteger(row.Confirmed), 0), 
c.Deaths = COALESCE(toInteger(row.Deaths), 0),
c.Recovered = COALESCE(toInteger(row.Recovered), 0),
c.Active = COALESCE(toInteger(row.Active), 0),
c.Incident_Rate = COALESCE(toFloat(row.Incident_Rate), 0),
c.Total_Test_Results = COALESCE(toFloat(row.Total_Test_Results), 0),
c.People_Hospitalized = COALESCE(toFloat(row.People_Hospitalized), 0),
c.Case_Fatality_Ratio = COALESCE(toFloat(row.Case_Fatality_Ratio), 0),
c.Testing_Rate = COALESCE(toFloat(row.Testing_Rate), 0),
c.Hospitalization_Rate = COALESCE(toFloat(row.Hospitalization_Rate), 0),
c.People_Tested = COALESCE(toFloat(row.People_Tested), 0),
c.Mortality_Rate = COALESCE(toFloat(row.Mortality_Rate), 0),
c.daily_deaths = COALESCE(toFloat(row.daily_deaths), 0),
c.rolling_deaths_3 = COALESCE(toFloat(row.rolling_deaths_3), 0),
c.rolling_deaths_7 = COALESCE(toFloat(row.rolling_deaths_7), 0),
c.FIPS = row.FIPS,
c.source = 'JHU'
RETURN count(c) as CASES
;

:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS 
FROM 'FILE:///02a-jhu_2022-11-18-05-14-54_v3.csv' AS row
MATCH (c:Reports{id: 'Reports' + row.Date + '-' + row.FIPS})
MATCH (a:State{fips: row.FIPS})
MERGE (c)-[r:REPORTED_IN]->(a)
RETURN count(r) as REPORTED_IN
;