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



Which months had similar unemployment?
SELECT Date, unemployment from econ_pct WHERE unemployment < 0.041 * 1.05 AND unemployment > 0.041 * 0.95;
None. We had to compute the % change over the 12-month moving average to compare changes in unemployment.
See the Jupyter notebook.
2010-03-01

Which products have sold the most?
SELECT p.name, SUM(p.price) AS sales, SUM(p.cost) AS cost, SUM(p.price-p.cost) AS profits FROM fact f LEFT JOIN product p ON f.prod_id = p.prod_id
GROUP BY p.name ORDER BY sales DESC;
Tablet PC (10 in. display, 64 GB)                                  | 4902069145 | 4851254985 |  50814160 |
| 173 GB SAS Disk                                                    |  818620025 |  712633114 | 105986911 |
| VPN Appliance (250 Clienti license)                                |  806135927 |  656986577 | 149149350 |
| Server (1U rackmount, hex-core, 16GB, 8TB)                         |  768481065 |  619406670 | 149074395 |
| Basic Desktop                                                      |  700655080 |  643103842 |  57551238

Which products have been the most profitable?
SELECT p.name, SUM(p.price) AS sales, SUM(p.cost) AS cost, SUM(p.price-p.cost) AS profits FROM fact f LEFT JOIN product p ON f.prod_id = p.prod_id
GROUP BY p.name ORDER BY profits DESC;

VPN Appliance (250 Clienti license)                                |  806135927 |  656986577 | 149149350 |
| Server (1U rackmount, hex-core, 16GB, 8TB)                         |  768481065 |  619406670 | 149074395 |
| 173 GB SAS Disk                                                    |  818620025 |  712633114 | 105986911 |
| Scanner                                                            |  459446737 |  370731095 |  88715642 |
| VPN Appliance (50 Clienti license)                                 |  689302223 |  628122638 |  61179585 |

Our consumer-grade tech (like tablets) seems to be far less profitable than professional grade equipment (VPN Appliances).

What about during our given economic conditions?
SELECT p.name, SUM(p.price) AS sales, SUM(p.cost) AS cost, SUM(p.price-p.cost) AS profits FROM fact f LEFT JOIN product p ON f.prod_id = p.prod_id
WHERE f.Date = '2010-03-01'
GROUP BY p.name ORDER BY profits DESC
LIMIT 5;

VPN Appliance (250 Clienti license)                                | 685927 | 557001 |  128926 |
| Tablet PC (10 in. display, 64 GB)                                  | 543566 | 535082 |    8484 |
| Server (1U rackmount, hex-core, 16GB, 8TB)                         | 470019 | 378842 |   91177 |
| 173 GB SAS Disk                                                    | 292624 | 249786 |   42838 |
| Scanner                                                            | 279870 | 223959 |   55911 |

Most profitable products during times with similar change in inflation:
+--------------------------------------------+--------+--------+---------+
| name                                       | sales  | cost   | profits |
+--------------------------------------------+--------+--------+---------+
| VPN Appliance (250 Clienti license)        | 685927 | 557001 |  128926 |
| Server (1U rackmount, hex-core, 16GB, 8TB) | 470019 | 378842 |   91177 |
| Scanner                                    | 279870 | 223959 |   55911 |
| 173 GB SAS Disk                            | 292624 | 249786 |   42838 |
| VPN Appliance (50 Clienti license)         | 196416 | 172258 |   24158 |
+--------------------------------------------+--------+--------+---------+

What about for tbill rates?
SELECT p.name, SUM(p.price) AS sales, SUM(p.cost) AS cost, SUM(p.price-p.cost) AS profits FROM fact f LEFT JOIN product p ON f.prod_id = p.prod_id
WHERE (f.Date = '2011-09-01' OR f.Date = '2011-12-01' OR f.Date = '2012-01-01' OR f.Date = '2012-02-01' OR f.Date = '2012-05-01' OR f.Date = '2013-01-01' OR f.Date = '2013-02-01' OR f.Date = '2013-03-01' OR f.Date = '2013-05-01')
GROUP BY p.name ORDER BY sales DESC;

