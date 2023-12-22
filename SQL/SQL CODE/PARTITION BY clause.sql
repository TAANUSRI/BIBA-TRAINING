CREATE TABLE india (name char(56),state char(76),sex char(76),age int(78),id int(10));

INSERT INTO india(name,state,sex,age,id)VALUES('Ram','goa','male',38,1);
INSERT INTO india(name,state,sex,age,id)VALUES('Rama','goa','female',28,2);
INSERT INTO india(name,state,sex,age,id)VALUES('latha','andhra','female',39,3);
INSERT INTO india(name,state,sex,age,id)VALUES('sita','kerla','female',40,4);
INSERT INTO india(name,state,sex,age,id)VALUES('krishna','delhi','male',24,5);
INSERT INTO india(name,state,sex,age,id)VALUES('krishna','delhi','male',45,6);

SELECT name,age,state,MAX(age) OVER (PARTITION BY state) AS "AGE GROUP"
FROM india;

