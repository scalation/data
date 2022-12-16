:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS 
FROM 'FILE:///03a-USCensusDP03IncomeState.csv' AS row 
MERGE (i:Income{id: 'Income-' + row.stateFips})
SET i.name = 'Income-' + row.stateFips,
    i.totalHouseholds = toInteger(row.totalHouseholds),
    i.householdIncomeLessThan10000USD = toInteger(row.householdIncomeLessThan10000USD),
    i.householdIncomeLessThan10000USDPct = toFloat(row.householdIncomeLessThan10000USDPct),
    i.householdIncome10000To14999USD = toInteger(row.householdIncome10000To14999USD),
    i.householdIncome10000To14999USDPct = toFloat(row.householdIncome10000To14999USDPct),
    i.householdIncome15000To24999USD = toInteger(row.householdIncome15000To24999USD),
    i.householdIncome15000To24999USDPct = toFloat(row.householdIncome15000To24999USDPct),
    i.householdIncome25000To34999USD = toInteger(row.householdIncome25000To34999USD),
    i.householdIncome25000To34999USDPct = toFloat(row.householdIncome25000To34999USDPct),
    i.householdIncome35000To49999USD = toInteger(row.householdIncome35000To49999USD),
    i.householdIncome35000To49999USDPct = toFloat(row.householdIncome35000To49999USDPct),
    i.householdIncome50000To74999USD = toInteger(row.householdIncome50000To74999USD),
    i.householdIncome50000To74999USDPct = toFloat(row.householdIncome50000To74999USDPct),
    i.householdIncome75000To99999USD = toInteger(row.householdIncome75000To99999USD),
    i.householdIncome75000To99999USDPct = toFloat(row.householdIncome75000To99999USDPct),
    i.householdIncome100000To149999USD = toInteger(row.householdIncome100000To149999USD),
    i.householdIncome100000To149999USDPct = toFloat(row.householdIncome100000To149999USDPct),
    i.householdIncome150000To199999USD = toInteger(row.householdIncome150000To199999USD),
    i.householdIncome150000To199999USDPct = toFloat(row.householdIncome150000To199999USDPct),
    i.householdIncomeMoreThan200000USD = toInteger(row.householdIncomeMoreThan200000USD),
    i.householdIncomeMoreThan200000USDPct = toFloat(row.householdIncomeMoreThan200000USDPct),
    i.medianHouseholdIncomeUSD = toInteger(row.medianHouseholdIncomeUSD),
    i.meanHouseholdIncomeUSD = toInteger(row.meanHouseholdIncomeUSD),
    i.stateFips = row.stateFips
RETURN count(i) as Income
;
:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS 
FROM 'FILE:///03a-USCensusDP03IncomeState.csv' AS row
MATCH (e:Economics{id: 'Economics-' + row.stateFips})
MATCH (i:Income{id: 'Income-' + row.stateFips})
MERGE (e)-[h:HAS_INCOME]->(i)
RETURN count(h) as HAS_INCOME
;