Tablet PC (10 in. display, 64 GB)                                  | 47361352 | 46937004 |  424348 |
| Server (1U rackmount, hex-core, 16GB, 8TB)                         |  7520304 |  6061472 | 1458832 |
| 173 GB SAS Disk                                                    |  5893579 |  5102588 |  790991 |
| Premium Gamer Desktop                                              |  5685636 |  5631736 |   53900 |
| Basic Desktop                                                      |  5673546 |  5273212 |  400334 |

Most profitable products during times with similar tbill rates
SELECT p.name, SUM(p.price) AS sales, SUM(p.cost) AS cost, SUM(p.price-p.cost) AS profits FROM fact f LEFT JOIN product p ON f.prod_id = p.prod_id
WHERE (f.Date = '2011-09-01' OR f.Date = '2011-12-01' OR f.Date = '2012-01-01' OR f.Date = '2012-02-01' OR f.Date = '2012-05-01' OR f.Date = '2013-01-01' OR f.Date = '2013-02-01' OR f.Date = '2013-03-01' OR f.Date = '2013-05-01')
GROUP BY p.name ORDER BY profits DESC
LIMIT 5;

| name                                       | sales   | cost    | profits |
+--------------------------------------------+---------+---------+---------+
| Server (1U rackmount, hex-core, 16GB, 8TB) | 7520304 | 6061472 | 1458832 |
| VPN Appliance (250 Clienti license)        | 4578340 | 3738508 |  839832 |
| 173 GB SAS Disk                            | 5893579 | 5102588 |  790991 |
| Scanner                                    | 3614481 | 2911039 |  703442 |
| VPN Appliance (50 Clienti license)         | 5530738 | 5035792 |  494946 |
+--------------------------------------------+---------+---------+---------+

SELECT p.name, SUM(p.price) AS sales, SUM(p.cost) AS cost, SUM(p.price-p.cost) AS profits FROM fact f LEFT JOIN product p ON f.prod_id = p.prod_id
WHERE f.Date = '2010-03-01' AND f.state = 'CA'
GROUP BY p.name ORDER BY profits DESC
LIMIT 5;

+-------------------------------------+--------+--------+---------+
| name                                | sales  | cost   | profits |
+-------------------------------------+--------+--------+---------+
| VPN Appliance (250 Clienti license) | 458658 | 377626 |   81032 |
| 173 GB SAS Disk                     | 195206 | 163704 |   31502 |
| Scanner                             | 111606 |  90061 |   21545 |
| Camcorder (Digital)                 |  86618 |  72852 |   13766 |
| Extension cord (20 ft., outdoor)    |  29864 |  18037 |   11827 |
+-------------------------------------+--------+--------+---------+

SELECT p.name, SUM(p.price) AS sales, SUM(p.cost) AS cost, SUM(p.price-p.cost) AS profits FROM fact f LEFT JOIN product p ON f.prod_id = p.prod_id
WHERE f.Date = '2010-03-01' AND f.state = 'IA'
GROUP BY p.name ORDER BY profits DESC
LIMIT 5;

+--------------------------------------------+--------+--------+---------+
| name                                       | sales  | cost   | profits |
+--------------------------------------------+--------+--------+---------+
| Server (1U rackmount, hex-core, 16GB, 8TB) | 470019 | 378842 |   91177 |
| VPN Appliance (50 Clienti license)         |  50159 |  40551 |    9608 |
| Scanner                                    |  27549 |  21920 |    5629 |
| Keyboard (wireless, with nub)              |  13709 |   8518 |    5191 |
| Firewall                                   |  28039 |  23650 |    4389 |
+--------------------------------------------+--------+--------+---------+

