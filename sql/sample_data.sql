USE library_db;

INSERT INTO MEMBER VALUES
(1, 'Alice', 'CSE', '9876543210', 'alice@example.com', '2024-06-01'),
(2, 'Bob',   'ECE', '9876500000', 'bob@example.com',   '2024-06-10');

INSERT INTO AUTHOR VALUES
(1, 'Dennis Ritchie', 'dennis@example.com'),
(2, 'Abraham Silberschatz', 'silber@example.com');

INSERT INTO PUBLISHER VALUES
(1, 'Pearson', 'Bangalore', '080-111111'),
(2, 'McGraw Hill', 'Mumbai', '022-222222');

INSERT INTO EMPLOYEE VALUES
(1, 'Rahul', 'Librarian', '9000011111', 'rahul@example.com'),
(2, 'Sneha', 'Assistant', '9000022222', 'sneha@example.com');

INSERT INTO BOOK VALUES
(1, 'C Programming', 'ISBN001', 'Programming', 450.00, 1),
(2, 'Operating Systems', 'ISBN002', 'OS', 550.00, 2);

INSERT INTO AUTHOR_BOOK VALUES
(1, 1),
(2, 2);

INSERT INTO ISSUE VALUES
(1, '2024-07-01', NULL, 1, 1, 1);
