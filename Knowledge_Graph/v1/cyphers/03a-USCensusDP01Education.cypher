:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS 
FROM 'FILE:///03a-USCensusDP02EducationState.csv' AS row 
MERGE (s:SocialCharacteristics{id: 'SocialCharacteristics-' + row.stateFips})
SET s.name = 'SocialCharacteristics-' + row.stateFips,
    s.stateFips = row.stateFips
;
:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS 
FROM 'FILE:///03a-USCensusDP02EducationState.csv' AS row
MATCH (a:State{fips: row.stateFips})
MATCH (s:SocialCharacteristics{id: 'SocialCharacteristics-' + row.stateFips})
MERGE (a)-[h:HAS_SOCIAL_CHARACTERISTICS]->(s)
RETURN count(h) as HAS_SOCIAL_CHARACTERISTICS
;
:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS 
FROM 'FILE:///03a-USCensusDP02EducationState.csv' AS row 
MERGE (e:Education{id: 'SocialCharacteristics-' + row.stateFips})
SET e.name = 'Education-' + row.stateFips,
    e.population25YearsAndOver = toInteger(row.population25YearsAndOver),
    e.lessThan9thGrade = toInteger(row.lessThan9thGrade),
    e.lessThan9thGradePct = toFloat(row.lessThan9thGradePct),
    e.grade9thTo12thNoDiploma = toInteger(row.grade9thTo12thNoDiploma),
    e.grade9thTo12thNoDiplomaPct = toFloat(row.grade9thTo12thNoDiplomaPct),
    e.highSchoolGraduate = toInteger(row.highSchoolGraduate),
    e.highSchoolGraduatePct = toFloat(row.highSchoolGraduatePct),
    e.someCollegeNoDegree = toInteger(row.someCollegeNoDegree),
    e.someCollegeNoDegreePct = toFloat(row.someCollegeNoDegreePct),
    e.associatesDegree = toInteger(row.associatesDegree),
    e.associatesDegreePct = toFloat(row.associatesDegreePct),
    e.bachelorsDegree = toInteger(row.bachelorsDegree),
    e.bachelorsDegreePct = toFloat(row.bachelorsDegreePct),
    e.graduateOrProfessionalDegree = toInteger(row.graduateOrProfessionalDegree),
    e.graduateOrProfessionalDegreePct = toFloat(row.graduateOrProfessionalDegreePct),
    e.highSchoolGraduateOrHigher = toInteger(row.highSchoolGraduateOrHigher),
    e.highSchoolGraduateOrHigherPct = toFloat(row.highSchoolGraduateOrHigherPct),
    e.bachelorsDegreeOrHigher = toInteger(row.bachelorsDegreeOrHigher),
    e.bachelorsDegreeOrHigherPct = toFloat(row.bachelorsDegreeOrHigherPct),            
    e.stateFips = row.stateFips
RETURN count(e) as Education
;
:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS 
FROM 'FILE:///03a-USCensusDP02EducationState.csv' AS row
MATCH (s:SocialCharacteristics{id: 'SocialCharacteristics-' + row.stateFips})
MATCH (e:Education{id: 'SocialCharacteristics-' + row.stateFips})
MERGE (s)-[h:HAS_EDUCATION]->(e)
RETURN count(h) as HAS_EDUCATION
;

Match (s:SocialCharacteristics {stateFips:"1"})
Match (n:State{fips:"01"})
MERGE (n)-[h:HAS_SOCIAL_CHARACTERISTICS]->(s)
;
Match (s:SocialCharacteristics {stateFips:"2"})
Match (n:State{fips:"02"})
MERGE (n)-[h:HAS_SOCIAL_CHARACTERISTICS]->(s)
;
Match (s:SocialCharacteristics {stateFips:"4"})
Match (n:State{fips:"04"})
MERGE (n)-[h:HAS_SOCIAL_CHARACTERISTICS]->(s)
;
Match (s:SocialCharacteristics {stateFips:"5"})
Match (n:State{fips:"05"})
MERGE (n)-[h:HAS_SOCIAL_CHARACTERISTICS]->(s)
;
Match (s:SocialCharacteristics {stateFips:"6"})
Match (n:State{fips:"06"})
MERGE (n)-[h:HAS_SOCIAL_CHARACTERISTICS]->(s)
;
Match (s:SocialCharacteristics {stateFips:"8"})
Match (n:State{fips:"08"})
MERGE (n)-[h:HAS_SOCIAL_CHARACTERISTICS]->(s)
;
Match (s:SocialCharacteristics {stateFips:"9"})
Match (n:State{fips:"09"})
MERGE (n)-[h:HAS_SOCIAL_CHARACTERISTICS]->(s)
;