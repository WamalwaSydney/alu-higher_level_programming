-- Script that creates a database and a user with SELECT privilege only
-- Create database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create user if not exists
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grant SELECT privilege to the user on the specified database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
-- Apply changes
FLUSH PRIVILEGES;
