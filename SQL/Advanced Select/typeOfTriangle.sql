SELECT CASE WHEN A+B<=C OR A+C<=B OR B+C<=A THEN 'Not A Triangle'
else CASE WHEN A=B and B=C THEN 'Equilateral' when A=C OR A=B OR C=B THEN 'Isosceles' else 'Scalene' end END

from triangles;