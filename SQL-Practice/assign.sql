--Question 10

SELECT DISTINCT orders.cid
FROM orders, olines
WHERE orders.oid = olines.oid AND orders.odate >= datetime('now', '-7 days')
EXCEPT
SELECT DISTINCT orders.cid
FROM orders, olines
WHERE orders.oid = olines.oid AND orders.odate >= datetime('now', '-7 days')
AND NOT EXISTS (SELECT * FROM goodprice WHERE olines.sid = goodprice.sid AND olines.pid = goodprice.pid);


SELECT orders.cid, orders.odate, olines.sid, olines.pid
FROM orders, olines
WHERE orders.oid = olines.oid AND orders.odate >= datetime('now', '-7 days');

--Question 9
DROP VIEW if exists goodprice;
CREATE VIEW goodprice( pid, sid, name, qty, uprice)
AS SELECT carries.pid, carries.sid, stores.name, carries.qty, carries.uprice
FROM carries,stores, (SELECT pid, MIN(uprice) AS minPrice
FROM carries
WHERE qty > 0
GROUP BY pid) Data
WHERE carries.pid = Data.pid AND carries.uprice = Data.minPrice AND carries.qty >0 AND carries.sid=stores.sid;


SELECT carries.pid, carries.sid, carries.qty, carries.uprice
FROM carries, (SELECT pid, MIN(uprice) AS minPrice
FROM carries
WHERE qty > 0
GROUP BY pid) Data
WHERE carries.pid = Data.pid AND carries.uprice = Data.minPrice AND carries.qty > 0;


SELECT pid, MIN(uprice)
FROM carries
WHERE qty > 0
GROUP BY pid;



--Question 8
SELECT orders.cid, olines.sid
FROM orders, olines
WHERE orders.oid = olines.oid;

SELECT DISTINCT orders.cid, olines.sid
FROM orders, olines
WHERE orders.oid = olines.oid;

SELECT Data.c, COUNT(*)
FROM (SELECT DISTINCT orders.cid AS c, olines.sid
FROM orders, olines
WHERE orders.oid = olines.oid) Data
GROUP BY Data.c


SELECT Data.c
FROM (SELECT DISTINCT orders.cid AS c, olines.sid
FROM orders, olines
WHERE orders.oid = olines.oid) Data
GROUP BY Data.c
HAVING COUNT(*) = 1
except
SELECT orders.cid
FROM orders,stores,olines
WHERE stores.sid=olines.sid AND orders.oid=olines.oid AND stores.name="Walmart";

--Question 7

select products.pid, products.name, COUNT(DISTINCT carries.sid)
FROM olines,products,carries
WHERE olines.pid=carries.pid AND olines.pid=products.pid
GROUP by olines.pid
ORDER BY COUNT(olines.oid) DESC
LIMIT 5;


select pid, COUNT(sid) as c
FROM carries
GROUP by pid
ORDER BY c DESC
LIMIT 5;

select pid, COUNT(oid) as c
FROM carries
GROUP by pid
ORDER BY c DESC


select pid, COUNT(olines.oid) as c
FROM olines
GROUP by pid
ORDER BY c DESC
LIMIT 5;


-- MY SOLUTION
SELECT carries.pid, products.name, COUNT(*)
FROM carries, products
WHERE carries.pid in (select pid
FROM olines
GROUP by pid
ORDER BY COUNT(olines.oid) DESC
LIMIT 5) AND carries.pid = products.pid
GROUP BY carries.pid;


--Question 6




SELECT products.cat, COUNT(DISTINCT carries.sid)
FROM products, carries
WHERE carries.pid = products.pid
GROUP BY products.cat;


SELECT carries.sid, products.cat
FROM products, carries
WHERE carries.pid = products.pid;

SELECT ProductData.c, COUNT(*)
FROM (SELECT categories.cat AS c, products.pid
FROM categories
LEFT JOIN products ON categories.cat = products.cat) ProductData
GROUP BY ProductData.c;


SELECT products.cat, COUNT(products.pid)
FROM products
GROUP BY products.cat;

SELECT categories.cat, COUNT(products.pid)
FROM categories, products
WHERE categories.cat = products.cat
GROUP BY products.cat;


SELECT categories.cat, products.pid
FROM categories
LEFT JOIN products ON categories.cat = products.cat;




SELECT categories.cat,COUNT(DISTINCT products.name),COUNT(DISTINCT carries.sid),COUNT(DISTINCT oid)
FROM products, categories
LEFT OUTER JOIN olines using (pid)
LEFT OUTER JOIN carries using (pid)
WHERE categories.cat=products.cat
GROUP BY categories.cat;


--Question 5

SELECT orders.cid, COUNT(orders.oid)
FROM orders
GROUP BY orders.cid;


SELECT orders.cid,  olines.sid, COUNT(DISTINCT orders.oid)
FROM orders, olines
WHERE orders.oid = olines.oid
GROUP BY orders.cid, olines.sid;




