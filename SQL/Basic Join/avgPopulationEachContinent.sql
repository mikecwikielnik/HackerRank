SELECT COUNTRY.Continent, FLOOR(AVG(CITY.Population))
FROM City
INNER Join Country
ON CITY.CountryCode = COUNTRY.Code
GROUP BY COUNTRY.Continent;