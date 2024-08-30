use studentmanagementsystem;
-- Task: Retrieve information about each student's ID, first name, last name, 
-- and their enrollment details including the enrollment ID and associated course ID.
SELECT 
    Student.studentid,
    Student.firstname,
    Student.lastname,
    Enrollment.enrollmentid,
    Enrollment.courseid
FROM 
    Student
INNER JOIN 
    Enrollment 
ON 
    Student.studentid = Enrollment.studentid;
