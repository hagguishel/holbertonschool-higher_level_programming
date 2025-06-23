CREATE DATABASE IF NOT EXISTS test_db;
USE test_db;
CREATE TABLE users (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100),
	email VARCHAR(100)
);
INSERT INTO users (name, email)
VALUES ('Shel', 'shel@example.com');
SELECT *
FROM users;