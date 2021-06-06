-- https://www.hackerrank.com/challenges/placements/problem
SELECT s.Name from Friends f
join Packages p1 on f.ID = p1.ID
join Packages p2 on f.Friend_ID = p2.ID
join Students s on s.ID = f.ID
where p2.Salary > p1.salary
order by p2.salary