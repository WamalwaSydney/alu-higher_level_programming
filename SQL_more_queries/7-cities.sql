-- Script that creates a database and a table with foreign key
-- Create database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use the created database
USE hbtn_0d_usa;
-- Create table cities
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
