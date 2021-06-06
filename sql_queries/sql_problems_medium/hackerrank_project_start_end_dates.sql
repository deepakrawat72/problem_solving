--https://www.hackerrank.com/challenges/sql-projects/problem
with projects_last_dates as (
	select project_last_date, IFNULL(lag(project_last_date)
	over (order by project_last_date), DATE('1000-01-01')) as prev_project_last_date from (
		select end_date as project_last_date, IFNULL(lead(end_date)
		over (order by end_date), DATE('9999-12-31')) as next_project_last_date from Projects
	) x where DATEDIFF(next_project_last_date, project_last_date) > 1
)


select project_start_date, project_end_date FROM (
SELECT MIN(start_date) as project_start_date, project_last_date as project_end_date, DATEDIFF(project_last_date, MIN(start_date)) as no_of_days
from projects_last_dates as pld
JOIN Projects as p
ON p.start_date > pld.prev_project_last_date AND p.end_date <= pld.project_last_date
GROUP BY project_last_date
) x
ORDER BY no_of_days asc, project_start_date asc