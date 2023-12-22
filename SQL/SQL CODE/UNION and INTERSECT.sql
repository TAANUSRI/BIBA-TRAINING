CREATE TABLE emp1(Name char(60),age int(50),id int(58),sname char(100));
CREATE TABLE emp2(SName char(60),age int(50),id int(58),rname char(100));

INSERT INTO emp1(Name,age,id,sname) VALUES ('R',50,1,'S');
INSERT INTO emp1(Name,age,id,sname) VALUES ('S',60,2,'T');
INSERT INTO emp1(Name,age,id,sname) VALUES ('U',70,3,'V');
INSERT INTO emp1(Name,age,id,sname) VALUES ('W',80,4,'X');

INSERT INTO emp2(SName,age,id,rname) VALUES ('A',10,4,'B');
INSERT INTO emp2(SName,age,id,rname) VALUES ('C',20,7,'D');
INSERT INTO emp2(SName,age,id,rname) VALUES ('E',30,8,'F');
INSERT INTO emp2(SName,age,id,rname) VALUES ('G',40,9,'H');
SELECT*FROM emp1;
SELECT*FROM emp2;

SELECT id,age FROM emp1 UNION SELECT id,age FROM emp2;

SELECT id FROM emp1 WHERE id<=4 UNION ALL SELECT id FROM emp2 WHERE id<8;
SELECT id FROM emp1 WHERE id<=4 UNION SELECT id FROM emp2 WHERE id<8;

SELECT *FROM emp1 INTERSECT SELECT *FROM emp2; 
