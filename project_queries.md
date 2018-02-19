CREATE TABLE fact(Date DATE, Prod_Id VARCHAR(20), Zip INT, State VARCHAR(10), City VARCHAR(30), CONSTRAINT PK_Fact PRIMARY KEY (Date,Prod_Id,Zip));

CREATE TABLE date(Date DATE, inflation DECIMAL(4,4), unemployment DECIMAL(4,4), tbill DECIMAL(4,4), natsales INT, CONSTRAINT PK_Date PRIMARY KEY (Date));


ALTER TABLE fact ADD CONSTRAINT FK_Date FOREIGN KEY (Date) REFERENCES fact(Date) ON DELETE CASCADE;

+-------------+-------------+------+-----+---------+-------+
| Field       | Type        | Null | Key | Default | Extra |
+-------------+-------------+------+-----+---------+-------+
| prod_id     | int(11)     | NO   | PRI | NULL    |       |
| brand       | varchar(20) | YES  |     | NULL    |       |
| name        | varchar(75) | YES  |     | NULL    |       |
| price       | int(11)     | YES  |     | NULL    |       |
| cost        | int(11)     | YES  |     | NULL    |       |
| shipping_wt | smallint(6) | YES  |     | NULL    |       |
+-------------+-------------+------+-----+---------+-------+

CREATE TABLE product(prod_id INT(11), brand VARCHAR(20), name VARCHAR(75), price INT(11), cost INT(11), CONSTRAINT PK_product PRIMARY KEY (prod_id), CONSTRAINT FK_product FOREIGN KEY (prod_id) REFERENCES fact(Prod_Id));

INSERT INTO econ.product (prod_id, brand, name, price, cost)
SELECT prod_id, brand, name, price, cost FROM dualcore.products;

LOAD DATA LOCAL INFILE '/home/mcmillwh/econ_monthly.csv'
INTO TABLE date
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

--insert data into fact table
INSERT INTO TABLE fact (Date)
SELECT COUNT(*)
FROM dualcore.order_details od LEFT INNER JOIN dualcore.orders o ON od.order_id = o.order_id;

SELECT COUNT(*) 
FROM dualcore.order_details od 
LEFT JOIN dualcore.orders o 
ON od.order_id = o.order_id
LEFT JOIN customers c
ON o.cust_id = c.cust_id;

3333244

SELECT *
FROM dualcore.order_details od 
LEFT JOIN dualcore.orders o 
ON od.order_id = o.order_id
LEFT JOIN customers c
ON o.cust_id = c.cust_id
LIMIT 20;

