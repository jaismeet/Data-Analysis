use bank;
create table employee (
emp_id int Primary Key, 
first_name varchar(20), 
last_name varchar(20), 
age tinyint, 
email varchar(40));


-- Task 1: Insert Data
INSERT INTO Employee (emp_id, first_name, last_name, age, email) 
VALUES
(1, 'John', 'Doe', 28, 'john.doe@example.com'), 
(2, 'Jane', 'Smith', 35, 'jane.smith@example.com'),
(3, 'Alice', 'Johnson', 42, 'alice.johnson@example.com');

-- Task 2: Retrieving Data Write an SQL SELECT statement to retrieve the first_name and last_name of all employees from the Employee table. 
SELECT first_name, last_name 
FROM Employee;

-- Task 3: Filtering Data Write an SQL SELECT statement to retrieve the first_name, last_name, and age of employees who are older than 30 years. 
SELECT first_name, last_name, age 
FROM Employee 
WHERE age > 30;

-- Task 4: Updating Data Write an SQL UPDATE statement to increase the age of employees by 1 year for all employees older than 25.
UPDATE Employee 
SET age = age + 1 
WHERE age > 25;