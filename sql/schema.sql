CREATE DATABASE IF NOT EXISTS library_db;
USE library_db;

CREATE TABLE MEMBER (
    member_id INT PRIMARY KEY,
    name       VARCHAR(100),
    department VARCHAR(100),
    phone      VARCHAR(20),
    email      VARCHAR(100),
    date       DATE
);

CREATE TABLE AUTHOR (
    author_id INT PRIMARY KEY,
    name      VARCHAR(100),
    email     VARCHAR(100)
);

CREATE TABLE PUBLISHER (
    publisher_id INT PRIMARY KEY,
    name         VARCHAR(100),
    address      VARCHAR(200),
    contact      VARCHAR(50)
);

CREATE TABLE EMPLOYEE (
    employee_id INT PRIMARY KEY,
    name        VARCHAR(100),
    role        VARCHAR(50),
    phone       VARCHAR(20),
    email       VARCHAR(100)
);

CREATE TABLE BOOK (
    book_id      INT PRIMARY KEY,
    book_title   VARCHAR(200),
    isbn         VARCHAR(30),
    category     VARCHAR(100),
    price        DECIMAL(8,2),
    publisher_id INT,
    FOREIGN KEY (publisher_id) REFERENCES PUBLISHER(publisher_id)
);

CREATE TABLE ISSUE (
    issue_id    INT PRIMARY KEY,
    issue_date  DATE,
    return_date DATE,
    member_id   INT,
    book_id     INT,
    employee_id INT,
    FOREIGN KEY (member_id)   REFERENCES MEMBER(member_id),
    FOREIGN KEY (book_id)     REFERENCES BOOK(book_id),
    FOREIGN KEY (employee_id) REFERENCES EMPLOYEE(employee_id)
);

CREATE TABLE AUTHOR_BOOK (
    author_id INT,
    book_id   INT,
    PRIMARY KEY (author_id, book_id),
    FOREIGN KEY (author_id) REFERENCES AUTHOR(author_id),
    FOREIGN KEY (book_id)   REFERENCES BOOK(book_id)
);
