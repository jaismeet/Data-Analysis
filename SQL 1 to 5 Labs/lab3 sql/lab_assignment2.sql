use bank;
ALTER TABLE Employee
ADD COLUMN salary DECIMAL(10, 2),
ADD COLUMN department VARCHAR(50);

UPDATE Employee
SET salary = 60000, department = 'IT'
WHERE emp_id = 1;

UPDATE Employee
SET salary = 55000, department = 'IT'
WHERE emp_id = 2;

UPDATE Employee
SET salary = 45000, department = 'HR'
WHERE emp_id = 3;

-- Task: Retrieve employees in the IT department with a salary greater than 50,000.
SELECT *
FROM Employee
WHERE department = 'IT' AND salary > 50000;

-- Task: Calculate the average salary of employees in each department.
SELECT department, AVG(salary) AS average_salary
FROM Employee
GROUP BY department;