+----------+---------+----------+---------+---------------------+---------+----------+-----------+--------------------------+---------------------+-------+---------+
| order_id | prod_id | order_id | cust_id | order_date          | cust_id | fname    | lname     | address                  | city                | state | zipcode |
+----------+---------+----------+---------+---------------------+---------+----------+-----------+--------------------------+---------------------+-------+---------+
|  5000001 | 1273719 |  5000001 | 1133938 | 2008-06-01 00:03:35 | 1133938 | Ruby     | Gibson    | 27640 West 8th Street    | Springfield         | IL    | 62706   |
|  5000001 | 1273767 |  5000001 | 1133938 | 2008-06-01 00:03:35 | 1133938 | Ruby     | Gibson    | 27640 West 8th Street    | Springfield         | IL    | 62706   |
|  5000001 | 1273779 |  5000001 | 1133938 | 2008-06-01 00:03:35 | 1133938 | Ruby     | Gibson    | 27640 West 8th Street    | Springfield         | IL    | 62706   |
|  5000002 | 1274124 |  5000002 | 1131278 | 2008-06-01 00:27:42 | 1131278 | Helen    | Speer     | 20296 West 17th Street   | San Francisco       | CA    | 94117   |
|  5000002 | 1273737 |  5000002 | 1131278 | 2008-06-01 00:27:42 | 1131278 | Helen    | Speer     | 20296 West 17th Street   | San Francisco       | CA    | 94117   |
|  5000002 | 1274227 |  5000002 | 1131278 | 2008-06-01 00:27:42 | 1131278 | Helen    | Speer     | 20296 West 17th Street   | San Francisco       | CA    | 94117   |
|  5000003 | 1274473 |  5000003 | 1153459 | 2008-06-01 00:49:37 | 1153459 | Sandy    | Weinstein | 1155 Fairbanks Road      | Sacramento          | CA    | 94274   |
|  5000003 | 1273673 |  5000003 | 1153459 | 2008-06-01 00:49:37 | 1153459 | Sandy    | Weinstein | 1155 Fairbanks Road      | Sacramento          | CA    | 94274   |
|  5000004 | 1274216 |  5000004 | 1159099 | 2008-06-01 01:05:28 | 1159099 | Kathleen | Coates    | 3243 North 3rd Street    | Mi Wuk Village      | CA    | 95346   |
|  5000004 | 1273748 |  5000004 | 1159099 | 2008-06-01 01:05:28 | 1159099 | Kathleen | Coates    | 3243 North 3rd Street    | Mi Wuk Village      | CA    | 95346   |
|  5000005 | 1274348 |  5000005 | 1020687 | 2008-06-01 01:08:36 | 1020687 | Kristi   | Stevens   | 3755 East 22nd Street    | Oakland             | CA    | 94649   |
|  5000005 | 1273719 |  5000005 | 1020687 | 2008-06-01 01:08:36 | 1020687 | Kristi   | Stevens   | 3755 East 22nd Street    | Oakland             | CA    | 94649   |
|  5000006 | 1274190 |  5000006 | 1187459 | 2008-06-01 01:11:09 | 1187459 | Marie    | Cummings  | 16942 North 25th Street  | Marysville          | OH    | 43041   |
|  5000006 | 1274200 |  5000006 | 1187459 | 2008-06-01 01:11:09 | 1187459 | Marie    | Cummings  | 16942 North 25th Street  | Marysville          | OH    | 43041   |
|  5000007 | 1274157 |  5000007 | 1048773 | 2008-06-01 01:36:35 | 1048773 | William  | Kelsey    | 1796 West Madison Street | Point Reyes Station | CA    | 94956   |
|  5000008 | 1274168 |  5000008 | 1064002 | 2008-06-01 01:36:52 | 1064002 | Marla    | Taylor    | 1003 North Baxter Street | Nipton              | CA    | 92364   |
|  5000008 | 1274164 |  5000008 | 1064002 | 2008-06-01 01:36:52 | 1064002 | Marla    | Taylor    | 1003 North Baxter Street | Nipton              | CA    | 92364   |
|  5000009 | 1274322 |  5000009 | 1096744 | 2008-06-01 01:49:46 | 1096744 | Roscoe   | Colon     | 1434 Howard Road         | Anchorage           | AK    | 99511   |
|  5000009 | 1274265 |  5000009 | 1096744 | 2008-06-01 01:49:46 | 1096744 | Roscoe   | Colon     | 1434 Howard Road         | Anchorage           | AK    | 99511   |
|  5000010 | 1274225 |  5000010 | 1107526 | 2008-06-01 03:07:14 | 1107526 | Diane    | Serra     | 1462 West 12th Street    | Onaga               | KS    | 66521   |
+----------+---------+----------+---------+---------------------+---------+----------+-----------+--------------------------+---------------------+-------+---------+

INSERT INTO econ.fact (Date, Prod_ID, Zip, State, City)
SELECT o.order_date, od.prod_id, c.zipcode, c.state, c.city
FROM dualcore.order_details od 
LEFT JOIN dualcore.orders o 
ON od.order_id = o.order_id
LEFT JOIN customers c
ON o.cust_id = c.cust_id;

ERROR 1062 (23000): Duplicate entry '2008-06-03-1273887-94720' for key 'PRIMARY'

ALTER TABLE fact ADD purch_id INT NOT NULL AUTO_INCREMENT, PRIMARY KEY (purch_id);

CREATE TABLE fact(purch_id INT NOT NULL AUTO_INCREMENT, Date DATE, Prod_Id VARCHAR(20), Zip INT, State VARCHAR(10), City VARCHAR(30), CONSTRAINT PK_Fact PRIMARY KEY (purch_id));


