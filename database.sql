CREATE DATABASE student_db;

USE student_db;

CREATE TABLE students(
student_id INT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
age INT,
course VARCHAR(50),
phone VARCHAR(15),
address VARCHAR(150),
gmail VARCHAR(100)
);
