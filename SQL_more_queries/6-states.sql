-- Script that creates a database and a table with primary key
-- Create database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use the created database
USE hbtn_0d_usa;
-- Create table states
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