INSERT INTO econ.fact (Date, Prod_ID, Zip, State, City)
SELECT o.order_date, od.prod_id, c.zipcode, c.state, c.city
FROM dualcore.order_details od 
LEFT JOIN dualcore.orders o 
ON od.order_id = o.order_id
LEFT JOIN dualcore.customers c
ON o.cust_id = c.cust_id;
Query OK, 3333244 rows affected, 65535 warnings (21.43 sec)
Records: 3333244  Duplicates: 0  Warnings: 3333194

mysql> SELECT * FROM fact LIMIT 10;
+------------+---------+-------+-------+----------------+----------+
| Date       | Prod_Id | Zip   | State | City           | purch_id |
+------------+---------+-------+-------+----------------+----------+
| 2008-06-01 | 1273719 | 62706 | IL    | Springfield    |      561 |
| 2008-06-01 | 1273767 | 62706 | IL    | Springfield    |      562 |
| 2008-06-01 | 1273779 | 62706 | IL    | Springfield    |      563 |
| 2008-06-01 | 1274124 | 94117 | CA    | San Francisco  |      564 |
| 2008-06-01 | 1273737 | 94117 | CA    | San Francisco  |      565 |
| 2008-06-01 | 1274227 | 94117 | CA    | San Francisco  |      566 |
| 2008-06-01 | 1274473 | 94274 | CA    | Sacramento     |      567 |
| 2008-06-01 | 1273673 | 94274 | CA    | Sacramento     |      568 |
| 2008-06-01 | 1274216 | 95346 | CA    | Mi Wuk Village |      569 |
| 2008-06-01 | 1273748 | 95346 | CA    | Mi Wuk Village |      570 |
+------------+---------+-------+-------+----------------+----------+


SELECT * FROM fact f LEFT JOIN date d ON YEAR(f.Date) = YEAR(d.Date) AND MONTH(f.Date) = MONTH(d.Date) 
LEFT JOIN product p ON p.prod_id = f.Prod_Id
LIMIT 10;
+------------+---------+-------+-------+----------------+----------+------------+-----------+--------------+--------+----------+---------+-------------+-------------------------------------+-------+-------+
| Date       | Prod_Id | Zip   | State | City           | purch_id | Date       | inflation | unemployment | tbill  | natsales | prod_id | brand       | name                                | price | cost  |
+------------+---------+-------+-------+----------------+----------+------------+-----------+--------------+--------+----------+---------+-------------+-------------------------------------+-------+-------+
| 2008-06-01 | 1273719 | 62706 | IL    | Springfield    |      561 | 2008-06-01 |    0.0101 |       0.0560 | 0.0410 |     1625 | 1273719 | Ultramegaco | Screen Cleaning Cloth (gray)        |  1839 |  1672 |
| 2008-06-01 | 1273767 | 62706 | IL    | Springfield    |      562 | 2008-06-01 |    0.0101 |       0.0560 | 0.0410 |     1625 | 1273767 | Megachango  | Rechargeable Batteries (AA, 4 pack) |  3059 |  1777 |
| 2008-06-01 | 1273779 | 62706 | IL    | Springfield    |      563 | 2008-06-01 |    0.0101 |       0.0560 | 0.0410 |     1625 | 1273779 | Gigabux     | Keyboard (basic PC101)              |  2979 |  2208 |
| 2008-06-01 | 1274124 | 94117 | CA    | San Francisco  |      564 | 2008-06-01 |    0.0101 |       0.0560 | 0.0410 |     1625 | 1274124 | Sparky      | 5.25" Drive Bay Adapter             |  1309 |  1297 |
| 2008-06-01 | 1273737 | 94117 | CA    | San Francisco  |      565 | 2008-06-01 |    0.0101 |       0.0560 | 0.0410 |     1625 | 1273737 | DevNull     | Batteries (AA, 2 pack)              |   389 |   248 |
| 2008-06-01 | 1274227 | 94117 | CA    | San Francisco  |      566 | 2008-06-01 |    0.0101 |       0.0560 | 0.0410 |     1625 | 1274227 | Megachango  | Power Supply (500W)                 |  2529 |  2344 |
| 2008-06-01 | 1274473 | 94274 | CA    | Sacramento     |      567 | 2008-06-01 |    0.0101 |       0.0560 | 0.0410 |     1625 | 1274473 | Dualcore    | Wireless N Modem Router             |  9869 |  8785 |
| 2008-06-01 | 1273673 | 94274 | CA    | Sacramento     |      568 | 2008-06-01 |    0.0101 |       0.0560 | 0.0410 |     1625 | 1273673 | Bigdeal     | High Speed HDMI Cable (36 in.)      |  2919 |  1078 |
| 2008-06-01 | 1274216 | 95346 | CA    | Mi Wuk Village |      569 | 2008-06-01 |    0.0101 |       0.0560 | 0.0410 |     1625 | 1274216 | Dualcore    | 3.2GHz CPU                          | 16229 | 14723 |
| 2008-06-01 | 1273748 | 95346 | CA    | Mi Wuk Village |      570 | 2008-06-01 |    0.0101 |       0.0560 | 0.0410 |     1625 | 1273748 | Orion       | Batteries (AAA, 4 pack)             |   749 |   435 |
+------------+---------+-------+-------+----------------+----------+------------+-----------+--------------+--------+----------+---------+-------------+-------------------------------------+-------+-------+