SELECT p.name, SUM(p.price) AS sales, SUM(p.cost) AS cost, SUM(p.price-p.cost) AS profits FROM fact f LEFT JOIN product p ON f.prod_id = p.prod_id
WHERE f.Date = '2010-03-01' AND f.state = 'MN'
GROUP BY p.name ORDER BY profits DESC
LIMIT 5;

+-------------------------------------+--------+--------+---------+
| name                                | sales  | cost   | profits |
+-------------------------------------+--------+--------+---------+
| VPN Appliance (250 Clienti license) | 227269 | 179375 |   47894 |
| 128 GB SSD Disk                     |  38689 |  32068 |    6621 |
| Scanner                             |  28309 |  21912 |    6397 |
| F Jack Male-to-Male Cable (60 in.)  |   7527 |   3193 |    4334 |
| 42" Wide Screen TV                  |  55169 |  52343 |    2826 |
+-------------------------------------+--------+--------+---------+

SELECT p.name, SUM(p.price) AS sales, SUM(p.cost) AS cost, SUM(p.price-p.cost) AS profits FROM fact f LEFT JOIN product p ON f.prod_id = p.prod_id
WHERE f.Date = '2010-03-01' AND f.state = 'IL'
GROUP BY p.name ORDER BY profits DESC
LIMIT 5;

+-----------------------------------+-------+-------+---------+
| name                              | sales | cost  | profits |
+-----------------------------------+-------+-------+---------+
| Tablet PC (7 in. display, 16 GB)  | 35019 | 30769 |    4250 |
| Server Motherboard                | 54238 | 50761 |    3477 |
| 64 GB SSD Disk                    | 21929 | 18968 |    2961 |
| Network Switch (Gigabit, 24-port) | 12729 | 10446 |    2283 |
| 1.0 TB SATA3 Disk                 | 10509 |  8230 |    2279 |
+-----------------------------------+-------+-------+---------+

SELECT p.name, SUM(p.price) AS sales, SUM(p.cost) AS cost, SUM(p.price-p.cost) AS profits FROM fact f LEFT JOIN product p ON f.prod_id = p.prod_id
WHERE f.Date = '2010-03-01' AND f.state = 'KS'
GROUP BY p.name ORDER BY profits DESC
LIMIT 5;

+--------------------------------------+-------+-------+---------+
| name                                 | sales | cost  | profits |
+--------------------------------------+-------+-------+---------+
| VPN Appliance (50 Clienti license)   | 50159 | 40551 |    9608 |
| Cable Modem                          | 13468 | 11371 |    2097 |
| MP3 Player (8 GB internal memory)    |  9739 |  7825 |    1914 |
| Rechargeable Batteries (AAA, 4 pack) |  2959 |  1179 |    1780 |
| Network Switch (Gigabit, 8-port)     |  6639 |  5125 |    1514 |
+--------------------------------------+-------+-------+---------+


SELECT p.name, SUM(p.price) AS sales, SUM(p.cost) AS cost, SUM(p.price-p.cost) AS profits FROM fact f LEFT JOIN product p ON f.prod_id = p.prod_id
WHERE f.Date = '2010-03-01' AND f.state = 'MA'
GROUP BY p.name ORDER BY profits DESC
LIMIT 5;

+--------------------+-------+-------+---------+
| name               | sales | cost  | profits |
+--------------------+-------+-------+---------+
| Basic Desktop      | 43929 | 37232 |    6697 |
| XTREME Motherboard | 17789 | 16451 |    1338 |
+--------------------+-------+-------+---------+

SELECT p.name, SUM(p.price) AS sales, SUM(p.cost) AS cost, SUM(p.price-p.cost) AS profits FROM fact f LEFT JOIN product p ON f.prod_id = p.prod_id
WHERE f.Date = '2010-03-01' AND f.state = 'NY'
GROUP BY p.name ORDER BY profits DESC
LIMIT 5;

