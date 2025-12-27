** Library-management-DBMS
Library Management System mini project for DBMS**

The Library Management System is a DBMS-based mini project developed to manage library operations such as maintaining member records, book details, authors, publishers, employees, and book issue transactions.
This project demonstrates database design, SQL implementation, and database connectivity using Python.

It is developed as my first academic mini project to gain hands-on experience in real-world database applications.

**Objectives**

To design a structured relational database for a library system

To model real-world entities using an ER diagram

To implement database tables using SQL

To enforce relationships using primary and foreign keys

To perform CRUD operations using Python and MySQL

** Technologies Used**

Database: MySQL

Programming Language: Python

Database Connector: mysql-connector-python

Design Tool: ER Diagram

Version Control: GitHub

IDE: VS Code

**System Design**
Entities Identified

MEMBER

EMPLOYEE

AUTHOR

PUBLISHER

BOOK

ISSUE

Relationships

A member can issue multiple books

A book can be issued many times

A book is published by one publisher

A book can have multiple authors (M:N)

An employee processes book issues

**How to Run the Project (Using CMD)**

Step 1: Database Setup

Open MySQL Workbench

Execute schema.sql to create the database and tables

Execute sample_data.sql to insert sample records

Step 2: Python Setup (CMD)

Open Command Prompt

Install MySQL connector (only once):

pip install mysql-connector-python


Navigate to the project folder:

cd path\to\your\project\folder


Run the Python file:

python main.py

**Sample Data**

Sample records are inserted into all tables to demonstrate:

Member registration

Book and author details

Publisher information

Employee records

Book issue transaction

**Key Concepts Used**

MySQL database connection using Python

SQL query execution from Python

Input validation (checking existence of member, book, employee)

JOIN queries for displaying issue details

**Conclusion**

This Library Management System successfully demonstrates:

ER modeling and relational database design

SQL table creation and data manipulation

Implementation of relationships using foreign keys

Integration of Python with MySQL

This project strengthened my understanding of DBMS concepts and real-world data handling.

**Future Enhancements
**
Add book return functionality

Add fine calculation for late returns

Develop a GUI or web interface

Implement authentication and roles

Add reporting and analytics features

**Academic Note**

This project was developed as part of my DBMS mini project and is intended for learning and academic purposes.
