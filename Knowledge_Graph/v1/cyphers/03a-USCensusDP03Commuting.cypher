:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS 
FROM 'FILE:///03a-USCensusDP03CommutingState.csv' AS row 
MERGE (c:Commuting{id: 'Commuting-' + row.stateFips})
SET c.name = 'Commuting-' + row.stateFips,
    c.workers16YearsAndOver = toInteger(row.workers16YearsAndOver),
    c.droveAloneToWorkInCarTruckOrVan = toInteger(row.droveAloneToWorkInCarTruckOrVan),
    c.droveAloneToWorkInCarTruckOrVanPct = toFloat(row.droveAloneToWorkInCarTruckOrVanPct),
    c.carpooledToWorkInCarTruckOrVan = toInteger(row.carpooledToWorkInCarTruckOrVan),
    c.carpooledToWorkInCarTruckOrVanPct = toFloat(row.carpooledToWorkInCarTruckOrVanPct),
    c.publicTransportToWork = toInteger(row.publicTransportToWork),
    c.publicTransportToWorkPct = toFloat(row.publicTransportToWorkPct),
    c.walkedToWork = toInteger(row.walkedToWork),
    c.walkedToWorkPct = toFloat(row.walkedToWorkPct),
    c.otherMeansOfCommutingToWork = toInteger(row.otherMeansOfCommutingToWork),
    c.otherMeansOfCommutingToWorkPct = toFloat(row.otherMeansOfCommutingToWorkPct),
    c.workedAtHome = toInteger(row.workedAtHome),
    c.workedAtHomePct = toFloat(row.workedAtHomePct),
    c.meanTravelTimeToWorkMinutes = toInteger(row.meanTravelTimeToWorkMinutes),
    c.stateFips = row.stateFips
RETURN count(c) as Commuting
;
:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS 
FROM 'FILE:///03a-USCensusDP03CommutingState.csv' AS row
MATCH (e:Economics{id: 'Economics-' + row.stateFips})
MATCH (c:Commuting{id: 'Commuting-' + row.stateFips})
MERGE (e)-[h:HAS_COMMUTING]->(c)
RETURN count(h) as HAS_COMMUTING
;