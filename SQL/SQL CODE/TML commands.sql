CREATE TABLE india (name char(56),jobd char(76),salary char(76),age int(78),id int(10));
INSERT INTO india(name,jobd,salary,age,id)VALUES('Ram','hr',40000,25,1);
INSERT INTO india(name,jobd,salary,age,id)VALUES('Rama','asst',20000,26,2);
INSERT INTO india(name,jobd,salary,age,id)VALUES('Rita','mgr',60000,28,3);
INSERT INTO india(name,jobd,salary,age,id)VALUES('lata','srmg',90000,29,4);
INSERT INTO india(name,jobd,salary,age,id)VALUES('krishna','dep',10000,30,5);

SELECT jobd,AVG(salary) FROM india  GROUP BY jobd ORDER BY AVG(salary)desc;
SELECT name,COUNT(id) FROM india  GROUP BY name;

SELECT jobd,AVG(salary) FROM india  GROUP BY jobd 
HAVING AVG(salary)>10000;

BEGIN tran
SELECT* FROM india where salary>=45000;
COMMIT;
SELECT* FROM india where salary>=45000;
ROLLBACK;

begin tran;
save tran a1;
delete from india where jobd='hr';
save tran a2;
select * from india where age = 29;
save tran a3;
select * from india where id =5;

rollback tran a1;



