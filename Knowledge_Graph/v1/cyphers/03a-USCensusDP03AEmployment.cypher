:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS 
FROM 'FILE:///03a-USCensusDP03EmploymentState.csv' AS row 
MERGE (e:Economics{id: 'Economics-' + row.stateFips})
SET e.name = 'Economics-' + row.stateFips
;
:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS 
FROM 'FILE:///03a-USCensusDP03EmploymentState.csv' AS row
MATCH (a:State{fips: row.stateFips})
MATCH (e:Economics{id: 'Economics-' + row.stateFips})
MERGE (a)-[h:HAS_ECONOMICS]->(e)
RETURN count(h) as HAS_ECONOMICS
;
:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS 
FROM 'FILE:///03a-USCensusDP03EmploymentState.csv' AS row 
MERGE (e:Employment{id: 'Employment-' + row.stateFips})
SET e.name = 'Employment-' + row.stateFips,
    e.population16YearsAndOver = toInteger(row.population16YearsAndOver),
    e.population16YearsAndOverInLaborForce = toInteger(row.population16YearsAndOverInLaborForce),
    e.population16YearsAndOverInLaborForcePct = toFloat(row.population16YearsAndOverInLaborForcePct),
    e.population16YearsAndOverInCivilianLaborForce = toInteger(row.population16YearsAndOverInCivilianLaborForce),
    e.population16YearsAndOverInCivilianLaborForcePct = toFloat(row.population16YearsAndOverInCivilianLaborForcePct),
    e.population16YearsAndOverInArmedForces = toInteger(row.population16YearsAndOverInArmedForces),
    e.population16YearsAndOverInArmedForcesPct = toFloat(row.population16YearsAndOverInArmedForcesPct),
    e.population16YearsAndOverNotInLaborForce = toInteger(row.population16YearsAndOverNotInLaborForce),
    e.population16YearsAndOverNotInLaborForcePct = toInteger(row.population16YearsAndOverNotInLaborForcePct), e.stateFips = row.stateFips
RETURN count(e) as Employment
;
:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS 
FROM 'FILE:///03a-USCensusDP03EmploymentState.csv' AS row
MATCH (e:Economics{id: 'Economics-' + row.stateFips})
MATCH (es:Employment{id: 'Employment-' + row.stateFips})
MERGE (e)-[h:HAS_EMPLOYMENT]->(es)
RETURN count(h) as HAS_EMPLOYMENT
;

Match (e:Economics {id: 'Economics-1'})
Match (n:State{fips:"01"})
MERGE (n)-[h:HAS_ECONOMICS]->(e)
;
Match (e:Economics {id: 'Economics-2'})
Match (n:State{fips:"02"})
MERGE (n)-[h:HAS_ECONOMICS]->(e)
;
Match (e:Economics {id: 'Economics-4'})
Match (n:State{fips:"04"})
MERGE (n)-[h:HAS_ECONOMICS]->(e)
;
Match (e:Economics {id: 'Economics-5'})
Match (n:State{fips:"05"})
MERGE (n)-[h:HAS_ECONOMICS]->(e)
;
Match (e:Economics {id: 'Economics-6'})
Match (n:State{fips:"06"})
MERGE (n)-[h:HAS_ECONOMICS]->(e)
;
Match (e:Economics {id: 'Economics-8'})
Match (n:State{fips:"08"})
MERGE (n)-[h:HAS_ECONOMICS]->(e)
;
Match (e:Economics {id: 'Economics-9'})
Match (n:State{fips:"09"})
MERGE (n)-[h:HAS_ECONOMICS]->(e)
;