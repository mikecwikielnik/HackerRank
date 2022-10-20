select distinct(CITY)
from STATION
where CITY like '%a'
or CITY like '%e'
or CITY like '%i'
or city like '%o'
or city like '%u';