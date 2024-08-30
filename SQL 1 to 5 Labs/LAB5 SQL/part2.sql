use studentmanagementsystem;
-- Task 1: Use FULL OUTER JOIN to retrieve all students and their corresponding enrollments, including unmatched rows from both tables.
SELECT Student.studentid, Student.firstname, Student.email, Enrollment.enrollmentid, Enrollment.courseid
from Student left join Enrollment on Student.studentid = Enrollment.studentid
union
select  Student.studentid, Student.firstname, Student.email, Enrollment.enrollmentid, Enrollment.courseid
from Student right join Enrollment on Student.studentid = Enrollment.studentid;


-- Task 2: Use NATURAL JOIN to retrieve student and enrollment details based on common columns.
SELECT 
    studentid,
    firstname,
    email,
    enrollmentid,
    courseid
FROM 
    Student
NATURAL JOIN 
    Enrollment;