+------------------------------+-------+-------+---------+
| name                         | sales | cost  | profits |
+------------------------------+-------+-------+---------+
| Wireless N Modem Router      | 10309 |  9062 |    1247 |
| Office Suite (Basic Edition) | 33989 | 33012 |     977 |
| Composite AV Cable (24 in.)  |  2419 |  1555 |     864 |
| Basic Desktop                | 61989 | 61174 |     815 |
| Cable Modem                  |  6829 |  6286 |     543 |
+------------------------------+-------+-------+---------+

SELECT p.name, SUM(p.price) AS sales, SUM(p.cost) AS cost, SUM(p.price-p.cost) AS profits FROM fact f LEFT JOIN product p ON f.prod_id = p.prod_id
WHERE f.Date = '2010-03-01' AND f.state = 'VA'
GROUP BY p.name ORDER BY profits DESC
LIMIT 5;

+-----------------------------------------+-------+-------+---------+
| name                                    | sales | cost  | profits |
+-----------------------------------------+-------+-------+---------+
| Multimedia Headset                      |  5519 |  3559 |    1960 |
| Stereo Component Streaming Media Player | 17969 | 16013 |    1956 |
| Extension cord (10 ft., outdoor)        |  4219 |  2611 |    1608 |
| Amplified Multimedia Speakers           |  8799 |  8412 |     387 |
| Batteries (9V, 1 pack)                  |   629 |   444 |     185 |
+-----------------------------------------+-------+-------+---------+

SELECT p.name, SUM(p.price) AS sales, SUM(p.cost) AS cost, SUM(p.price-p.cost) AS profits FROM fact f LEFT JOIN product p ON f.prod_id = p.prod_id
WHERE f.Date = '2010-03-01' AND f.state = 'NC'
GROUP BY p.name ORDER BY profits DESC
LIMIT 5;

empty set

SELECT p.name, SUM(p.price) AS sales, SUM(p.cost) AS cost, SUM(p.price-p.cost) AS profits FROM fact f LEFT JOIN product p ON f.prod_id = p.prod_id
WHERE f.Date = '2010-03-01' AND f.state = 'FL'
GROUP BY p.name ORDER BY profits DESC
LIMIT 5;

+-------------------------------------+-------+-------+---------+
| name                                | sales | cost  | profits |
+-------------------------------------+-------+-------+---------+
| 128 GB SSD Disk                     | 38689 | 32068 |    6621 |
| Compact Charger                     |  3949 |  2684 |    1265 |
| Extension cord (36 in., heavy duty) |  2849 |  1586 |    1263 |
| F Jack Male-to-Male Cable (36 in.)  |  1949 |  1027 |     922 |
| Wireless N USB Adapter              |  6629 |  5709 |     920 |
+-------------------------------------+-------+-------+---------+

## Dualcore sales and profits were very low for two of these months, but we had significant growth for two others. Which states performed best during these months? 
* For all of the months, the order of top performers and under performers stayed pretty much the same across states. Do our top performers buy different products during tougher eocnomic conditions?

SELECT p.name, SUM(p.price) AS sales, SUM(p.cost) AS cost, SUM(p.price-p.cost) AS profits FROM fact f LEFT JOIN product p ON f.prod_id = p.prod_id
WHERE f.Date = '2010-03-01' AND f.state = 'PA'
GROUP BY p.name ORDER BY profits DESC
LIMIT 5;

Which brands have been the most and least profitable?
SELECT p.brand, SUM(p.price) AS sales, SUM(p.cost) AS cost, SUM(p.price-p.cost) AS profits FROM fact f LEFT JOIN product p ON f.prod_id = p.prod_id
GROUP BY p.brand ORDER BY profits DESC
WHERE f.Date = '2011-06-01'
LIMIT 5;

