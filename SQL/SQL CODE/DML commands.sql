CREATE TABLE india (name char(56),state char(76),sex char(76),age int(78),id int(10));
CREATE TABLE america (name char(56),state char(76),sex char(76),age int(78),id int(10));
SHOW TABLES;

INSERT INTO india(name,state,sex,age,id)VALUES('Ram','goa','male',38,1);
INSERT INTO america(name,state,sex,age,id)VALUES('george','austin','male',38,1);
INSERT INTO india(name,state,sex,age,id)VALUES('Rama','goa','female',28,2);
INSERT INTO india(name,state,sex,age,id)VALUES('latha','andhra','female',39,3);
INSERT INTO india(name,state,sex,age,id)VALUES('sita','kerla','female',40,4);
INSERT INTO india(name,state,sex,age,id)VALUES('krishna','delhi','male',24,5);

SELECT age FROM india WHERE sex='female';

UPDATE america SET state='san' WHERE state='austin';
SELECT * FROM america;

SELECT*FROM india ORDER BY age desc;

ALTER TABLE india ADD COLUMN lastname char(78);
INSERT INTO india(name,state,sex,age,id,lastname) VALUES('Ram','goa','male',38,1,'tarun');
INSERT INTO india(name,state,sex,age,id,lastname)VALUES('Rama','goa','female',28,2,'krishna');
INSERT INTO india(name,state,sex,age,id,lastname)VALUES('latha','andhra','female',39,3,'kavya');
INSERT INTO india(name,state,sex,age,id,lastname)VALUES('sita','kerla','female',40,4,'varun');
INSERT INTO india(name,state,sex,age,id,lastname)VALUES('krishna','delhi','male',24,5,'lata');
SELECT * FROM india;
ALTER TABLE india DROP COLUMN lastname;

DELETE FROM india WHERE sex='male';
SELECT*FROM india;
SELECT *FROM india WHERE id=3;


ALTER TABLE india RENAME COLUMN sex TO gender;
SELECT*from india;



CREATE TABLE emp1(Stid int(69),Stuname char(56));
CREATE TABLE emp2(Cid int(69),Section char(56));
INSERT INTO emp1(Stid,Stuname) VALUES (21,'RITA');
INSERT INTO emp1(Stid,Stuname) VALUES (22,'MARY');
INSERT INTO emp2(Cid,Section) VALUES (21,'A');
INSERT INTO emp2(Cid,Section) VALUES (22,'B');
SELECT *FROM emp1 JOIN emp2 ON emp1.Stid=emp2.Cid;
