CREATE TABLE stu1(name char(67),marks int(56),rlno int(78),tmarks int(67));
INSERT INTO stu1 (name,marks,rlno,tmarks) VALUES ('rita',50,5,150);
INSERT INTO stu1 (name,marks,rlno,tmarks) VALUES ('sita',70,3,290);
INSERT INTO stu1 (name,marks,rlno,tmarks) VALUES ('lita',20,2,100);
INSERT INTO stu1 (name,marks,rlno,tmarks) VALUES ('jita',80,4,300);
INSERT INTO stu1 (name,marks,rlno,tmarks) VALUES ('radha',40,1,130);
INSERT INTO stu1 (name,marks,rlno,tmarks) VALUES ('dhana',40,6,230);

SELECT name,marks,ROW_NUMBER() OVER (ORDER BY name) AS rank FROM stu1;
SELECT name,rlno,tmarks,RANK()OVER (ORDER BY marks DESC) AS rank FROM stu1;
SELECT name,rlno,tmarks,DENSE_RANK()OVER (ORDER BY tmarks DESC) AS rank FROM stu1;
SELECT name,marks,NTILE(5)OVER (ORDER BY marks ASC) AS rank FROM stu1;
