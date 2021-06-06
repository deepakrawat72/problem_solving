--https://www.hackerrank.com/challenges/binary-search-tree-1/problem
select node as N,
case when child  is null then 'Leaf'
     when parent is null then 'Root'
     else 'Inner' end as `type`
from (
select distinct b2.P as child, b1.N as node, b1.P as parent
FROM BST b1 LEFT JOIN BST b2
on b1.N = b2.P
) a
order by node