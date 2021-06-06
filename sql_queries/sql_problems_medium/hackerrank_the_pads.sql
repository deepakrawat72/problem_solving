--https://www.hackerrank.com/challenges/the-pads/problemv
with concat_names_and_prof as (
    select 0 as i, CONCAT(Name, '(', substr(occupation, 1, 1), ')') AS str,
    row_number() over (order by Name asc) as rn
from occupations
),
occ_count as (
    select i, cnt, occ, row_number() over (order by cnt asc, occ asc) as rn from (
    select 1 as i , lower(occupation) as occ, count(*) as cnt from occupations
    group by occupation
    order by cnt, occ
    ) x
)

select str from (
    select str, i, rn from concat_names_and_prof
    union all
    select concat('There are a total of ',cnt,' ' ,occ, 's.') AS str, i, rn from occ_count
) x order by i, rn