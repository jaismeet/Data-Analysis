use studentmanagementsystem;

-- Task 1: Update the Student table with the following information: Change the email to 'jane_Smith@example.com' Where FirstName is 'Jane' and LastName is 'Smith'; 
-- Update the Instructor with the following information: Change the email to 'rogerwhite@example.com' Where FirstName of the instructor is 'Roger' and LastName is 'White';

UPDATE Student
SET email = 'jane_Smith@example.com'
WHERE firstname = 'Jane' AND lastname = 'Smith';

UPDATE Instructor
SET email = 'rogerwhite@example.com'
WHERE firstname = 'Roger' AND lastname = 'White';

-- Task 2: Delete records from the Student table where the last name is Smith.
DELETE FROM Student
WHERE lastname = 'Smith';

-- Task 3: List the students whose first name starts with 'J'.
SELECT *
FROM Student
WHERE first_name LIKE 'J%';
