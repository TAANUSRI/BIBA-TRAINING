CREATE TABLE Customers(id int(67),Name VARCHAR(20),Country VARCHAR(20),City VARCHAR(20));
INSERT INTO Customers (id,Name,Country,City)VALUES (1, 'Aakash', 'INDIA', 'Mumbai');
INSERT INTO Customers (id,Name,Country,City) VALUES (2, 'George', 'USA', 'New York');
INSERT INTO Customers (id,Name,Country,City) VALUES (3, 'David', 'INDIA', 'Bangalore');
INSERT INTO Customers  (id,Name,Country,City)VALUES (4, 'Leo', 'SPAIN', 'Madrid');
SELECT * FROM Customers;
CREATE TABLE Branches(code int(45),Country VARCHAR(20),City VARCHAR(20));
INSERT INTO Branches(code,Country,City) VALUES (101, 'INDIA', 'Mumbai');
INSERT INTO Branches (code,Country,City) VALUES (201, 'INDIA', 'Bangalore');
INSERT INTO Branches (code,Country,City) VALUES (301, 'USA', 'Chicago');
INSERT INTO Branches (code,Country,City)VALUES (401, 'USA', 'New York');
SELECT * FROM Branches;