FULL TABLE:
SELECT SUM(p.price) FROM fact f LEFT JOIN date d ON YEAR(f.Date) = YEAR(d.Date) AND MONTH(f.Date) = MONTH(d.Date) 
 LEFT JOIN product p ON p.prod_id = f.Prod_Id
 GROUP BY state
 LIMIT 10;


-- Which 5 states have been the most profitable?
SELECT state, (SUM(p.price) - SUM(p.cost)) profit FROM fact f LEFT JOIN date d ON YEAR(f.Date) = YEAR(d.Date) AND MONTH(f.Date) = MONTH(d.Date)   LEFT JOIN product p ON p.prod_id = f.Prod_Id GROUP BY state ORDER BY profit DESC LIMIT 5;
mysql> SELECT state, (SUM(p.price) - SUM(p.cost)) profit FROM fact f LEFT JOIN date d ON YEAR(f.Date) = YEAR(d.Date) AND MONTH(f.Date) = MONTH(d.Date)   LEFT JOIN product p ON p.prod_id = f.Prod_Id GROUP BY state ORDER BY profit DESC LIMIT 5;
+-------+------------+
| state | profit     |
+-------+------------+
| CA    | 1496888516 |
| IA    |  152305755 |
| MN    |  152022145 |
| IL    |  143999047 |
| KS    |  112145161 |
+-------+------------+

We are interested in economic conditions similar to those of today, so we are most interested in previous times when levels were near the following:

CPI_W: +0.6% in January 2018
		+2.1% since January 2017

Unemployment: 4.1%

TBill: 1.89

E-Retail sales: 
4541	Electronic shopping and mail order houses	
43,590	43,906	44,416	44,815	45,186	45,145	46,137	45,599	46,177	46,286	47,888	47,877

//Create a Report View to answer our business questions
CREATE VIEW trends AS
SELECT * FROM ( (SELECT DISTINCT d.Date FROM date d)  AS
dates CROSS JOIN (SELECT DISTINCT f.Zip, f.State, f.City FROM fact f) AS Locs) 
LEFT JOIN date ON dates.Date = date.Date
LEFT JOIN ProfSales ps ON YEAR(date.Date) = ps.Yr AND MONTH(date.Date) = ps.Mn
LIMIT 20;

SELECT * FROM ( (SELECT DISTINCT d.Date FROM date d)  AS
dates CROSS JOIN (SELECT DISTINCT f.Zip, f.State, f.City FROM fact f) AS Locs) 
LEFT JOIN date ON dates.Date = date.Date

LIMIT 20;

