MySQL> create database StudentManagementSystem ;
Query OK, 1 row affected (0.01 sec)

mysql> use StudentManagementSystem ;
Database changed
mysql> create table Student(
    -> StudentID int primary key,
    -> FirstName varchar(50) not null,
    -> LastName varchar(50) not null,
    -> DateOfBirth date ,
    -> Gender enum('m','f'),
    -> Email varchar(60),
    -> Phone varchar(20));
Query OK, 0 rows affected (0.03 sec)

mysql> insert into Student values(1,'Harry','Potter','1998-11-02','m','harrypotter@gmail.com',9876543210);
Query OK, 1 row affected (0.02 sec)

mysql> select * from Student;
+-----------+-----------+----------+-------------+--------+-----------------------+------------+
| StudentID | FirstName | LastName | DateOfBirth | Gender | Email                 | Phone      |
+-----------+-----------+----------+-------------+--------+-----------------------+------------+
|         1 | Harry     | Potter   | 1998-11-02  | m      | harrypotter@gmail.com | 9876543210 |
+-----------+-----------+----------+-------------+--------+-----------------------+------------+
1 row in set (0.00 sec)

--------------------------------------------------------------------------------------------------------------------------

mysql> CREATE TABLE Course (
    ->     CourseID INT PRIMARY KEY,
    ->     CourseTitle VARCHAR(255) NOT NULL,
    ->     Credits INT NOT NULL
    -> );
Query OK, 0 rows affected (0.04 sec)

mysql> INSERT INTO Course (CourseID, CourseTitle, Credits)VALUES (1, 'Introduction to Computer Science', 4);
Query OK, 1 row affected (0.02 sec)

mysql> select * from Course;
+----------+----------------------------------+---------+
| CourseID | CourseTitle                      | Credits |
+----------+----------------------------------+---------+
|        1 | Introduction to Computer Science |       4 |
+----------+----------------------------------+---------+
1 row in set (0.00 sec)

-----------------------------------------------------------------------------------------------------------------------------

mysql> CREATE TABLE Instructor (
    ->     InstructorID INT PRIMARY KEY,
    ->     FirstName VARCHAR(50) NOT NULL,
    ->     LastName VARCHAR(50) NOT NULL,
    ->     Email VARCHAR(100) UNIQUE NOT NULL
    -> );
Query OK, 0 rows affected (0.04 sec)

mysql> INSERT INTO Instructor (InstructorID, FirstName, LastName, Email)VALUES (1, 'John', 'Doe', 'john.doe@example.com'),(2, 'Jane', 'Smith', 'jane.smith@example.com');
Query OK, 2 rows affected (0.02 sec)
mysql> select * from Instructor;
+--------------+-----------+----------+------------------------+
| InstructorID | FirstName | LastName | Email                  |
+--------------+-----------+----------+------------------------+
|            1 | John      | Doe      | john.doe@example.com   |
|            2 | Jane      | Smith    | jane.smith@example.com |
+--------------+-----------+----------+------------------------+
2 rows in set (0.00 sec)

---------------------------------------------------------------------------------------------------------------------------------

mysql> CREATE TABLE Enrollment (
    ->     EnrollmentID INT PRIMARY KEY,
    ->     EnrollmentDate DATE NOT NULL,
    ->     StudentID INT,
    ->     CourseID INT,
    ->     InstructorID INT,
    ->     FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    ->     FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
    ->     FOREIGN KEY (InstructorID) REFERENCES Instructor(InstructorID)
    -> );
Query OK, 0 rows affected (0.07 sec)

mysql> INSERT INTO Enrollment (EnrollmentID, EnrollmentDate, StudentID, CourseID, InstructorID)VALUES (1, '2024-08-23', 1, 1, 1);
Query OK, 1 row affected (0.02 sec)

mysql> select * from Enrollment;
+--------------+----------------+-----------+----------+--------------+
| EnrollmentID | EnrollmentDate | StudentID | CourseID | InstructorID |
+--------------+----------------+-----------+----------+--------------+
|            1 | 2024-08-23     |         1 |        1 |            1 |
+--------------+----------------+-----------+----------+--------------+
1 row in set (0.00 sec)

------------------------------------------------------------------------------------------------------------------------

mysql> CREATE TABLE Score (
    ->     ScoreID INT PRIMARY KEY,
    ->     CourseID INT,
    ->     StudentID INT,
    ->     DateOfExam DATE NOT NULL,
    ->     CreditObtained DECIMAL(5, 2) NOT NULL,
    ->     FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
    ->     FOREIGN KEY (StudentID) REFERENCES Student(StudentID)
    -> );
Query OK, 0 rows affected (0.05 sec)

mysql> INSERT INTO Score (ScoreID, CourseID, StudentID, DateOfExam, CreditObtained)VALUES (1, 1, 1, '2024-08-23', 3.00);
Query OK, 1 row affected (0.02 sec)

mysql> select * from Score;
+---------+----------+-----------+------------+----------------+
| ScoreID | CourseID | StudentID | DateOfExam | CreditObtained |
+---------+----------+-----------+------------+----------------+
|       1 |        1 |         1 | 2024-08-23 |           3.00 |
+---------+----------+-----------+------------+----------------+
1 row in set (0.00 sec)

-------------------------------------------------------------------------------------------------------------

mysql> CREATE TABLE Feedback (
    ->     FeedbackID INT PRIMARY KEY,
    ->     StudentID INT,
    ->     Date DATE NOT NULL,
    ->     InstructorName VARCHAR(100) NOT NULL,
    ->     Feedback TEXT NOT NULL,
    ->     FOREIGN KEY (StudentID) REFERENCES Student(StudentID)
    -> );
Query OK, 0 rows affected (0.06 sec)

mysql> INSERT INTO Feedback (FeedbackID, StudentID, Date, InstructorName, Feedback)VALUES (1, 1, '2024-08-23', 'Dr. Alice Johnson', 'Great course, very informative!');
Query OK, 1 row affected (0.01 sec)

mysql> select * from Feedback;
+------------+-----------+------------+-------------------+---------------------------------+
| FeedbackID | StudentID | Date       | InstructorName    | Feedback                        |
+------------+-----------+------------+-------------------+---------------------------------+
|          1 |         1 | 2024-08-23 | Dr. Alice Johnson | Great course, very informative! |
+------------+-----------+------------+-------------------+---------------------------------+
1 row in set (0.00 sec)
