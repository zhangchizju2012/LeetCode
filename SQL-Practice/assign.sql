
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
