:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS 
FROM 'FILE:///03a-USCensusDP03OccupationState.csv' AS row 
MERGE (o:Occupation{id: 'Occupation-' + row.stateFips})
SET o.name = 'Occupation-' + row.stateFips,
    o.civilianEmployedPopulation16YearsAndOver = toInteger(row.civilianEmployedPopulation16YearsAndOver),
    o.managementBusinessScienceAndArtsOccupations = toInteger(row.managementBusinessScienceAndArtsOccupations),
    o.managementBusinessScienceAndArtsOccupationsPct = toFloat(row.managementBusinessScienceAndArtsOccupationsPct),
    o.serviceOccupations = toInteger(row.serviceOccupations),
    o.serviceOccupationsPct = toFloat(row.serviceOccupationsPct),
    o.salesAndOfficeOccupations = toInteger(row.salesAndOfficeOccupations),
    o.salesAndOfficeOccupationsPct = toFloat(row.salesAndOfficeOccupationsPct),
    o.naturalResourcesConstructionAndMaintenanceOccupations = toInteger(row.naturalResourcesConstructionAndMaintenanceOccupations),
    o.naturalResourcesConstructionAndMaintenanceOccupationsPct = toFloat(row.naturalResourcesConstructionAndMaintenanceOccupationsPct),
    o.productionTransportationAndMaterialMovingOccupations = toInteger(row.productionTransportationAndMaterialMovingOccupations),
    o.productionTransportationAndMaterialMovingOccupationsPct = toFloat(row.productionTransportationAndMaterialMovingOccupationsPct),
    o.stateFips = row.stateFips
RETURN count(o) as Occupation
;
:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS 
FROM 'FILE:///03a-USCensusDP03OccupationState.csv' AS row
MATCH (e:Economics{id: 'Economics-' + row.stateFips})
MATCH (o:Occupation{id: 'Occupation-' + row.stateFips})
MERGE (e)-[h:HAS_OCCUPATION]->(o)
RETURN count(h) as HAS_OCCUPATION
;