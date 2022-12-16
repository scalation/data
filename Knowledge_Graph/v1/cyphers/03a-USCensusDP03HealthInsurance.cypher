:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS 
FROM 'FILE:///03a-USCensusDP03HealthInsuranceState.csv' AS row 
MERGE (h:HealthInsurance{id: 'HealthInsurance-' + row.stateFips})
SET h.name = 'HealthInsurance-' + row.stateFips,
    h.civilianNoninstitutionalizedPopulation = toInteger(row.civilianNoninstitutionalizedPopulation),
    h.withHealthInsuranceCoverage = toInteger(row.withHealthInsuranceCoverage),
    h.withHealthInsuranceCoveragePct = toFloat(row.withHealthInsuranceCoveragePct),
    h.withPrivateHealthInsurance = toInteger(row.withPrivateHealthInsurance),
    h.withPrivateHealthInsurancePct = toFloat(row.withPrivateHealthInsurancePct),
    h.withPublicCoverage = toInteger(row.withPublicCoverage),
    h.withPublicCoveragePct = toFloat(row.withPublicCoveragePct),
    h.noHealthInsuranceCoverage = toInteger(row.noHealthInsuranceCoverage),
    h.noHealthInsuranceCoveragePct = toFloat(row.noHealthInsuranceCoveragePct),
    h.stateFips = row.stateFips
RETURN count(h) as HealthInsurance
;
:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS 
FROM 'FILE:///03a-USCensusDP03HealthInsuranceState.csv' AS row
MATCH (e:Economics{id: 'Economics-' + row.stateFips})
MATCH (h:HealthInsurance{id: 'HealthInsurance-' + row.stateFips})
MERGE (e)-[hh:HAS_HEALTH_INSURANCE]->(h)
RETURN count(hh) as HAS_HEALTH_INSURANCE
;