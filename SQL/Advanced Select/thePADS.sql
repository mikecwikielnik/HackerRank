SELECT 
CASE
    WHEN OCCUPATION = 'Doctor' then concat(name, '(D)')
    WHEN OCCUPATION = 'Singer' then concat(name, '(S)')
    WHEN OCCUPATION = 'Actor' then concat(name, '(A)')
    else concat(name, '(P)')
END
FROM OCCUPATIONS
ORDER BY NAME ASC;

SELECT CONCAT('There are a total of ',count(occupation),' ',lower(occupation),'s.') 
from occupations 
group by occupation 
order by count(occupation) asc;