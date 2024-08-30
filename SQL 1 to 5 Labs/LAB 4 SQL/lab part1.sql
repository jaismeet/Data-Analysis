use studentmanagementsystem;

-- Task 1: Retrieve information about students born after June 16, 2009.
SELECT *
FROM Student
WHERE birth_date > '2009-06-16';

-- Task 2: Retrieve records of students whose first names start with either 'A' or 'J'.
SELECT *
FROM Student
WHERE first_name LIKE 'A%' OR first_name LIKE 'J%';

-- Task 3: Retrieve records of students whose first name is not 'Alice' and whose email addresses contain the domain '@example.com'.
SELECT *
FROM Student
WHERE first_name != 'Alice' AND email LIKE '%@example.com';
