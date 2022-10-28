Select 
    max(Case When occupation = 'Doctor' then Name END) as Doctor,
    max(Case When occupation = 'Professor' then Name END) as Professor,  
    max(Case When occupation = 'Singer' then Name END) as Singer, 
    max(Case When occupation = 'Actor' then Name END) as Actor
from
  (Select 
    *, Row_number() over(partition by occupation order by name) rn 
    from occupations) a
Group by a.rn