-- Student and Department

SELECT Departments.DEPT_NAME, IFNULL(Data.number, 0) AS number
FROM Departments, 
LEFT JOIN (SELECT DEPT_ID, COUNT(STUDENT_ID) AS number
FROM Students
GROUP BY DEPT_ID) Data
ON Departments.DEPT_ID = Data.DEPT_ID
ORDER BY number DESC, Departments.DEPT_NAME ASC

-- Investments in 2016
-- 会导致重复，存在几个b就存在几个重复
SELECT a.TIV_2016, a.PID, b.PID
FROM insurance a, insurance b
WHERE (a.PID <> b.PID AND a.TIV_2015 = b.TIV_2015) 
	AND NOT EXISTS 
		(SELECT * FROM insurance c WHERE a.PID <> c.PID AND a.LAT = c.LAT AND a.LON = c.LON)

SELECT a.TIV_2016
FROM insurance a
WHERE EXISTS
		(SELECT * FROM insurance b WHERE a.PID <> b.PID AND a.TIV_2015 = b.TIV_2015)
	AND NOT EXISTS 
		(SELECT * FROM insurance c WHERE a.PID <> c.PID AND a.LAT = c.LAT AND a.LON = c.LON


# select 这一行可以看成是最后处理的
SELECT SUM(a.TIV_2016) AS TIV_2016
FROM insurance a
WHERE EXISTS
		(SELECT * FROM insurance b WHERE a.PID <> b.PID AND a.TIV_2015 = b.TIV_2015)
	AND NOT EXISTS 
		(SELECT * FROM insurance c WHERE a.PID <> c.PID AND a.LAT = c.LAT AND a.LON = c.LON)