CREATE VIEW ProfSales AS
SELECT Zip, Year(d.Date) Yr, Month(d.Date) Mn, (SUM(p.price)) sales, SUM(p.price - p.cost) profits FROM fact f LEFT JOIN date d ON YEAR(f.Date) = YEAR(d.Date) AND MONTH(f.Date) = MONTH(d.Date)   LEFT JOIN product p ON p.prod_id = f.Prod_Id GROUP BY Zip, Year(Date), Month(Date);

INSERT INTO date 
CREATE TABLE trends(Date DATE, Zip INT, State VARCHAR(10), City VARCHAR(30), inflation DECIMAL(4,4), unemployment DECIMAL(4,4), tbill DECIMAL(4,4), natsales INT, natsales_chg DECIMAL(4,4), dc_sales INT, dc_sales_chg DECIMAL(4,4), dc_profit INT, dc_profit_chg DECIMAL(4,4));

INSERT INTO trends ( Date, Zip, State, City, inflation, unemployment, tbill, natsales )
SELECT dates.Date, Locs.Zip, Locs.State, Locs.City, inflation, unemployment, tbill, natsales FROM ((SELECT DISTINCT d.Date FROM date d)  AS
dates CROSS JOIN (SELECT DISTINCT f.Zip, f.State, f.City FROM fact f) AS Locs) 
LEFT JOIN date ON dates.Date = date.Date;



UPDATE trends, ProfSales
SET trends.dc_sales = ProfSales.sales
WHERE trends.Zip = ProfSales.Zip AND YEAR(trends.Date) = ProfSales.Yr AND MONTH(trends.Date) = ProfSales.Mn;

UPDATE trends, ProfSales
SET trends.dc_profit= ProfSales.profits
WHERE trends.Zip = ProfSales.Zip AND YEAR(trends.Date) = ProfSales.Yr AND MONTH(trends.Date) = ProfSales.Mn;

--add % changes
SELECT *
FROM trends S1 JOIN trends S2
ON S1.Date = (S2.Date+1)
LIMIT 20;

BUSINESS QUESTIONS:
1. Does our sales match the yearly trend of overall electronics sale at the US ? If not, at which years did we perform better or poorer ? This can be drilled down to months

Which years were most profitable?
SELECT YEAR(f.Date), (SUM(p.price) - SUM(p.cost)) profit FROM fact f LEFT JOIN date d ON YEAR(f.Date) = YEAR(d.Date) AND MONTH(f.Date) = MONTH(d.Date) LEFT JOIN product p ON p.prod_id = f.Prod_Id GROUP BY YEAR(f.Date) ORDER BY profit DESC;

+--------------+-----------+
| YEAR(f.Date) | profit    |
+--------------+-----------+
|         2012 | 918017250 |
|         2013 | 901310855 |
|         2011 | 789712634 |
|         2010 | 506276399 |
|         2009 | 213418156 |
|         2008 |  54443767 |
+--------------+-----------+

SELECT o.order_date, od.prod_id
FROM dualcore.order_details od 
LEFT JOIN dualcore.orders o 
ON od.order_id = o.order_id;

What was sales growth for each year over the previous year?

-- sales for each year divided by sales from last year

SELECT YEAR(f.Date), (SUM(p.price)) growth FROM fact f LEFT JOIN date d ON YEAR(f.Date) = YEAR(d.Date) AND MONTH(f.Date) = MONTH(d.Date) LEFT JOIN product p ON p.prod_id = f.Prod_Id GROUP BY YEAR(f.Date) ORDER BY profit DESC;

Sales and percent growth for each month
Date, profit, profit_chg, sales, sales_chg


--export to csv
SELECT *
INTO LOCAL OUTFILE '/tmp/trends1.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
ESCAPED BY '\\'
LINES TERMINATED BY '\n'
FROM trends;

CREATE TABLE econ_pct(Date DATE, dc_sales INT, dc_profits INT, inflation DECIMAL(4,4), unemployment DECIMAL(4,4), tbill DECIMAL(4,4), natsales INT, dc_sales_chg DECIMAL(4,4), dec_profits_chg DECIMAL(4,4), natsales_chg DECIMAL(4,4), CONSTRAINT PK_Fact PRIMARY KEY (Date));

LOAD DATA LOCAL INFILE '/home/mcmillwh/econ_percentages.csv'
INTO TABLE econ_pct
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES;



