-- Create a databse and a table in that database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
id INT PRIMARY KEY UNIQUE NOT NULL AUTO_INCREMENT,
name VARCHAR(256) NOT NULL
);
