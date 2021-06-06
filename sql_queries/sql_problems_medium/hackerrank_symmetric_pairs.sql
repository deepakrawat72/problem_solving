---https://www.hackerrank.com/challenges/symmetric-pairs/problem

--20,20
--20,21
--23,22
--22,23
--21,20

select f1.X as x1, f1.y as y1 from Functions f1 JOIN Functions f2
ON f1.X = f2.Y and f1.Y = f2.X
AND f1.X <= f1.Y
GROUP BY x1, y1
having not (x1 = y1 and count(*) = 1) -- this condition will remove all pairs x=y and are present due to join
--e.g (20,20) is present only once so it will also get included due to join
order by x1