Create a state-level reporting table
CREATE TABLE state_trends(Date DATE, State VARCHAR(2), dc_sales INT, dc_profits INT, CONSTRAINT PK_st PRIMARY KEY(Date, State));

INSERT INTO state_trends ( Date, State, dc_sales, dc_profits )
SELECT Date, state, SUM(dc_sales), SUM(dc_profit) FROM trends GROUP BY state, Date;


SELECT * 
INTO OUTFILE '/tmp/states.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
ESCAPED BY '\\'
LINES TERMINATED BY '\n'
FROM state_trends s JOIN date d ON s.Date = d.Date;

--Find months with conditions similar to 
CPI_W: +0.6% in January 2018
		+2.1% since January 2017

Unemployment: 4.1%



E-Retail sales: 
4541	Electronic shopping and mail order houses	
43,590	43,906	44,416	44,815	45,186	45,145	46,137	45,599	46,177	46,286	47,888	47,877


Which months had tbill rates within 5% of 1.89?
MariaDB [econ]> SELECT Date, tbill from econ_pct WHERE tbill < 0.0189 * 1.05 AND tbill > 0.0189 * 0.95;
+------------+--------+
| Date       | tbill  |
+------------+--------+
| 2011-09-01 | 0.0197 |
| 2011-12-01 | 0.0197 |
| 2012-01-01 | 0.0197 |
| 2012-02-01 | 0.0197 |
| 2012-05-01 | 0.0180 |
| 2013-01-01 | 0.0191 |
| 2013-02-01 | 0.0198 |
| 2013-03-01 | 0.0196 |
| 2013-05-01 | 0.0194 |
+------------+--------+

Which states had the best sales during these months overall?
SELECT *
FROM state_trends 
WHERE (Date = '2011-09-01' OR Date = '2011-12-01' OR Date = '2012-01-01' OR Date = '2012-02-01' OR Date = '2012-05-01' OR Date = '2013-01-01' OR Date = '2013-02-01' OR Date = '2013-03-01' OR Date = '2013-05-01')
GROUP BY dc_sales DESC LIMIT 10;

| Date       | State | dc_sales  | dc_profits |
+------------+-------+-----------+------------+
| 2013-05-01 | CA    | 989412761 |   59265807 |
| 2013-03-01 | CA    | 538690951 |   66930768 |
| 2013-02-01 | CA    | 497833458 |   62317205 |
| 2013-01-01 | CA    | 477849660 |   59354733 |
| 2012-05-01 | CA    | 392373943 |   47131825 |
| 2012-01-01 | CA    | 341960668 |   41789620 |
| 2012-02-01 | CA    | 339380258 |   41161586 |
| 2011-12-01 | CA    | 300047341 |   36865780 |
| 2011-09-01 | CA    | 295484485 |   35496563 |
| 2013-05-01 | IL    | 202058070 |   11959346 |

Which states had the worst performance during these months?
SELECT *
FROM state_trends 
WHERE (Date = '2011-09-01' OR Date = '2011-12-01' OR Date = '2012-01-01' OR Date = '2012-02-01' OR Date = '2012-05-01' OR Date = '2013-01-01' OR Date = '2013-02-01' OR Date = '2013-03-01' OR Date = '2013-05-01')
GROUP BY dc_sales ASC LIMIT 10;

 Date       | State | dc_sales | dc_profits |
+------------+-------+----------+------------+
| 2011-09-01 | RI    |    20572 |       4845 |
| 2011-12-01 | DE    |    72553 |      11543 |
| 2011-12-01 | RI    |    87393 |       7626 |
| 2012-05-01 | RI    |    94057 |      13499 |
| 2011-09-01 | DE    |   116250 |      17617 |
| 2012-05-01 | DE    |   136667 |      19145 |
| 2013-01-01 | RI    |   144714 |      19685 |
| 2012-01-01 | DE    |   153545 |      16936 |
| 2012-02-01 | RI    |   157345 |      13106 |
| 2011-09-01 | DC    |   183534 |      22173 |
+------------+-------+----------+------------+




