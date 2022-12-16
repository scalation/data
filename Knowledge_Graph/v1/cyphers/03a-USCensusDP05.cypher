:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS 
FROM 'FILE:///03a-USCensusDP05State.csv' AS row 
MERGE (d:Demographics{id: 'Demographics-' + row.stateFips})
SET d.name = 'Demographics-' + row.stateFips,
    d.totalPopulation = toInteger(row.totalPopulation), 
    d.male = toInteger(row.male), d.female = toInteger(row.female),
    d.age0_4 = toInteger(row.age0_4), d.age5_9 = toInteger(row.age5_9), d.age10_14 = toInteger(row.age10_14),
    d.age15_19 = toInteger(row.age15_19), d.age20_24 = toInteger(row.age20_24), 
    d.age25_34 = toInteger(row.age25_34), d.age35_44 = toInteger(row.age35_44), 
    d.age45_54 = toInteger(row.age45_54), d.age55_59 = toInteger(row.age55_59), 
    d.age60_64 = toInteger(row.age60_64), d.age65_74 = toInteger(row.age65_74), 
    d.age75_84 = toInteger(row.age75_84), d.age85_ = toInteger(row.age85_),
    d.white = toInteger(row.white), d.blackOrAfricanAmerican = toInteger(row.blackOrAfricanAmerican), 
    d.americanIndianAndAlaskaNative = toInteger(row.americanIndianAndAlaskaNative), 
    d.asian = toInteger(row.asian), 
    d.nativeHawaiianAndOtherPacificIslander = toInteger(row.nativeHawaiianAndOtherPacificIslander),
    d.otherRace = toInteger(row.otherRace), d.twoOrMoreRaces = toInteger(row.twoOrMoreRaces),
    d.hispanicOrLatino = toInteger(row.hispanicOrLatino), 
    d.notHispanicOrLatino = toInteger(row.notHispanicOrLatino),
    d.stateFips = row.stateFips
RETURN count(d) as Demographics
;
:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS 
FROM 'FILE:///03a-USCensusDP05State.csv' AS row
MATCH (a:State{fips: row.stateFips})
MATCH (d:Demographics{id: 'Demographics-' + row.stateFips})
MERGE (a)-[h:HAS_DEMOGRAPHICS]->(d)
RETURN count(h) as HAS_DEMOGRAPHICS
;

Match (e:Demographics {id: 'Demographics-1'})
Match (n:State{fips:"01"})
MERGE (n)-[h:HAS_DEMOGRAPHICS]->(e)
;
Match (e:Demographics {id: 'Demographics-2'})
Match (n:State{fips:"02"})
MERGE (n)-[h:HAS_DEMOGRAPHICS]->(e)
;
Match (e:Demographics {id: 'Demographics-4'})
Match (n:State{fips:"04"})
MERGE (n)-[h:HAS_DEMOGRAPHICS]->(e)
;
Match (e:Demographics {id: 'Demographics-5'})
Match (n:State{fips:"05"})
MERGE (n)-[h:HAS_DEMOGRAPHICS]->(e)
;
Match (e:Demographics {id: 'Demographics-6'})
Match (n:State{fips:"06"})
MERGE (n)-[h:HAS_DEMOGRAPHICS]->(e)
;
Match (e:Demographics {id: 'Demographics-8'})
Match (n:State{fips:"08"})
MERGE (n)-[h:HAS_DEMOGRAPHICS]->(e)
;
Match (e:Demographics {id: 'Demographics-9'})
Match (n:State{fips:"09"})
MERGE (n)-[h:HAS_DEMOGRAPHICS]->(e)
;