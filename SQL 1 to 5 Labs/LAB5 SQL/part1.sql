
use studentmanagementsystem;
-- Task: Use RIGHT OUTER JOIN to retrieve data showing all enrollments, including students not enrolled in any courses.
SELECT 
    Student.studentid,
    Student.firstname,
    Student.lastname,
    Enrollment.enrollmentid,
    Enrollment.courseid
FROM 
    Student
RIGHT OUTER JOIN 
    Enrollment 
ON 
    Student.studentid = Enrollment.studentid;
    
    
-- Task: Use LEFT JOIN to retrieve data showing all students and their corresponding enrollments.

SELECT 
    Student.studentid,
    Student.firstname,
    Student.email,
    Enrollment.enrollmentid,
    Enrollment.courseid
FROM 
    Student
LEFT JOIN 
    Enrollment 
ON 
    Student.studentid = Enrollment.studentid;
