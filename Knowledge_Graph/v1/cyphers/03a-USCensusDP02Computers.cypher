:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS 
FROM 'FILE:///03a-USCensusDP02ComputersState.csv' AS row 
MERGE (c:Computers{id: 'SocialCharacteristics-' + row.stateFips})
SET c.name = 'Computers-' + row.stateFips,
    c.totalHouseholds = toInteger(row.totalHouseholds),
    c.withComputer = toInteger(row.withComputer),
    c.withComputerPct = toFloat(row.withComputerPct),
    c.withBroadbandInternet = toInteger(row.withBroadbandInternet),
    c.withBroadbandInternetPct = toFloat(row.withBroadbandInternetPct),           
    c.stateFips = row.stateFips
RETURN count(c) as Computers
;
:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS 
FROM 'FILE:///03a-USCensusDP02ComputersState.csv' AS row
MATCH (s:SocialCharacteristics{id: 'SocialCharacteristics-' + row.stateFips})
MATCH (c:Computers{id: 'SocialCharacteristics-' + row.stateFips})
MERGE (s)-[h:HAS_COMPUTERS]->(c)
RETURN count(h) as HAS_Computers
;