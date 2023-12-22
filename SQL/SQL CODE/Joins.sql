CREATE TABLE stu1(name char(67),marks int(56),rlno int(78),tmarks int(67));
CREATE TABLE coll(id int(67),crname char(100));
INSERT INTO stu1 (name,marks,rlno,tmarks) VALUES ('rita',50,5,150);
INSERT INTO stu1 (name,marks,rlno,tmarks) VALUES ('sita',70,3,290);
INSERT INTO stu1 (name,marks,rlno,tmarks) VALUES ('lita',20,2,100);
INSERT INTO stu1 (name,marks,rlno,tmarks) VALUES ('jita',80,4,300);
INSERT INTO stu1 (name,marks,rlno,tmarks) VALUES ('radha',40,1,130);
INSERT INTO stu1 (name,marks,rlno,tmarks) VALUES ('dhana',40,6,230);

INSERT INTO coll(id,crname) VALUES (2,'maths');
INSERT INTO coll(id,crname) VALUES (1,'sciece');
INSERT INTO coll(id,crname) VALUES (3,'social');
INSERT INTO coll(id,crname) VALUES (4,'english');
INSERT INTO coll(id,crname) VALUES (5,'cs');
INSERT INTO coll(id,crname) VALUES (7,'sql');

SELECT name,marks,rlno,tmarks FROM stu1 INNER JOIN coll ON stu1.rlno=coll.id;
SELECT name,marks,rlno,coll.crname FROM stu1 LEFT JOIN coll ON stu1.rlno=coll.crname;
SELECT name,marks,rlno,coll.crname FROM stu1 RIGHT JOIN coll ON stu1.rlno=coll.id;
SELECT name,marks,rlno,coll.crname FROM stu1 CROSS JOIN coll;