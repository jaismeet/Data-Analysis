create database db;
-- Task 1: Create the Person table with PersonID as the PRIMARY KEY.
CREATE TABLE Person (
    PersonID INT PRIMARY KEY,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    Age INT
);

-- Task 2: Create the Employee table with emp_id as the PRIMARY KEY.
CREATE TABLE Employee (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INT
);

-- Task 3: Insert data into the Person table.
INSERT INTO Person (PersonID, FirstName, LastName, Age) 
VALUES 
(1, 'John', 'Doe', 28),
(2, 'Jane', 'Smith', 35),
(3, 'Alice', 'Brown', 22);

-- Task 4: Insert data into the Employee table.
INSERT INTO Employee (emp_id, first_name, last_name, age) 
VALUES 
(1, 'Robert', 'Johnson', 40),
(2, 'Emily', 'Davis', 30),
(3, 'Michael', 'Wilson', 25);

-- Task 5: Create a UNION of the Person and Employee tables.
SELECT FirstName, LastName, Age 
FROM Person
UNION
SELECT first_name, last_name, age 
FROM Employee;
