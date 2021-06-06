--https://www.hackerrank.com/challenges/occupations/problem
SELECT
MAX(CASE WHEN Occupation = 'Doctor' THEN Name else NULL end) as Doctor,
MAX(CASE WHEN Occupation = 'Professor' THEN Name else NULL end) as Professor,
MAX(CASE WHEN Occupation = 'Singer' THEN Name else NULL end) as Singer,
MAX(CASE WHEN Occupation = 'Actor' THEN Name else NULL end) as Actor
FROM (
select *, rank() over (partition by Occupation order by Name) as rnk
from OCCUPATIONS
) x
group by x.rnk