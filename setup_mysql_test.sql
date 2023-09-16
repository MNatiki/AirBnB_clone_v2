-- Creates database hbnb_test_db and user hbnb_test
-- and grants some privileges
-- Create the hbnb_test_db table if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create the hbnb_dev user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test' @'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- granting previelage on `hbnb_dev_db`
GRANT USAGE ON *.* TO 'hbnb_test' @'localhost';
-- granting previlage on performance schema
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test' @'localhost';
-- granting all previlage on `hbnb_dev_db`
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test' @'localhost';
