LOAD CSV WITH HEADERS 
FROM 'FILE:///00e-GeoNamesCountry-US.csv' AS row 
MERGE (c:Country{id: row.id})
SET c.name = row.name, c.iso = row.iso, c.iso3 = row.iso3, c.isoNumeric = row.isoNumeric, c.geonameId = row.geonameId, c.areaSqKm = toInteger(row.areaSqKm), c.population = toInteger(row.population),
c.location = point({longitude: toFloat(row.longitude), latitude: toFloat(row.latitude)})
RETURN count(c) as Country
;
