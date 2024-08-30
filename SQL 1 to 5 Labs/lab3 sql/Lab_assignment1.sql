-- Task: Let's consider a scenario where you want to retrieve information about students from a database table named student and display the results in ascending order based on their last names. Hint: Use orderBy clause in a ascending Order 
use studentmanagementsystem;
SELECT *
FROM Student
ORDER BY lastname ASC;

-- Task: Count the number of students based on their gender.
SELECT gender, COUNT(*) AS gender_count
FROM Student
GROUP BY gender;
