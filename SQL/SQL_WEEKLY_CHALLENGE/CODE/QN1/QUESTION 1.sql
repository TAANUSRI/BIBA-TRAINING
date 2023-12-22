CREATE TABLE emp(Ename char(70),Eage int(80),Esal int(100),Eid int UNIQUE KEY,Egen char(70));
CREATE TABLE com(name char(80),cid int UNIQUE KEY,Chq varchar(70));
INSERT INTO emp VALUES('Ram',45,10000,4,'male');
INSERT INTO emp VALUES('Sita',40,20000,3,'female');
INSERT INTO emp VALUES('Gaza',24,4000,2,'male');
INSERT INTO emp VALUES('Lata',25,2000,1,'female');
INSERT INTO emp VALUES('Lata',25,2000,5,'female');
INSERT INTO com VALUES('HEXA',2,'PUNE');
INSERT INTO com VALUES('TCS',1,'BOMBAY');
INSERT INTO com VALUES('IBM',4,'CHENNAI');
INSERT INTO com VALUES('CTS',3,'HYDERABAD');

SELECT*FROM emp;
SELECT *FROM com;
-- Inner Join
SELECT emp.Ename,emp.Eid,com.cid,com.name FROM emp INNER JOIN com ON emp.Eid=com.cid ORDER BY Eid ASC;

-- Left Join
SELECT emp.Ename,emp.Eid,com.cid,com.Chq FROM emp LEFT JOIN com ON emp.Eid=com.cid ORDER BY Eid ASC;

-- Right Join
SELECT emp.Ename,emp.Eid,com.cid,com.Chq FROM emp RIGHT JOIN com ON emp.Eid=com.cid ORDER BY Eid ASC;

-- Subquery with having clause
SELECT MAX(Esal), Ename FROM emp GROUP BY Ename HAVING MAX(Esal) > 1000;

-- Subquery with WHERE clause
SELECT Ename,Esal,Eid FROM emp WHERE Eid>2;

-- Subquery with GROUPBY clause
SELECT Ename, Egen, MIN(Eage) AS Minage FROM emp GROUP BY Ename, Egen ORDER BY Minage DESC;


