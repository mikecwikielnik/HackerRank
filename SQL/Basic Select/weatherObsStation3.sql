select DISTINCT(CITY)
from STATION
where mod(ID, 2) = 0;