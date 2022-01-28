--   Given the SALES_TRANSACTION table below, write a query which returns a
--   summary of monthly sales for each sales person in the following format:

--   SALES_TRANSACTION

--   SALES_PERSON_ID, 	SALES_DATE, 	SALES_QTY
--   SP1                       			1-Jan-2021         10
--   SP1                       			2-Jan-2021         12
--   SP1                      			 3-Jan-2021        25

--   The output should look like the below, ie a result-set with 13 columns - the first
--   column is the sales_person, and the next 12 columns are the cumulative sales for each month

--   SALES_PERSON_ID, C, FEB_SALES, MAR_SALES ………. DEC_SALES
--   SP1			 47		xx		yy			zz
--   SP2     		aa		bb		cc			d

-- create a table
CREATE TABLE sales_transactions (
  SALES_PERSON_ID INTEGER,
  SALES_DATE VARCHAR(10),
  SALES_QTY INT
);
-- insert some values
INSERT INTO sales_transactions VALUES (1, '1-Jan-2021', 10);
INSERT INTO sales_transactions VALUES (1, '2-Jan-2021', 12);
INSERT INTO sales_transactions VALUES (1, '3-Feb-2021', 25);
INSERT INTO sales_transactions VALUES (1, '3-Dec-2021', 25);
INSERT INTO sales_transactions VALUES (2, '3-Jan-2021', 25);
INSERT INTO sales_transactions VALUES (2, '3-Dec-2021', 25);

select * from sales_transactions;

SELECT
  SALES_PERSON_ID,
  SUM(CASE WHEN SALES_MONTH = 'Jan' THEN SALES_QTY ELSE NULL END) AS JAN_SALES,
  SUM(CASE WHEN SALES_MONTH = 'Feb' THEN SALES_QTY ELSE NULL END) AS FEB_SALES,
  SUM(CASE WHEN SALES_MONTH = 'Mar' THEN SALES_QTY ELSE NULL END) AS MAR_SALES,
  SUM(CASE WHEN SALES_MONTH = 'Apr' THEN SALES_QTY ELSE NULL END) AS APR_SALES,
  SUM(CASE WHEN SALES_MONTH = 'May' THEN SALES_QTY ELSE NULL END) AS MAY_SALES,
  SUM(CASE WHEN SALES_MONTH = 'Jun' THEN SALES_QTY ELSE NULL END) AS JUN_SALES,
  SUM(CASE WHEN SALES_MONTH = 'Jul' THEN SALES_QTY ELSE NULL END) AS JUL_SALES,
  SUM(CASE WHEN SALES_MONTH = 'Aug' THEN SALES_QTY ELSE NULL END) AS AUG_SALES,
  SUM(CASE WHEN SALES_MONTH = 'Sep' THEN SALES_QTY ELSE NULL END) AS SEP_SALES,
  SUM(CASE WHEN SALES_MONTH = 'Oct' THEN SALES_QTY ELSE NULL END) AS OCT_SALES,
  SUM(CASE WHEN SALES_MONTH = 'Nov' THEN SALES_QTY ELSE NULL END) AS NOV_SALES,
  SUM(CASE WHEN SALES_MONTH = 'Dec' THEN SALES_QTY ELSE NULL END) AS DEC_SALES
FROM (
	SELECT SALES_PERSON_ID, substring_index(substring_index(SALES_DATE, '-', 2), '-', -1) AS SALES_MONTH, SALES_QTY
	FROM sales_transactions
) SALES_DATA
GROUP BY SALES_PERSON_ID