SELECT p.brand, SUM(p.price) AS sales, SUM(p.cost) AS cost, SUM(p.price-p.cost) AS profits FROM fact f LEFT JOIN product p ON f.prod_id = p.prod_id GROUP BY p.brand ORDER BY profits DESC LIMIT 20;
+------------------+------------+------------+-----------+
| brand            | sales      | cost       | profits   |
+------------------+------------+------------+-----------+
| Megachango       | 1125690980 |  895805537 | 229885443 |
| Orion            | 1842070780 | 1613349084 | 228721696 |
| Dualcore         | 1658101980 | 1468933147 | 189168833 |
| Sparky           | 1200239340 | 1022113131 | 178126209 |
| ACME             | 1333104119 | 1173483802 | 159620317 |
| ElCheapo         | 1082462656 |  935746682 | 146715974 |
| Duff             |  771428774 |  627318500 | 144110274 |
| Foocorp          |  794003847 |  653123707 | 140880140 |
| Ultramegaco      |  738348052 |  604207316 | 134140736 |
| DevNull          |  735961449 |  619982130 | 115979319 |
| United Digistuff |  937368767 |  830539082 | 106829685 |
| McDowell         |  424875153 |  320430287 | 104444866 |
| Tyrell           |  470325146 |  369509408 | 100815738 |
| Krustybitz       |  700500020 |  601166198 |  99333822 |
| TPS              |  864764333 |  768906996 |  95857337 |
| Chestnut         |  251806265 |  156810264 |  94996001 |
| XYZ              |  746236266 |  651337461 |  94898805 |
| Lemmon           | 1004100761 |  914458812 |  89641949 |
| BuckLogix        |  690942923 |  603500106 |  87442817 |
| Bigdeal          |  312289847 |  235225677 |  77064170 |
+------------------+------------+------------+-----------+
SELECT p.brand, SUM(p.price) AS sales, SUM(p.cost) AS cost, SUM(p.price-p.cost) AS profits FROM fact f LEFT JOIN product p ON f.prod_id = p.prod_id GROUP BY p.brand ORDER BY profits ASC LIMIT 20;

SELECT p.brand, SUM(p.price) AS sales, SUM(p.cost) AS cost, SUM(p.price-p.cost) AS profits FROM fact f LEFT JOIN product p ON f.prod_id = p.prod_id GROUP BY p.brand ORDER BY profits ASC LIMIT 20;
+----------------+------------+------------+----------+
| brand          | sales      | cost       | profits  |
+----------------+------------+------------+----------+
| Weebits        |   20557389 |   19327232 |  1230157 |
| Byteweasel     | 4893541781 | 4889903802 |  3637979 |
| Artie          |   57399240 |   49926981 |  7472259 |
| Bytefortress   |   21142431 |   13101417 |  8041014 |
| Weisenheimer   |  159628496 |  151317563 |  8310933 |
| Whiteacre      |   41369370 |   32376743 |  8992627 |
| Texi           |  164874369 |  154608578 | 10265791 |
| Overtop        |  210058956 |  197915184 | 12143772 |
| SuperGamer     |  228908615 |  206968059 | 21940556 |
| Bitmonkey      |  264143802 |  238749918 | 25393884 |
| ARCAM          |  155932110 |  126115858 | 29816252 |
| Terrapin Sands |  161601222 |  130435560 | 31165662 |
| Gigabux        |  132352712 |   99361462 | 32991250 |
| Chatter Audio  |  250694606 |  217347070 | 33347536 |
| Spindown       |  192218608 |  158560026 | 33658582 |
| Sprite         |  131766321 |   93174851 | 38591470 |
| Wernham        |  294592612 |  255434039 | 39158573 |
| BDT            |  384232490 |  344863543 | 39368947 |
| Electrosaurus  |  563365208 |  522179115 | 41186093 |
| Tortoise       |  302604531 |  259472733 | 43131798 |
+----------------+------------+------------+----------+

SELECT p.brand, SUM(p.price) AS sales, SUM(p.cost) AS cost, SUM(p.price-p.cost) AS profits FROM fact f LEFT JOIN product p ON f.prod_id = p.prod_id
WHERE f.Date = '2011-06-01'
GROUP BY p.brand ORDER BY profits DESC
LIMIT 5;

