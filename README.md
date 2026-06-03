# Student Management System

A Student Management System developed using Python and MySQL for managing student records efficiently. This project allows users to add, view, search, update, and delete student information through a menu-driven interface.

## Features

- Add New Student
- View All Students
- Search Student by ID
- Update Student Details
- Delete Student Record
- MySQL Database Integration
- Menu Driven Interface

## Technologies Used

- Python 3.x
- MySQL
- mysql-connector-python

## Database Fields

The student database contains the following fields:

- Student ID
- Name
- Age
- Course
- Phone Number
- Address
- Gmail ID

## Database Setup

Create the database and table using the following SQL commands:

```sql
CREATE DATABASE student_db;
USE student_db;

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(50),
    phone VARCHAR(15),
    address VARCHAR(150),
    gmail VARCHAR(100)
);
```

## Installation

Install MySQL Connector for Python:

```bash
pip install mysql-connector-python
```

## How to Run

1. Open MySQL and create the database.
2. Run the SQL script.
3. Update your MySQL username and password in the Python file.
4. Run the program:

```bash
python student_management.py
```

## Project Structure

```text
Student-Management-System
│
├── student_management.py
├── database.sql
└── README.md
```

## Sample Operations

- Add Student
- View Students
- Search Student
- Update Student
- Delete Student

## Learning Outcomes

This project helped in understanding:

- Python Functions
- MySQL Database Operations
- CRUD Operations
- Python-MySQL Connectivity
- Menu Driven Programming

## Future Enhancements

- Graphical User Interface (GUI)
- Student Attendance Management
- Login Authentication
- Web-Based Version
- Report Generation

## Author

Priyanshu Sachan
BCA Student