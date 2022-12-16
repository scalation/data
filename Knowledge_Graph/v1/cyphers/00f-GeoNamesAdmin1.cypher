LOAD CSV WITH HEADERS 
FROM 'FILE:///00f-GeoNamesAdmin1-US.csv' AS row 
MERGE (a:State{id: row.id})
SET a.name = row.name, a.code = row.code, a.country = row.parentId, a.geonameId = row.geonameId, a.population = toInteger(row.population), a.elevation = toInteger(row.elevation),
a.location = point({longitude: toFloat(row.longitude), latitude: toFloat(row.latitude)})
RETURN count(a) as State
;
LOAD CSV WITH HEADERS 
FROM 'FILE:///00f-GeoNamesAdmin1-US.csv' AS row 
MATCH (a:State{id: row.id})
MATCH (ct:Country{id: row.parentId})
MERGE (a)-[i:IN]->(ct)
RETURN count(i) as IN
;
