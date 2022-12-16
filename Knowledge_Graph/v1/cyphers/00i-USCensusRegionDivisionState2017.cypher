LOAD CSV WITH HEADERS 
FROM 'FILE:///00i-USCensus2017State.csv' AS row 
MATCH (a:State{name: row.name, country: 'US'})
SET a.fips = row.fips
RETURN count(a) as FIPS
;