+------------+--------+--------+---------+
| brand      | sales  | cost   | profits |
+------------+--------+--------+---------+
| Orion      | 942912 | 803179 |  139733 |
| Megachango | 750005 | 613528 |  136477 |
| Foocorp    | 717342 | 591345 |  125997 |
| Dualcore   | 848570 | 731605 |  116965 |
| Sparky     | 796204 | 680956 |  115248 |
+------------+--------+--------+---------+

SELECT p.brand, SUM(p.price) AS sales, SUM(p.cost) AS cost, SUM(p.price-p.cost) AS profits FROM fact f LEFT JOIN product p ON f.prod_id = p.prod_id
WHERE f.Date = '2010-03-01'
GROUP BY p.brand ORDER BY profits DESC
LIMIT 5;
+------------+--------+--------+---------+
| brand      | sales  | cost   | profits |
+------------+--------+--------+---------+
| Sparky     | 539666 | 442549 |   97117 |
| Foocorp    | 524692 | 430225 |   94467 |
| Orion      | 480989 | 420405 |   60584 |
| BuckLogix  | 354546 | 295235 |   59311 |
| Megachango | 290776 | 239773 |   51003 |
+------------+--------+--------+---------+

SELECT p.brand, SUM(p.price) AS sales, SUM(p.cost) AS cost, SUM(p.price-p.cost) AS profits FROM fact f LEFT JOIN product p ON f.prod_id = p.prod_id
WHERE f.Date = '2008-07-01'
GROUP BY p.brand ORDER BY profits DESC
LIMIT 5;

SELECT p.brand, SUM(p.price) AS sales, SUM(p.cost) AS cost, SUM(p.price-p.cost) AS profits FROM fact f LEFT JOIN product p ON f.prod_id = p.prod_id
WHERE f.Date = '2011-06-01' AND f.state = 'PA'
GROUP BY p.brand ORDER BY profits DESC
LIMIT 5;

+---------------+-------+-------+---------+
| brand         | sales | cost  | profits |
+---------------+-------+-------+---------+
| Olde-Gray     | 62469 | 59514 |    2955 |
| Chatter Audio | 17999 | 15463 |    2536 |
| McDowell      |  1739 |  1325 |     414 |
| Dorx          |  2879 |  2545 |     334 |
+---------------+-------+-------+---------+

CREATE VIEW brands_VW AS
SELECT f.Date, p.brand, SUM(p.price) AS sales, SUM(p.cost) AS cost, SUM(p.price-p.cost) AS profits FROM fact f LEFT JOIN product p ON f.prod_id = p.prod_id
GROUP BY p.brand, f.Date;

SELECT *
INTO OUTFILE '/tmp/brands.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
ESCAPED BY '\\'
LINES TERMINATED BY '\n'
FROM brands_VW;

Which ZIP codes in underperforming states have been most profitable?

SELECT f.state, f.zip, (SUM(p.price) - SUM(p.cost)) profit 
FROM fact f LEFT JOIN date d ON YEAR(f.Date) = YEAR(d.Date) AND MONTH(f.Date) = MONTH(d.Date) LEFT JOIN product p ON p.prod_id = f.Prod_Id 
WHERE d.Date = '2011-06-01' AND f.state in ('FL','GA','NC', 'VA', 'PA', 'OH', 'NY', 'NJ', 'MA')
GROUP BY zip ORDER BY profit DESC LIMIT 5;

Which cities in underperforming states have been most profitable?

SELECT f.state, f.city, (SUM(p.price) - SUM(p.cost)) profit 
FROM fact f LEFT JOIN date d ON YEAR(f.Date) = YEAR(d.Date) AND MONTH(f.Date) = MONTH(d.Date) LEFT JOIN product p ON p.prod_id = f.Prod_Id 
WHERE d.Date = '2010-03-01' AND f.state in ('FL','GA','NC', 'VA', 'PA', 'OH', 'NY', 'NJ', 'MA')
GROUP BY city ORDER BY profit DESC LIMIT 5;

