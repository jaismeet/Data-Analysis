-- Use the StudentManagementSystem database
USE StudentManagementSystem;

-- Insert records into the Course table
INSERT INTO Course (CourseID, CourseTitle, Credits)
VALUES 
('C01', 'Math', 3),
('C002', 'Science', 4),
('C003', 'History', 2),
('C004', 'Art', 1),
('C005', 'Music', 2);


-- Insert records into the Student table
INSERT INTO Student (StudentID, FirstName, LastName, DateOfBirth, Gender, Email, Phone)
VALUES 
('S101', 'John', 'Doe', '2000-01-15', 'M', 'john1@mail.com', 9876543210),
('S102', 'Jane', 'Smith', '1999-02-20', 'F', 'janes@mail.com', 9876543211),
('S103', 'Alice', 'Brown', '2001-03-10', 'F', 'alice.b@mail.com', 9876543212),
('S104', 'Bob', 'Johnson', '2000-04-25', 'M', 'bobjson@mail.com', 9876543213),
('S105', 'Eve', 'Davis', '1998-05-30', 'F', 'eves@mail.com', 9876543214);

-- Insert records into the Instructor table
INSERT INTO Instructor (InstructorID, FirstName, LastName, Email)
VALUES 
('I001', 'Michael', 'Scott', '01michael@mail.com'),
('I002', 'Dwight', 'Schrute', '02dwight@mail.com'),
('I003', 'Jim', 'Halpert', '03jim@mail.com'),
('I004', 'Pam', 'Beesly', '04pam@mail.com'),
('I005', 'Stanley', 'Hudson', '05stanley@mail.com');

-- Insert records into the Enrollment table
INSERT INTO Enrollment (EnrollmentID, EnrollmentDate, StudentID, CourseID, InstructorID)
VALUES 
('E001', '2023-01-10', 'S001', 'C001', 'I001'),
('E002', '2023-01-11', 'S002', 'C002', 'I002'),
('E003', '2023-01-12', 'S003', 'C003', 'I003'),
('E004', '2023-01-13', 'S004', 'C004', 'I004'),
('E005', '2023-01-14', 'S005', 'C005', 'I005');

-- Insert records into the Score table
INSERT INTO Score (ScoreID, CourseID, StudentID, DateOfExam, CreditObtained)
VALUES 
(1, 'C001', 'S001', '2023-06-15', 2.50),
(2, 'C002', 'S002', '2023-06-16', 3.80),
(3, 'C003', 'S003', '2023-06-17', 1.75),
(4, 'C004', 'S004', '2023-06-18', 0.90),
(5, 'C005', 'S005', '2023-06-19', 2.10);


-- Insert records into the Feedback table
INSERT INTO Feedback (FeedbackID, StudentID, Date, InstructorName, Feedback)
VALUES 
(1, 'S001', '2023-07-01', 'Michael Scott', 'Great teacher, very engaging.'),
(2, 'S002', '2023-07-02', 'Dwight Schrute', 'Very knowledgeable, but strict.'),
(3, 'S003', '2023-07-03', 'Jim Halpert', 'Relaxed and friendly teaching style.'),
(4, 'S004', '2023-07-04', 'Pam Beesly', 'Encouraging and supportive.'),
(5, 'S005', '2023-07-05','Stanley Hudson', 'Straight to the point, no-nonsense.');

-- Retrieve data from all tables and display
SELECT * FROM Student;
SELECT * FROM Course;
SELECT * FROM Instructor;
SELECT * FROM Enrollment;
SELECT * FROM Score;
SELECT * FROM Feedback;

