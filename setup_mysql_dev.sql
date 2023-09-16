-- Creates database hbnb_dev_db and user hbnb_dev
-- and grants some privileges
-- Create the hbnb_test_db table if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create the hbnb_dev user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev' @'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- granting previelage on `hbnb_dev_db`
GRANT USAGE ON *.* TO 'hbnb_dev' @'localhost';
-- granting previlage on performance schema
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev' @'localhost';
-- granting all previlage on `hbnb_dev_db`
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev' @'localhost';