SELECT orders.cid,  olines.sid, COUNT(DISTINCT orders.oid), Data.cou
FROM orders, olines, (SELECT orders.cid AS ci, COUNT(orders.oid) AS cou
FROM orders
GROUP BY orders.cid) Data
WHERE orders.oid = olines.oid AND orders.cid = Data.ci
GROUP BY orders.cid, olines.sid
HAVING COUNT(DISTINCT orders.oid) >= Data.cou * 0.5;


SELECT orders.cid,  olines.sid
FROM orders, olines, (SELECT orders.cid AS ci, COUNT(orders.oid) AS cou
FROM orders
GROUP BY orders.cid) Data
WHERE orders.oid = olines.oid AND orders.cid = Data.ci
GROUP BY orders.cid, olines.sid
HAVING COUNT(DISTINCT orders.oid) >= Data.cou * 0.5;



SELECT DISTINCT orders.cid, orders.oid, olines.sid
FROM orders, olines
WHERE orders.oid = olines.oid;


SELECT orders.cid, orders.oid, olines.sid
FROM orders, olines
WHERE orders.oid = olines.oid;




SELECT DISTINCT cid, sid
FROM olines, orders
WHERE olines.oid = orders.oid AND sid IN
(SELECT sid
FROM (SELECT cid, sid
FROM olines, orders
WHERE olines.oid = orders.oid) Data
GROUP BY sid
HAVING COUNT(DISTINCT cid) >= 0.5 * (SELECT COUNT(cid) FROM customers));


SELECT DISTINCT cid, sid
FROM olines, orders
WHERE olines.oid = orders.oid AND sid IN
(SELECT sid
FROM (SELECT cid, sid
FROM olines, orders
WHERE olines.oid = orders.oid) Data
GROUP BY sid);



SELECT sid, COUNT(DISTINCT cid)
FROM (SELECT cid, sid
FROM olines, orders
WHERE olines.oid = orders.oid) Data
GROUP BY sid
HAVING COUNT(DISTINCT cid) >= 0.5 * (SELECT COUNT(cid) FROM customers);



SELECT sid, COUNT(cid)
FROM (SELECT cid, sid
FROM olines, orders
WHERE olines.oid = orders.oid) Data
GROUP BY sid
HAVING COUNT(cid) > 2;

SELECT sid, COUNT(DISTINCT cid)
FROM (SELECT cid, sid
FROM olines, orders
WHERE olines.oid = orders.oid) Data
GROUP BY sid
HAVING COUNT(DISTINCT cid) > 2;

SELECT cid, sid
FROM olines, orders
WHERE olines.oid = orders.oid;


SELECT sid, COUNT(DISTINCT oid)
FROM olines
GROUP BY sid
HAVING COUNT(DISTINCT oid) > 2;

SELECT COUNT(DISTINCT cid)
FROM orders;

SELECT COUNT(cid)
FROM customers;


--Question 4
SELECT sid, COUNT(*)
FROM carries
WHERE pid IN (SELECT pid
FROM carries
GROUP BY pid
HAVING COUNT(sid) = 1)
GROUP BY sid;

-- SELECT pid
-- FROM carries
-- GROUP BY pid
-- HAVING COUNT(sid) = 1;

-- SELECT pid, COUNT(sid)
-- FROM carries
-- GROUP BY pid;


--Question 3
SELECT trackingno
FROM deliveries, customers, orders
WHERE customers.name = 'John Doe' AND customers.cid = orders.cid 
AND orders.oid = deliveries.oid AND dropOffTime IS NULL AND date('now') = deliveries.pickUpTime;


--Question 2
SELECT DISTINCT o1.oid
FROM olines o1, olines o2, categories c1, categories c2, products p1, products p2
WHERE o1.oid = o2.oid AND o1.sid <> o2.sid AND c1.name = 'Dairy' AND p1.cat = c1.cat AND o1.pid = p1.pid
AND c2.name = 'Dairy' AND p2.cat = c2.cat AND o2.pid = p2.pid;

--Question 1
SELECT cid
FROM customers
EXCEPT
SELECT DISTINCT orders.cid
FROM orders, olines, products, categories
WHERE orders.oid = olines.oid AND categories.name = 'Dairy' AND products.cat = categories.cat AND olines.pid = products.pid;

--Question 1

SELECT pid
FROM products, categories
WHERE categories.name = 'Dairy' AND products.cat = categories.cat;
--find cid of product from the dairy categories
SELECT orders.cid, olines.pid
FROM orders, olines
WHERE orders.oid = olines.oid;
--find cid and pid

SELECT orders.cid, olines.pid
FROM orders, olines
WHERE orders.oid = olines.oid AND olines.pid IN (SELECT pid
FROM products, categories
WHERE categories.name = 'Dairy' AND products.cat = categories.cat);


SELECT DISTINCT orders.cid
FROM orders, olines
WHERE orders.oid = olines.oid AND olines.pid IN (SELECT pid
FROM products, categories
WHERE categories.name = 'Dairy' AND products.cat = categories.cat);


SELECT cid
FROM customers
EXCEPT
SELECT DISTINCT orders.cid
FROM orders, olines
WHERE orders.oid = olines.oid AND olines.pid IN (SELECT pid
FROM products, categories
WHERE categories.name = 'Dairy' AND products.cat = categories.cat);
