CREATE DATABASE IF NOT EXISTS OrganizationsDB;

USE OrganizationsDB;

CREATE TABLE IF NOT EXISTS Organizations (
	OrganizationID int NOT NULL,
	Organization_name VARCHAR ( 50 ) NOT NULL,
	Website VARCHAR ( 50 ) NOT NULL,
	Country VARCHAR ( 50 ) NOT NULL,
	Descrip VARCHAR ( 255 ) NOT NULL,
    Founded VARCHAR ( 10 ) NOT NULL,
    Industry VARCHAR ( 255 ) NOT NULL,
	CreatedOn TIMESTAMP NOT NULL,
    PRIMARY KEY (OrganizationID)
);

CREATE TABLE IF NOT EXISTS Employees (
	EmployeeID int NOT NULL,
    OrganizationID int, 
	FirstName VARCHAR ( 50 ) NOT NULL,
	LastName VARCHAR ( 50 ) NOT NULL,
	Sex VARCHAR ( 10 ) NOT NULL,
	Email VARCHAR ( 255 ) UNIQUE NOT NULL,
	Phone VARCHAR ( 255 ) NOT NULL,
    DateOfBirth VARCHAR ( 20 ) NOT NULL,
    JobTitle VARCHAR ( 255 ) NOT NULL,
	CreatedOn TIMESTAMP NOT NULL,
    PRIMARY KEY (EmployeeID),
    FOREIGN KEY (OrganizationID) REFERENCES Organizations(OrganizationID)
);
