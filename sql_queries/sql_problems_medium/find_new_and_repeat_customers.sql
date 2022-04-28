
--input
--+----------+-------------+------------+--------------+
--| order_id | customer_id | order_date | order_amount |
--+----------+-------------+------------+--------------+
--|        1 |         100 | 2022-01-01 |         2000 |
--|        2 |         200 | 2022-01-01 |         2500 |
--|        3 |         300 | 2022-01-01 |         2100 |
--|        4 |         100 | 2022-01-02 |         2000 |
--|        5 |         400 | 2022-01-02 |         2200 |
--|        6 |         500 | 2022-01-02 |         2700 |
--|        7 |         100 | 2022-01-03 |         3000 |
--|        8 |         400 | 2022-01-03 |         1000 |
--|        9 |         600 | 2022-01-03 |         3000 |
--+----------+-------------+------------+--------------+

--output
--+------------+--------------+-----------------+
--| order_date | new_customer | repeat_customer |
--+------------+--------------+-----------------+
--| 2022-01-01 |            3 |               0 |
--| 2022-01-02 |            2 |               1 |
--| 2022-01-03 |            1 |               2 |
--+------------+--------------+-----------------+


use sql_practise;

create table if not exists customer_orders (
order_id integer,
customer_id integer,
order_date date,
order_amount integer
);

select * from customer_orders;

insert into customer_orders values(1,100,cast('2022-01-01' as date),2000);
insert into customer_orders values(2,200,cast('2022-01-01' as date),2500);
insert into customer_orders values(3,300,cast('2022-01-01' as date),2100);
insert into customer_orders values(4,100,cast('2022-01-02' as date),2000);
insert into customer_orders values(5,400,cast('2022-01-02' as date),2200);
insert into customer_orders values(6,500,cast('2022-01-02' as date),2700);
insert into customer_orders values(7,100,cast('2022-01-03' as date),3000);
insert into customer_orders values(8,400,cast('2022-01-03' as date),1000);
insert into customer_orders values(9,600,cast('2022-01-03' as date),3000);

SELECT
	order_date,
	SUM(CASE WHEN old_customer IS NULL then 1 else 0 end) as new_customer,
	SUM(CASE WHEN old_customer IS NOT NULL then 1 else 0 end) as repeat_customer
	FROM (
		SELECT DISTINCT curr.customer_id as customer, old.customer_id as old_customer, curr.order_date
		FROM customer_orders as curr
		LEFT JOIN customer_orders as old
		ON curr.customer_id = old.customer_id
		AND old.order_date < curr.order_date
	) AS TEMP
GROUP BY order_date